import streamlit as st
import pandas as pd
import importlib

# Daftar halaman utama
main_pages = {
    "Literatur": "Literatur.py",
    "Profil": "Profil Kelompok.py"
}

# Sidebar untuk navigasi
with st.sidebar:
    st.header("Literatur Page")
    main_page_choice = st.selectbox("Select Sub Page", list(main_pages.keys()))

# Fungsi untuk memuat halaman
def load_page(page_name):
    module = importlib.import_module(f"pages.{pages[page_name]}")
    module.run()

# Jalankan halaman yang dipilih
load_page(selected_page)

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
