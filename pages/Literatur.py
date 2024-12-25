import streamlit as st
import pandas as pd

# Load datasets
df = pd.read_csv('Data_Sales_Platform_SRIBU.csv')
dfproc = pd.read_csv('result_rfm_3cluster.csv')

# Judul halaman
st.markdown(
    """
    <h1 style='text-align: center;'>CLUSTERING PELANGGAN PLATFORM SRIBU DENGAN MENGGUNAKAN METODE KOMBINASI ANTARA RFM (RECENCY, FREQUENCY, MONETARY) DAN ALGORITMA K-MEANS</h1>
    """, 
    unsafe_allow_html=True
)

# Pilihan literatur
st.write("Literatur Pengertian Setiap Kolom")
lit = ['Dataset Awal', 'Algoritma', 'RFM Data']
literatur = st.selectbox('Pilih Literatur yang ingin Anda ketahui', lit)

# Penjelasan berdasarkan pilihan literatur
if literatur == 'Dataset Awal':
    st.header('Dataset Awal')
    st.markdown("""
    Dataset yang digunakan adalah dataset transaksi pelanggan selama 1 tahun dari Platform Sribu, yang memiliki kolom-kolom berikut:
    - Nama Jobs
    - Type
    - Category
    - Subcategory
    - Client User Id
    - Register Date
    - Order Date
    - Status Invoice
    - Paid At
    - Total Paid
    """)
    st.write(df)

elif literatur == 'Algoritma':
    st.header('Algoritma')
    st.subheader('RFM dan K-Means')
    
    lital = ['RFM', 'K-Means']
    literatural = st.selectbox('Pilih penjelasan algoritma yang ingin Anda ketahui:', lital)

    if literatural == 'RFM':
        st.header('RFM')
        st.subheader('Recency, Frequency, Monetary')
        st.write("""
        **RFM (Recency, Frequency, Monetary)** adalah metode analisis pelanggan yang membagi mereka berdasarkan:
        - **Recency**: Seberapa baru pelanggan terakhir bertransaksi di Platform Sribu.
        - **Frequency**: Seberapa sering pelanggan bertransaksi selama menggunakan Platform Sribu.
        - **Monetary**: Total uang yang dihabiskan pelanggan untuk melakukan transaksi selama menggunakan Platform Sribu.
        """)
        # Penjelasan tambahan tentang RFM menggunakan tombol
        st.write("Apakah Anda ingin penjelasan lebih lanjut tentang RFM di dataset yang telah diolah?")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Iya"):
               st.header("Pilih Penjelasan RFM yang ingin Anda Ketahui")
                
                    litrfm = ['Recency', 'Frequency','Monetary']
                    literaturrfm = st.selectbox('Pilih penjelasan algoritma yang ingin Anda ketahui:', litrfm)
                
                    if literaturrfm == 'Recency':
                        st.header('Recency')
                        st.subheader('Kebaharuan')
                        st.write(""" Recency (R)
                        - **Definisi** : Seberapa baru pelanggan terakhir kali berinteraksi (misalnya, melakukan pembelian).
                        - **Mengapa Penting** : Pelanggan yang baru saja bertransaksi cenderung lebih terlibat dan lebih mungkin untuk melakukan pembelian lagi.
                        - **Pengukuran** : Interval waktu sejak transaksi terakhir hingga hari ini.
                        
                        Contoh : Pelanggan yang terakhir kali membeli 7 hari lalu memiliki nilai recency yang lebih tinggi dibanding pelanggan yang terakhir membeli 30 hari lalu. """)

                    elif literaturrfm == 'Frequency':
                        st.header('Frequency')
                        st.subheader('Intensitas')
                        st.write(""" Frequency (F)
                        - **Definisi** : Seberapa sering pelanggan bertransaksi dalam periode tertentu.
                        - **Mengapa Penting** : Pelanggan yang sering membeli menunjukkan loyalitas lebih tinggi dibanding pelanggan dengan frekuensi rendah.
                        - **Pengukuran** : Jumlah total transaksi pelanggan selama periode tertentu.
                        
                        Contoh : Pelanggan yang melakukan pembelian 10 kali lebih sering berinteraksi dibanding pelanggan dengan hanya 2 transaksi. """)
                        
                    elif literaturrfm == 'Monetary':
                        st.header('Monetary')
                        st.subheader('Total Nilai Uang')
                        st.write(""" Monetary (M)
                        - **Definisi** : Total nilai uang yang dihabiskan oleh pelanggan.
                        - **Mengapa Penting** : Pelanggan dengan pengeluaran lebih besar memberikan kontribusi lebih besar pada pendapatan perusahaan.
                        - **Pengukuran** : Jumlah total uang yang dihabiskan pelanggan dalam transaksi mereka.
                        
                        Contoh: Pelanggan dengan total pengeluaran Rp 5 juta lebih bernilai dibanding pelanggan yang hanya menghabiskan Rp 500 ribu. """)
        with col2:
            if st.button("Tidak"):
               st.warning("Baiklah :), silakan lanjutkan aktivitas Anda!")


    elif literatural == 'K-Means':
        st.header('K-Means')
        st.subheader('Penjelasan Singkat tentang Algoritma K-Means')
        st.markdown("""
        **K-Means** adalah algoritma clustering yang mengelompokkan data ke dalam sejumlah grup berdasarkan kesamaan. 
        Cara kerjanya meliputi:
        1. Inisialisasi: Tentukan jumlah cluster **k** dan pilih centroid awal secara acak.
        2. Penugasan Cluster: Data diberikan ke cluster terdekat berdasarkan jarak Euclidean.
        3. Update Centroid: Hitung ulang centroid berdasarkan rata-rata data dalam cluster.
        4. Iterasi: Ulangi langkah 2 dan 3 hingga centroid tidak berubah.
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Keuntungan K-Means**")
            st.markdown("- Cepat dan efisien.\n- Mudah dipahami dan diimplementasikan.")
        with col2:
            st.markdown("**Kekurangan K-Means**")
            st.markdown("- Harus menentukan jumlah **k** di awal.\n- Sensitif terhadap inisialisasi dan outlier.")

elif literatur == 'RFM Data':
    st.header('Data Yang Telah Diolah')
    st.subheader('Hasil Pengolahan dengan RFM dan K-Means')
    st.markdown("""
    Dataset yang telah diolah menggunakan metode RFM dan algoritma K-Means memiliki kolom berikut:
    - Client User Id
    - Paid At
    - Recency
    - Frequency
    - Monetary
    - Cluster
    """)
    st.write(dfproc)
