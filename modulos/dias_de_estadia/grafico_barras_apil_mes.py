# Grafico de barras apiladas dias de estadia
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def grafico(datos):
    fig_1 = px.bar(
    datos,
    x="Mes",
    y=["Dias de estada prequirurgicos totales","Pacientes intervenidos totales,"],
    height=700,
    orientation="v",
    barmode="group")
    fig_1.update_layout(title="Días de estadia y pacientes intervenidos por mes")   

    return fig_1