import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi Halaman
st.set_page_config(page_title="Analytical Process", layout="wide")

# (Asumsi data sudah di-load di sini)
# df = pd.read_csv('Data_Sales_Platform_SRIBU.csv')
# df_missing1 = pd.read_csv('data_missing_1.csv')
# ... (load dataset lainnya sesuai kode asli Anda)

# --- HEADER ---
st.markdown("<h1 style='text-align: center;'>📖 Storytelling & Analytical Process</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Dokumentasi langkah demi langkah dari raw data hingga model Machine Learning</p>", unsafe_allow_html=True)
st.markdown("---")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Tahapan Analisis")
tahapan = [
    '1. Dataset Awal', 
    '2. Explorasi Dataset (EDA)', 
    '3. Treatment Dataset',
    '4. Penghapusan Anomali',
    '5. Algoritma (RFM & K-Means)',
    '6. One-Hot Encoding', 
    '7. Proses RFMC',
    '8. Model Clustering'
]
pilihan = st.sidebar.radio("Pilih Proses:", tahapan)

# --- LOGIKA KONTEN BERDASARKAN PILIHAN ---

if pilihan == '1. Dataset Awal':
    st.header("1. Dataset Awal")
    st.write("Dataset transaksi pelanggan selama 1 tahun dari Platform Sribu dengan total fitur awal:")
    
    # Menampilkan data dalam expander atau dataframe agar rapi
    st.dataframe(df, use_container_width=True) # Gunakan dataframe agar ada fitur scroll
    
    st.info("""
    **Fitur Utama:** Nama Jobs, Type, Category, Subcategory, Client User Id, Register Date, Order Date, Status Invoice, Paid At, Total Paid.
    """)

elif pilihan == '2. Explorasi Dataset (EDA)':
    st.header("2. Explorasi Dataset (EDA)")
    st.write("Menjelajahi karakteristik dasar dataset untuk menemukan anomali, tipe data yang tidak sesuai, dan missing values.")
    
    # Mengganti tombol "Iya/Tidak" dengan TABS yang jauh lebih praktis
    tab1, tab2, tab3 = st.tabs(["📊 Info Tipe Data", "🔍 Cek Missing Value", "📂 Detail Data Kosong"])
    
    with tab1:
        st.subheader("Peninjauan Tipe Data")
        st.code("""
        # Rangkuman df.info()
        - nama_jobs      : 8233 non-null (object)
        - client_user_id : 8194 non-null (object)
        - register_date  : 8233 non-null (datetime64[ns])
        ...
        """, language='text')
        
    with tab2:
        st.subheader("Pengecekan Missing Value")
        st.error("""
        **Ditemukan beberapa anomali:**
        - `category` & `subcategory`: 1522 missing values
        - `status_invoice`: 3312 missing values
        - `client_user_id`: 39 missing values
        """)
        
    with tab3:
        st.subheader("Investigasi Data Kosong")
        st.write("Analisis mendalam terhadap baris yang memiliki nilai Null:")
        with st.expander("Lihat 1452 baris Status Invoice tidak jelas (namun Total Paid terisi)"):
            st.dataframe(df_missing1, use_container_width=True)
        with st.expander("Lihat 39 baris Client User ID kosong"):
            st.dataframe(df_missing5, use_container_width=True)

elif pilihan == '3. Treatment Dataset':
    st.header("3. Treatment Terhadap Dataset")
    
    tab_imp, tab_out = st.tabs(["🛠️ Imputasi Null Value", "✂️ Penanganan Outliers"])
    
    with tab_imp:
        st.write("Agar tidak menjadi noise saat proses RFM, missing values diimputasi dengan nilai default.")
        st.code("""
        df['status_invoice'] = df['status_invoice'].fillna('success')
        df['category'] = df['category'].fillna('Unknown')
        df['client_user_id'] = df['client_user_id'].fillna('No_one')
        """, language='python')
        
    with tab_out:
        st.write("Outliers pada kolom numerik (`total_paid`) diatasi menggunakan metode **Interquartile Range (IQR)**.")
        col1, col2 = st.columns(2)
        with col1:
            st.image('IQR 3.png', caption='Sebelum: Outliers ekstrem hingga 7M')
        with col2:
            st.image('IQR 4.png', caption='Sesudah: Data tersaring di bawah 2.5M')
            
        with st.expander("Lihat Perhitungan Matematika IQR"):
            st.latex(r"IQR = Q_3 - Q_1")
            st.latex(r"Lower Bound = Q_1 - 1.5 \times IQR")
            st.latex(r"Upper Bound = Q_3 + 1.5 \times IQR")
            st.write("- **Q1:** 10,000")
            st.write("- **Q3:** 638,931")

