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
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("> Bagus Rahma AC")
    st.write("Ketua Kelompok 1")
    
with col2:
    st.subheader("> Tannu Wibowo")
    st.write("Anggota Kelompok 1")

with col3:
    st.subheader("> Annisa Firdaus Nst")
    st.write("Anggota Kelompok 1")

with col4:
    st.subheader("> Ismi Nurhadiyanti")
    st.write("Anggota Kelompok 1")

st.subheader("Supported By :")

col5, col6 = st.columns(2)

with col5:
     st.image("Sribu.png", use_column_width=True)

with col6:
     st.image("ds.png", use_column_width=True)
