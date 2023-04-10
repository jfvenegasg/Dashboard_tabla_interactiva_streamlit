import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px



datos = pd.read_excel("datos/datos_supensiones_por_especialidad.xlsx",sheet_name="Hoja1",usecols="M:O",skiprows=0,nrows=72,header=0)
datos = datos.groupby(['Tipo']).sum()

labels = datos.index
values = datos.iloc[:,0]

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
   
