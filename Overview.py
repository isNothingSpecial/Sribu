import streamlit as st
import os
# 1. Konfigurasi Halaman (Harus di baris paling atas)
st.set_page_config(
    page_title="Portfolio Sribu | Segmentasi Pelanggan",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Header dan Subheader yang Lebih Bersih
st.markdown("<h1 style='text-align: center;'>🎯 Segmentasi Pelanggan Sribu.com</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: gray;'>Pendekatan Analisis RFM & Algoritma K-Means</h3>", unsafe_allow_html=True)
st.write("") # Memberikan sedikit jarak

# 3. Hero Section (Membagi Logo dan Konteks agar logo tidak memakan seluruh layar)
col_img, col_intro = st.columns([1, 2.5])

with col_img:
    # Catatan: use_column_width sudah deprecated, gunakan use_container_width
    try:
        st.image("sribu.png", use_container_width=True)
    except:
        st.error("Gambar Sribu.png tidak ditemukan.")

with col_intro:
    st.write("""
    **Sribu (sebelumnya Sribulancer)** adalah platform pasar daring terkemuka di Indonesia yang menghubungkan 
    pemilik bisnis dengan pekerja lepas (freelancer) profesional di berbagai bidang seperti desain grafis, 
    pemrograman web, hingga pemasaran.
    """)
    
    # Menggunakan kotak highlight untuk menonjolkan tujuan utama proyek
    st.info("""
    **💡 Objektif Proyek:** 
    Mengidentifikasi dan memetakan karakteristik pelanggan berdasarkan perilaku transaksi mereka. 
    Hasil clustering ini digunakan untuk menciptakan strategi retensi dan pemasaran yang lebih terarah (personalized).
    """)

st.markdown("---")

# 4. Penggunaan Tabs untuk merapikan informasi agar pengguna tidak perlu banyak scroll ke bawah
tab1, tab2 = st.tabs(["📊 Metodologi Proyek", "🏢 Latar Belakang Perusahaan"])

with tab1:
    st.subheader("Parameter Analisis")
    st.write("Pemetaan cluster dilakukan dengan mengekstrak 4 pilar utama perilaku pelanggan:")
    
    # Menggunakan st.metric untuk visualisasi parameter yang menarik
    col_r, col_f, col_m, col_c = st.columns(4)
    col_r.metric(label="Recency", value="Waktu", delta="Kapan transaksi terakhir?")
    col_f.metric(label="Frequency", value="Jumlah", delta="Seberapa sering order?")
    col_m.metric(label="Monetary", value="Nilai", delta="Berapa total pengeluaran?")
    col_c.metric(label="Category", value="Jenis", delta="Layanan apa yang dibeli?", delta_color="off")
    
    st.write("")
    # Menggunakan kotak sukses untuk menyoroti alasan pemilihan algoritma
    st.success("""
    **⚙️ Mengapa menggunakan K-Means?**  
    Algoritma *Unsupervised Learning* ini dipilih karena **cepat dan efisien** dalam memproses dataset pelanggan yang besar, 
    serta menghasilkan pemisahan kelompok yang logis dan mudah diterjemahkan ke dalam keputusan bisnis.
    """)

with tab2:
    col_hist, col_achieve = st.columns(2)
    
    with col_hist:
        st.subheader("Sejarah Singkat")
        st.markdown("""
        - **2011**: Diluncurkan sebagai platform kontes desain.
        - **2012**: Menerima pendanaan awal dari East Ventures.
        - **2014**: Investasi dari Asteria Japan, ekspansi layanan di luar desain.
        - **2018**: Pendanaan dari Crowdworks (Jepang).
        - **2022**: Diakuisisi penuh oleh Mynavi Japan.
        """)
        
    with col_achieve:
        st.subheader("Pencapaian")
        st.markdown("""
        - Melayani lebih dari **30.000 klien**.
        - Memiliki komunitas freelancer yang dikurasi ketat berdasarkan kualitas komunikasi, waktu, dan hasil.
        - **Penghargaan:** Indonesia ICT Awards 2013 & SparxUp Award 2011.
        """)
