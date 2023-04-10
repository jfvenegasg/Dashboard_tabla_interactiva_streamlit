# Grafico de barras apiladas dias de estadia
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def grafico(datos):
    fig_2 = px.bar(
    datos,
    x="Especialidad",
    y=["Dias de estada prequirurgicos totales","Pacientes intervenidos totales,"],
    height=700,
    orientation="v",
    barmode="group")
    fig_2.update_layout(title="Días de estadia y pacientes intervenidos por mes")  

    return fig_2