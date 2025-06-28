import streamlit as st
import joblib
import numpy as np
import pandas as pd
import os # Tambahkan import os untuk pengecekan file

def show_prediction_interface():
    st.header("🔍 Try Input New Data")

    st.markdown("""
    Masukkan data kendaraan yang ingin diprediksi harga jualnya.
    Model ini menggunakan kombinasi fitur numerik dan kategorikal.
    """)

    # --- Load model dan preprocessor ---
    # Tentukan jalur relatif ke direktori 'models'
    base_path = 'models/' 

    supervised_model_path = os.path.join(base_path, 'random_forest_regressor.pkl')
    supervised_preprocessor_path = os.path.join(base_path, 'preprocessor_supervised.pkl')
    unsupervised_model_path = os.path.join(base_path, 'kmeans_clusterer.pkl')
    unsupervised_preprocessor_path = os.path.join(base_path, 'preprocessor_unsupervised.pkl')

    model_supervised = None
    preprocessor_supervised = None
    supervised_label_encoders = {}

    model_unsupervised = None
    preprocessor_unsupervised = None
    unsupervised_label_encoders = {}
    cluster_descriptions = {} 

    try:
        # Muat Supervised Models
        if os.path.exists(supervised_preprocessor_path):
            loaded_supervised_objects = joblib.load(supervised_preprocessor_path)
            preprocessor_supervised = loaded_supervised_objects['preprocessor']
            supervised_label_encoders = loaded_supervised_objects.get('label_encoders', {})
            st.success("✔ Preprocessor supervised dan Label Encoders berhasil dimuat.")
        else:
            st.warning(f"❗ Peringatan: File preprocessor supervised tidak ditemukan di {supervised_preprocessor_path}. Prediksi harga tidak akan berfungsi.")

        if os.path.exists(supervised_model_path):
            model_supervised = joblib.load(supervised_model_path)
            st.success("✔ Model supervised berhasil dimuat.")
        else:
            st.warning(f"❗ Peringatan: File model supervised tidak ditemukan di {supervised_model_path}. Prediksi harga tidak akan berfungsi.")

        # Muat Unsupervised Models
        if os.path.exists(unsupervised_preprocessor_path):
            loaded_unsupervised_objects = joblib.load(unsupervised_preprocessor_path)
            preprocessor_unsupervised = loaded_unsupervised_objects['preprocessor']
            unsupervised_label_encoders = loaded_unsupervised_objects.get('label_encoders', {})
            # Asumsi cluster_descriptions disimpan di dalam bundle preprocessor unsupervised
            cluster_descriptions = loaded_unsupervised_objects.get('cluster_descriptions', {
                0: "Klaster 0 (Lower Tier): Segmen ini didominasi oleh mobil dengan [Harga Jual Terendah], [Kondisi Kurang Baik], dan [Odometer Paling Tinggi]. Ini adalah segmen dengan nilai terendah di pasar bekas.",
                1: "Klaster 1: Segmen ini cenderung memiliki mobil dengan [Harga Jual Sedang], [Kondisi Rata-Rata], dan [Odometer Sedang]. Mereka mewakili sebagian besar pasar bekas dengan nilai yang seimbang.",
                2: "Klaster 2: Klaster ini berisi mobil dengan [Harga Jual Cukup Tinggi], [Kondisi Baik], dan [Odometer Rendah]. Mobil di segmen ini menawarkan keseimbangan antara kualitas dan harga yang lebih premium.",
                3: "Klaster 3 (Upper Tier): Ini adalah segmen mobil premium dengan [Harga Jual Paling Tinggi], [Kondisi Sangat Baik atau Baru], dan [Odometer Paling Rendah]. Mobil di klaster ini mewakili penawaran terbaik atau termahal di pasar.",
            })
            st.success("✔ Preprocessor unsupervised, Label Encoders, dan Deskripsi Klaster berhasil dimuat.")
        else:
            st.warning(f"❗ Peringatan: File preprocessor unsupervised tidak ditemukan di {unsupervised_preprocessor_path}. Segmentasi klaster tidak akan berfungsi.")

        if os.path.exists(unsupervised_model_path):
            model_unsupervised = joblib.load(unsupervised_model_path)
            st.success("✔ Model unsupervised berhasil dimuat.")
        else:
            st.warning(f"❗ Peringatan: File model unsupervised tidak ditemukan di {unsupervised_model_path}. Segmentasi klaster tidak akan berfungsi.")

    except Exception as e:
        st.error(f"❌ Gagal memuat model atau preprocessor: {e}")
        return 

    # --- Fungsi Prediksi dan Segmentasi (Disesuaikan untuk Streamlit) ---
    def predict_car_price(input_data_df, preprocessor, model, label_encoders_dict):
        processed_df = input_data_df.copy()
        try:
            for col, le in label_encoders_dict.items():
                if col in processed_df.columns:
                    # Pastikan nilai ada di kelas encoder, jika tidak, gunakan label 'Other_{col}'
                    # Jika 'Other_{col}' juga tidak ada di encoder.classes_, tambahkan secara dinamis
                    # atau pastikan pra-pemrosesan di notebook sudah menambahkan ini secara konsisten.
                    unknown_label_str = f'Other_{col}'
                    if unknown_label_str not in le.classes_: 
                         le.classes_ = np.append(le.classes_, unknown_label_str)

                    processed_df[col] = processed_df[col].astype(str).apply(
                        lambda x: x if x in le.classes_ else unknown_label_str
                    )
                    processed_df[col] = le.transform(processed_df[col])

            processed_input = preprocessor.transform(processed_df)
            predicted_price = model.predict(processed_input)[0]
            return predicted_price
        except Exception as e:
            st.error(f"Error saat prediksi harga: {e}")
            return None

    def segment_car_cluster(input_data_df, preprocessor, model, label_encoders_dict):
        processed_df = input_data_df.copy()
        try:
            for col, le in label_encoders_dict.items():
                if col in processed_df.columns:
                    unknown_label_str = f'Other_{col}'
                    if unknown_label_str not in le.classes_:
                         le.classes_ = np.append(le.classes_, unknown_label_str)

                    processed_df[col] = processed_df[col].astype(str).apply(
                        lambda x: x if x in le.classes_ else unknown_label_str
                    )
                    processed_df[col] = le.transform(processed_df[col])

            # *** Sesuaikan daftar fitur ini dengan yang digunakan untuk UNsupervised Processing ***
            # Pastikan kolom-kolom ini ada di input_data_df dan dalam urutan yang benar
            features_for_unsupervised = [
                'mmr', 'sellingprice', 'year', 'odometer', 'condition',
                'body', 'make', 'model', 'trim', 'seller'
            ]
            
            # Pastikan hanya fitur yang relevan yang masuk ke preprocessor unsupervised
            # Gunakan .reindex(columns=...) untuk memastikan urutan kolom sama seperti saat training
            input_for_cluster_seg = processed_df[features_for_unsupervised]

            processed_input = preprocessor.transform(input_for_cluster_seg)
            cluster_label = model.predict(processed_input)[0]
            return cluster_label
        except Exception as e:
            st.error(f"Error saat segmentasi klaster: {e}")
            return None

    # --- Form Input ---
    with st.form("form_input"):
        st.subheader("🧾 Masukkan Data Kendaraan")

        col1, col2 = st.columns(2)

        with col1:
            year = st.number_input("Tahun Kendaraan", min_value=1990, max_value=2025, value=2019)
            odometer = st.number_input("Odometer (mil)", min_value=0, value=67282)
            # mmr dan sellingprice perlu diisi untuk clustering juga
            mmr = st.number_input("MMR (Market Value)", min_value=1000, value=37500.0)
            sellingprice = st.number_input("Selling Price (untuk Clustering)", min_value=1000, value=47750.0) # Penting untuk clustering
            condition = st.selectbox("Kondisi Kendaraan (1=terburuk, 5=terbaik)", [1, 2, 3, 4, 5], index=3) # index 3 = 4

        with col2:
            make = st.selectbox("Merk", ['Other_make', 'toyota', 'honda', 'ford', 'chevrolet', 'Volvo'], index=5) # Tambah Volvo
            model_car = st.selectbox("Model", ['Other_model', 'camry', 'accord', 'S60'], index=3) # Tambah S60
            trim = st.selectbox("Trim", ['Other_trim', 'LE', 'SE', 'LX'], index=3) # Tambah LX
            body = st.selectbox("Jenis Body", ['Other_body', 'sedan', 'suv', 'pickup'], index=1) # index 1 = sedan
            transmission = st.selectbox("Transmisi", ['Other_transmission', 'automatic', 'manual'], index=1) # index 1 = automatic
            state = st.selectbox("Negara Bagian", ['Other_state', 'CA', 'TX', 'NY'], index=1) # index 1 = CA
            color = st.selectbox("Warna", ['Other_color', 'black', 'white', 'silver'], index=1) # index 1 = white
            interior = st.selectbox("Interior", ['Other_interior', 'black', 'gray', 'beige'], index=0) # index 0 = black
            seller = st.selectbox("Penjual", ['Other_seller', 'CARVANA', 'DriveTime', 'volvo na rep/world omni'], index=3) # Tambah penjual

        submitted = st.form_submit_button("🔮 Prediksi & Segmentasi")

    if submitted:
        # Buat DataFrame satu baris dari input
        input_dict = {
            'year': [year],
            'make': [make],
            'model': [model_car],
            'trim': [trim],
            'body': [body],
            'transmission': [transmission],
            'state': [state],
            'condition': [condition],
            'odometer': [odometer],
            'color': [color],
            'interior': [interior],
            'seller': [seller],
            'mmr': [mmr],
            'sellingprice': [sellingprice]
        }
        input_df = pd.DataFrame(input_dict)

        st.subheader("### Hasil Prediksi dan Segmentasi ###")

        # --- Prediksi Harga ---
        if model_supervised and preprocessor_supervised and supervised_label_encoders:
            # Untuk prediksi harga, 'sellingprice' adalah target, jadi kita bisa menghilangkannya dari input
            input_for_price_pred = input_df.drop(columns=['sellingprice'], errors='ignore')
            predicted_price = predict_car_price(input_for_price_pred, preprocessor_supervised, model_supervised, supervised_label_encoders)

            if predicted_price is not None:
                st.success(f"💰 Estimasi Harga Jual Kendaraan: **${predicted_price:,.2f}**")
            else:
                st.error("❌ Prediksi harga gagal.")
        else:
            st.warning("❗ Model supervised atau preprocessor/label encoders tidak tersedia. Tidak dapat melakukan prediksi harga.")

        st.write("---")

        # --- Segmentasi Klaster ---
        if model_unsupervised and preprocessor_unsupervised:
            cluster_label = segment_car_cluster(input_df, preprocessor_unsupervised, model_unsupervised, unsupervised_label_encoders)
            if cluster_label is not None:
                st.info(f"🏷️ Mobil ini masuk ke Klaster: **{cluster_label}**")
                description = cluster_descriptions.get(cluster_label, "Tidak ada deskripsi spesifik untuk klaster ini. Anda bisa menganalisis karakteristik rata-rata dari klaster ini untuk memahami segmen pasar mobil ini.")
                st.markdown(f"**👉 {description}**")
            else:
                st.error("❌ Segmentasi klaster gagal.")
        else:
            st.warning("❗ Model unsupervised atau preprocessor/label encoders tidak tersedia. Tidak dapat melakukan segmentasi klaster.")
