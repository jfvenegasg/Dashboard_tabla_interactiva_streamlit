# Grafico de barras apiladas dias de estadia
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def grafico(datos):
    datos = pd.read_excel("datos/datos_suspensiones_bd.xlsx",sheet_name="Sheet1",usecols="A:D",skiprows=0,nrows=145,header=0)
    
    
    datos = datos[(datos['Descripcion']=="% de total 15 Años Y Más junto con Causas De Suspensión Atribuibles A:")]
    datos["Valor Anual"] = datos["Valor"]/12
    datos = datos.groupby(['Causa.de.suspension']).sum()
    datos = datos.sort_values('Valor Anual', ascending=False)   
    datos['Porcentaje Acumulado'] = 100 * datos['Valor Anual'].cumsum() / datos['Valor Anual'].sum()

    # Creamos el objeto figura
    fig = go.Figure()

    # Agregamos las barras
    fig.add_trace(go.Bar(
    x=datos.index,
    y=datos.iloc[:,1],
    name="Ventas",
    marker=dict(
    color="lightblue"  # Color de las barras
    )))
    
    # Agregamos la línea
    fig.add_trace(go.Scatter(
    x=datos.index,
    y=datos.iloc[:,2],yaxis="y2",mode='lines+markers',
    name="Porcentaje Acumulado"))

    fig.update_layout(
    xaxis=dict(title='Causa.de.suspension'),
    yaxis=dict(title='Valor anual', side='left'),
    yaxis2=dict(title='Porcentaje Acumulado', side='right', overlaying='y', showgrid=False, range=[0, 100]))

    
    return fig


