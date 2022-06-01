from dash import html, callback, Input, Output
from utils.stylesheet import SIDEBAR_STYLE, JUMBOTRON
import sidebars.gallery
import gallery.html_object_collection, gallery.mokesciai

content_children=html.P("Čia sukelti appsai, kuriuos lengva sukodint")

sidebar = html.Div(children=sidebars.gallery.sections, id="gallery-sidebar", style=SIDEBAR_STYLE)
content = html.Div(children=content_children, id="gallery-content")


@callback(Output('gallery-sidebar', 'children'),
          Output('gallery-content', 'children'),
          [Input('page-url', 'pathname')],
          prevent_initial_call=False)
def display_content(pathname):
    path = pathname.strip('/').split('/')
    if path[:2] == ["gallery"]: return sidebar, content
    elif path[:2] == ["gallery", "html_object_collection"]: return sidebar, gallery.html_object_collection.content
    elif path[:2] == ["gallery", "mokesciai"]: return sidebar, gallery.mokesciai.content
    else: return sidebar, JUMBOTRON(pathname)

