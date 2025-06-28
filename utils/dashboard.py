import streamlit as st

def show_dashboard():

    # === CSS Styling ===
    st.markdown("""
        <style>
            .main-title {
                font-size: 2.5em;
                font-weight: 700;
                color: #2c3e50;
                margin-bottom: 0.5em;
            }
            .section-title {
                font-size: 1.6em;
                font-weight: 600;
                color: #2980b9;
                margin-top: 1.5em;
                margin-bottom: 0.5em;
            }
            .content-box {
                background-color: #f9f9f9;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
                margin-bottom: 20px;
                color: #2c3e50; /* Tambahkan warna teks lebih gelap */
            }
            .anggota {
                font-size: 1.05em;
                margin-bottom: 0.3em;
            }
            .highlight {
                background-color: #ecf0f1;
                padding: 1em;
                border-left: 6px solid #3498db;
                border-radius: 8px;
                font-size: 1.1em;
                color: #2c3e50; /* Tambahkan warna teks lebih gelap */
            }
        </style>
    """, unsafe_allow_html=True)

    # === Judul Dashboard ===
    st.markdown('<div class="main-title">📊 Dashboard Proyek Data Analysis</div>', unsafe_allow_html=True)

    # ---
    # === Judul Proyek ===
    st.markdown('<div class="section-title">📝 Judul Proyek</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="content-box">
            <b>Analisis dan Prediksi Harga Jual Mobil Bekas serta Segmentasi Pasar Menggunakan Machine Learning</b>
        </div>
    """, unsafe_allow_html=True)

    # ---
    # === Deskripsi Proyek ===
    st.markdown('<div class="section-title">📚 Deskripsi Singkat Proyek</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="highlight">
            Proyek ini didedikasikan untuk menganalisis dataset ekstensif yang berisi informasi tentang **mobil bekas** di pasar, dengan tujuan utama untuk memberikan wawasan yang mendalam dan solusi prediktif. Kami menggunakan pendekatan **Machine Learning** untuk mencapai dua objektif utama:<br><br>
            🔹 **Supervised Learning (Regresi):** Mengembangkan model untuk secara akurat memprediksi **harga jual mobil bekas** berdasarkan berbagai fitur. Ini memungkinkan penjual menetapkan harga yang optimal dan kompetitif.<br>
            🔹 **Unsupervised Learning (Clustering):** Mengidentifikasi **segmen-segmen alami atau kelompok-kelompok kendaraan** dengan karakteristik serupa. Ini membantu dalam memahami preferensi pasar dan merumuskan strategi pemasaran yang lebih bertarget.<br><br>
            Selain itu, proyek ini juga menyediakan antarmuka interaktif yang memungkinkan pengguna untuk menguji input kendaraan baru dan melihat hasil prediksi harga atau mengidentifikasi segmen klaster secara langsung.
        </div>
    """, unsafe_allow_html=True)

    # === Daftar Anggota Kelompok ===
    st.markdown('<div class="section-title">👥 Anggota Kelompok</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="anggota">1. Agung Nur Hakim Somantri (220102008)</div>', unsafe_allow_html=True)
        st.markdown('<div class="anggota">2. Fauzi Zamhur Darmawan (220102036)</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="anggota">3. Melani Nurazizah (220102045)</div>', unsafe_allow_html=True)
        st.markdown('<div class="anggota">4. Tegar Wirasatya Al Ashar K (220102083)</div>', unsafe_allow_html=True)