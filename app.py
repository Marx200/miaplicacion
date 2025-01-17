import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Mi Aplicación Python")
st.sidebar.title("Parámetros")

st.image("Imagen2.png",width=1200)
st.sidebar.image("Imagen1.jfif")

modulo = st.sidebar.selectbox("Seleccione un Modulo",["Modulo 1","Modulo 2","Modulo 3"])

if modulo=="Modulo 1":
    st.write("Usted esta en el Modulo 1")
    ge=st.number_input("Ingrese al Gravedad Especifica",min_value=0.1,max_value=1.0,value=0.85)
    api=(141.5/ge)-131.5
    st.write(api)

elif modulo=="Modulo 2":
    st.write("Usted esta en el Modulo 2")
    df = pd.read_csv("Resultados.csv")
    st.write (df)
    fig=px.line(df,x="GE",y="API")
    st.write (fig)

else: 
    st.write("Usted esta en el Modulo 3")
    uploader_file = st.file_uploader("Sube to archivo csv o excel",type=["csv","xlsx","xls"])
    if uploader_file is not None:
        st.write("Archivo Cargado Exitosamente")
        if uploader_file.name.endswith(".csv"):
            df=pd.read_csv(uploader_file)
        elif uploader_file.name.endswith(".xlsx"):
            df=pd.read_excel(uploader_file)
        else:
            df=pd.read_excel(uploader_file)
        st.write(df)
    else:
        st.write("Cargue el archivo")
