import streamlit as st
import pandas as pd
import importlib

# Load datasets
df = pd.read_csv('Data_Sales_Platform_SRIBU.csv')
dfproc = pd.read_csv('data_cleaned.csv')
dfwill = pd.read_csv('data_will_cluster.csv')
dfcluster = pd.read_csv('data_cluster.csv')

# Judul halaman
st.markdown(
    """
    <h1 style='text-align: center;'>CLUSTERING PELANGGAN PLATFORM SRIBU DENGAN MENGGUNAKAN METODE KOMBINASI ANTARA RFM (RECENCY, FREQUENCY, MONETARY) DAN ALGORITMA K-MEANS</h1>
    """, 
    unsafe_allow_html=True
)

# Daftar halaman utama
main_pages = {
    "Main Page": "main_page",
    "Page 1": "page_1",  # Hanya page ini yang memiliki sub-page
    "Page 2": "page_2"
}

# Sidebar untuk navigasi
with st.sidebar:
    st.header("Navigation")
    main_page_choice = st.selectbox("Main Pages", list(main_pages.keys()))

# Fungsi untuk memuat modul halaman
def load_page(module_name):
    module = importlib.import_module(f"pages.{module_name}")
    module.run()

# Logika untuk memuat halaman utama
load_page(main_pages[main_page_choice])
