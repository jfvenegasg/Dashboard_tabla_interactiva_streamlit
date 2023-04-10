# Grafico de barras apiladas
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

datos = pd.read_excel("datos/datos_suspensiones_bd.xlsx",sheet_name="Sheet1",usecols="A:D",skiprows=0,nrows=146,header=0)
datos=datos[(datos['Descripcion']=='% de total Suspensiones totales junto con Causas De Suspensión Atribuibles A:')]
fig=px.bar(data_frame=datos,x="Mes",y="Valor",color="Causa.de.suspension",barmode='stack')