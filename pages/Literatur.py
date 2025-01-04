import streamlit as st
import pandas as pd

# Load datasets
df = pd.read_csv('Data_Sales_Platform_SRIBU.csv')
df_missing1 = pd.read_csv('data_missing_1.csv')
df_missing2 = pd.read_csv('data_missing_2.csv')
df_missing3 = pd.read_csv('data_missing_3.csv')
df_missing4 = pd.read_csv('data_missing_4.csv')
df_missing5 = pd.read_csv('data_missing_5.csv')
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
st.markdown('''Literatur dan Story Telling Analitical Process
Dimana pada halaman ini berisi tentang penjelasan tentang setiap Proses yang dilakukan selama proses analisis berjalan,berawal dari :
- Dataset Awal
- Explorasi Dataset
- Visualisasi Insight yang diperoleh dalam Dataset
- Algoritma apa yang akan Dipakai
- Pemisahan Kolom Category menjadi Kolom-Kolom Kategori biner
- Pengolahan Data Menggunakan Metode RFM
- Clustering Data

''')
lit = [' ','Dataset Awal', 'Explorasi Dataset' ,'Treatment Terhadap Dataset','Visualisasi Insight','Algoritma','Pemisahan Kolom Category menjadi Kolom-Kolom Kategori biner', 'RFM Data','Clustering']
literatur = st.selectbox('Pilih Literatur yang ingin Anda ketahui', lit)

# Logika berdasarkan literatur
if literatur == ' ' :
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

elif literatur == 'Explorasi Dataset':
    st.header('Explorasi Dataset')
    st.subheader('Kegiatan Menjelajahi hal dasar yang dimiliki oleh dataset')

    st.markdown(""" Explorasi Dataset adalah kegiatan mendasar dalam proses analisis dimana fungsinya adalah untuk mengetahui hal-hal dasar yang dimiliki oleh dataset dan divisualkan dalam sebuah rangkuman,dimana hal yang sering dilakukan adalah :
    - Peninjauan tipe data setiap kolom dari dataset yang akan dianalisis
    - Pengecekan NULL VALUE yang dimiliki oleh dataset 
    - Peninjauan Data yang memiliki NULL VALUE dimana saja dan memiliki value apa saja di dalam dataset tersebut
    """)

    # Inisialisasi session_state untuk tombol
    if "ex_iya_pressed" not in st.session_state:
        st.session_state.ex_iya_pressed = False
    if "ex_tidak_pressed" not in st.session_state:
        st.session_state.ex_tidak_pressed = False

    # Tombol Iya dan Tidak
    st.write("Apakah Anda ingin penjelasan lebih lanjut tentang Explorasi Dataset?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Iya"):
            st.session_state.ex_iya_pressed = True
            st.session_state.ex_tidak_pressed = False
    with col2:
        if st.button("Tidak"):
            st.session_state.ex_iya_pressed = False
            st.session_state.ex_tidak_pressed = True

    # Logika berdasarkan tombol yang ditekan
    if st.session_state.ex_iya_pressed:
        st.header("Pilih Penjelasan Explorasi Dataset yang ingin Anda Ketahui")
        litex = ['Peninjauan Info Dataset', 'Pengecekan NULL VALUE', 'Peninjauan Data yang memiliki NULL VALUE']
        literaturex = st.selectbox('Pilih penjelasan tentang Explorasi yang ingin Anda ketahui:', litex)

        if literaturex == 'Peninjauan Info Dataset':
            st.header('Peninjauan Tipe Data')
            st.subheader('Melihat Tipe Data dari setiap kolom')
            st.markdown(f""" Dalam proses peninjauan tipe data menggunakan perintah (.info) dimana dengan menggunakan perintah tersebut kita bisa mengetahui info-info yang dimiliki oleh dataset yang akan dianalisis seperti :
            - Nama Kolom
            - Value Kolom (Non NULL)
            Tipe Data dari setiap Kolom yang ada dalam dataset yang akan dianalisis

            Berikut info yang diperoleh dari Dataset Transaksi Platform SRIBU selama 1 tahun :
            - 0   nama_jobs       8233 non-null   object        
            - 1   type            8233 non-null   object        
            - 2   category        6711 non-null   object        
            - 3   subcategory     6711 non-null   object        
            - 4   client_user_id  8194 non-null   object        
            - 5   register_date   8233 non-null   datetime64[ns]
            - 6   order_date      8233 non-null   datetime64[ns]
            - 7   status_invoice  4921 non-null   object        
            - 8   paid_at         8233 non-null   datetime64[ns]
            - 9   total_paid      8233 non-null   int64 
            """)
        elif literaturex == 'Pengecekan NULL VALUE':
            st.header('Pengecekan NULL VALUE')
            st.subheader('Pengecekan NULL VALUE di setiap kolom')
            st.markdown(f''' Dalam proses Pengecekan NULL VALUE dilakukan setelah melakukan Peninjauan Info Dataset,dimana apabila dalam informasi value kolom Non NULL,
            memiliki nilai yang berbeda dari total value yang dimiliki oleh dataset maka patut dilakukan Pengecekan NULL VALUE,dimana dengan memakai perintah (.isnull dan .sum) maka akan menghasilkan informasi rangkuman NULL VALUE setiap kolom

            Berikut adalah rangkuman NULL VALUE dari Setiap Kolom :
            - nama_jobs        memiliki NULL VALUE sejumlah : 0
            - type             memiliki NULL VALUE sejumlah : 0
            - category         memiliki NULL VALUE sejumlah : 1522
            - subcategory      memiliki NULL VALUE sejumlah : 1522
            - client_user_id   memiliki NULL VALUE sejumlah : 39
            - register_date    memiliki NULL VALUE sejumlah : 0
            - order_date       memiliki NULL VALUE sejumlah : 0
            - status_invoice   memiliki NULL VALUE sejumlah : 3312
            - paid_at          memiliki NULL VALUE sejumlah : 0
            - total_paid       memiliki NULL VALUE sejumlah : 0
            ''')
        elif literaturex == 'Peninjauan Data yang memiliki NULL VALUE':
            st.header('Peninjauan Data yang memiliki NULL VALUE')
            st.subheader('Peninjauan Data yang Memiliki NULL VALUE memiliki informasi apa saja')
            st.markdown(""" Informasi yang bisa didapat dari dataset yang memiliki NULL antara lainnya adalah : """)

            st.write("1. Status Invoice yang merupakan NULL VALUE sebanyak 1452 baris, dimana sebanyak 1452 data transaksi tersebut memiliki nilai pada kolom Total Paid namun Status Invoicenya tidak jelas :")
            st.write(df_missing1)

            st.write("2. Status Invoice yang merupakan NULL VALUE sebanyak 1860 baris, dimana sebanyak 1860 data transaksi tersebut memiliki Total Paid = 0,dan Status Invoicenya tidak jelas :")
            st.write(df_missing3)
            
            st.write("3. Kolom Kategori yang merupakan NULL VALUE sebanyak 1522 baris memiliki informasi sebagai berikut :")
            st.write(df_missing2)

            st.write("4. Kolom Sub Kategori yang merupakan NULL VALUE sebanyak 1522 baris memiliki informasi sebagai berikut :")
            st.write(df_missing4)

            st.write("5. Client User ID yang merupakan NULL VALUE atau User yang tanpa nama namun memiliki data transaksi sebanyak 39 baris memiliki informasi sebagai berikut :")
            st.write(df_missing5)
            
    elif st.session_state.ex_tidak_pressed:
        st.warning("Baiklah :), silakan lanjutkan aktivitas Anda!")


