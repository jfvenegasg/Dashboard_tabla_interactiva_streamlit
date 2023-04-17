import hydralit_components  

def home():
    hydralit.set_block_container_style()
    hydralit.title("Página de inicio")
    hydralit.caption("Bienvenido a mi aplicación web")

def about():
    hydralit.set_block_container_style()
    hydralit.title("Acerca de")
    hydralit.caption("Esta aplicación web fue desarrollada por mí")

menu_items = {"Inicio": home, "Acerca de": about}

app = hydralit.Hydralit()

with app:
    hydralit.components.Menu(menu_items)