import streamlit as st

def show_unsupervised_result():
    st.markdown("## 📊 Hasil Preprocessing untuk Modeling Unsupervised")
    
    st.info("""
    Proses preprocessing unsupervised dimulai dengan memuat data dari `base_processed_data.csv` yang terdiri dari **558.837 baris** dan **14 kolom**. 
    Tujuannya adalah menyiapkan data untuk model clustering seperti **K-Means**, dengan menjaga keseimbangan antara relevansi fitur dan efisiensi pemrosesan.
    """)

    st.subheader("✅ Fitur yang Digunakan")
    st.markdown("""
    - **Fitur numerik:** `mmr`, `sellingprice`, `year`, `odometer`, `condition`  
    - **Fitur kategorikal:** `body`, `make`
    """)

    st.subheader("🧹 Pengelompokan Kategori Langka (Aggressive Grouping)")
    st.markdown("""
    Untuk mengurangi kompleksitas:
    - Kolom `make` dikelompokkan menjadi **26** kategori (Top 25 + 'Other') dari 96 nilai unik.
    - Kolom `body` dikelompokkan menjadi **11** kategori dari 87 nilai unik.
    """)

    st.subheader("⚙️ Transformasi Fitur")
    st.markdown("""
    - Kolom numerik dinormalisasi menggunakan **Standard Scaler**.
    - Kolom kategorikal diencode menggunakan **One-Hot Encoding**.
    - Hasil akhir menghasilkan **40 fitur** (5 numerik + 35 kategorikal).
    """)

    st.subheader("📉 Efisiensi Memori")
    st.markdown("""
    - Ukuran memori awal: **170.54 MB**  
    - Ukuran setelah optimasi: **85.27 MB**  
    - **Hemat memori sebesar 50%**
    """)

    st.subheader("📂 Output yang Disimpan")
    st.markdown("""
    - Data hasil transformasi disimpan ke: `../data/unsupervised_ready_data.csv`  
    - Preprocessor disimpan ke: `../models/preprocessor_unsupervised.pkl`
    """)

    st.success("Data berhasil disiapkan untuk modeling unsupervised. Siap digunakan dalam algoritma clustering.")
