import pandas as pd
import plotly.graph_objects as go
#Grafico Sankey

datos = pd.read_excel("datos/datos_suspensiones_sankey_bd.xlsx",sheet_name="Sheet1_py",usecols="A:C",skiprows=0,nrows=35,header=0)
label = pd.read_excel("datos/datos_suspensiones_sankey_bd.xlsx",sheet_name="Sheet1_py",usecols="E",skiprows=0,nrows=35,header=0)

# Definir los nodos del gráfico
nodos = dict(
type = 'sankey',
node = dict(
pad = 20,
thickness = 20,
line = dict(
color = "black",
width = 0.5
),
label = label,
color = ["lightblue", "lightgreen", "orange", "pink", "lightgray","red"]
),
# Definir las conexiones entre los nodos
link = dict(
source = datos.iloc[:,0],
target = datos.iloc[:,1],
value = datos.iloc[:,2]
)
)

# Crear la figura del gráfico
fig = go.Figure(data=[nodos])
fig.update_layout(title_text="<b>Desglose motivos de suspensión</b><br>cirugías",
font_size=15,width=1200,height=800,margin=dict(t=210,l=90,b=20,r=30))