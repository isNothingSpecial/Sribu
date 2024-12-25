import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Data Sales Platform - SRIBU.xlsx')
dfproc = pd.read_csv('result_rfm_3cluster.csv')

st.markdown(
    """
    <h1 style='text-align: center;'>CLUSTERING PELANGGAN PLATFORM SRIBU DENGAN MENGGUNAKAN METODE KOMBINASI ANTARA RFM (RECENCY,FREQUENCY,MONETARY) DAN ALGORITMA K-MEANS</h1>
    """, 
    unsafe_allow_html=True
)
st.write('Literatur Pengertian Setiap Kolom')

lit = ['Dataset Awal,Algoritma,RFM Data']

literatur = st.selectbox('Pilih Literatur yang ingin anda ketahui', lit)
        
if literatur == 'Dataset Awal':
    st.header('Dataset Awal')
    st.markdown(''' Dataset yang digunakan adalah Dataset Transaksi Pelanggan selama 1 Tahun dari Platform Sribu dimana memiliki kolom-kolom ,sebagai berikut :
- Nama_Jobs
- Type
- Category
- Subcategory
- Client User Id
- Register Date
- Order Date
- Status Invoice
- Paid At
- Total Paid' Detailnya sebagai berikut : ''')
    st.write(df)

    elif literatur == 'Algoritma':
        st.header('Algoritma')
        st.subheader('RFM dan K-Means')
        st.write('Pilih Penjelasan Algoritma yang digunakan di project ini')

            lital = ['RFM,K-Means']
            literatural = st.selectbox('Pilih literatur Chest Pain yang ingin anda ketahui : ', lital)
    
            if literatural == 'RFM':
                st.header('Chest Pain Type 1')
                st.subheader('Chest Pain Type 1 atau Nyeri Dada Type Asimtomatik')
                st.write('Nyeri dada asimtomatik adalah nyeri dada yang tidak memiliki tanda atau gejala yang jelas, atau memiliki gejala yang tidak khas dari masalah jantung. Hal ini dapat disebabkan oleh berbagai kondisi, seperti iskemia miokard, serangan jantung diam, emboli paru, gagal jantung, atau gangguan kardiovaskular, muskuloskeletal, gastrointestinal, paru, atau kejiwaan lainnya. Nyeri dada tanpa gejala bisa sulit didiagnosis dan mungkin memerlukan tes lebih lanjut untuk menyingkirkan kondisi serius.')
    
            elif literatural == 'K-Means':
                st.header('K-Means')
                st.subheader('Penjelasan singkat tentang Algoritma K-Means')
                st.markdown(''' K-Means adalah salah satu algoritma clustering yang paling sederhana dan populer untuk mengelompokkan data ke dalam sejumlah grup berdasarkan kesamaan. Algoritma ini termasuk dalam jenis unsupervised learning, yang berarti tidak memerlukan label atau target untuk membentuk kelompok.
Cara Kerja K-Means

1. Inisialisasi:
- Tentukan jumlah kluster 𝑘 yang ingin dibuat.
- Pilih secara acak 𝑘 titik awal (centroid) sebagai pusat kluster.

2. Penugasan Cluster:
- Setiap data akan dihitung jaraknya ke centroid yang ada.
- Data akan diberikan ke kluster dengan centroid terdekat berdasarkan metrik jarak (umumnya Euclidean).

3. Update Centroid:
- Setelah semua data diberi kluster, hitung ulang posisi centroid sebagai rata-rata dari semua data dalam kluster tersebut.

4. Iterasi:
- Ulangi langkah 2 dan 3 hingga posisi centroid tidak lagi berubah secara signifikan atau mencapai jumlah iterasi maksimum.

5. Hasil Akhir:
- Setiap data akan termasuk dalam satu kluster, dan centroid mencerminkan pusat setiap kluster.
''')
            col1,col2 = st.columns(2)
            with col1:
                st.markdown(''' Keuntungan K-Means
                - Cepat dan efisien, terutama pada dataset yang besar.
                - Mudah dipahami dan diimplementasikan. ''')

            with col2:
                st.markdown('''Kekurangan K-Means
                - Harus menentukan 𝑘 (jumlah kluster) di awal.
                - Sensitif terhadap titik awal (initialization).
                - Tidak bekerja baik untuk kluster dengan bentuk yang kompleks atau ukuran yang sangat bervariasi.
                - Rentan terhadap outlier, karena mereka dapat menggeser posisi centroid.''')
        
    elif literatural == 'RFM Data':
        st.header('Data Yang Telah Diolah')
        st.subheader('Data yang telah diolah menggunakan metode RFM dan Algoritma K-Means')
        st.markdown(''' Data Awal yang telah diolah menggunakan metode RFM dan Algoritma K-Means lalu disimpan kedalam dataset baru dimana datasetnya memiliki kolom-kolom sebagai berikut : 
        - Client User Id
        - Paid At
        - Recency
        - Frequency
        - Monetary
        - Cluster
        
        Selengkapnya sebagai berikut : ''')
        st.write(dfproc)
 # Pertanyaan dengan tombol "Iya" dan "Tidak"
pilihan = st.radio("Apakah Anda ingin penjelasan tentang RFM?", ("Iya", "Tidak"))

# Tampilkan respons berdasarkan pilihan
if pilihan == "Iya":
    st.header("RFM")
    st.subheader("Recency,Frequency,Monetary")
    st.write("""
    **RFM (Recency, Frequency, Monetary)** adalah metode analisis data pelanggan yang membantu bisnis memahami perilaku pelanggan dengan membagi mereka ke dalam kategori berdasarkan:
    - **Recency**: Seberapa baru pelanggan melakukan Transaksi di Platform Sribu.
    - **Frequency**: Seberapa sering pelanggan melakukan Transaksi di Platform Sribu.
    - **Monetary**: Berapa banyak total uang yang dihabiskan pelanggan selama bertransaksi di platform Sribu.
    """)
else:
    st.warning("Baiklah, silakan lanjutkan aktivitas Anda!")
    else:
        st.write('pilih penjelasan Algoritma apa yang ingin anda ketahui')


else:
    st.error("Silakan pilih penjelasan apa yang ingin anda ketahui")
