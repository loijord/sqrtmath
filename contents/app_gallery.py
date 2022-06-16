from dash import html, callback, Input, Output, dcc
from utils.stylesheet import SIDEBAR_STYLE, JUMBOTRON
from utils.utils import nice_app_display
import sidebars.gallery
import gallery.html_object_collection, gallery.mokesciai, gallery.jumbotron, \
    gallery.sidebar, gallery.interactive_graphs, gallery.multiindex_table


content_children = dcc.Markdown("""Ši sekcija skirta pademonstruoti, kokius appsus galima sukurti naudojant
 [`Dash`](https://dash.plotly.com/) biblioteką. Kiekvienoje skiltyje rasite veikiantį appsą, o apačioje - jo source kodą""")

sidebar = html.Div(children=sidebars.gallery.sections, id="gallery-sidebar", style=SIDEBAR_STYLE)
content = html.Div(children=content_children, id="gallery-content")


@callback(Output('gallery-sidebar', 'children'),
          Output('gallery-content', 'children'),
          [Input('page-url', 'pathname')],
          prevent_initial_call=False)
def display_content(pathname):
    path = pathname.strip('/').split('/')
    if path[:2] == ["gallery"]: return sidebar, content
    elif path[:2] == ["gallery", "html_object_collection"]: return sidebar, nice_app_display(gallery.html_object_collection)
    elif path[:2] == ["gallery", "mokesciai"]: return sidebar, nice_app_display(gallery.mokesciai)
    elif path[:2] == ["gallery", "jumbotron"]: return sidebar, nice_app_display(gallery.jumbotron)
    elif path[:2] == ["gallery", "sidebar"]: return sidebar, nice_app_display(gallery.sidebar)
    elif path[:2] == ["gallery", "interactive_graphs"]: return sidebar, nice_app_display(gallery.interactive_graphs)
    elif path[:2] == ["gallery", "multiindex_table"]: return sidebar, nice_app_display(gallery.multiindex_table)
    else: return sidebar, JUMBOTRON(pathname)

