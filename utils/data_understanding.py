import streamlit as st
import pandas as pd

def show_data_understanding():
    df = pd.read_csv('data/car_prices.csv')

    # === Custom CSS ===
    st.markdown("""
        <style>
            .main-title {
                text-align: center;
                font-size: 2.3em;
                font-weight: bold;
                color: #2c3e50;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                font-size: 1.4em;
                color: #3498db;
                margin-top: -10px;
                margin-bottom: 30px;
            }
            .section-header {
                font-size: 1.3em;
                font-weight: 600;
                color: #3498db;
                margin-top: 25px;
                margin-bottom: 10px;
            }
            .info-box {
                background-color: #f5f7fa;
                color: #2c3e50;
                padding: 16px;
                border-left: 6px solid #3498db;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0 3px 6px rgba(0,0,0,0.05);
                font-size: 1.05em;
            }
            .highlight {
                font-weight: bold;
                color: #2c3e50;
            }
        </style>
    """, unsafe_allow_html=True)

    # === Judul Halaman ===
    st.markdown('<div class="main-title">📊 DATA UNDERSTANDING 📊</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Eksplorasi Awal Dataset</div>', unsafe_allow_html=True)

    # === Dataset Preview ===
    st.markdown('<div class="section-header">🔍 Dataset Preview</div>', unsafe_allow_html=True)
    st.write("Berikut adalah 5 baris pertama dari dataset yang digunakan:")
    st.dataframe(df.head(), use_container_width=True)

    # === Shape of Dataset ===
    st.markdown('<div class="section-header">📝 Ukuran Dataset</div>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="info-box">
            Dataset memiliki <span class="highlight">{df.shape[0]}</span> baris dan 
            <span class="highlight">{df.shape[1]}</span> kolom.
        </div>
    """, unsafe_allow_html=True)

    # === Data Types ===
    st.markdown('<div class="section-header">📋 Tipe Data</div>', unsafe_allow_html=True)
    num_cols = len(df.select_dtypes(include=['int64', 'float64']).columns)
    cat_cols = len(df.select_dtypes(include=['object']).columns)

    st.markdown(f"""
        <div class="info-box">
            Jumlah kolom berdasarkan tipe data:
            <ul>
                <li>Kolom numerik: <span class="highlight">{num_cols}</span></li>
                <li>Kolom kategorikal: <span class="highlight">{cat_cols}</span></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    # === Nama Kolom & Jumlah Nilai Unik ===
    st.markdown('<div class="section-header">🔑 Nama Kolom dan Nilai Unik</div>', unsafe_allow_html=True)
    unique_vals = pd.DataFrame({
        'Kolom': df.columns,
        'Tipe Data': df.dtypes.values,
        'Jumlah Nilai Unik': df.nunique().values
    })
    st.dataframe(unique_vals, use_container_width=True)

    # === Missing Values ===
    st.markdown('<div class="section-header">⚠️ Nilai yang Hilang (Missing Values)</div>', unsafe_allow_html=True)
    missing = df.isnull().sum()
    missing = missing[missing > 0].sort_values(ascending=False)

    if not missing.empty:
        missing_df = pd.DataFrame({
            "Nama Kolom": missing.index,
            "Jumlah Nilai Hilang": missing.values
        })
        st.dataframe(missing_df, use_container_width=True)
    else:
        st.markdown("""
            <div class="info-box">
                Tidak terdapat nilai yang hilang dalam dataset.
            </div>
        """, unsafe_allow_html=True)

    # === Duplicate Rows ===
    st.markdown('<div class="section-header">🔄 Data Duplikat</div>', unsafe_allow_html=True)
    dup_count = df.duplicated().sum()
    st.markdown(f"""
        <div class="info-box">
            Jumlah baris duplikat dalam dataset: <span class="highlight">{dup_count}</span>
        </div>
    """, unsafe_allow_html=True)

    # === Statistik Numerik ===
    st.markdown('<div class="section-header">📈 Statistik Kolom Numerik</div>', unsafe_allow_html=True)
    st.dataframe(df.describe(), use_container_width=True)

    # === Statistik Kategorikal ===
    st.markdown('<div class="section-header">📊 Statistik Kolom Kategorikal</div>', unsafe_allow_html=True)
    st.dataframe(df.describe(include='object'), use_container_width=True)

    # === Korelasi Antar Kolom Numerik ===
    st.markdown('<div class="section-header">📎 Korelasi Antar Kolom Numerik</div>', unsafe_allow_html=True)
    corr = df.select_dtypes(include=['int64', 'float64']).corr()
    st.dataframe(corr, use_container_width=True)

    # === Ringkasan Akhir ===
    st.markdown('<div class="section-header">📌 Kesimpulan Awal</div>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="info-box">
            Dataset terdiri dari berbagai kolom numerik dan kategorikal dengan total <span class="highlight">{df.shape[1]}</span> fitur.
            Terdapat <span class="highlight">{dup_count}</span> baris duplikat dan 
            <span class="highlight">{missing.sum()}</span> nilai yang hilang (jika ada). 
            Korelasi antar fitur numerik telah dianalisis secara awal.
            Tahap selanjutnya adalah eksplorasi visual untuk pemahaman pola dan hubungan antar variabel.
        </div>
    """, unsafe_allow_html=True)
