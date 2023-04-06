import pandas as pd
import streamlit as st
import streamlit_echarts as ste
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from streamlit_option_menu import option_menu
import streamlit_nested_layout as stn
import plotly.express as px
from streamlit_elements import elements, mui, html
import hydralit_components as hc

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
    
    datos = pd.read_excel("datos/set_de_datos_1.xlsx",sheet_name="Horas",usecols="E:G",skiprows=14,nrows=22,header=0,names=["Mes","Tipo de Hora","Valor"])
    

    fig = px.bar(
    datos,
    x="Mes",
    y="Valor",
    height=700,
    orientation="v")
    fig.update_layout(title="Utilización de quirofanos")
    
    col_report_1,col_report_2=st.columns([4,2],gap="small")  
    
    with col_report_1:
       
        #ste.st_echarts(key=1,options=option, height="400px")
        st.plotly_chart(fig, use_container_width=True)

 
             
    with col_report_2:
        st.metric(label="Promedio porcentaje de ocupación de quirófanos",value="60%",label_visibility="visible")  
        st.metric(label="Horas programadas respecto a las habilidades",value="79%")  
        st.metric(label="Horas ocupadas respecto a las programadas",value="80%")  

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
               
elif selected =="Suspensiones por Especialidad":
    col1, col2, col3 = st.columns(3)


elif selected =="Hospitalización domiciliaria":
    
    

    datos = pd.read_excel("datos/datos_hospitalizacion_domiciliaria.xlsx",sheet_name="Sheet1",usecols="A:C",skiprows=0,nrows=12,header=0)
    

    fig = px.bar(
    datos,
    x="Componentes",
    y=["Número cupos programados","Número cupos utilizados"],
    height=700,
    orientation="v",
    barmode="group")
    fig.update_layout(title="Hospitalización domiciliaria")
    
    col_report_1,col_report_2=st.columns([4,2],gap="small")  
    
    with col_report_1:
       
        #ste.st_echarts(key=1,options=option, height="400px")
        st.plotly_chart(fig, use_container_width=True)

 
             
    with col_report_2:
        st.metric(label="Promedio porcentaje de ocupación de quirófanos",value="60%",label_visibility="visible")  
        st.metric(label="Horas programadas respecto a las habilidades",value="79%")  
        st.metric(label="Horas ocupadas respecto a las programadas",value="80%")  

elif selected =="Días de estadia":

    with st.empty():

        datos_1 = pd.read_excel("datos/datos_dias_estada.xlsx",sheet_name="Hoja1",usecols="A,B,C,D,I",skiprows=0,nrows=168,header=0)
                
        col_report_1,col_report_2=st.columns([4,2],gap="small")  
            
        with col_report_2:
            selector_1=st.selectbox("Selección de especialidad",("CIRUGÍA GENERAL",
                                                    "CIRUGÍA CARDIOVASCULAR",
                                                    "CIRUGÍA MÁXILOFACIAL",
                                                    "CIRUGÍA TÓRAX",
                                                    "TRAUMATOLOGÍA",
                                                    "NEUROCIRUGÍA",
                                                    "OTORRINOLARINGOLOGÍA",
                                                    "OFTALMOLOGÍA","OBSTETRICIA Y GINECOLOGÍA","GINECOLOGÍA",
                                                    "UROLOGÍA","RESTO ESPECIALIDADES","TODAS"))

                
            st.metric(label="Promedio porcentaje de ocupación de quirófanos",value="60%",label_visibility="visible")  
            st.metric(label="Horas programadas respecto a las habilidades",value="79%")  
            st.metric(label="Horas ocupadas respecto a las programadas",value="80%")
        
        with col_report_1:
            datos_1 = datos_1[(datos_1['Especialidad']==selector_1)]         

            fig_1 = px.bar(
            datos_1,
            x="Mes",
            y=["Dias de estada prequirurgicos totales","Pacientes intervenidos totales,"],
            height=700,
            orientation="v",
            barmode="group")
            fig_1.update_layout(title="Días de estadia y pacientes intervenidos por mes")         

            st.plotly_chart(fig_1, use_container_width=True)
            
            
    with st.empty():

        
        datos_2 = pd.read_excel("datos/datos_dias_estada.xlsx",sheet_name="Hoja1",usecols="A,B,C,D,I",skiprows=0,nrows=168,header=0)

        col_report_1,col_report_2=st.columns([4,2],gap="small")  
            
        with col_report_2:
            
            selector_2=st.selectbox("Selección de mes",("enero","febrero","marzo",
                                                    "abril","mayo","junio","julio",
                                                    "agosto","septiembre","octubre",
                                                    "noviembre","diciembre"))
                
            st.metric(label="Promedio porcentaje de ocupación de quirófanos",value="60%",label_visibility="visible")  
            st.metric(label="Horas programadas respecto a las habilidades",value="79%")  
            st.metric(label="Horas ocupadas respecto a las programadas",value="80%")
            
               
            
    with col_report_1:
        

        datos_2 = datos_2[(datos_2['Mes']==selector_2)]

        fig_2 = px.bar(
        datos_2,
        x="Especialidad",
        y=["Dias de estada prequirurgicos totales","Pacientes intervenidos totales,"],
        height=700,
        orientation="v",
        barmode="group")
        fig_2.update_layout(title="Días de estadia y pacientes intervenidos por mes")

       
        st.plotly_chart(fig_2, use_container_width=True)
            

else:
    col1, col2, col3 = st.columns(3)
