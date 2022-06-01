from utils.dry import nav
from dash import html

sections = [html.H2("App Gallery"), html.Hr(),
           nav({"🏠 Home": "/",
                "HTML collection": "/gallery/html_object_collection",
                "Mokesčiai": "/gallery/mokesciai"})]