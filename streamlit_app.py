import pandas as pd
import streamlit as st
import streamlit_echarts as ste
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from streamlit_option_menu import option_menu
import streamlit_nested_layout as stn
import plotly.express as px
from streamlit_elements import elements, mui, html

st.set_page_config(layout = "wide")
# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Sistema de gestión HCM", ["Inicio","Reporte quirófanos", "Suspensiones por causa","Suspensiones por especialidad","Hospitalización domiciliaria","Días de estadia"], 
        icons=['house', 'person-rolodex','person-badge-fill','person-badge-fill','file-earmark-medical','file-earmark-medical'], menu_icon="cast", default_index=0)
    selected

if selected == "Inicio":
     
 
    
        #st.set_page_config(
        #    layout="centered", page_icon="🖱️", page_title="Interactive table app"   
        #)
    c=st.empty()
        
    col_inicio_1,col_inicio_2=st.columns(2,gap="small")
        
    c.image("hcm.png")
    with col_inicio_1:
            st.button(label="Reporte quirofanos")
            st.button(label="Suspensiones por causa")
            st.button(label="Suspensiones por especialidad")
    with col_inicio_2:
            st.button(label="Hospitalización domiciliaria")
            st.button(label="Dias de estadia")
    
elif selected =="Reporte quirófanos":
    option = {
            "xAxis": {
                "type": "category",
                "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            },
            "yAxis": {"type": "value"},
            "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320],
                        "type": "line"}],
             "title": ["titulo"]}
    iris = pd.read_excel("datos_suspensiones_sankey_bd.xlsx")
    
    fig = px.bar(
    iris,
    y="target",
    x="value",
    height=700,
    orientation="h")
    fig.update_layout(title="GDP per Capita vs. Life Expectancy")
    
    col_report_1,col_report_2=st.columns([4,1],gap="small")  
    
    with col_report_1:
       
        #ste.st_echarts(key=1,options=option, height="400px")
        st.plotly_chart(fig, use_container_width=True)

 
             
    with col_report_2:
        st.write("tarjeta 1")   
        st.write("tarjeta 2")
        st.write("tarjeta 3")
elif selected =="Suspensiones por causa":
    col1,col2=st.columns(2,gap="small")    
    with col1:

        STREAMLIT_AGGRID_URL = "https://github.com/PablocFonseca/streamlit-aggrid"
        st.title("🖱️ Columna 1")
        st.write(
            """ Esta app muestra como puedes usar el componente [streamlit-aggrid](STREAMLIT_AGGRID_URL)
            de Streamlit de forma interactiva de acuerdo a lo que el usuario seleccione."""
        )

        option = {
            "xAxis": {
                "type": "category",
                "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            },
            "yAxis": {"type": "value"},
            "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
        }
        ste.st_echarts(key=2,
            options=option, height="400px")

        st.write("Prueba y haz click sobre cualquier fila de la tabla")


        def aggrid_interactive_table(df: pd.DataFrame):
            """Creates an st-aggrid interactive table based on a dataframe.

            Args:
                df (pd.DataFrame]): Source dataframe

            Returns:
                dict: The selected row
            """
            options = GridOptionsBuilder.from_dataframe(
                df, enableRowGroup=True, enableValue=True, enablePivot=True
            )

            options.configure_side_bar()

            options.configure_selection("single")
            selection = AgGrid(
                df,
                enable_enterprise_modules=True,
                gridOptions=options.build(),
                theme="alpine",
                update_mode=GridUpdateMode.MODEL_CHANGED,
                allow_unsafe_jscode=True,
            )

            return selection


        iris = pd.read_excel("datos_suspensiones_sankey_bd.xlsx")

        selection = aggrid_interactive_table(df=iris)

        if selection:
            st.write("Has seleccionado la siguiente seccion:")
            st.json(selection["selected_rows"])

        st.write("## Code")

    with col2:

        STREAMLIT_AGGRID_URL = "https://github.com/PablocFonseca/streamlit-aggrid"
        #st.set_page_config(
        #    layout="centered", page_icon="🖱️", page_title="Interactive table app"   
        #)
        st.title("🖱️ Columna 2")
        st.write(
            """ Esta app muestra como puedes usar el componente [streamlit-aggrid](STREAMLIT_AGGRID_URL)
            de Streamlit de forma interactiva de acuerdo a lo que el usuario seleccione."""
        )

        option = {
            "xAxis": {
                "type": "category",
                "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            },
            "yAxis": {"type": "value"},
            "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
        }
        ste.st_echarts(key=3,
            options=option, height="400px")
        
else:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")       