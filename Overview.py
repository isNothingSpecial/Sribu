import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

## data

st.set_page_config(page_title="Homepage",layout="wide")
#side bar
#st.sidebar.header("Segmentasi Pelanggan Produk HNI")
#st.sidebar.image("1835901.jpg")

##layout

# Menggunakan HTML dan CSS untuk membuat header dan subheader rata tengah
st.markdown(
    """
    <h1 style='text-align: center;'>CLUSTERING PELANGGAN PLATFORM SRIBU DENGAN MENGGUNAKAN METODE KOMBINASI ANTARA RFM (RECENCY,FREQUENCY,MONETARY) DAN ALGORITMA K-MEANS</h1>
    """, 
    unsafe_allow_html=True
)

# Membuat tiga kolom
col1, col2, col3,col4 = st.columns(4)

# Menampilkan konten di setiap kolom
with col1:
    st.image("Sribu.png", use_column_width=True)

with col2:
    st.write(''' Sribu atau dulu bernama Sribulancer adalah platform pasar daring yang menghubungkan pemilik bisnis dengan pekerja lepas (freelancer) di berbagai bidang, termasuk desain grafis, pemrograman web, video, foto, audio, penulisan, terjemahan, pemasaran, dan iklan. Didirikan pada September 2011 oleh Ryan Gondokusumo dan Wenes Kusnadi, perusahaan ini berkantor pusat di Jakarta, Indonesia.''')

with col3:
    st.markdown('''Sejarah Singkat Sribu :
- 2011: Sribu diluncurkan sebagai platform kontes desain yang berfokus pada pasar Indonesia, menawarkan berbagai kategori seperti desain logo, desain kemasan, dan desain interior.
- 2012: Menerima pendanaan awal dari East Ventures, yang memungkinkan ekspansi layanan.
- 2014: Mendapat investasi tambahan dari Asteria Japan dan memperluas kategori layanan untuk mencakup lebih dari sekadar desain grafis.
- 2018: Menerima pendanaan dari Crowdworks, pasar freelance terbesar di Jepang.
- 2022: Diakuisisi oleh Mynavi Japan dan menjadi anak perusahaan mereka.
''')

with col4:
    st.markdown('''Pencapaian Sribu :
Hingga tahun 2022, Sribu telah melayani lebih dari 30.000 klien dengan komunitas freelancer yang dikurasi secara ketat untuk memastikan kualitas dalam komunikasi, ketepatan waktu, dan hasil kerja.
Sribu juga telah menerima beberapa penghargaan, termasuk Indonesia ICT Awards 2013 dan SparxUp Award 2011
''')

st.markdown('''Data diatas masih berupa RAW data,yang mana nantinya akan diolah melalui beberapa proses antara lain:  
1. Import relevant libraries
2. Set Up the current working directory & Import Dataset
3. Exploratory Data Analysis (EDA)
4. Count Categorical Value
5. Mengubah Nominal Variabel
6. Clean the Dataset
7. Visualizations
8. Scalling
9. Modelling
10. Evaluasi
        
Berikut adalah data yang telah diolah sebelum dilakukannya scalling hingga evaluasi: ''')
