import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('result_rfm_3cluster.csv')

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
    st.markdown(''Dataset yang digunakan adalah Dataset Transaksi Pelanggan selama 1 Tahun dari Platform Sribu dimana memiliki kolom-kolom ,sebagai berikut :
- Nama_Jobs
- Type
- Category
- Subcategory
- Client User Id
- Register Date
- Order Date
- Status Invoice
- Paid At
- Total Paid'

Detailnya sebagai berikut : ''')
    st.write(df)

    elif literatur == 'Algoritma':
        st.header('Algoritma')
        st.subheader('K-Means')
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
    
    litcp = ['Chest Pain Type 1', 'Chest Pain Type 2', 'Chest Pain Type 3', 'Chest Pain Type 4']
    literaturcp = st.selectbox('Pilih literatur Chest Pain yang ingin anda ketahui : ', litcp)
    
    if literaturcp == 'Chest Pain Type 1':
        st.header('Chest Pain Type 1')
        st.subheader('Chest Pain Type 1 atau Nyeri Dada Type Asimtomatik')
        st.write('Nyeri dada asimtomatik adalah nyeri dada yang tidak memiliki tanda atau gejala yang jelas, atau memiliki gejala yang tidak khas dari masalah jantung. Hal ini dapat disebabkan oleh berbagai kondisi, seperti iskemia miokard, serangan jantung diam, emboli paru, gagal jantung, atau gangguan kardiovaskular, muskuloskeletal, gastrointestinal, paru, atau kejiwaan lainnya. Nyeri dada tanpa gejala bisa sulit didiagnosis dan mungkin memerlukan tes lebih lanjut untuk menyingkirkan kondisi serius.')
    
    elif literaturcp == 'Chest Pain Type 2':
        st.header('Chest Pain Type 2')
        st.subheader('Chest Pain Type 2 atau Nyeri Dada Tipe Atipikal Angina')
        st.write('Angina atipikal mengacu pada nyeri dada atau ketidaknyamanan yang tidak memiliki karakteristik khas angina klasik. Ini mungkin hadir dengan gejala yang berbeda atau mungkin tidak mengikuti pola nyeri dada yang biasa terkait dengan masalah jantung.')
        
    elif literaturcp == 'Chest Pain Type 3':
        st.header('Chest Pain Type 3')
        st.subheader('Chest Pain Type 3 atau Nyeri Dada Tipe non tipikal Angina')
        st.write('Angina non-tipikal mengacu pada nyeri dada yang tidak berasal dari jantung dan kadang-kadang tidak mewakili gejala iskemik angina pada kasus penyakit jantung yang khas.')
    
    elif literaturcp == 'Chest Pain Type 4':
        st.header('Chest Pain Type 4')
        st.subheader('Chest Pain Type 4 atau Nyeri Dada Tipe tipikal Angina')
        st.write('Angina khas, juga dikenal sebagai angina stabil, adalah nyeri dada atau ketidaknyamanan yang terjadi ketika otot jantung tidak menerima aliran darah yang cukup, biasanya selama aktivitas fisik atau stres. Ini ditandai dengan pola yang dapat diprediksi, sering dipicu oleh kegiatan seperti olahraga atau stres emosional, dan cenderung mereda dengan istirahat atau obat-obatan.')
  
    else:
        st.write('pilih Tipikal Chest Pain di atas')


else:
    st.subheader('Pilih literatur yang ingin anda ketahui ')
