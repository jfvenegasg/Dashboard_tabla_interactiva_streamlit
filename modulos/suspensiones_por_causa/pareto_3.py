# Grafico de barras apiladas dias de estadia
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def grafico(datos):
    #datos = pd.read_excel("datos/datos_suspensiones_sankey_bd.xlsx",sheet_name="Sheet1",usecols="A:D",skiprows=0,nrows=35,header=0)
    
    datos = datos.groupby(['target']).sum()
    datos = datos.sort_values('value', ascending=False)   
    datos['Porcentaje Acumulado'] = 100*datos['value'].cumsum() / datos['value'].sum()

    # Creamos el objeto figura
    fig = go.Figure()

    # Agregamos las barras
    fig.add_trace(go.Bar(
    x=datos.index,
    y=datos.iloc[:,0],
    name="Valor",
    marker=dict(
    color="lightblue"  # Color de las barras
    )))
    
    # Agregamos la línea
    fig.add_trace(go.Scatter(
    x=datos.index,
    y=datos.iloc[:,1],yaxis="y2",mode='lines+markers',
    name="Porcentaje Acumulado"))

    fig.update_layout(
    xaxis=dict(title='target'),
    yaxis=dict(title='value', side='left'),
    yaxis2=dict(title='Porcentaje Acumulado', side='right', overlaying='y', showgrid=False, range=[0, 100]),height=900)

    return fig


