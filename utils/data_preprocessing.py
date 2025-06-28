import streamlit as st
import pandas as pd
import numpy as np # Pastikan numpy diimpor jika belum

# Fungsi dummy untuk show_data_preprocessing, Anda akan menempatkannya di file terpisah
# atau di sini jika ini adalah bagian dari file utama Streamlit Anda.

def show_data_preprocessing():
    # === CSS Styling (sama seperti sebelumnya) ===
    st.markdown("""
    <style>
        /* Gaya global untuk memastikan warna teks dasar */
        body {
            color: #2c3e50 !important; /* Warna teks default untuk seluruh body */
        }
        p, li, b { /* Target paragraf, daftar, dan bold text secara umum */
            color: #2c3e50 !important; /* Pastikan teks ini juga gelap */
        }

        .main-title {
            text-align: center;
            font-size: 2.3em;
            font-weight: bold;
            color: #2c3e50 !important; /* Pastikan warna ini diterapkan */
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 1.4em;
            color: #3498db !important;
            margin-top: -10px;
            margin-bottom: 30px;
        }
        .section-header {
            font-size: 1.4em;
            font-weight: 600;
            color: #3498db !important;
            margin-top: 25px;
            margin-bottom: 10px;
        }
        .info-box {
            background-color: #f5f7fa; /* Latar belakang terang */
            color: #2c3e50 !important; /* Teks gelap */
            padding: 16px;
            border-left: 6px solid #3498db;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 3px 6px rgba(0,0,0,0.05);
            font-size: 1.05em;
        }
        .highlight-text { /* Gaya baru untuk teks penting */
            background-color: #e8f3f8; /* Latar belakang terang */
            padding: 10px;
            border-radius: 8px;
            font-weight: bold;
            color: #1f618d !important; /* Teks gelap */
        }
        .code-block {
            background-color: #eeeeee;
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
            white-space: pre-wrap;
            word-wrap: break-word;
            color: #333333 !important; /* Tambahkan warna teks untuk blok kode */
        }
    </style>
    """, unsafe_allow_html=True)

    # === Judul dan Subjudul ===
    st.markdown('<div class="main-title">🛠️ DATA PREPROCESSING 🛠️</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Transformasi Data untuk Analisis dan Pemodelan yang Optimal</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        Tahap <b>Data Preprocessing</b> adalah fondasi penting dalam setiap proyek <i>Data Science</i>. Pada tahap ini, data mentah dibersihkan, diubah, dan distrukturkan agar siap untuk analisis lebih lanjut dan pemodelan Machine Learning. Proses ini vital untuk memastikan kualitas, konsistensi, dan relevansi data, serta mengoptimalkan kinerja model.
    </div>
    """, unsafe_allow_html=True)

    # === Dropdown untuk Memilih Tipe Preprocessing ===
    st.markdown('<div class="section-header">Pilih Tahapan Preprocessing yang Ingin Anda Pelajari:</div>', unsafe_allow_html=True)
    preprocessing_type = st.selectbox(
        " ", # Label kosong agar tidak ada label redundan di atas dropdown
        ["Pilih Tipe Preprocessing", "Base Processing", "Supervised Processing", "Unsupervised Processing"],
        index=0 # Pilih item pertama sebagai default
    )

    # === Konten Berdasarkan Pilihan Dropdown ===
    if preprocessing_type == "Base Processing":
        st.markdown('<div class="section-header" style="font-size: 2em; font-weight: bold; color: #4CAF50; margin-top: 1em; margin-bottom: 0.5em;">Base Processing (Pemrosesan Dasar)</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #e0f7fa; padding: 15px; border-radius: 8px; border-left: 5px solid #00BCD4; margin-bottom: 1em;">
            <b>Base Processing</b> adalah langkah awal yang fundamental untuk membersihkan dan mempersiapkan dataset mentah. Tujuannya adalah menangani inkonsistensi, nilai yang hilang, dan format yang tidak sesuai, sehingga data menjadi bersih dan terstruktur untuk analisis lebih lanjut.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #f0f4c3; padding: 15px; border-radius: 8px; margin-bottom: 1em;">
            Tahapan ini mencakup operasi kunci yang diterapkan pada dataset penjualan mobil bekas:
            <ul>
                <li><b>Pemuatan Data:</b> Dataset mentah dimuat dari file CSV.</li>
                <li><b>Penghapusan Kolom Tidak Relevan:</b> Kolom <code>'vin'</code> (Vehicle Identification Number) dan <code>'saledate'</code> dihapus karena dianggap tidak relevan secara langsung untuk tujuan prediksi harga atau segmentasi, dan juga untuk mengurangi dimensi data awal.</li>
                <li><b>Imputasi Nilai Hilang:</b>
                    <ul>
                        <li>Untuk kolom numerik (seperti <code>'condition'</code>, <code>'odometer'</code>, <code>'mmr'</code>, <code>'sellingprice'</code>, <code>'year'</code>), nilai yang hilang diisi menggunakan <b>median</b> dari kolom tersebut.</li>
                        <li>Untuk kolom kategorikal (seperti <code>'make'</code>, <code>'model'</code>, <code>'trim'</code>, <code>'body'</code>, <code>'transmission'</code>, <code>'state'</code>, <code>'color'</code>, <code>'interior'</code>, <code>'seller'</code>), nilai yang hilang diisi menggunakan <b>modus (nilai paling sering muncul)</b> dari kolom tersebut.</li>
                    </ul>
                </li>
            </ul>
            <br>
            <h4>Pustaka Python yang Digunakan:</h4>
            <ul>
                <li><code><b>pandas</b></code>: Untuk manipulasi dan analisis data (memuat CSV, menghapus kolom, menangani DataFrame).</li>
                <li><code><b>numpy</b></code>: Digunakan bersama pandas untuk operasi numerik, terutama dalam mengidentifikasi kolom numerik dan kategorikal.</li>
                <li><code><b>sklearn.impute.SimpleImputer</b></code>: Untuk mengisi nilai-nilai yang hilang (strategi median dan modus).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #d4edda; padding: 15px; border-radius: 8px; border-left: 5px solid #28a745; font-weight: bold;">
            Hasil dari <b>Base Processing</b> adalah dataset yang bersih dari nilai hilang, dengan kolom-kolom yang relevan, dan siap untuk diproses lebih lanjut pada tahapan Supervised atau Unsupervised Processing.
        </div>
        """, unsafe_allow_html=True)

    elif preprocessing_type == "Supervised Processing":
        st.markdown('<div class="section-header" style="font-size: 2em; font-weight: bold; color: #4CAF50; margin-top: 1em; margin-bottom: 0.5em;">Supervised Processing (Untuk Model Prediksi Harga)</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #e0f7fa; padding: 15px; border-radius: 8px; border-left: 5px solid #00BCD4; margin-bottom: 1em;">
            Setelah <b>Base Processing</b>, data disiapkan secara khusus untuk model <b>Supervised Learning</b> yang bertujuan memprediksi <b>harga jual mobil</b>. Proses ini fokus pada transformasi fitur agar optimal untuk algoritma regresi, sekaligus menjaga ukuran model tetap ringkas.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #f0f4c3; padding: 15px; border-radius: 8px; margin-bottom: 1em;">
            Langkah-langkah utama yang dilakukan:
            <ul>
                <li><b>Pengelompokan Kategori Langka:</b> Kolom kategorikal dengan kardinalitas sangat tinggi (seperti <code>'model'</code>, <code>'trim'</code>, <code>'seller'</code>) dikelompokkan. Nilai-nilai yang sangat jarang muncul digabungkan ke dalam kategori 'Other'. Ini secara drastis mengurangi jumlah kolom yang dihasilkan setelah One-Hot Encoding dan sangat krusial untuk menjaga ukuran model Random Forest tetap kecil (dari GB menjadi MB).</li>
                <li><b>Label Encoding:</b> Kolom kategorikal yang sudah dikelompokkan (<code>'model'</code>, <code>'trim'</code>, <code>'seller'</code>) diubah menjadi representasi numerik ordinal. Ini cocok untuk fitur dengan urutan implisit atau saat ingin menjaga dimensi lebih rendah dari One-Hot Encoding.</li>
                <li><b>One-Hot Encoding:</b> Kolom kategorikal dengan kardinalitas rendah hingga sedang (misalnya <code>'make'</code>, <code>'body'</code>, <code>'transmission'</code>, <code>'state'</code>, <code>'color'</code>, <code>'interior'</code>) diubah menjadi fitur biner.</li>
                <li><b>Standard Scaling:</b> Semua fitur numerik (termasuk hasil Label Encoding dan fitur asli seperti <code>'mmr'</code>, <code>'odometer'</code>, <code>'condition'</code>, <code>'year'</code>) dinormalisasi agar memiliki rata-rata nol dan variansi satu. Ini penting untuk algoritma yang sensitif terhadap skala fitur.</li>
                <li><b>Optimasi Tipe Data:</b> Menyesuaikan kembali tipe data kolom numerik yang telah diproses menjadi representasi yang lebih hemat memori (<code>float32</code>).</li>
            </ul>
            <br>
            <h4>Pustaka Python yang Digunakan:</h4>
            <ul>
                <li><code><b>pandas</b></code>: Untuk manipulasi dan analisis data.</li>
                <li><code><b>numpy</b></code>: Untuk operasi numerik.</li>
                <li><code><b>sklearn.preprocessing.LabelEncoder</b></code>: Untuk mengonversi label kategorikal ke numerik.</li>
                <li><code><b>sklearn.preprocessing.StandardScaler</b></code>: Untuk menstandarkan fitur numerik.</li>
                <li><code><b>sklearn.preprocessing.OneHotEncoder</b></code>: Untuk mengubah fitur kategorikal ke representasi one-hot.</li>
                <li><code><b>sklearn.compose.ColumnTransformer</b></code>: Untuk menerapkan berbagai transformasi ke kolom yang berbeda.</li>
                <li><code><b>sklearn.pipeline.Pipeline</b></code>: Untuk mengurutkan langkah-langkah transformasi.</li>
                <li><code><b>joblib</b></code>: Untuk menyimpan dan memuat objek Python (seperti preprocessor).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #d4edda; padding: 15px; border-radius: 8px; border-left: 5px solid #28a745; font-weight: bold;">
            Fokus utama pada tahap ini adalah <b>reduksi dimensi cerdas</b> (melalui pengelompokan kategori dan pemilihan encoding) dan <b>optimasi tipe data</b>. Strategi ini terbukti efektif dalam menghasilkan model Supervised (Random Forest Regressor) yang sangat ringkas, berubah dari ukuran gigabyte menjadi hanya belasan megabyte, tanpa mengorbankan performa secara signifikan.
        </div>
        """, unsafe_allow_html=True)

    elif preprocessing_type == "Unsupervised Processing":
        st.markdown('<div class="section-header" style="font-size: 2em; font-weight: bold; color: #4CAF50; margin-top: 1em; margin-bottom: 0.5em;">Unsupervised Processing (Untuk Model Segmentasi Klaster)</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #e0f7fa; padding: 15px; border-radius: 8px; border-left: 5px solid #00BCD4; margin-bottom: 1em;">
            Setelah <b>Base Processing</b>, data disiapkan secara khusus untuk model <b>Unsupervised Learning</b>, khususnya untuk <b>segmentasi klaster kendaraan</b>. Tahap ini berfokus pada fitur-fitur yang paling relevan untuk menemukan pola tersembunyi dalam data tanpa label target.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #f0f4c3; padding: 15px; border-radius: 8px; margin-bottom: 1em;">
            Langkah-langkah utama yang dilakukan:
            <ul>
                <li><b>Pemuatan Data Dasar:</b> Dataset yang telah melalui *Base Processing* (<code>base_processed_data.csv</code>) dimuat sebagai input.</li>
                <li><b>Seleksi Fitur untuk Klastering:</b> Hanya fitur-fitur yang paling relevan untuk tujuan segmentasi klaster yang dipilih. Berdasarkan analisis, fitur-fitur ini meliputi <code>'mmr'</code>, <code>'sellingprice'</code>, <code>'year'</code>, <code>'odometer'</code>, <code>'condition'</code>, <code>'body'</code>, dan <code>'make'</code>. Perlu dicatat bahwa <code>'sellingprice'</code> di sini diperlakukan sebagai fitur input untuk klastering, bukan sebagai target.</li>
                <li><b>Pengelompokan Kategori Langka (Lebih Agresif):</b> Untuk kolom kategorikal yang dipilih (<code>'make'</code>, <code>'body'</code>), kategori yang jarang muncul dikelompokkan secara lebih agresif ke dalam kategori 'Other_kolom_nama'. Ini bertujuan untuk mengurangi dimensi fitur yang dihasilkan setelah One-Hot Encoding, yang penting untuk efisiensi model unsupervised seperti K-Means.</li>
                <li><b>Column Transformation:</b> Sebuah <code>ColumnTransformer</code> dibangun untuk menerapkan transformasi berbeda pada jenis kolom yang berbeda dalam fitur-fitur yang dipilih:
                    <ul>
                        <li><b>Standard Scaling:</b> Kolom numerik yang dipilih (<code>'mmr'</code>, <code>'sellingprice'</code>, <code>'year'</code>, <code>'odometer'</code>, <code>'condition'</code>) dinormalisasi menggunakan <code>StandardScaler</code> untuk menstandarkan skala fitur.</li>
                        <li><b>One-Hot Encoding:</b> Kolom kategorikal yang dipilih (<code>'body'</code>, <code>'make'</code>) diubah menjadi representasi biner menggunakan <code>OneHotEncoder</code> (dengan <code>handle_unknown='ignore'</code> dan <code>drop='first'</code>).</li>
                    </ul>
                </li>
                <li><b>Optimasi Tipe Data:</b> Tipe data dari kolom-kolom dalam DataFrame yang telah diproses dioptimalkan menjadi representasi yang lebih hemat memori (<code>float32</code> atau integer yang lebih kecil jika memungkinkan).</li>
                <li><b>Penyimpanan Hasil:</b>
                    <ul>
                        <li>DataFrame fitur yang telah diproses disimpan ke <code>unsupervised_ready_data.csv</code>.</li>
                        <li>Objek <code>ColumnTransformer</code> (<code>preprocessor_unsupervised</code>) yang digunakan disimpan ke <code>preprocessor_unsupervised.pkl</code>. Ini penting agar transformasi yang sama dapat diterapkan pada data baru saat melakukan inferensi klaster.</li>
                    </ul>
                </li>
            </ul>
            <br>
            <h4>Pustaka Python yang Digunakan:</h4>
            <ul>
                <li><code><b>pandas</b></code>: Untuk manipulasi dan analisis data.</li>
                <li><code><b>numpy</b></code>: Untuk operasi numerik.</li>
                <li><code><b>sklearn.preprocessing.StandardScaler</b></code>: Untuk menstandarkan fitur numerik.</li>
                <li><code><b>sklearn.preprocessing.OneHotEncoder</b></code>: Untuk mengubah fitur kategorikal ke representasi one-hot.</li>
                <li><code><b>sklearn.compose.ColumnTransformer</b></code>: Untuk menerapkan berbagai transformasi ke kolom yang berbeda.</li>
                <li><code><b>sklearn.pipeline.Pipeline</b></code>: Untuk mengurutkan langkah-langkah transformasi (meskipun tidak secara eksplisit digunakan di ColumnTransformer, ia adalah bagian dari ekosistem `sklearn`).</li>
                <li><code><b>joblib</b></code>: Untuk menyimpan dan memuat objek Python (seperti preprocessor).</li>
                <li><code><b>sys</b></code>: Digunakan untuk mendapatkan informasi lingkungan Python (opsional, untuk debugging).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #d4edda; padding: 15px; border-radius: 8px; border-left: 5px solid #28a745; font-weight: bold;">
            Hasil dari <b>Unsupervised Processing</b> adalah dataset yang siap digunakan untuk melatih model klastering, serta objek transformasi yang dapat digunakan kembali untuk data baru.
        </div>
        """, unsafe_allow_html=True)

    else: # Default state when "Pilih Tipe Preprocessing" is selected
        st.info("Silakan pilih salah satu tahapan preprocessing dari dropdown di atas untuk melihat penjelasannya.")
