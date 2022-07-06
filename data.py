import streamlit as st
import plotly_express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Visualizacion de la Data")

st.sidebar.subheader("Configuración de visualización")

uploaded_file = st.sidebar.file_uploader(label="Sube tu archivo CSV o Excel.",
                        type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("Hello")
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

try:
    st.write(df)
    st.subheader("Visualización")
    st.bar_chart(df)

    #get correlations mapa de calor
    st.header('Correlaciones')
    corrmat = df.corr()
    top_corr_features = corrmat.index
    fig_corr = plt.figure(figsize=(20,20))
    #plot heat map
    g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")
    st.write(corrmat)
    st.header('Mapa de calor')
    st.pyplot(fig_corr)
    

except Exception as e:
    print(e)
    st.write("Por favor sube tu archivo")

    