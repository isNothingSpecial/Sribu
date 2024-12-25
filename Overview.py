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
st.image("Sribu.png", use_column_width=True)

st.write(''' Sribu atau dulu bernama Sribulancer adalah platform pasar daring yang menghubungkan pemilik bisnis dengan pekerja lepas (freelancer) di berbagai bidang, termasuk desain grafis, pemrograman web, video, foto, audio, penulisan, terjemahan, pemasaran, dan iklan. Didirikan pada September 2011 oleh Ryan Gondokusumo dan Wenes Kusnadi, perusahaan ini berkantor pusat di Jakarta, Indonesia.''')

col1,col2 = st.columns(2)
with col1:
    st.markdown('''Sejarah Singkat Sribu :
- 2011: Sribu diluncurkan sebagai platform kontes desain yang berfokus pada pasar Indonesia, menawarkan berbagai kategori seperti desain logo, desain kemasan, dan desain interior.
- 2012: Menerima pendanaan awal dari East Ventures, yang memungkinkan ekspansi layanan.
- 2014: Mendapat investasi tambahan dari Asteria Japan dan memperluas kategori layanan untuk mencakup lebih dari sekadar desain grafis.
- 2018: Menerima pendanaan dari Crowdworks, pasar freelance terbesar di Jepang.
- 2022: Diakuisisi oleh Mynavi Japan dan menjadi anak perusahaan mereka.
''')

with col2:
    st.markdown('''Pencapaian Sribu :
- Hingga tahun 2022, Sribu telah melayani lebih dari 30.000 klien dengan komunitas freelancer yang dikurasi secara ketat untuk memastikan kualitas dalam komunikasi, ketepatan waktu, dan hasil kerja.
- Sribu juga telah menerima beberapa penghargaan, termasuk Indonesia ICT Awards 2013 dan SparxUp Award 2011
''')

st.markdown(''' Tujuan melakukan Clustering ini adalah untuk mengidentifikasi karakteristik pelanggan dimana dalam kasus ini adalah menggunakan Karakteristik-karakteristik,seperti :
- Recency
- Frequency
- Monetary

Dimana setelah setelah mengetahui karakteristik karakteristik diatas lalu data tersebut diolah untuk melakukan pemetaan cluster dari data yang diperoleh tersebut,lalu setelah dimasukkan mesin akan mengolah data tersebut guna memahami dengan karakteristik sebagai berikut termasuk kedalam cluster yang mana.

Dalam Project ini algoritma yang digunakan adalah menggunakan algoritma K-Means,dimana Algoritma K-Means sendiri sering digunakan dalam project-project berbasis unsupervised learning,dimana algoritma ini memiliki keuntungan yang diantaranya adalah :
- Cepat dan efisien, terutama pada dataset yang besar.
- Mudah dipahami dan diimplementasikan.''')
