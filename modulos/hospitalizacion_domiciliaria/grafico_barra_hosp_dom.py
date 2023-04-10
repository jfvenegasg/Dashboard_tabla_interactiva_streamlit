# Grafico de barras hospitalizacion domiciliaria
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

datos = pd.read_excel("datos/datos_hospitalizacion_domiciliaria.xlsx",sheet_name="Sheet1",usecols="A:C",skiprows=0,nrows=12,header=0)
    

fig = px.bar(
datos,
x="Componentes",
y=["Número cupos programados","Número cupos utilizados"],
height=700,
orientation="v",
barmode="group")
fig.update_layout(title="Hospitalización domiciliaria")