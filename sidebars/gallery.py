from utils.utils import nav
from dash import html

sections = [html.H2("App Gallery"), html.Hr(),
           nav({"🏠 Home": "/",
                "HTML collection": "/gallery/html_object_collection",
                "Mokesčiai": "/gallery/mokesciai",
                "Jumbotron": "/gallery/jumbotron",
                "Sidebar": "/gallery/sidebar",
                "Interaktyvūs grafai": "/gallery/interactive_graphs",
                "Hierarchinės lentelės": "/gallery/multiindex_table"})]