elif literatur == 'Treatment Terhadap Dataset':
    st.header('Treatment Terhadap Dataset')
    st.subheader('Cara untuk memperlakukan Dataset sebelum analisis')
    st.markdown(""" Berikut adalah treatment-treatment untuk melihat anomali dalam dataset dan penananganannya,diantaranya adalah :
    - Imputasi NULL VALUE 
    - Pengecheckan Outliers
    - Pembersihan Outliers
     """)
    littreat = ['Imputasi NULL VALUE', 'Pengecheckan Outliers', 'Pembersihan Outliers']
    literaturttreat = st.selectbox('Pilih penjelasan tentang Explorasi yang ingin Anda ketahui:', littreat)

    if literaturttreat =='Imputasi NULL VALUE':
        st.header('Imputasi NULL VALUE')
        st.subheader('Mengubah nilai-nilai NULL VALUE dari setiap kolom ')
        st.markdown(""" Dimana tujuan dari mengubah nilai-nilai NULL VALUE adalah :
        - Agar tidak menjadi anomali ketika melakukan proses RFM ataupun Clustering
        - Agar terlihat jelas ketika akan melakukan visualisasi dan distribusi nilai dari setiap kolom
        """)
        st.markdown(""" Berikut adalah langkah-langkah untuk melakukan Imputasi NULL VALUE :
        - df['status_invoice'] = df['status_invoice'].fillna('success')
        - df['category'] = df['category'].fillna('Unknown')
        - df['subcategory'] = df['subcategory'].fillna('Unknown')
        - df['client_user_id'] = df['client_user_id'].fillna('No_one') """)
    elif literaturttreat =='Pengecheckan Outliers':
        st.header('Pengecheckan Outliers')
        st.subheader('')
    elif literaturttreat =='Pembersihan Outliers':
        st.header('Pembersihan Outliers')
        st.subheader('')


elif literatur == 'Algoritma':
    st.header('Algoritma')
    st.subheader('RFMC dan K-Means')

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
        if "algo_iya_pressed" not in st.session_state:
            st.session_state.algo_iya_pressed = False
        if "algo_tidak_pressed" not in st.session_state:
            st.session_state.algo_tidak_pressed = False

        # Tombol Iya dan Tidak
        st.write("Apakah Anda ingin penjelasan lebih lanjut tentang RFM?")
        col3, col4 = st.columns(2)
        with col3:
            if st.button("Iya"):
                st.session_state.algo_iya_pressed = True
                st.session_state.algo_tidak_pressed = False
        with col4:
            if st.button("Tidak"):
                st.session_state.algo_iya_pressed = False
                st.session_state.algo_tidak_pressed = True

        # Logika berdasarkan tombol yang ditekan
        if st.session_state.algo_iya_pressed:
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
        elif st.session_state.algo_tidak_pressed:
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
