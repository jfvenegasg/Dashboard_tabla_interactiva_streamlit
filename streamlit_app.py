import pandas as pd
import streamlit as st
import streamlit_echarts as ste
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from streamlit_option_menu import option_menu
import streamlit_nested_layout as stn
st.set_page_config(layout = "wide")
# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Inicio","Visualizacion", 'Configuracion'], 
        icons=['house', 'stack','gear'], menu_icon="cast", default_index=1)
    selected

if selected == "Inicio":
     
 
    col1,col2=st.columns(2,gap="small")
    
    with col1:

        STREAMLIT_AGGRID_URL = "https://github.com/PablocFonseca/streamlit-aggrid"
        #st.set_page_config(
        #    layout="centered", page_icon="🖱️", page_title="Interactive table app"   
        #)
        st.title("🖱️ Aplicacion de Tabla Interactiva")
        st.write(
            """ Esta app muestra como puedes usar el componente [streamlit-aggrid](STREAMLIT_AGGRID_URL)
            de Streamlit de forma interactiva de acuerdo a lo que el usuario seleccione."""
        )

        option = {
            "xAxis": {
                "type": "category",
                "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            },
            "yAxis": {"type": "value"},
            "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
        }
        ste.st_echarts(key=1,
            options=option, height="400px")

        st.write("Prueba y haz click sobre cualquier fila de la tabla")


        def aggrid_interactive_table(df: pd.DataFrame):
            """Creates an st-aggrid interactive table based on a dataframe.

            Args:
                df (pd.DataFrame]): Source dataframe

            Returns:
                dict: The selected row
            """
            options = GridOptionsBuilder.from_dataframe(
                df, enableRowGroup=True, enableValue=True, enablePivot=True
            )

            options.configure_side_bar()

            options.configure_selection("single")
            selection = AgGrid(
                df,
                enable_enterprise_modules=True,
                gridOptions=options.build(),
                theme="alpine",
                update_mode=GridUpdateMode.MODEL_CHANGED,
                allow_unsafe_jscode=True,
            )

            return selection


        iris = pd.read_excel("datos_suspensiones_sankey_bd.xlsx")

        selection = aggrid_interactive_table(df=iris)

        if selection:
            st.write("Has seleccionado la siguiente seccion:")
            st.json(selection["selected_rows"])

        st.write("## Code")

        st.code(
            '''
        import pandas as pd
        import streamlit as st
        from st_aggrid import AgGrid, GridOptionsBuilder
        from st_aggrid.shared import GridUpdateMode

        iris = pd.read_csv(
            "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
        )

        def aggrid_interactive_table(df: pd.DataFrame):
            """Creates an st-aggrid interactive table based on a dataframe.

            Args:
                df (pd.DataFrame]): Source dataframe

            Returns:
                dict: The selected row
            """
            options = GridOptionsBuilder.from_dataframe(
                df, enableRowGroup=True, enableValue=True, enablePivot=True
            )

            options.configure_side_bar()

            options.configure_selection("single")
            selection = AgGrid(
                df,
                enable_enterprise_modules=True,
                gridOptions=options.build(),
                theme="light",
                update_mode=GridUpdateMode.MODEL_CHANGED,
                allow_unsafe_jscode=True,
            )

            return selection


        iris = pd.read_csv(
            "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
        )

        selection = aggrid_interactive_table(df=iris)

        if selection:
            st.write("You selected:")
            st.json(selection["selected_rows"])
        ''',
            "python",
        )

    with col2:

        STREAMLIT_AGGRID_URL = "https://github.com/PablocFonseca/streamlit-aggrid"
        #st.set_page_config(
        #    layout="centered", page_icon="🖱️", page_title="Interactive table app"   
        #)
        st.title("🖱️ Aplicacion de Tabla Interactiva")
        st.write(
            """ Esta app muestra como puedes usar el componente [streamlit-aggrid](STREAMLIT_AGGRID_URL)
            de Streamlit de forma interactiva de acuerdo a lo que el usuario seleccione."""
        )

        option = {
            "xAxis": {
                "type": "category",
                "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            },
            "yAxis": {"type": "value"},
            "series": [{"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}],
        }
        ste.st_echarts(key=2,
            options=option, height="400px")
        
else:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")       