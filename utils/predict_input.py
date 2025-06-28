import streamlit as st
import joblib
import numpy as np
import pandas as pd

def show_prediction_interface():
    st.header("🔍 Try Input New Data")

    st.markdown("""
    Masukkan data kendaraan yang ingin diprediksi harga jualnya. 
    Model ini menggunakan kombinasi fitur numerik dan kategorikal.
    """)

    # Load model dan preprocessor
    try:
        model = joblib.load('models/random_forest_regressor.pkl')
        preprocess_bundle = joblib.load('models/preprocessor_supervised.pkl')
        preprocessor = preprocess_bundle['preprocessor']
        label_encoders = preprocess_bundle['label_encoders']
        feature_names = preprocess_bundle['processed_feature_names']
    except Exception as e:
        st.error(f"❌ Gagal memuat model atau preprocessor: {e}")
        return

    # Form Input
    with st.form("form_input"):
        st.subheader("🧾 Masukkan Data Kendaraan")

        col1, col2 = st.columns(2)

        with col1:
            year = st.number_input("Tahun Kendaraan", min_value=1990, max_value=2025, value=2015)
            odometer = st.number_input("Odometer (mil)", min_value=0, value=50000)
            mmr = st.number_input("MMR (Market Value)", min_value=1000, value=12000)
            condition = st.selectbox("Kondisi Kendaraan (1=terburuk, 5=terbaik)", [1, 2, 3, 4, 5])

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


        submitted = st.form_submit_button("🔮 Prediksi Harga")

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

        }

        input_df = pd.DataFrame(input_dict)

         # 🔧 Tangani label encoder dengan unseen value
        for col, encoder in label_encoders.items():
            if col in input_df.columns:
                unknown_label = f'Other_{col}'
                if unknown_label not in encoder.classes_:
                    encoder.classes_ = np.append(encoder.classes_, unknown_label)

                input_df[col] = input_df[col].astype(str).apply(
                    lambda x: x if x in encoder.classes_ else unknown_label
                )
                input_df[col] = encoder.transform(input_df[col])

        # Transformasi dan prediksi
        try:
            input_processed = preprocessor.transform(input_df)
            prediction = model.predict(input_processed)[0]
            st.success(f"💰 Estimasi Harga Jual Kendaraan: **${prediction:,.2f}**")
        except Exception as e:
            st.error(f"❌ Gagal melakukan prediksi: {e}")
