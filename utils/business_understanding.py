import streamlit as st

def show_business_understanding():

    # === Universal CSS ===
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
                font-size: 1.4em;
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
            .image-container {
                display: flex;
                justify-content: center;
                margin-bottom: 25px;
            }
            .rounded-image {
                border-radius: 12px;
                width: 65%;
                box-shadow: 0 4px 8px rgba(0,0,0,0.08);
            }
        </style>
    """, unsafe_allow_html=True)

    # === Judul dan Subjudul ===
    st.markdown('<div class="main-title">💼 BUSINESS UNDERSTANDING 💼</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Analisis dan Pemodelan Data untuk Pasar Mobil Bekas</div>', unsafe_allow_html=True)

    # === Gambar Placeholder ===
    # Menggunakan gambar yang lebih relevan dengan kendaraan atau analisis data.
    # Anda bisa menggantinya dengan URL gambar mobil bekas, grafik, atau ikon AI yang relevan.
    st.markdown('<div class="image-container"><img class="rounded-image" src="https://www.pngall.com/wp-content/uploads/1/Used-Car.png"></div>', unsafe_allow_html=True) # Contoh: ikon mobil bekas

    # ---
    # === Permasalahan Utama ===
    st.markdown('<div class="section-header">🔍 Permasalahan Utama</div>', unsafe_allow_html=True)
    st.markdown("""
        Dalam industri penjualan mobil bekas, penentuan harga yang akurat dan pemahaman pasar adalah kunci kesuksesan. Penjual seringkali menghadapi tantangan dalam **menetapkan harga jual yang kompetitif namun menguntungkan**, serta **mengidentifikasi segmen pembeli atau karakteristik kendaraan yang paling diminati**. Tanpa insight yang jelas, keputusan penetapan harga bisa bersifat spekulatif, berpotensi mengakibatkan kerugian atau lambatnya penjualan.
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="info-box">
            Ketidakpastian harga jual dan kurangnya pemahaman tentang segmen pasar dapat menghambat efisiensi operasional dan profitabilitas bisnis mobil bekas.
        </div>
    """, unsafe_allow_html=True)

    # ---
    # === Tujuan Proyek ===
    st.markdown('<div class="section-header">🎯 Tujuan Proyek</div>', unsafe_allow_html=True)
    st.markdown("""
        Proyek ini bertujuan untuk mengatasi permasalahan di atas dengan memanfaatkan data historis penjualan mobil bekas melalui pendekatan **Machine Learning**:

        - **Prediksi Harga Jual (Supervised Learning):** Mengembangkan model regresi untuk memprediksi harga jual mobil bekas secara akurat berdasarkan berbagai fitur kendaraan seperti tahun, merek, model, jarak tempuh, kondisi, dan data pasar (MMR). Model ini akan membantu penjual menetapkan harga yang optimal.
        - **Segmentasi Klaster Kendaraan (Unsupervised Learning):** Menerapkan algoritma *clustering* untuk mengidentifikasi segmen atau kelompok mobil bekas dengan karakteristik serupa. Ini akan membantu dalam memahami preferensi pasar, mengoptimalkan inventaris, dan menargetkan strategi pemasaran dengan lebih efektif.

        Dataset akan dianalisis secara menyeluruh untuk menghasilkan insight yang dapat digunakan oleh pengambil keputusan dalam industri ini.
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="info-box">
            Tujuan akhirnya adalah mengubah data mentah penjualan mobil bekas menjadi informasi yang bermakna dan *actionable* untuk pengambilan keputusan bisnis yang lebih cerdas dan menguntungkan.
        </div>
    """, unsafe_allow_html=True)

    # ---
    # === Aspek Penting Proyek ===
    st.markdown('<div class="section-header">🔑 Aspek Penting Proyek</div>', unsafe_allow_html=True)
    st.markdown("""
        1.  <b>Pemahaman Konteks Bisnis:</b> Mengkaji faktor-faktor kunci yang mempengaruhi harga mobil bekas dan karakteristik pembeli/pasar.
        2.  <b>Pemrosesan Data Efisien:</b> Melakukan *feature engineering* dan *preprocessing* data yang optimal (termasuk penanganan kardinalitas tinggi dan optimasi ukuran data) agar siap dianalisis dan dimodelkan.
        3.  <b>Pengembangan dan Validasi Model:</b> Membangun dan mengevaluasi model regresi dan *clustering* menggunakan metrik yang relevan dan teknik validasi yang tepat.
        4.  <b>Interpretasi dan Implementasi Solusi:</b> Menerjemahkan hasil model menjadi insight yang mudah dipahami dan dapat diimplementasikan oleh *stakeholder* di industri penjualan mobil bekas.
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="info-box">
            Keberhasilan proyek ini bergantung pada pemahaman mendalam terhadap masalah bisnis, kemampuan mengelola dan mentransformasi data besar, serta mengaitkan hasil analisis dan model dengan kebutuhan nyata pasar mobil bekas.
        </div>
    """, unsafe_allow_html=True)

    # ---
    # === Manfaat Proyek ===
    st.markdown('<div class="section-header">💡 Manfaat bagi Stakeholder</div>', unsafe_allow_html=True)
    st.markdown("""
        -   **Penetapan Harga Otomatis & Akurat:** Memungkinkan penjual menetapkan harga jual yang optimal, mengurangi risiko kerugian dan mempercepat penjualan.
        -   **Pemahaman Pasar Mendalam:** Mengidentifikasi segmen pasar yang berbeda dan karakteristik kendaraan yang diminati oleh setiap segmen.
        -   **Optimasi Inventaris:** Membantu dalam pengelolaan stok kendaraan yang lebih efisien berdasarkan permintaan pasar yang teridentifikasi.
        -   **Strategi Pemasaran Bertarget:** Memungkinkan kampanye pemasaran yang lebih efektif dengan menargetkan segmen pembeli yang relevan.
        -   **Peningkatan Efisiensi Operasional:** Mengurangi waktu dan upaya yang dihabiskan untuk riset harga manual.
        -   **Dasar Pengambilan Keputusan Strategis:** Memberikan wawasan berbasis data untuk pengembangan strategi bisnis jangka panjang dalam industri mobil bekas.
    """, unsafe_allow_html=True)

    # ---
    # === Kriteria Keberhasilan ===
    st.markdown('<div class="section-header">🏆 Kriteria Keberhasilan</div>', unsafe_allow_html=True)
    st.markdown("""
        Keberhasilan proyek ini akan diukur dari:

        -   **Akurasi Prediksi Harga:** Tingkat kesalahan yang rendah (misalnya, MAE dan RMSE yang kompetitif) pada model *supervised learning*.
        -   **Relevansi Segmentasi:** Kesesuaian dan kejelasan klaster yang dihasilkan oleh model *unsupervised learning* dalam mengelompokkan kendaraan.
        -   **Reduksi Ukuran Model:** Keberhasilan dalam meminimalkan ukuran file model (`.pkl`) untuk efisiensi *deployment*.
        -   **Wawasan yang Dapat Ditindaklanjuti:** Kemampuan untuk menyediakan insight yang dapat langsung digunakan oleh penjual mobil atau pemangku kepentingan lainnya.
        -   **Relevansi Solusi:** Solusi yang diusulkan secara signifikan mengatasi tantangan penetapan harga dan pemahaman pasar yang ada.
    """, unsafe_allow_html=True)