import streamlit as st

def show_unsupervised_overview():
    st.markdown("## 🧠 Overview: Modeling Unsupervised Learning")

    st.markdown("### 1. Load data hasil preprocessing dari file `unsupervised_ready_data.csv`")
    st.code("""
import pandas as pd
data = pd.read_csv('../data/unsupervised_ready_data.csv')
print(data.shape)
""", language='python')

    st.markdown("### 2. Lakukan standarisasi fitur dengan StandardScaler")
    st.code("""
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data)
""", language='python')

    st.markdown("### 3. Tentukan jumlah klaster optimal dengan Elbow Method (optional)")
    st.code("""
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Metode Elbow')
plt.xlabel('Jumlah Klaster')
plt.ylabel('WCSS')
plt.show()
""", language='python')

    st.markdown("### 4. Terapkan algoritma KMeans")
    st.code("""
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_scaled)
""", language='python')

    st.markdown("### 5. Evaluasi hasil clustering")
    st.code("""
from sklearn.metrics import silhouette_score
score = silhouette_score(X_scaled, labels)
print(f"Silhouette Score: {score}")
""", language='python')

    st.markdown("### 6. Visualisasi hasil clustering (PCA)")
    st.code("""
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

plt.scatter(components[:, 0], components[:, 1], c=labels, cmap='viridis', s=10)
plt.title('Visualisasi Klaster')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.grid(True)
plt.show()
""", language='python')

    st.markdown("### 7. Tambahkan label klaster ke DataFrame dan simpan")
    st.code("""
data['cluster'] = labels
data.to_csv('../data/clustered_data.csv', index=False)
""", language='python')

    st.warning("⚠️ Catatan: Ini hanya overview dan potongan kode, bukan untuk dijalankan langsung di aplikasi.")
