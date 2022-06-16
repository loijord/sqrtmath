import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback

import contents.home
import contents.mokiniai
import contents.roadmap
import contents.app_gallery

import sidebars.home
from utils.stylesheet import SIDEBAR_STYLE, CONTENT_STYLE, JUMBOTRON

app = dash.Dash(external_stylesheets=[
    dbc.themes.BOOTSTRAP,
    r'''https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'''], #5 star ranking system
    suppress_callback_exceptions=True)
location = dcc.Location(id="page-url", refresh=False)
sidebar = html.Div(sidebars.home.sections, id="page-sidebar", className='sidebar')
content = html.Div(id="page-content", className='content')
app.layout = html.Div([location, sidebar, content])

@callback(Output("page-sidebar", "children"),
          Output("page-content", "children"),
          [Input("page-url", "pathname")],
          prevent_initial_call=True)
def render_page_content(pathname):
    path = pathname.strip('/').split('/')
    if path[:1] == [""]: return sidebar, contents.home.content
    elif path[:1] == ["mokiniai"]: return contents.mokiniai.sidebar, contents.mokiniai.content
    elif path[:1] == ["roadmap"]: return contents.roadmap.sidebar, contents.roadmap.content
    elif path[:1] == ["gallery"]: return contents.app_gallery.sidebar, contents.app_gallery.content
    else: return sidebar, JUMBOTRON(pathname)

server = app.server
#if __name__ == '__main__': app.run_server(debug=True, port = 8870)

