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

def run():
    st.title("Uji Coba Dropdown Page")

    # Dropdown untuk sub-pages
    sub_page_choice = st.selectbox("Choose Sub-page", ["Literatur", "Profil Kelompok"])

    # Memuat modul berdasarkan sub-page yang dipilih
    if sub_page_choice == "Literatur":
        sub_module = importlib.import_module("pages.page_1a")
    elif sub_page_choice == "Profil Kelompok":
        sub_module = importlib.import_module("pages.page_1b")
    
    # Jalankan fungsi `run` dari modul sub-page
    sub_module.run()
