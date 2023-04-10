import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px



datos = pd.read_excel("datos/datos_supensiones_por_especialidad.xlsx",sheet_name="Hoja1",usecols="M:O",skiprows=0,nrows=72,header=0,names=["Tipo","Especialidad","Cantidad"])

fig=px.bar(data_frame=datos,y="Especialidad",x="Cantidad",color="Tipo",barmode='stack',orientation="h",height=500)
