import streamlit as st
from streamlit_webrtc import webrtc_streamer

# Menggunakan HTML dan CSS untuk membuat header dan subheader rata tengah
st.header('KELOMPOK 1')

st.markdown(
    """
    <h3 style='text-align: center;'>Bagus Rahma Aulia Chandra</h3>
    <h5 style='text-align: center;'>Ketua Kelompok 1</h5>
    """, 
    unsafe_allow_html=True
)

# Membuat tiga kolom
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Tannu Wibowo")
    st.write("Anggota Kelompok 1")

with col2:
    st.subheader("Annisa Firdaus Nst")
    st.write("Anggpta Kelompok 1")

with col3:
    st.subheader("Ismi Nurhadiyanti")
    st.write("Anggpta Kelompok 1")

st.subheader("Supported By :")

col4, col5 = st.columns(2)

with col4:
     st.image("Sribu.png", use_column_width=True)

with col5:
     st.image("ds.png", use_column_width=True)
