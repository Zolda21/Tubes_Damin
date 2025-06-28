import streamlit as st

# === Import modul untuk setiap halaman utama ===
from utils.dashboard import show_dashboard
from utils.business_understanding import show_business_understanding
from utils.data_understanding import show_data_understanding
from utils.exploratory_data_analysis import show_eda
# from utils.data_preprocessing import show_preprocessing
from utils.predict_input import show_prediction_interface
from utils.modeling_supervised_result import show_supervised_result
from utils.modeling_supervised_overview import show_supervised_overview
from utils.data_preprocessing import show_data_preprocessing



# === Konfigurasi dasar halaman ===
st.set_page_config(
    page_title="Data Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === Sidebar Navigasi ===
st.sidebar.title("📊 Navigasi")
menu = st.sidebar.radio(
    "Pilih Halaman:",
    (
        "Dashboard",
        "Business Understanding",
        "Data Understanding",
        "Exploratory Data Analysis",
        "Data Preprocessing",
        "Modeling dan Evaluation",
        "Try Input New Data"
    )
)

# === Routing Konten ===
if menu == "Dashboard":
    show_dashboard()

elif menu == "Business Understanding":
    show_business_understanding()

elif menu == "Data Understanding":
    show_data_understanding()

elif menu == "Exploratory Data Analysis":
    show_eda()

elif menu == "Data Preprocessing":
   show_data_preprocessing()

elif menu == "Modeling dan Evaluation":
    st.header("🧠 Modeling dan Evaluation")

    # === 4 Sub-tab dalam menu Modeling dan Evaluation ===
    tab1, tab2, tab3, tab4 = st.tabs([
        "📘 Overview: Supervised Learning",
        "📈 Supervised Modeling & Evaluation",
        "📕 Overview: Unsupervised Learning",
        "📉 Unsupervised Modeling & Evaluation"
    ])

    with tab1:
        from utils.modeling_supervised_overview import show_supervised_overview
        show_supervised_overview()

    with tab2:
        from utils.modeling_supervised_result import show_supervised_result
        show_supervised_result()

    with tab3:
        from utils.modeling_unsupervised_overview import show_unsupervised_overview
        show_unsupervised_overview()

    with tab4:
        from utils.modeling_unsupervised_result import show_unsupervised_result
        show_unsupervised_result()

elif menu == "Try Input New Data":
    show_prediction_interface()
