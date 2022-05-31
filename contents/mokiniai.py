from dash import html, callback, Input, Output
from utils.stylesheet import SIDEBAR_STYLE, JUMBOTRON
import sidebars.mokiniai
import contents.ugne_ir_mantas, contents.ieva

content_children=html.P("sqrtmath - vieta, kur mokosi, kas tik nori")

sidebar = html.Div(children=sidebars.mokiniai.sections, id="mokiniai-sidebar", style=SIDEBAR_STYLE)
content = html.Div(children=content_children, id="mokiniai-content")


@callback(Output('mokiniai-sidebar', 'children'),
          Output('mokiniai-content', 'children'),
          [Input('page-url', 'pathname')],
          prevent_initial_call=False)
def display_content(pathname):
    path = pathname.strip('/').split('/')
    if path[:2] == ["mokiniai"]: return sidebar, content
    elif path[:2] == ["mokiniai", "ieva"]: return sidebar, contents.ieva.content
    elif path[:2] == ["mokiniai", "ugne_ir_mantas"]: return sidebar, contents.ugne_ir_mantas.content
    else: return sidebar, JUMBOTRON(pathname)

