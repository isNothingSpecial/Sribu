import streamlit as st
import pandas as pd

# Load datasets
df = pd.read_csv('Data_Sales_Platform_SRIBU.csv')
df_missing1 = pd.read_csv('data_missing_1.csv')
df_missing2 = pd.read_csv('data_missing_2.csv')
df_missing3 = pd.read_csv('data_missing_3.csv')
df_missing4 = pd.read_csv('data_missing_4.csv')
df_missing5 = pd.read_csv('data_missing_5.csv')
onehot_data = pd.read_csv('data_onehot.csv')
scalling = pd.read_csv('scalling.csv')
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
lit = [' ','Dataset Awal', 'Explorasi Dataset' ,'Treatment Terhadap Dataset','Crosscheck and Deleting Anomali','Algoritma','Pemisahan Kolom Category menjadi Kolom-Kolom Kategori biner', 'RFMC Data','Clustering']
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
            - Tipe Data dari setiap Kolom yang ada dalam dataset yang akan dianalisis

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
        st.markdown('''Dimana tujuan dari mengubah nilai-nilai NULL VALUE adalah :

        _
        - Agar tidak menjadi anomali ketika melakukan proses RFM ataupun Clustering
        - Agar terlihat jelas ketika akan melakukan visualisasi dan distribusi nilai dari setiap kolom
        
       ''')
        
        st.markdown(f"""Berikut adalah langkah-langkah untuk melakukan Imputasi NULL VALUE :

        _
        - df['status_invoice'] = df['status_invoice'].fillna('success')
        - df['category'] = df['category'].fillna('Unknown')
        - df['subcategory'] = df['subcategory'].fillna('Unknown')
        - df['client_user_id'] = df['client_user_id'].fillna('No_one')
        """)
        
    elif literaturttreat =='Pengecheckan Outliers':
        st.header('Pengecheckan Outliers')
        st.subheader('Pengecheckan data yang merupakan Outliers dalam kolom numerik dalam dataset')
        st.write('Outliers adalah nilai-nilai yang sangat berbeda atau tidak biasa dalam sebuah dataset jika dibandingkan dengan nilai-nilai lainnya. Outliers bisa berupa data yang secara signifikan lebih besar atau lebih kecil dari sebagian besar data lainnya. Mereka sering kali dapat memengaruhi analisis statistik, model prediksi, dan kesimpulan yang diambil dari data.')

        st.markdown("""Pentingnya melakukan Pengecheckan Outliers dalam dataset memiliki beberapa manfaat,diantaranya :
        
        - Meningkatkan Akurasi Terhadap Model
        - Mencegah Bias dalam Statistik
        - Memahami Pola Tidak Biasa
        - Mendukung Pengambilan Keputusan
        """)
        st.markdown ("""Metode-metode dalam Pengecheckan Outliers diantaranya :
        
        - Menggunakan Statistik Deskriptif
        - Menggunakan IQR (Interquartile Range)
        - Menggunakan Z-Score
        - Menggunakan Visualisasi
        """)
        st.write('Dalam Pengecheckan Outliers dalam Analisis kali ini adalah menggunakan Visualisasi berupa Boxplot dimana visualisasinya adalah sebagai berikut :')
        st.write('')
    elif literaturttreat =='Pembersihan Outliers':
        st.header('Pembersihan Outliers')
        st.subheader('Melakukan Treatment kepada anomali Outliers')
        st.write('Dalam Pembersihan Outliers kali ini adalah menggunakan metode Interquartile Range (IQR), dimana memiliki langkah-langkah di antaranya:')

        st.markdown(""" Menghitung Batas Atas dan Batas Bawah melalui Kuartil bawah dan kuartil atas, dengan menggunakan IQR dari kolom total_paid, dimana :
        -
        - Kuartil Bawah (Q1) : adalah nilai dari kolom total_paid di mana 25% data berada di bawahnya, dan dalam dataset ini memiliki nilai : 10,000  
        - Kuartil Atas (Q3) : adalah nilai dari kolom total_paid di mana 75% data berada di bawahnya, dan dalam dataset ini memiliki nilai : 638,931
        """)
            
        st.markdown("""Sehingga ketika telah mengetahui nilai Kuartil Atas dan Kuartil Bawah,lalu dilanjutkan dengan proses perhitungan IQR dengan menggunakan rumus :
        
        - IQR = Q3-Q1
        """)

        st.markdown("""Setelah mengetahui nilai IQRnya, dilanjutkan lagi dengan menghitung batas atas dan batas bawah dari nilai dalam kolom total_paid tersebut di mana memiliki rumus sebagai berikut:

        - Rumus :
        - lower_bound = Q1 - 1.5 * IQR
        - upper_bound = Q3 + 1.5 * IQR
        """)

        st.markdown("""Setelah menghitung IQR,batas atas dan batas bawah,lalu step terakhir adalah menyaring total value yang ada dalam kolom total_paid dengan hasil batas atas dan batas bawah dari hasil yang telah dihitung tadi,dimana melalui alur sebagai berikut :
        
        - df3_cleaned = df3[(df3['total_paid'] >= lower_bound) & (df3['total_paid'] <= upper_bound)]
        """)

        st.markdown("""Dimana step tersebut memiliki arti apabila :

        -
        - Data di kolom total_paid yang lebih besar atau sama dengan lower_bound dan
        - Data di kolom total_paid yang lebih kecil atau sama dengan upper_bound""")

        st.write('Maka Data yang tidak memenuhi kriteria diatas akan dihapus dari dataset,lalu disimpan dalam perintah `df3_cleaned`.')