elif pilihan == '4. Penghapusan Anomali':
    st.header("4. Crosscheck & Deleting Anomali")
    st.write("Untuk menjaga kemurnian hasil K-Means, data yang tidak merepresentasikan transaksi organik dihapus.")
    
    st.warning("**1. Total Paid = 0**\nDihapus karena akan merusak perhitungan akumulasi *Monetary* pada tahap RFM.")
    st.warning("**2. Client User ID = 'No_one'**\nTransaksi tanpa identitas pengguna (anonim) tidak bisa dikelompokkan dalam segmentasi retensi pelanggan.")
    st.warning("**3. Type = 'deposit'**\nBerdasarkan konfirmasi dengan *domain expert* Sribu, ini adalah pencatatan top-up saldo internal/finance, bukan transaksi pembelian jasa.")

elif pilihan == '5. Algoritma (RFM & K-Means)':
    st.header("5. Pemilihan Algoritma")
    
    tab_rfm, tab_kmeans = st.tabs(["Metode Pendekatan: RFM", "Machine Learning: K-Means"])
    with tab_rfm:
        st.subheader("Recency, Frequency, Monetary")
        col_r, col_f, col_m = st.columns(3)
        col_r.info("**Recency (Kebaharuan)**\nInterval waktu sejak transaksi terakhir. Mengukur tingkat *engagement* saat ini.")
        col_f.info("**Frequency (Intensitas)**\nJumlah transaksi. Mengukur tingkat loyalitas pelanggan.")
        col_m.info("**Monetary (Nilai Uang)**\nTotal pengeluaran. Mengukur *Customer Lifetime Value* (CLV).")
        
    with tab_kmeans:
        st.subheader("Mengapa K-Means?")
        st.write("K-Means mengelompokkan pelanggan berdasarkan kedekatan jarak (*Euclidean Distance*) dari titik pusat (*Centroid*).")
        st.success("**Kelebihan:** Sangat cepat untuk dataset besar dan pemisahan clusternya mudah diterjemahkan ke strategi bisnis Sribu.")

elif pilihan == '6. One-Hot Encoding':
    st.header("6. One-Hot Encoding (OHE)")
    st.write("Algoritma K-Means hanya menerima data numerik. Kolom `Category` (teks) harus dipecah menjadi kolom biner (0 dan 1).")
    
    st.code("df_encoded = pd.get_dummies(df_cleaned, columns=['category'])", language='python')
    
    st.write("**Hasil Transformasi:**")
    st.dataframe(onehot_data, use_container_width=True)

elif pilihan == '7. Proses RFMC':
    st.header("7. Ekstraksi Fitur (RFMC)")
    st.write("Mengubah data transaksi mentah (*transaction-level*) menjadi data agregat per pelanggan (*customer-level*).")
    
    with st.expander("Lihat Logika Agregasi Pandas"):
        st.code("""
        # Recency (Max Order Date vs Reference Date)
        recency = df.groupby('client_user_id')['paid_at'].max()
        
        # Frequency (Count of Orders)
        frequency = df.groupby('client_user_id').size()
        
        # Monetary (Sum of Total Paid)
        monetary = df.groupby('client_user_id')['total_paid'].sum()
        """, language='python')
        
    st.write("Tabel Final Siap Clustering:")
    st.dataframe(dfwill, use_container_width=True)

elif pilihan == '8. Model Clustering':
    st.header("8. Proses Clustering K-Means")
    
    tab_scale, tab_elbow, tab_result, tab_eval = st.tabs(["1. Scaling", "2. K-Optimal (Elbow)", "3. Hasil Cluster", "4. Evaluasi Model"])
    
    with tab_scale:
        st.write("**MinMaxScaler** digunakan untuk menekan semua rentang angka (seperti Monetary yang jutaan dan Frequency yang satuan) menjadi skala 0 hingga 1.")
        st.dataframe(scalling.head(), use_container_width=True)
        
    with tab_elbow:
        st.write("Menggunakan metode *Within-Cluster Sum of Squares (WCSS)* untuk mencari patahan (*Elbow*).")
        st.image('WCSS.png', caption='Patahan optimal (k) berada di angka 4')
        
    with tab_result:
        st.write("**Distribusi 4 Cluster Pelanggan Sribu:**")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Cluster 0", "1,069 Pelanggan")
        col2.metric("Cluster 1", "770 Pelanggan")
        col3.metric("Cluster 2", "334 Pelanggan")
        col4.metric("Cluster 3", "375 Pelanggan")
        st.image('Cluster.png')
        
    with tab_eval:
        st.write("Mengukur validitas pemisahan cluster menggunakan *Silhouette Score*.")
        st.metric(label="Silhouette Score", value="0.60", delta="Good Cohesion & Separation")
        st.success("Skor **0.60** mengindikasikan bahwa data di setiap kelompok sudah relatif homogen di dalam clusternya sendiri, dan cukup berbeda batasnya dari cluster tetangga.")
