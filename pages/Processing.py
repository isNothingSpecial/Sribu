import streamlit as st
import pandas as pd # Pandas (version : 1.1.5) 
import numpy as np # Numpy (version : 1.19.2)
import matplotlib.pyplot as plt # Matplotlib (version :  3.3.2)
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans # Scikit Learn (version : 0.23.2)
import seaborn as sns # Seaborn (version : 0.11.1)
from streamlit_webrtc import webrtc_streamer

df = pd.read_csv('result_rfm_3cluster.xlsx')
rfm_features = ['Recency', 'Frequency', 'Monetary']  # Replace with actual column names
df_rfm = df[rfm_features]

kms = KMeans(n_clusters=3, init='k-means++', random_state=42)
kms.fit(df_rfm)

st.title(''' CLUSTERING PELANGGAN PLATFORM SRIBU DENGAN MENGGUNAKAN METODE KOMBINASI ANTARA RFM (RECENCY,FREQUENCY,MONETARY) DAN ALGORITMA K-MEANS ''')
st.write('Prediksi Data Baru')

input_recency = st.number_input ("Recency (≥ 0)", )
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_frequency = st.number_input ("Frequency", )
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_monetary = st.number_input ("Monetary")

result = "-"

# Predict button
if st.button("Predict"):
    if input_recency > 0 and input_frequency > 0 and input_monetary > 0:
        # Prepare input data
        new_data = np.array([[input_recency, input_frequency, input_monetary]])
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(new_data)
        
        # Predict cluster
        prediction = kms.predict(scaled_data)[0]
        
        # Display result
        st.subheader(f"Cluster: {prediction}")
        if prediction == 0:
            st.write("""
            **Cluster 0: One-Time Buyers**  
            Pelanggan yang termasuk pada cluster ini adalah pelanggan yang bertipe One-Time Buyers,dimana Cluster tersebut merupakan dimana Pelanggan memiliki Recency sekian-Frequency Sekian-Monetary Sekian,sehingga pelanggan yang berada di Cluster ini bisa terbentuk karena banyak faktor,apakah mereka merupakan pelanggan baru,dimana mereka masih mencoba - coba membeli jasa-jasa freelancer yang telah disediakan oleh Sribu untuk pertama kalinya,apakah mereka merupakan pelanggan yang hanya membutuhkan jasa freelancer hanya di hari mereka order saja,sehingga hanya menggunakan jasa freelancer ketika dia membutuhkan saja. 
            """)
        elif prediction == 1:
            st.write("""
            **Cluster 1: Potential Buyers**  
            Pelanggan yang termasuk pada cluster ini adalah pelanggan bertipe Potentials Buyers,dimana Cluster tersebut merupakan dimana Pelanggan memiliki Recency sekian-Frequency Sekian-Monetary Sekian,sehingga pelanggan yang berada di Cluster ini bisa terbentuk karena banyak faktor,mereka merupakan pelanggan yang memiliki frequency yang lumayan tinggi,dan history melakukan transaksi terbilang relatif singkat,dimana bisa disebakan karena Pelanggan yang berada di cluster ini terkadang membutuhkan jasa-jasa freelancer sehingga akhirnya ketika ia membutuhkan lebih memilih untuk membeli jasa-jasa freelancer yang telah disediakan oleh Sribu.
            """)
        elif prediction == 2:
            st.write("""
            **Cluster 2: Loyal Customers**  
            Pelanggan yang termasuk pada cluster ini adalah pelanggan bertipe Loyal Customers,dimana Cluster tersebut merupakan dimana Pelanggan memiliki Recency sekian-Frequency Sekian-Monetary Sekian,sehingga pelanggan yang berada di Cluster tersebut merupakan dimana Pelanggan melakukan sering sekali melakukan transaksi dengan kuantitas yang tergolong banyak dan memiliki nilai history transaksi yang rendah,dimana bisa disebakan karena Pelanggan yang berada di cluster ini sangat membutuhkan jasa-jasa freelancer sehingga akhirnya sering membeli jasa-jasa freelancer yang telah disediakan oleh Sribu.
            """)
    else:
        st.error("Silakan masukkan semua nilai dengan benar!")