elif literatur == 'Crosscheck and Deleting Anomali':
    st.header('Crosscheck and Deleting Anomali')
    st.subheader('Proses untuk membuang data-data yang tidak diperlukan')
    st.markdown(""" Proses ini dilakukan dengan tujuan untuk efisiensi analisis,karena apabila dalam suatu dataset,ada data yang rancu,tidak diperlukan,ataupun data yang termasuk anomali,itu harus diperlakukan khusus dimana diantaranya :
    1. Sesuai dengan proses yang sebelumnya yakni Imputasi Data yang merupakan NULL VALUE
    2. Crosscheck ulang dengan pemilik data
    3. Melakukan Penghapusan Data-Data yang tidak diperlukan,rancu,ataupun anomali
    """)
    st.markdown("""
    Dimana dalam dataset ini memiliki beberapa data yang termasuk anomali,dan data yang tidak diperlukan dimana diantaranya adalah :
    
    - **Penghapusan Data yang memiliki total_paid 0**
        - Mengapa dihapus,karena dalam proses RFM,dimana akan menghitung akumulasi dari Frequentcy yaitu Seberapa sering pelanggan melakukan transaksi dan Monetary,atau total uang yang sudah di keluarkan selama bertransaksi menggunakan platform Sribu,sehingga,agar murni hanya pelanggan yang memiliki total_paid yang jelas.
    - **Penghapusan Data dimana pada kolom client_user_id dimana diawalnya tanpa nama atau NULL VALUE,dan pada proses sebelumnya telah diimputasi dengan kata-kata 'No_one'.**
        - Mengapa dihapus,karena apabila dipertahankan akan terjadi rancu dimana user tersebut memiliki transaksi,akan tetapi tanpa nama,sehingga agar clusteringnya agar murni hanya dalam analisis ini,hanya data yang bersih tidak ada kerancuan dalam proses analisisnya.
    - **Penghapusan Data pada kolom Type dengan nama 'deposit'**
        - Mengapa dihapus,dimana setelah melakukan crosscheck ulang dengan pemilik data,yakni Sribu mendapatkan jawaban dimana data pada kolom Type dengan nama 'deposit',memiliki definisi Client mentransfer sejumlah uang dan uang tersebut menjadi deposit untuk membayar jasa yg ada di platform. Karena mentransfer sejumlah uang makanya ada dokumen invoices untuk pencatatan finance, Sehingga kolom Type dengan nama 'deposit',bukan merupakan sebuah data transaksi tapi hanya sekedar transfer uang dan dicatat ke dalam pembukuan keuangan,sehingga 'deposit' memiliki pencatatan invoice.
    """)
    

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

