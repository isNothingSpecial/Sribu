import streamlit as st
import os

# --- HEADER TIM ---
st.markdown("<h1 style='text-align: center;'>👨‍💻 Tim Pengembang</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Kelompok 1 - Bootcamp Data Science</h4>", unsafe_allow_html=True)
st.markdown("---")

st.write("Aplikasi segmentasi pelanggan ini dikembangkan sebagai *Final Project* oleh tim Kelompok 1, dengan menggabungkan keahlian dalam Analisis Data, Machine Learning, dan UI/UX Design.")
st.write("") # Spasi tambahan

# --- PROFIL ANGGOTA (Menggunakan desain "Card" warna-warni) ---
col1, col2, col3 = st.columns(3)

with col1:
    # Menggunakan kotak info biru untuk menonjolkan Ketua Tim
    st.info("👑 **Ketua Kelompok**")
    st.subheader("Bagus Rahma AC")
    st.write("Data Scientist / Data Analyst")
    # Opsional: Anda bisa menghapus tanda '#' dan menambahkan link LinkedIn/GitHub Anda di sini
    # st.markdown("[LinkedIn](#) | [GitHub](https://github.com/isNothingSpecial)")
    
with col2:
    # Menggunakan kotak hijau untuk Anggota
    st.success("👤 **Anggota**")
    st.subheader("Tannu Wibowo")
    st.write("Data Scientist / Data Analyst")
    
with col3:
    st.success("👤 **Anggota**")
    st.subheader("Annisa Firdaus Nst")
    st.write("Data Scientist / Data Analyst")

st.markdown("---")

# --- BAGIAN SPONSOR / DUKUNGAN ---
st.markdown("<h3 style='text-align: center;'>Supported By :</h3>", unsafe_allow_html=True)
st.write("") 

# Trik Layout: Menggunakan 4 kolom ([1, 2, 2, 1]) untuk meletakkan 2 logo tepat di tengah layar
col_empty1, col_sribu, col_ds, col_empty2 = st.columns([1, 2, 2, 1])

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with col_sribu:
    sribu_path = os.path.join(BASE_DIR, "sribu.png")
    try:
        if os.path.exists(sribu_path):
            st.image(sribu_path, use_column_width=True) # Tetap menggunakan versi lama agar aman
        else:
            st.image("https://blog.sribu.com/wp-content/uploads/2023/10/Logo-Sribu-2023.png", use_column_width=True)
    except:
        st.error("Gagal memuat logo Sribu")

with col_ds:
    ds_path = os.path.join(BASE_DIR, "ds.png")
    try:
        if os.path.exists(ds_path):
            st.image(ds_path, use_column_width=True)
        else:
            # Fallback URL jika ds.png (Digital Skola) terhapus/hilang
            st.image("https://digitalskola.com/wp-content/uploads/2021/04/Logo-Digital-Skola-1-1.png", use_column_width=True)
    except:
        st.error("Gagal memuat logo ds.png")
