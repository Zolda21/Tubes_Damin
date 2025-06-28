import streamlit as st

def show_supervised_overview():
    st.markdown("## 🤖 Overview Preprocessing: Supervised Learning")
    st.markdown("""
Preprocessing supervised dilakukan untuk menyiapkan data sebelum digunakan dalam model regresi atau klasifikasi. Berikut alur dan contoh implementasinya.
    """)

    st.markdown("### 🔄 Alur Proses:")
    st.markdown("""
1. Load data awal dari CSV
2. Cek & kelompokkan kategori langka
3. Label Encoding untuk fitur kategorikal kardinalitas tinggi
4. One-Hot Encoding untuk fitur kategorikal kardinalitas rendah
5. Scaling fitur numerik
6. Gabungkan semua fitur
7. Optimasi memori
8. Simpan data dan preprocessor
    """)

    st.markdown("---")
    st.markdown("### 📥 1. Load Data Awal")
    st.code("""
import pandas as pd
df = pd.read_csv('../data/base_processed_data.csv')
print(df.shape)
    """, language='python')

    st.markdown("### 🧹 2. Pengelompokan Kategori Langka")
    st.markdown("Mengelompokkan kategori dengan frekuensi kecil menjadi satu kategori 'Other'.")

    st.code("""
def group_rare_categories(df, column_name, top_n=25):
    top = df[column_name].value_counts().nlargest(top_n).index
    df[column_name] = df[column_name].apply(lambda x: x if x in top else f'Other_{column_name}')
    return df
    """, language='python')

    st.markdown("### 🔠 3. Label Encoding untuk Kolom Kardinalitas Tinggi")
    st.code("""
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['model'] = le.fit_transform(df['model'])
    """, language='python')

    st.markdown("### 🧾 4. One-Hot Encoding untuk Kolom Kardinalitas Rendah")
    st.code("""
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

categorical_cols = ['make', 'body', 'state']
onehot_pipeline = Pipeline([('onehot', OneHotEncoder(drop='first', handle_unknown='ignore'))])
    """, language='python')

    st.markdown("### ⚖️ 5. StandardScaler untuk Kolom Numerik")
    st.code("""
from sklearn.preprocessing import StandardScaler

numeric_cols = ['year', 'condition', 'odometer', 'mmr']
numeric_pipeline = Pipeline([('scaler', StandardScaler())])
    """, language='python')

    st.markdown("### 🧩 6. Gabungkan Semua Fitur dengan ColumnTransformer")
    st.code("""
preprocessor = ColumnTransformer([
    ('num', numeric_pipeline, numeric_cols),
    ('cat', onehot_pipeline, categorical_cols)
], remainder='passthrough')

X_processed = preprocessor.fit_transform(df.drop(columns='sellingprice'))
    """, language='python')

    st.markdown("### 💾 7. Simpan ke CSV dan Pickle")
    st.code("""
import joblib

# Simpan hasil
df.to_csv('../data/supervised_ready_data.csv', index=False)

# Simpan preprocessor
joblib.dump(preprocessor, '../models/preprocessor_supervised.pkl')
    """, language='python')

    st.success("✅ Overview selesai. Preprocessing ini menyiapkan data numerik dan kategorikal agar siap digunakan oleh model supervised seperti regresi.")