elif literatur == 'Pemisahan Kolom Category menjadi Kolom-Kolom Kategori biner':
    st.header('Pemisahan Kolom Category menjadi Kolom-Kolom Kategori Biner')
    st.subheader('Proses Penjabaran Kolom Category sebelum melakukan Pengolahan Data dengan RFM dan K-Means')
    st.write(''' One-Hot Encoding adalah teknik transformasi data yang digunakan untuk mengubah data kategorikal (data non-numerik) menjadi format numerik yang dapat digunakan dalam algoritma machine learning.
    Teknik ini bekerja dengan membuat kolom baru untuk setiap kategori unik dalam kolom aslinya dan mengisi kolom baru tersebut dengan nilai biner (0 atau 1), tergantung pada apakah kategori itu muncul di baris tertentu
    ''')

    # Data contoh
    data = {'Username': ['Alice', 'Bob', 'Charlie'],
        'Category Ordered': ['Desain Grafis & Branding','Penulisan & Penerjemahan','Web & Pemrograman'],
        'Money': ['100000', '1000000', '350000']}
    df_cat = pd.DataFrame(data)

    st.write('''Contoh Alur Onehot Encoder : 
    Dataset Awal
    ''')
    st.write(df_cat)
    st.markdown(""" Dalam Dataset Awal Terlihat Dimana dalam kolom Category Ordered memiliki 3 kategori yang diorder oleh pelanggan yakni :

    - Alice melakukan order dengan Category Orderan Desain Grafis & Branding dengan harga 100.000
    - Bob melakukan order dengan Category Orderan Penulisan & Penerjemahan dengan harga 1.000.000
    - Charlie melakukan order dengan Category Orderan Web & Pemrograman dengan harga 350.000
    """)
    st.markdown(""" Dengan melakukan Onehot Encoder dengan perintah :

    - df4 = pd.get_dummies(df3_cleaned, columns=['category'])

    Dimana menghasilkan Dataset yang memiliki kolom Category Ordered yang nantinya terpecah sesuai dengan ada berapa kategori yang ada dalam kolom Category Ordered,dan menghasilkan menjadi seperti ini :
    """)
    # Data contoh
    Onehot = {'Username': ['Alice', 'Bob', 'Charlie'],
        'Money': ['100000', '1000000', '350000'],
        'Category Ordered_Desain Grafis & Branding': [1,0,0],
        'Category Ordered_Penulisan & Penerjemahan': [0,1,0],
        'Category Ordered_Web & Pemrograman': [0,0,1]}
    df_Onehot = pd.DataFrame(Onehot)
    st.write(df_Onehot)

        # Inisialisasi session_state untuk tombol
    if "onehot_iya_pressed" not in st.session_state:
        st.session_state.onehot_iya_pressed = False
    if "onehot_tidak_pressed" not in st.session_state:
        st.session_state.onehot_tidak_pressed = False

        # Tombol Iya dan Tidak
    st.write("Apakah Anda ingin melihat Dataset yang akan dianalisa yang telah di Onehot")
    col5, col6 = st.columns(2)
    with col5:
        if st.button("Iya"):
            st.session_state.onehot_iya_pressed = True
            st.session_state.onehot_tidak_pressed = False
    with col6:
        if st.button("Tidak"):
            st.session_state.onehot_iya_pressed = False
            st.session_state.onehot_tidak_pressed = True

    # Logika berdasarkan tombol yang ditekan
    if st.session_state.onehot_iya_pressed:
        st.write("Berikut Adalah Dataset yang Akan Diolah yang Telah di Onehot Encoder")
        st.write(onehot_data)
            
    elif st.session_state.onehot_tidak_pressed:
        st.warning("Baiklah :), silakan lanjutkan aktivitas Anda!")

