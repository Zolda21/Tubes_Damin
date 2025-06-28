import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os # Tambahkan import os untuk penanganan jalur file

def show_prediction_interface():
    st.header("🔍 Try Input New Data")

    st.markdown("""
    Masukkan data kendaraan yang ingin diprediksi harga jualnya.
    Model ini menggunakan kombinasi fitur numerik dan kategorikal.
    """)

    # --- Load model dan preprocessor (untuk supervised dan unsupervised) ---
    # Tentukan jalur relatif ke direktori 'models'
    base_path = 'models/' # Asumsi script Streamlit berada di root project, dan folder 'models' ada di sana

    # Variabel untuk supervised learning (prediksi harga)
    model_supervised = None
    preprocessor_supervised = None
    supervised_label_encoders = {}
    # feature_names_supervised = None # Tidak digunakan di sini, bisa diabaikan

    # Variabel untuk unsupervised learning (clustering)
    model_unsupervised = None
    preprocessor_unsupervised = None
    unsupervised_label_encoders = {}
    cluster_descriptions = {} # Untuk menyimpan deskripsi klaster

    try:
        # Muat Model Supervised (untuk prediksi harga)
        model_supervised = joblib.load(os.path.join(base_path, 'random_forest_regressor.pkl'))
        preprocess_bundle_supervised = joblib.load(os.path.join(base_path, 'preprocessor_supervised.pkl'))
        preprocessor_supervised = preprocess_bundle_supervised['preprocessor']
        supervised_label_encoders = preprocess_bundle_supervised['label_encoders']
        # feature_names_supervised = preprocess_bundle_supervised['processed_feature_names'] # Tidak digunakan

        # Muat Model Unsupervised (untuk clustering)
        model_unsupervised = joblib.load(os.path.join(base_path, 'kmeans_clusterer.pkl'))
        preprocess_bundle_unsupervised = joblib.load(os.path.join(base_path, 'preprocessor_unsupervised.pkl'))
        preprocessor_unsupervised = preprocess_bundle_unsupervised['preprocessor']
        unsupervised_label_encoders = preprocess_bundle_unsupervised.get('label_encoders', {}) # Gunakan .get() untuk keamanan
        # Asumsi cluster_descriptions disimpan di dalam bundle preprocessor unsupervised
        cluster_descriptions = preprocess_bundle_unsupervised.get('cluster_descriptions', {
            0: "Klaster 0 (Lower Tier): Segmen ini didominasi oleh mobil dengan [Harga Jual Terendah], [Kondisi Kurang Baik], dan [Odometer Paling Tinggi].",
            1: "Klaster 1: Segmen ini cenderung memiliki mobil dengan [Harga Jual Sedang], [Kondisi Rata-Rata], dan [Odometer Sedang].",
            2: "Klaster 2: Klaster ini berisi mobil dengan [Harga Jual Cukup Tinggi], [Kondisi Baik], dan [Odometer Rendah].",
            3: "Klaster 3 (Upper Tier): Ini adalah segmen mobil premium dengan [Harga Jual Paling Tinggi], [Kondisi Sangat Baik atau Baru], dan [Odometer Paling Rendah]."
            # Tambahkan deskripsi default lainnya jika ada lebih banyak klaster atau jika deskripsi tidak ditemukan dalam file
        })

    except FileNotFoundError as fnfe:
        st.error(f"❌ Gagal memuat file model/preprocessor. Pastikan file ada di folder 'models/'. Error: {fnfe}")
        return # Keluar dari fungsi jika file tidak ditemukan
    except KeyError as ke:
        st.error(f"❌ Gagal memuat bundle preprocessor. Objek .pkl mungkin tidak memiliki kunci yang diharapkan (misal: 'preprocessor', 'label_encoders', 'cluster_descriptions'). Error: {ke}")
        return # Keluar dari fungsi jika kunci tidak ditemukan
    except Exception as e:
        st.error(f"❌ Terjadi error tak terduga saat memuat model/preprocessor: {e}")
        return # Keluar dari fungsi jika error lain terjadi

    # --- Fungsi untuk Segmentasi Klaster (hanya fungsi ini yang ditambahkan) ---
    def segment_car_cluster(input_data_df_cluster, preprocessor_clus, model_clus, label_encoders_clus_dict):
        processed_df_clus = input_data_df_cluster.copy()
        try:
            # Tangani label encoder untuk kolom kategorikal yang digunakan di clustering
            for col, le in label_encoders_clus_dict.items():
                if col in processed_df_clus.columns:
                    unknown_label_str = f'Other_{col}'
                    # Pastikan 'Other_{col}' ada di kelas encoder, jika tidak, tambahkan secara dinamis
                    if unknown_label_str not in le.classes_:
                         le.classes_ = np.append(le.classes_, unknown_label_str)

                    processed_df_clus[col] = processed_df_clus[col].astype(str).apply(
                        lambda x: x if x in le.classes_ else unknown_label_str
                    )
                    processed_df_clus[col] = le.transform(processed_df_clus[col])

            # *** PENTING: Sesuaikan daftar fitur ini dengan yang digunakan saat melatih model K-Means ***
            # Berdasarkan notebook Anda, fitur untuk unsupervised adalah:
            # 'mmr', 'sellingprice', 'year', 'odometer', 'condition',
            # 'body', 'make', 'model', 'trim', 'seller'
            features_for_unsupervised = [
                'mmr', 'sellingprice', 'year', 'odometer', 'condition',
                'body', 'make', 'model', 'trim', 'seller'
            ]

            # Pastikan hanya fitur yang relevan yang masuk ke preprocessor unsupervised
            # Gunakan .reindex(columns=...) untuk memastikan urutan kolom sama seperti saat training
            input_for_cluster_seg = processed_df_clus.reindex(columns=features_for_unsupervised)

            # Transformasi input menggunakan preprocessor_unsupervised
            processed_input_clus = preprocessor_clus.transform(input_for_cluster_seg)

            # Prediksi klaster
            cluster_label = model_clus.predict(processed_input_clus)[0]
            return cluster_label
        except Exception as e:
            st.error(f"❌ Error saat segmentasi klaster: {e}")
            return None

    # --- Form Input ---
    with st.form("form_input"):
        st.subheader("🧾 Masukkan Data Kendaraan")

        col1, col2 = st.columns(2)

        with col1:
            year = st.number_input("Tahun Kendaraan", min_value=1990, max_value=2025, value=2015)
            odometer = st.number_input("Odometer (mil)", min_value=0, value=50000)
            mmr = st.number_input("MMR (Market Value)", min_value=1000, value=12000)
            condition = st.selectbox("Kondisi Kendaraan (1=terburuk, 5=terbaik)", [1, 2, 3, 4, 5])
            # Tambahkan input sellingprice karena ini digunakan untuk clustering
            sellingprice = st.number_input("Selling Price (untuk Klastering)", min_value=1000, value=15000)


        with col2:
            make = st.selectbox("Merk", ['Other_make', 'toyota', 'honda', 'ford', 'chevrolet'])
            body = st.selectbox("Jenis Body", ['Other_body', 'sedan', 'suv', 'pickup'])
            seller = st.selectbox("Penjual", ['Other_seller', 'CARVANA', 'DriveTime'])
            model_car = st.selectbox("Model", ['Other_model', 'camry', 'accord'])
            trim = st.selectbox("Trim", ['Other_trim', 'LE', 'SE'])
            state = st.selectbox("Negara Bagian", ['Other_state', 'CA', 'TX', 'NY'])
            color = st.selectbox("Warna", ['Other_color', 'black', 'white', 'silver'])
            interior = st.selectbox("Interior", ['Other_interior', 'black', 'gray', 'beige'])
            transmission = st.selectbox("Transmisi", ['Other_transmission', 'automatic', 'manual'])


        submitted = st.form_submit_button("🔮 Prediksi & Segmentasi")

    if submitted:
        # Buat DataFrame satu baris
        input_dict = {
            'year': [year],
            'odometer': [odometer],
            'mmr': [mmr],
            'condition': [condition],
            'make': [make],
            'body': [body],
            'seller': [seller],
            'model': [model_car],
            'trim': [trim],
            'state': [state],
            'color': [color],
            'interior': [interior],
            'transmission': [transmission],
            'sellingprice': [sellingprice] # Masukkan sellingprice ke DataFrame input
        }

        input_df = pd.DataFrame(input_dict)

        # --- Bagian Prediksi Harga (sesuai kode asli Anda) ---
        st.subheader("### Hasil Prediksi Harga ###")
        try:
            # Tangani label encoder dengan unseen value untuk prediksi harga (pakai supervised_label_encoders)
            temp_input_df_for_supervised = input_df.copy() # Buat salinan agar tidak mempengaruhi input_df asli
            for col, encoder in supervised_label_encoders.items():
                if col in temp_input_df_for_supervised.columns:
                    unknown_label = f'Other_{col}'
                    if unknown_label not in encoder.classes_:
                        encoder.classes_ = np.append(encoder.classes_, unknown_label)

                    temp_input_df_for_supervised[col] = temp_input_df_for_supervised[col].astype(str).apply(
                        lambda x: x if x in encoder.classes_ else unknown_label
                    )
                    temp_input_df_for_supervised[col] = encoder.transform(temp_input_df_for_supervised[col])

            # Untuk prediksi harga, 'sellingprice' adalah target, jadi kita bisa menghilangkannya dari input
            input_for_price_pred = temp_input_df_for_supervised.drop(columns=['sellingprice'], errors='ignore')
            input_processed = preprocessor_supervised.transform(input_for_price_pred)
            prediction = model_supervised.predict(input_processed)[0]
            st.success(f"💰 Estimasi Harga Jual Kendaraan: **${prediction:,.2f}**")
        except Exception as e:
            st.error(f"❌ Gagal melakukan prediksi harga: {e}")

        st.write("---") # Garis pemisah

        # --- Bagian Segmentasi Klaster (yang ditambahkan) ---
        st.subheader("### Hasil Segmentasi Klaster ###")
        if model_unsupervised and preprocessor_unsupervised:
            # Gunakan input_df yang sudah memiliki 'sellingprice' untuk clustering
            cluster_label = segment_car_cluster(input_df, preprocessor_unsupervised, model_unsupervised, unsupervised_label_encoders)
            if cluster_label is not None:
                st.info(f"🏷️ Mobil ini masuk ke Klaster: **{cluster_label}**")
                # Ambil deskripsi dari kamus
                description = cluster_descriptions.get(cluster_label, "Tidak ada deskripsi spesifik untuk klaster ini. Anda bisa menganalisis karakteristik rata-rata dari klaster ini.")
                st.markdown(f"**👉 {description}**")
            else:
                st.error("❌ Segmentasi klaster gagal.")
        else:
            st.warning("❗ Model unsupervised atau preprocessor/label encoders tidak tersedia. Tidak dapat melakukan segmentasi klaster.")
