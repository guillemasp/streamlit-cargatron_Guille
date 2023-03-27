import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="My streamlit project",
    page_icon="🧊",
    layout="wide")

option = st.sidebar.selectbox(
    'Selecciona la vista: ',
    ('Home', 'Visualizaciones', 'Mapa'),
    index=0)

st.sidebar.write(option)

uploaded_file = st.sidebar.file_uploader("Elige un csv", type=["csv"])
if uploaded_file is not None:
    datos = pd.read_csv(uploaded_file)

datos = pd.read_csv("data/red_recarga_acceso_publico_2021.csv", sep=";")

if option == "Home":

    st.title('My App Home')


    with st.expander("Detalles de la aplicación- Haz clic para expandir"):
        st.write("""
        Esto es una apliación bla.
        1º Hola.
        2º Adiós.
        3º Idiota.
        """)
    st.image('https://pbs.twimg.com/media/FTh_sKmWUAI5ws6?format=jpg&name=4096x4096', width = 500,
            caption="Mestalla en el partido de leyendas")


    with st.echo():
        st.write(datos)

    with st.echo():
        #Código para generar números pares
        lista = list(range(10))
        even_list = [x for x in lista if x%2 == 0]
        st.write()

    st.balloons()


elif option == "Mapa":
    datos_pal_mapa = datos[["latidtud", "longitud"]]
    datos_pal_mapa.columns = ["lat", "lon"]
    st.subheader("Mapa de cargadores")
    st.map(datos_pal_mapa)

elif option == "Visualizaciones":
    datos_pal_barchar= datos.groupby("DISTRITO")[["Nº CARGADORES"]].sum().reset_index()
    st.subheader("Numero de cargadores por distrito")
    st.bar_chart(datos, x = "DISTRITO", y = "Nº CARGADORES")