elif literatur == 'RFMC Data':
    st.header('Data Yang Telah Diolah Melalui Proses RFMC')
    st.subheader('Dataset yang telah di Preprocessing untuk di RFM')
    st.markdown("""
    Pada tahap RFM+C adalah tahapan dimana data masuk kedalam pengolahan untuk mengetahui nilai :
    - Recency
    - Frequency
    - Monetary
    - Category mana saja yang pernah di order oleh pelanggan selama menggunakan platform Sribu
    """)
    st.markdown(""" 
    Dimana proses tersebut dilakukan dengan cara :

    - Memasukkan referensi tanggal yang nantinya digunakan sebagai pengurang dari tanggal kapan pelanggan terakhir melakukan transaksi.
        - Berikut adalah referensi datanya yang diambil dari MAX dari kolom paid_at sehingga mendapatkan hasil yakni tanggal 2 Desember 2024,Pukul 07.00
            - reference_date = datetime(2024, 12, 2, 7, 0, 0) 
            
    - Setelah Memasukkan referensi tanggal,lamgkah selanjutnya adalah melakukan pencarian recency dengan cara 
        - Dataset yang akan diproses di groupping berdasarkan client user id 
        - Melakukan kalkulasi dengan cara referensi tanggal dikurangi dengan kapan pelanggan tersebut terakhir melakukan transaksi
        - Berikut adalah langkah-langkahnya :
            - recency = df4.groupby('client_user_id')['paid_at'].max().reset_index()
            - recency['Recency'] = (reference_date - recency['paid_at']).dt.days
            
    - Selanjutnya adalah melakukan perhitungan untuk mengetahui **Intensitas Pelanggan** atau **Frequency** yakni dengan cara melakukan rangkuman data groupping berdasar kolom 'client_user_id' lalu outputnya adalah angka seberapa banyak nama pelanggan tersebut keluar
        - Berikut adalah langkah-langkahnya :
            - frequency = df4.groupby('client_user_id').size().reset_index(name='Frequency')
    - Monetary atau Total pembayaran per pelanggan,yakni adalah dengan mengakumulasi data pada kolom total_paid dari seiap nilai total_paid yang keluar pada client user id tersebut
        - Berikut adalah langkah-langkahnya :
            - monetary = df4.groupby('client_user_id')['total_paid'].sum().reset_index()
            - monetary.rename(columns={'total_paid': 'Monetary'}, inplace=True)
    - Proses terakhir adalah melakukan pengelompokkan kategori berdasarkan kolom Categpry,dimana dengan tujuan pelanggan dengan Client User ID ini pernah melakukan order dengan kategori apa saja selama menggunakan Platform Sribu
        - Berikut adalah lanngkah-langkahnya :
            - category = df4.groupby('client_user_id')[columns_convert_booltoint].max().reset_index()
    """)
    st.markdown("""
    Setelah melakukan kalkulasi setiap tahap,yakni RFMC,Berikut adalah Dataset yang telah diolah menggunakan metode RFMC memiliki kolom berikut:
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

    dan Berikut adalah output dataset yang telah diolah dengan metode RFMC :
    """)
    st.write(dfproc)
    st.write("Dataset yang telah diolah menggunakan metode RFM sebelum melakukan Clustering,dimasukkan dahulu ke dalam proses pengecheckan cluster dengan Boxplot,dimana memiliki tampilan sebagai berikut  :")
    st.image('IQR 3.png')
    st.write('Dalam BoxPlot diatas terlihat jelas dimana pada kolom Monetary terdapat banyak sekali outliers dimana itu nantinya sangat mempengaruhi hasil Clustering apabila tidak dihapus,dan jumlah data sebelum membersihkan outliers adalah sebanyak 2942 data')
    st.image('IQR 4.png')
    st.write('Setelah melakukan pembersihan Outliers dengan menggunakan IQR,dalam BoxPlot diatas terlihat jelas perbedaannya dimana pada kolom Monetary yang tadinya memiliki rentang yang sangat jauh hingga mencapai kisaran 7M,setelah melakukan pembersihan Outliers hingga tersisa di Monetary kisaran 2.5M keatas,perbedaan se signifikan itu juga nantinya akan memberikan pengaruh yang signifikan pula pada proses clustering nantinya,dan jumlah data setelah membersihkan outliers adalah sebanyak 2548 data')
    st.write('Berikut adalah dataset yang telah diolah dengan metode RFM dan telah dibersihkan dari outliers :')
    st.write(dfwill)

