import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv('data_will_cluster.csv')

# Define features for clustering
rfm_features = ['Recency', 'Frequency', 'Monetary',
                'category_Desain Grafis & Branding', 'category_Gaya Hidup',
                'category_Konsultasi', 'category_Pemasaran & Periklanan',
                'category_Penulisan & Penerjemahan', 'category_Unknown',
                'category_Video, Fotografi & Audio', 'category_Web & Pemrograman']

df_rfm = df[rfm_features]

# Fit KMeans model
kms = KMeans(n_clusters=4, init='k-means++', random_state=42)
kms.fit(df_rfm)

# Streamlit App
st.title("CLUSTERING PELANGGAN PLATFORM SRIBU")
st.write("Prediksi Data Baru")

# Input fields
input_recency = st.number_input("Recency", step=1, format='%d')
input_frequency = st.number_input("Frequency", step=1, format='%d')
input_monetary = st.number_input("Monetary", step=1, format='%d')

# Multiselect for categories
categories = [
    'category_Desain Grafis & Branding', 'category_Gaya Hidup',
    'category_Konsultasi', 'category_Pemasaran & Periklanan',
    'category_Penulisan & Penerjemahan', 'category_Unknown',
    'category_Video, Fotografi & Audio', 'category_Web & Pemrograman'
]

selected_categories = st.multiselect("Pilih kategori yang pernah diorder:", categories)

# Prepare category inputs as one-hot encoding
category_input = [1 if category in selected_categories else 0 for category in categories]

result = "-"

# Predict button
if st.button("Predict"):
    if input_recency > 0 and input_frequency > 0 and input_monetary > 0:
        # Prepare input data
        new_data = np.array([[input_recency, input_frequency, input_monetary] + category_input])
        
        # Predict cluster
        prediction = kms.predict(new_data)[0]
        
        # Display result
        st.subheader(f"Cluster: {prediction}")
        if prediction == 0:
            st.write(f"""
            **Cluster 0: One-Time Buyers**  
            - Recency: {input_recency}
            - Frequency: {input_frequency}
            - Monetary: {input_monetary}
            - Categories: {', '.join(selected_categories) if selected_categories else 'None'}
            
            Pelanggan yang termasuk pada cluster ini adalah pelanggan bertipe One-Time Buyers...
            """)
        elif prediction == 1:
            st.write(f"""
            **Cluster 1: Potential Buyers**  
            - Recency: {input_recency}
            - Frequency: {input_frequency}
            - Monetary: {input_monetary}
            - Categories: {', '.join(selected_categories) if selected_categories else 'None'}
            
            Pelanggan yang termasuk pada cluster ini adalah pelanggan bertipe Potential Buyers...
            """)
        elif prediction == 2:
            st.write(f"""
            **Cluster 2: Loyal Customers**  
            - Recency: {input_recency}
            - Frequency: {input_frequency}
            - Monetary: {input_monetary}
            - Categories: {', '.join(selected_categories) if selected_categories else 'None'}
            
            Pelanggan yang termasuk pada cluster ini adalah pelanggan bertipe Loyal Customers...
            """)
        elif prediction == 3:
            st.write(f"""
            **Cluster 3: High-Value Customers**  
            - Recency: {input_recency}
            - Frequency: {input_frequency}
            - Monetary: {input_monetary}
            - Categories: {', '.join(selected_categories) if selected_categories else 'None'}
            
            Pelanggan yang termasuk pada cluster ini adalah pelanggan bertipe High-Value Customers...
            """)
    else:
        st.error("Silakan masukkan semua nilai dengan benar!")
