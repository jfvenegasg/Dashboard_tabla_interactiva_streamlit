import pandas as pd
import streamlit as st
#import streamlit_echarts as ste
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from streamlit_option_menu import option_menu
import streamlit_nested_layout as stn
import plotly.express as px
from streamlit_elements import elements, mui, html
import hydralit_components as hc
import plotly.graph_objects as go
import holoviews as hv
from plotly.subplots import make_subplots
import sys
sys.path.append("modulos/suspensiones_por_causa")
sys.path.append("modulos/suspensiones_por_especialidad")
sys.path.append("modulos/reporte_quirofanos")
sys.path.append("modulos/hospitalizacion_domiciliaria")
sys.path.append("modulos/dias_de_estadia")

import grafico_sankey, grafico_barras, grafico_de_barra, grafico_barra_hosp_dom, grafico_barras_apil_mes
import grafico_barras_apil_espe, pareto_1,pareto_2,pareto_3,circular_1,circular_2,grafico_barra

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
      
    col_report_1,col_report_2=st.columns([4,2],gap="small")  
    
    with col_report_1:
       
        #ste.st_echarts(key=1,options=option, height="400px")
        st.plotly_chart(grafico_de_barra.fig, use_container_width=True)

 
             
    with col_report_2:
        st.metric(label="Promedio porcentaje de ocupación de quirófanos",value="60%",label_visibility="visible")  
        st.metric(label="Horas programadas respecto a las habilidades",value="79%")  
        st.metric(label="Horas ocupadas respecto a las programadas",value="80%")  

elif selected =="Suspensiones por causa":

    with st.empty():
        col1,col2=st.columns([4,1],gap="small")    
        with col1:

                    
            st.write("Motivos de suspensión por mes")
                       
            
            st.plotly_chart(grafico_barras.fig, use_container_width=True)

        with col2:

            st.metric(label="Suspensiones debido a la causal paciente",value="42%",label_visibility="visible")  
            st.metric(label="Suspensiones debido a la causal equipo quirurgico",value="23%") 

    with st.empty():
        
        #Mostrar el gráfico
        st.plotly_chart(grafico_sankey.fig, use_container_width=True)

    with st.empty():

        col_1,col_2=st.columns([1,1])

        with col_1:
            datos = pd.read_excel("datos/datos_suspensiones_bd.xlsx",sheet_name="Sheet1",usecols="A:D",skiprows=0,nrows=146,header=0)
            
            

            # Mostramos la figura
            st.plotly_chart(pareto_1.grafico(datos), use_container_width=True)

        with col_2:

            datos = pd.read_excel("datos/datos_suspensiones_bd.xlsx",sheet_name="Sheet1",usecols="A:D",skiprows=0,nrows=146,header=0)

            

            # Mostramos la figura
            st.plotly_chart(pareto_2.grafico(datos), use_container_width=True)

    with st.empty():
            datos = pd.read_excel("datos/datos_suspensiones_sankey_bd.xlsx",sheet_name="Sheet1",usecols="A:D",skiprows=0,nrows=35,header=0)
    

            # Mostramos la figura
            st.plotly_chart(pareto_3.grafico(datos), use_container_width=True)

elif selected =="Suspensiones por especialidad":
    
    with st.empty():
        col_report_1,col_report_2=st.columns([1,1],gap="small")  
    
        with col_report_1:
            st.write("Motivos de suspensión por mes")
        
        
            st.plotly_chart(circular_1.fig, use_container_width=True)
        with col_report_2:
            st.write("Motivos de suspensión por mes")
        
        
            st.plotly_chart(circular_2.fig, use_container_width=True)
    with st.empty():
            st.plotly_chart(grafico_barra.fig, use_container_width=True)

elif selected =="Hospitalización domiciliaria":
          
    col_report_1,col_report_2=st.columns([4,2],gap="small")  
    
    with col_report_1:
       
        #ste.st_echarts(key=1,options=option, height="400px")
        st.plotly_chart(grafico_barra_hosp_dom.fig, use_container_width=True)
       
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

            dias_totales=sum(datos_1[(datos_1['Especialidad']==selector_1)].iloc[:,3])    
            pac_int_totales=sum(datos_1[(datos_1['Especialidad']==selector_1)].iloc[:,4])
            dias_prom_pac=round(sum(datos_1[(datos_1['Especialidad']==selector_1)].iloc[:,2])/len(datos_1[(datos_1['Especialidad']=="CIRUGÍA GENERAL")].iloc[:,2]),2)

            st.metric(label="Días totales de estadia",value=dias_totales,label_visibility="visible")  
            st.metric(label="Pacientes intervenidos totales",value=pac_int_totales)  
            st.metric(label="Días de estadía promedio por paciente",value=dias_prom_pac)
        
        with col_report_1:
            datos_1 = datos_1[(datos_1['Especialidad']==selector_1)]         
            
            st.plotly_chart(grafico_barras_apil_mes.grafico(datos_1), use_container_width=True)
            
            
    with st.empty():

        
        datos_2 = pd.read_excel("datos/datos_dias_estada.xlsx",sheet_name="Hoja1",usecols="A,B,C,D,I",skiprows=0,nrows=168,header=0)

        col_report_1,col_report_2=st.columns([4,2],gap="small")  
            
        with col_report_2:
            
            selector_2=st.selectbox("Selección de mes",("enero","febrero","marzo",
                                                    "abril","mayo","junio","julio",
                                                    "agosto","septiembre","octubre",
                                                    "noviembre","diciembre"))
                
            dias_totales=sum(datos_2[(datos_2['Mes']==selector_2)].iloc[:,3])    
            pac_int_totales=sum(datos_2[(datos_2['Mes']==selector_2)].iloc[:,4])
            dias_prom_pac=round(sum(datos_2[(datos_2['Mes']==selector_2)].iloc[:,2])/len(datos_2[(datos_2['Mes']==selector_2)].iloc[:,2]),2)

            st.metric(label="Días totales de estadia",value=dias_totales,label_visibility="visible")  
            st.metric(label="Pacientes intervenidos totales",value=pac_int_totales)  
            st.metric(label="Días de estadía promedio por paciente",value=dias_prom_pac)
            
               
            
    with col_report_1:
        

        datos_2 = datos_2[(datos_2['Mes']==selector_2)]

               
        st.plotly_chart(grafico_barras_apil_espe.grafico(datos_2),use_container_width=True)
            

else:
    col1, col2, col3 = st.columns(3)
