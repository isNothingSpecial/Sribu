import streamlit as st
import pandas as pd

# Load datasets
df = pd.read_csv('Data_Sales_Platform_SRIBU.csv')
dfproc = pd.read_csv('data_cleaned.csv')
dfwill = pd.read_csv('data_will_cluster.csv')
dfcluster = pd.read_csv('data_cluster.csv')

# Judul halaman
st.markdown(
    """
    <h1 style='text-align: center;'>Literatur dan Story Telling Analitical Process</h1>
    """, 
    unsafe_allow_html=True
)

# Pilihan literatur
st.write("Literatur Pengertian Setiap Kolom")
lit = ['" ",Dataset Awal', 'Algoritma', 'RFM Data']
literatur = st.selectbox('Pilih Literatur yang ingin Anda ketahui', lit)

# Logika berdasarkan literatur
if literatur == '" "' :
    st.warning("Silakan pilih opsi Hal yang ingin diketahui untuk melanjutkan.")
elif literatur == 'Dataset Awal':
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

    Berikut adalah Dataset Awal yang di dapat dari Platform Sribu :
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

        # Inisialisasi session_state untuk tombol
        if "iya_pressed" not in st.session_state:
            st.session_state.iya_pressed = False
        if "tidak_pressed" not in st.session_state:
            st.session_state.tidak_pressed = False

        # Tombol Iya dan Tidak
        st.write("Apakah Anda ingin penjelasan lebih lanjut tentang RFM?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Iya"):
                st.session_state.iya_pressed = True
                st.session_state.tidak_pressed = False
        with col2:
            if st.button("Tidak"):
                st.session_state.iya_pressed = False
                st.session_state.tidak_pressed = True

        # Logika berdasarkan tombol yang ditekan
        if st.session_state.iya_pressed:
            st.header("Pilih Penjelasan RFM yang ingin Anda Ketahui")
            litrfm = ['Recency', 'Frequency', 'Monetary']
            literaturrfm = st.selectbox('Pilih aspek RFM:', litrfm)

            if literaturrfm == 'Recency':
                st.header('Recency')
                st.subheader('Kebaharuan')
                st.write("""
                - **Definisi**: Seberapa baru pelanggan terakhir kali berinteraksi (misalnya, melakukan pembelian).
                - **Pengukuran**: Interval waktu sejak transaksi terakhir hingga data ini diambil.
                - **Mengapa Penting**: Pelanggan yang baru saja bertransaksi cenderung lebih terlibat dan lebih mungkin untuk melakukan pembelian lagi.
                """)
            elif literaturrfm == 'Frequency':
                st.header('Frequency')
                st.subheader('Intensitas')
                st.write("""
                - **Definisi**: Seberapa sering pelanggan bertransaksi dalam periode tertentu.
                - **Pengukuran**: Jumlah total transaksi pelanggan selama periode tertentu.
                - **Mengapa Penting**: Pelanggan yang sering membeli menunjukkan loyalitas lebih tinggi.
                """)
            elif literaturrfm == 'Monetary':
                st.header('Monetary')
                st.subheader('Total Nilai Uang')
                st.write("""
                - **Definisi**: Total nilai uang yang dihabiskan oleh pelanggan selama ia melakukan transaksi.
                - **Pengukuran**: Jumlah total uang yang dihabiskan pelanggan dalam transaksi mereka.
                - **Mengapa Penting**: Pelanggan dengan pengeluaran lebih besar memberikan kontribusi lebih besar pada pendapatan perusahaan.
                """)
        elif st.session_state.tidak_pressed:
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
    st.subheader('Proses Terbentuknya Hasil Akhir Pengolahan Data dengan RFM dan K-Means')
    st.markdown("""
    Berikut adalah Dataset yang telah diolah menggunakan metode RFM dan menambahkan hasil onehot kolom Category memiliki kolom berikut:
    - Client User Id
    - Paid At
    - Recency
    - Frequency
    - Monetary
    - Category Desain Grafis & Branding
    - Category Gaya Hidup
    - Category Konsultasi
    - Category Pemasaran & Periklanan
    - Category Penulisan & Penerjemahan
    - Category Unknown
    - Category Video, Fotografi & Audio
    - Category Web & Pemrograman'

    Berikut adalah dataset yang telah diolah dengan metode RFM :
    """)
    st.write(dfproc)
    st.markdown("""
    Dataset yang telah diolah menggunakan metode RFM dan dibersihkan dari outliers dan akan dimasukkan ke dalam proses clustering,memiliki perbedaan dimana jumlah data total telah berkurang dikarenakan proses pembersihan outliers :
    - Jumlah data sebelum membersihkan outliers: 2942
    - Jumlah data setelah membersihkan outliers: 2548

    Berikut adalah dataset yang telah diolah dengan metode RFM dan telah dibersihkan dari outliers :
    """)
    st.write(dfwill)
    st.markdown("""
    Dataset yang telah diolah menggunakan metode RFM dan telah melakukan proses clustering dengan metode K-Means,dari data diatas menghasilkan persebaran cluster sebanyak 4 cluster,dengan persebaran anggota seperti berikut :
    - Cluster 0 = 1069 anggota
    - Cluster 1 = 770 anggota
    - Cluster 2 = 334 anggota
    - Cluster 3 = 375 anggota

    Berikut adalah dataset final yang telah diolah dengan metode RFM dan pengclusteran dengan algoritma K-Means :
    """)
    st.write(dfcluster)
