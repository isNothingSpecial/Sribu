import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# 1. Optimasi Performa: Cache Model agar tidak ditraining ulang setiap kali tombol diklik
@st.cache_resource
def load_and_train_model():
    df = pd.read_csv('data_will_cluster.csv')
    rfm_features = [
        'Recency', 'Frequency', 'Monetary',
        'category_Desain Grafis & Branding', 'category_Gaya Hidup',
        'category_Konsultasi', 'category_Pemasaran & Periklanan',
        'category_Penulisan & Penerjemahan', 'category_Unknown',
        'category_Video, Fotografi & Audio', 'category_Web & Pemrograman'
    ]
    df_rfm = df[rfm_features]
    
    # Catatan: Jika di halaman literatur Anda menggunakan MinMaxScaller, 
    # pastikan Anda juga men-scaling data di sini pada implementasi aslinya.
    kms = KMeans(n_clusters=4, init='k-means++', random_state=42)
    kms.fit(df_rfm)
    return kms

kms = load_and_train_model()

# --- UI HEADER ---
st.markdown("<h1 style='text-align: center;'>🔮 Prediksi Segmen Pelanggan</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Simulasi Machine Learning untuk memprediksi cluster pelanggan baru secara Real-Time</p>", unsafe_allow_html=True)
st.markdown("---")

# --- UI INPUT SECTION ---
st.subheader("📝 Masukkan Data Pelanggan Baru")

# Membagi RFM menjadi 3 kolom agar hemat tempat dan rapi
col_r, col_f, col_m = st.columns(3)

with col_r:
    input_recency = st.number_input("Recency (Hari)", min_value=0, step=1, help="Berapa hari sejak transaksi terakhir?")
with col_f:
    input_frequency = st.number_input("Frequency (Kali)", min_value=0, step=1, help="Berapa kali pelanggan pernah bertransaksi?")
with col_m:
    input_monetary = st.number_input("Monetary (Rp)", min_value=0, step=100000, format='%d', help="Total nominal transaksi pelanggan.")

st.write("") # Spasi

# Menggunakan Multiselect alih-alih Checkbox yang memanjang ke bawah
kategori_list = [
    'Desain Grafis & Branding', 'Gaya Hidup', 'Konsultasi', 
    'Pemasaran & Periklanan', 'Penulisan & Penerjemahan', 
    'Unknown', 'Video, Fotografi & Audio', 'Web & Pemrograman'
]

selected_categories = st.multiselect(
    "Kategori Layanan yang Pernah Dipesan:", 
    options=kategori_list,
    help="Pilih satu atau lebih kategori layanan."
)

# Konversi pilihan multiselect menjadi array One-Hot Encoding (0 atau 1)
category_input = [1 if cat in selected_categories else 0 for cat in kategori_list]

st.markdown("---")

# --- PREDICTION BUTTON & OUTPUT ---
# Menengahkan tombol prediksi
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
with col_btn2:
    predict_btn = st.button("🚀 Prediksi Cluster Pelanggan", use_container_width=True)

if predict_btn:
    if input_frequency > 0 and input_monetary > 0:
        # Prepare input data
        new_data = np.array([[input_recency, input_frequency, input_monetary] + category_input])
        
        # Predict cluster
        prediction = kms.predict(new_data)[0]
        
        # --- UI TAMPILAN HASIL ---
        st.subheader("🎯 Hasil Analisis")
        
        # Menampilkan detail input sebagai verifikasi
        kat_teks = ', '.join(selected_categories) if selected_categories else 'Tidak ada'
        
        if prediction == 0:
            st.success("### 👤 Cluster 0: One-Time Buyers")
            st.write("Pelanggan ini cenderung hanya melakukan transaksi sesekali atau baru mencoba layanan Sribu.")
            with st.expander("💡 Rekomendasi Aksi Bisnis (Actionable Insight)"):
                st.write("- **Strategi Pemasaran:** Berikan promo diskon *first-timer* atau *bundling* layanan untuk mendorong transaksi kedua.")
                st.write("- **Komunikasi:** Kirimkan email edukasi tentang manfaat jangka panjang menggunakan freelancer Sribu.")
                
        elif prediction == 1:
            st.info("### 👥 Cluster 1: Potential Buyers")
            st.write("Pelanggan ini menunjukkan ketertarikan yang solid dan memiliki potensi untuk menjadi pelanggan setia.")
            with st.expander("💡 Rekomendasi Aksi Bisnis (Actionable Insight)"):
                st.write("- **Strategi Pemasaran:** Tawarkan program *referral* atau *cashback* bersyarat.")
                st.write("- **Komunikasi:** Ingatkan mereka tentang kategori layanan lain yang relevan dengan riwayat pesanan mereka.")

        elif prediction == 2:
            st.warning("### ⭐ Cluster 2: Loyal Customers")
            st.write("Pelanggan dengan frekuensi transaksi tinggi. Mereka adalah pilar pendapatan reguler platform.")
            with st.expander("💡 Rekomendasi Aksi Bisnis (Actionable Insight)"):
                st.write("- **Strategi Pemasaran:** Masukkan ke dalam program *Loyalty/VIP*. Jangan terlalu sering memberi diskon harga, melainkan berikan *value-add* (prioritas *support*, akses ke top freelancer).")
                
        elif prediction == 3:
            st.error("### 💎 Cluster 3: High-Value Customers") # Menggunakan st.error (merah) atau komponen lain agar mencolok
            st.write("Pelanggan 'Paus' (Whales). Mungkin frekuensinya tidak selalu paling tinggi, namun nilai proyek (Monetary) mereka sangat masif.")
            with st.expander("💡 Rekomendasi Aksi Bisnis (Actionable Insight)"):
                st.write("- **Strategi Pemasaran:** Berikan layanan *Account Manager* khusus atau *Key Account Handling*.")
                st.write("- **Komunikasi:** Kirimkan hadiah eksklusif tahunan dan laporan personal tentang efisiensi yang telah mereka capai.")
                
        # Menampilkan ulang data yang diinput untuk konfirmasi visual
        st.write("---")
        st.write(f"**Ringkasan Data Input:** Recency: `{input_recency} hari` | Frequency: `{input_frequency} kali` | Monetary: `Rp {input_monetary:,}` | Kategori: `{kat_teks}`")

    else:
        st.warning("⚠️ Masukkan nilai Frequency dan Monetary yang valid (lebih dari 0) untuk melakukan prediksi.")
