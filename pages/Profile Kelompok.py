import streamlit as st
from streamlit_webrtc import webrtc_streamer

# Menggunakan HTML dan CSS untuk membuat header dan subheader rata tengah
st.markdown(
    """
    <h1 style='text-align: center;'>KELOMPOK 1</h1>
    """, 
    unsafe_allow_html=True
)

# Membuat tiga kolom
col1, col2 = st.columns(2)

# Menampilkan konten di setiap kolom
with col1:
    st.header("Bagus Rahma Aulia Chandra")
    st.write("Ketua Kelompok")

with col2:
    st.header("Tannu Wibowo")
    st.write("Anggota")

col3, col4 = st.columns(2)

with col3:
    st.header("Annisa Firdaus Nasution")
    st.write("Anggpta")

with col4:
    st.header("Ismi Nurhadiyanti Rusmana")
    st.write("Anggpta")

st.write("Supported By :

col5, col6 = st.columns(2)

with col5:
     st.image("Sribu.png", use_column_width=True)

with col6:
     st.image("ds.png", use_column_width=True)
