import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

def show_eda():
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
        </style>
    """, unsafe_allow_html=True)

    # === Title & Subtitle ===
    st.markdown('<div class="main-title">🔎 EXPLORATORY DATA ANALYSIS 🔎</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Visualisasi dan Pemahaman Awal terhadap Dataset</div>', unsafe_allow_html=True)

    # === Korelasi Matriks ===
    st.markdown('<div class="section-header">🔗 Korelasi Antar Variabel Numerik</div>', unsafe_allow_html=True)
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns
    plt.figure(figsize=(12, 8))
    correlation_matrix = df[numerical_features].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Matriks Korelasi', fontsize=16)
    st.pyplot(plt.gcf())

    # === Boxplot untuk semua fitur numerik ===
    st.markdown('<div class="section-header">📦 Distribusi Fitur Numerik (Boxplot)</div>', unsafe_allow_html=True)
    st.write("Boxplot membantu mengenali distribusi dan potensi outlier dari masing-masing fitur:")

    num_plots = len(numerical_features)
    cols = 2
    rows = (num_plots + 1) // cols

    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(18, 5 * rows))
    axes = axes.flatten()

    for i, col in enumerate(numerical_features):
        sns.boxplot(x=df[col], ax=axes[i], color='skyblue')
        axes[i].set_title(f'Boxplot: {col}', fontsize=14)
        axes[i].set_xlabel('')
        axes[i].set_ylabel('')

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    st.pyplot(fig)

    # === Distribusi Merk Mobil (Top 10) ===
    st.markdown('<div class="section-header">🚗 Top 10 Merk Mobil Paling Umum</div>', unsafe_allow_html=True)
    top_makes = df['make'].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_makes.values, y=top_makes.index, ax=ax, palette='viridis')
    ax.set_title('10 Merk Mobil Terbanyak')
    ax.set_xlabel('Jumlah')
    st.pyplot(fig)

    # === Distribusi Transmisi Mobil ===
    st.markdown('<div class="section-header">⚙️ Distribusi Tipe Transmisi</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.countplot(data=df, y='transmission', order=df['transmission'].value_counts().index, palette='pastel')
    ax.set_title('Jenis Transmisi')
    ax.set_xlabel('Jumlah')
    st.pyplot(fig)

    # === Distribusi Body Type Mobil ===
    st.markdown('<div class="section-header">🚘 Tipe Bodi Mobil</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    top_body = df['body'].value_counts().head(10)
    sns.barplot(x=top_body.values, y=top_body.index, ax=ax, palette='muted')
    ax.set_title('Top 10 Jenis Bodi Mobil')
    ax.set_xlabel('Jumlah')
    st.pyplot(fig)

    # === Selling Price vs Condition ===
    st.markdown('<div class="section-header">💵 Harga Jual vs Kondisi Mobil</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='condition', y='sellingprice', data=df, ax=ax, color='lightgreen')
    ax.set_title('Distribusi Harga Jual Berdasarkan Kondisi Mobil')
    st.pyplot(fig)

    # === Histogram Selling Price ===
    st.markdown('<div class="section-header">💰 Distribusi Harga Jual Mobil</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.histplot(df['sellingprice'], bins=50, kde=True, color='steelblue')
    ax.set_title('Distribusi Harga Jual Mobil')
    ax.set_xlabel('Harga Jual')
    st.pyplot(fig)

    # === Harga Rata-rata per Merk (Top 10) ===
    st.markdown('<div class="section-header">🏷️ Rata-rata Harga Jual per Merk (Top 10)</div>', unsafe_allow_html=True)
    avg_price_by_make = df.groupby('make')['sellingprice'].mean().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=avg_price_by_make.values, y=avg_price_by_make.index, ax=ax, palette='coolwarm')
    ax.set_title('Rata-rata Harga Jual per Merk')
    ax.set_xlabel('Harga Rata-rata')
    st.pyplot(fig)

    # === Distribusi Tahun Mobil ===
    st.markdown('<div class="section-header">📆 Distribusi Tahun Pembuatan Mobil</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='year', order=sorted(df['year'].unique()), color='lightblue')
    ax.set_title('Jumlah Mobil Berdasarkan Tahun')
    ax.set_xlabel('Tahun')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # === Harga Rata-rata Berdasarkan Tahun ===
    st.markdown('<div class="section-header">📈 Rata-rata Harga Jual per Tahun</div>', unsafe_allow_html=True)
    avg_price_by_year = df.groupby('year')['sellingprice'].mean()
    fig, ax = plt.subplots()
    sns.lineplot(x=avg_price_by_year.index, y=avg_price_by_year.values, marker='o')
    ax.set_title('Harga Rata-rata Mobil Berdasarkan Tahun')
    ax.set_ylabel('Rata-rata Harga')
    ax.set_xlabel('Tahun')
    st.pyplot(fig)

    # === Distribusi Odometer ===
    st.markdown('<div class="section-header">🛣️ Distribusi Kilometer (Odometer)</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    sns.histplot(df['odometer'], bins=60, kde=True, color='darkorange')
    ax.set_title('Distribusi Kilometer Tempuh')
    ax.set_xlabel('Kilometer')
    st.pyplot(fig)
