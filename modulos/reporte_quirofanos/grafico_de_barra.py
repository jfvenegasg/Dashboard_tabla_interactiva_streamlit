# Grafico de barras
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

datos = pd.read_excel("datos/set_de_datos_1.xlsx",sheet_name="Horas",usecols="E:G",skiprows=14,nrows=22,header=0,names=["Mes","Tipo de Hora","Valor"])
    

fig = px.bar(
datos,
x="Mes",
y="Valor",
height=700,
orientation="v")
fig.update_layout(title="Utilización de quirofanos")