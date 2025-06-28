import streamlit as st

def show_supervised_result():
    st.markdown("## 🧠 Hasil Preprocessing untuk Modeling Supervised")
    st.info("""
    Proses ini menyiapkan data untuk *supervised learning* seperti regresi harga mobil. 
    Tahapan ini fokus pada transformasi fitur agar efisien, akurat, dan ringan untuk model pembelajaran mesin.
    """)

    st.subheader("📥 Jalur File")
    st.markdown("""
    - **Input CSV:** `../data/base_processed_data.csv`  
    - **Output CSV:** `../data/supervised_ready_data.csv`  
    - **Output Preprocessor:** `../models/preprocessor_supervised.pkl`
    """)

    st.subheader("📊 Informasi Dataset Awal")
    st.markdown("- Jumlah baris: **558.837**")
    st.markdown("- Jumlah kolom: **14**")

    st.subheader("🔍 Pengelompokan Kategori Langka")
    st.markdown("""
    Untuk menghindari tingginya dimensi data akibat **One-Hot Encoding**, dilakukan pengelompokan kategori langka:

    - `seller` → Top 25  
    - `model` → Top 25  
    - `trim` → Top 25  
    - `make` → Top 20  
    - `state` → Top 15  
    - `color` → Top 10  
    - `body` → Top 5  
    """)

    st.markdown("> Setelah pengelompokan, fitur-fitur kategorikal jadi lebih ringkas dan tetap informatif.")

    st.subheader("🛠️ Teknik Encoding")
    st.markdown("""
    - **Label Encoding:** Untuk kolom ber-kardinalitas tinggi: `model`, `trim`, `seller`.  
    - **One-Hot Encoding:** Untuk kolom ber-kardinalitas rendah: `make`, `body`, `transmission`, `state`, `color`, `interior`.
    """)

    st.subheader("📏 Scaling dan Optimasi")
    st.markdown("""
    - Kolom numerik seperti `year`, `odometer`, `mmr`, `condition` dan hasil label encoding discaling dengan `StandardScaler`.
    - Optimasi tipe data dilakukan untuk menghemat memori.
    """)

    st.subheader("📦 Hasil Akhir")
    st.markdown("""
    - Jumlah fitur hasil preprocessing: **76 fitur input + 1 target** = **77 kolom**
    - Ukuran data akhir: `(558837, 77)`
    - Penghematan memori: **50%**
    """)

    st.success("✅ Data berhasil disimpan dan siap digunakan untuk pelatihan model supervised learning seperti Random Forest Regressor.")
