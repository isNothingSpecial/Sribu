import streamlit as st
import pandas as pd # Pandas (version : 1.1.5) 
import numpy as np # Numpy (version : 1.19.2)
import matplotlib.pyplot as plt # Matplotlib (version :  3.3.2)
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans # Scikit Learn (version : 0.23.2)
import seaborn as sns # Seaborn (version : 0.11.1)
from streamlit_webrtc import webrtc_streamer

df = pd.read_excel('result_rfm_3cluster.xlsx')

kms = KMeans(n_clusters=3, init='k-means++', random_state=42)
kms.fit(df)

st.title(''' CLUSTERING PELANGGAN PLATFORM SRIBU DENGAN MENGGUNAKAN METODE KOMBINASI ANTARA RFM (RECENCY,FREQUENCY,MONETARY) DAN ALGORITMA K-MEANS ''')
st.write('Prediksi Data Baru')

input_recency = st.number_input ("Recency", )
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_frequency = st.number_input ("Frequency", )
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_monetary = st.number_input ("Monetary")

result = "-"

if st.button("Predict"):
        
Predict =st.button("Predict")

if Predict:
    if input_recency != str(0.00) and input_frequency != str(0.00) and input_monetary != str(0.00):
        recency = float(input_recency)
        frequency = float(input_frequency)
        monetary = float(input_monetary)
        clustering_data = ([[recency, frequency, monetary]])
        scaler = StandardScaler()
        clustering_data_scaled = scaler.fit_transform(clustering_data)
        clustering_data_scaled
        prediction = kms.predict([[clustering_data_scaled]])[0]
        result = str(prediction)
        if result =='0':
            st.subheader(f"Cluster : {result}")
            st.write('Cluster 0 merupakan Cluster dimana Cluster dimana termasuk cluster pelanggan bertipe One-Time Buyers,dimana Cluster tersebut merupakan dimana Pelanggan memiliki Recency sekian-Frequency Sekian-Monetary Sekian,sehingga pelanggan yang berada di Cluster ini bisa terbentuk karena banyak faktor,apakah mereka merupakan pelanggan baru,dimana mereka masih mencoba - coba membeli jasa-jasa freelancer yang telah disediakan oleh Sribu untuk pertama kalinya,apakah mereka merupakan pelanggan yang hanya membutuhkan jasa freelancer hanya di hari mereka order saja,sehingga hanya menggunakan jasa freelancer ketika dia membutuhkan saja.')
        elif result =='1':
            st.subheader(f"Prediction : {result}")
            st.write('Cluster 1 merupakan Cluster dimana Cluster dimana termasuk cluster pelanggan bertipe Potentials Buyers,dimana Cluster tersebut merupakan dimana Pelanggan memiliki Recency sekian-Frequency Sekian-Monetary Sekian,sehingga pelanggan yang berada di Cluster ini bisa terbentuk karena banyak faktor,mereka merupakan pelanggan yang memiliki frequency yang lumayan tinggi,dan history melakukan transaksi terbilang relatif singkat,dimana bisa disebakan karena Pelanggan yang berada di cluster ini terkadang membutuhkan jasa-jasa freelancer sehingga akhirnya ketika ia membutuhkan lebih memilih untuk membeli jasa-jasa freelancer yang telah disediakan oleh Sribu.')
        elif result =='2':
            st.subheader(f"Prediction : {result}")
            st.write('Cluster 2 merupakan Cluster dimana Cluster dimana termasuk cluster Loyal Customers,dimana Cluster tersebut merupakan dimana Pelanggan memiliki Recency sekian-Frequency Sekian-Monetary Sekian,sehingga pelanggan yang berada di Cluster tersebut merupakan dimana Pelanggan melakukan sering sekali melakukan transaksi dengan kuantitas yang tergolong banyak dan memiliki nilai history transaksi yang rendah,dimana bisa disebakan karena Pelanggan yang berada di cluster ini sangat membutuhkan jasa-jasa freelancer sehingga akhirnya sering membeli jasa-jasa freelancer yang telah disediakan oleh Sribu.')
    else:
        result = "-"
else :
    result = "Please complete form above!"