import streamlit as st
import plotly_express as px
import pandas as pd



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
    st.subheader("Visuazlizacion")
    st.bar_chart(df)
except Exception as e:
    print(e)
    st.write("Por favor sube tu archivo")

    