elif literatur == 'Clustering':
    st.header('Proses Clustering')
    st.subheader('Proses terbentuknya hasil akhir yakni Clustering dengan menggunakan K-Means')
    st.markdown(""" Proses Clustering adalah teknik unsupervised learning yang bertujuan untuk mengelompokkan data ke dalam beberapa kelompok atau cluster berdasarkan kesamaan fitur.
    Dalam clustering, data dalam satu kelompok akan lebih mirip satu sama lain dibandingkan dengan data dari kelompok lain. Clustering sering digunakan untuk segmentasi pelanggan, analisis pola, atau penemuan struktur tersembunyi dalam dataset.
    
    Dalam Proses Clustering untuk project Clustering pelanggan melalui Data Transaksi Sribu ini menggunakan algoritma K-Means,dimana telah dijelaskan pada tab Algoritma,dan disini lebih ke penjelasan step by stepnya,dimana :
    
    - Setelah melakukan RFM dan pembersihan Outliers,selanjutnya aalah melakukan Scalling dimana dalam Scalling kali ini adalah untuk menyamaratakan nilai dari setiap kolom menjadi 0-1 sehingga dalam melakukan modelling tidak menemukan nilai yang terlampau jauh selisih antara nilai kolom 1 dengan yang lainnya
    - Setelah Scalling adalah melakukan evaluasi guna menentukan cluster mana yang paling optimal sebelum menentukan nilai cluster yang akan digunakan
    - Penentuan Nilai Cluster dengan menggunakan nilai k yang ditentukan dengan Curva WCSS sebelumnya
    - Visualisasi Persebaran Nilai Cluster
    - Evaluasi dengan menggunakan Silhouette Score
    """)
    litclus = ['Scalling', 'Evaluasi WCSS', 'Inisialisasi Nilai K', 'Visualisasi Persebaran Nilai Cluster','Evaluasi Menggunakan Nilai Silhouette Score']
    literaturclus = st.selectbox('Pilih Step Clustering yang ingin diketahui :', litclus)

    if literaturclus == 'Scalling':
        st.header('Scalling')
        st.subheader('Skala Ulang')
        st.write("""
        Scaling atau skala ulang data adalah proses transformasi nilai-nilai fitur dalam dataset agar berada pada rentang yang sama. 
        Hal ini penting terutama dalam algoritma seperti K-Means, di mana perhitungan jarak (misalnya Euclidean distance) sangat dipengaruhi oleh perbedaan skala antar fitur.
        Jika satu fitur memiliki rentang nilai yang jauh lebih besar dari fitur lain, hasil clustering dapat bias.

        Dimana dalam Proses Analisis kali ini,adalah dengan metode Scalling menggunakan MinMaxScaller,dimana Scalling menggunakan MinMaxScaller adalah 
        MinMaxScaler adalah teknik scaling yang mengubah nilai data ke dalam rentang tertentu, biasanya antara 0 dan 1.
        Metode ini bekerja dengan cara meregangkan atau meremas data berdasarkan nilai minimum dan maksimum dalam setiap fitur.

        berikut adalah kelebihan dan kekurangan dalam penggunaan MinMaxScaller
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Kelebihan MinMaxScaller")
            st.markdown("""
            - Memiliki rentang nilai yang Konsisten
            - Tidak Memengaruhi Distribusi
            - Mudah Diterapkan
            - Ideal untuk Algoritma Berbasis Jarak
            """)
        with col2:
            st.subheader("Kelemahan MinMaxScaller")
            st.markdown("""
            - Sensitif terhadap Outlier
            - Bergantung pada Rentang Data
            """)
            
        st.markdown("""Kapan Menggunakan MinMaxScaler 

        Tips menggunakan MinMaxScaller :
        - Saat ingin menjaga rentang data dalam [0, 1] untuk memastikan kompatibilitas dengan model tertentu.
        - Jika data tidak memiliki outlier ekstrem.
        - Saat distribusi data sudah sesuai dengan kebutuhan analisis dan tidak perlu diubah.
        - Ketika menggunakan algoritma seperti K-Means, KNN, atau Neural Networks yang performanya sangat dipengaruhi oleh skala fitur.
        """)
        st.write('Berikut adalah dataset yang telah di scalling dengan menggunakan MinMaxScaller : ')
        st.write(scalling)
        
    elif literaturclus == 'Evaluasi WCSS':
        st.header('Evaluasi WCSS')
        st.subheader('Evaluasi Menggunakan metode WCSS ( Within-Cluster Sum of Squares)')
        st.write("""WCSS adalah singkatan dari Within-Cluster Sum of Squares, yaitu metrik yang digunakan dalam clustering untuk mengevaluasi seberapa baik data telah dikelompokkan ke dalam cluster. WCSS mengukur jumlah kuadrat jarak antara setiap titik data dalam cluster dengan centroidnya.
        """)
        st.image('WCSS.png')
        st.write("""Telihat dalam Curva Elbow untuk penentuan jumlah nilai cluster (k) yang paling optimal,terlihat bahwa :
        **Cluster yang paling optimal dalam persebaran clusternya,adalah di angka 4 cluster.**
        """)
    elif literaturclus == 'Inisialisasi Nilai K':
        st.header('Inisialisasi Nilai K')
        st.subheader('Penentuan Berapa Jumlah Cluster')
        st.write("""Setelah melakukan evaluasi menggunakan WCSS proses selanjutnya adalah memasukkan nilai cluster yang sudah ditampilkan dengan menggunakan Curva WCSS selanjutnya adalah memasukkan nilai k yang sudah ditentukan.
        Dimana dalam analisis kali ini menggunakan nilai cluster 4,dan memanggil algoritma yang akan digunakan,dimana menggunakan perintah sebagai berikut :
        
        # Jumlah cluster optimal (dari metode Elbow) lalu dijalankan menggunakan algoritma K-Means
        - n_clusters = 4
        - kmeans = KMeans(n_clusters=n_clusters,init='k-means++', random_state=42)

        Setelah melakukan pemanggilan selanjutnya adalah melakukan clustering dan ketika sudah diolah,dimasukkan kedalam kolom cluster dengan membuat kolom baru,yakni Kolom Cluster,dengan menggunakan fungsi 
        - df5_cleaned['Cluster'] = kmeans.fit_predict(rfm_scaled)
        """)
    elif literaturclus == 'Visualisasi Persebaran Nilai Cluster':
        st.header('Visualisasi')
        st.subheader('Visualisasi Persebaran Nilai Cluster')
        st.markdown("""
        Dataset yang telah diolah menggunakan metode RFM dan telah melakukan proses clustering dengan metode K-Means,dari data diatas menghasilkan persebaran cluster sebanyak 4 cluster,dengan persebaran anggota seperti berikut :
        - Cluster 0 = 1069 anggota
        - Cluster 1 = 770 anggota
        - Cluster 2 = 334 anggota
        - Cluster 3 = 375 anggota

        Berikut adalah dataset final dan Proporsi Distribusi Nilai setiap anggota cluster dari dataset yang telah diolah dengan metode RFM dan pengclusteran dengan algoritma K-Means :
        """)
        st.write(dfcluster)
        st.write('Distribusi Anggota Setiap Cluster')
        st.image('Cluster.png')
    elif literaturclus == 'Evaluasi Menggunakan Nilai Silhouette Score':
        st.header('Evaluasi Silhouettem Score')
        st.subheader('Evaluasi Final setelah clustering')
        st.write("Evaluasi menggunakan Silhouette Score adalah Metrik evaluasi untuk mengukur kualitas clustering. Nilai ini menunjukkan seberapa baik data telah dikelompokkan dengan mempertimbangkan kedekatan antar anggota dalam satu cluster (cohesion) dan perbedaan antar cluster (separation).")

        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Kelebihan Silhouette Score")
            st.markdown("""
            - **Interpretasi Jelas** : Nilai Silhouette Score memberikan indikasi langsung tentang seberapa baik cluster terbentuk.
            - **Metrik Komprehensif** : Menggabungkan aspek internal (kedekatan dalam cluster) dan eksternal (perbedaan antar cluster).
            - **Algoritma Agnostik** : Cocok digunakan untuk mengevaluasi berbagai algoritma clustering.
            """)
        with col4:
            st.subheader("Kelemahan Silhouette Score")
            st.markdown("""
            - **Sensitif pada Skala Data** : Hasil dapat bias jika data tidak diskalakan dengan benar.
            - **Tidak Efektif untuk Cluster Non-Linear** : Tidak ideal untuk bentuk cluster kompleks, seperti cluster berbentuk melengkung atau non-konveks.
            - **Bias pada Jumlah Cluster** : Nilai cenderung lebih rendah saat jumlah cluster sangat kecil atau sangat besar.
            - **Kompleksitas Perhitungan** : Membutuhkan perhitungan jarak antara semua pasangan data, yang dapat memakan waktu pada dataset besar.
            """)

        st.markdown(""" 
        Dalam Proses Clustering Pelanggan pada Platform Sribu menggunakan algoritma K-Means pada project kali ini,menghasilkan nilai evaluasi sebesar 0.60,dimana :
        - Dengan nilai 0.60 menunjukkan bahwa cluster memiliki pemisahan yang cukup baik. Data dalam setiap cluster relatif lebih dekat dengan centroid cluster masing-masing dibandingkan dengan cluster lain.
        - Persebaran anggota yang tidak terlalu timpang antara cluster menunjukkan pembagian yang cukup proporsional, sehingga dapat memberikan wawasan beragam tentang karakteristik pelanggan Sribu.
        """)
