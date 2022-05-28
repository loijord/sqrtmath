"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
from utils.dry import cut

import pages.home
import pages.savokos
import pages.taisykles
import pages.uzdaviniai
import pages.sprendimai
import pages.atvejai
import pages.kursas
import pages.mokiniai
import pages.mokesciai

from utils.stylesheet import SIDEBAR_STYLE, CONTENT_STYLE

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True)
sidebar = html.Div(
    [
        #html.H2("Sidebar", className="display-4"),
        dcc.Markdown(r'$\Huge \sqrt{MATH}$', mathjax=True),
        html.Hr(),
        #html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav([dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Sąvokos", href="/savokos", active="exact"),
                dbc.NavLink("Taisyklės", href="/taisykles", active="exact"),
                dbc.NavLink("Uždaviniai", href="/uzdaviniai", active="exact"),
                dbc.NavLink("Sprendimai", href="/sprendimai", active="exact"),
                dbc.NavLink("Atvejai", href="/atvejai", active="exact"),
                dbc.NavLink("Kursas", href="/kursas", active="exact"),
                dbc.NavLink("Mokiniai", href="/mokiniai", active="exact"),
                dbc.NavLink("Mokesčiai", href="/mokesciai", active="exact")],
            vertical=True, pills=True,)],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    front_layout = html.P("The sqrt command produces the square root (radical) symbol")
    if pathname == "/": return front_layout
    elif pathname == "/savokos": return pages.savokos.create_view()
    elif pathname == "/taisykles": return pages.taisykles.create_view()
    elif pathname == "/uzdaviniai": return pages.uzdaviniai.create_view()
    elif pathname == "/sprendimai": return pages.sprendimai.create_view()
    elif pathname == "/atvejai": return pages.atvejai.create_view()
    elif pathname == "/kursas": return pages.kursas.create_view()
    elif pathname == '/mokiniai':
        return pages.mokiniai.layout
    elif pathname == '/mokesciai':
        return pages.mokesciai.layout

    # If the user tries to reach a different page, return a 404 message
    """
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
    """

server = app.server
#if __name__ == '__main__': app.run_server(debug=True, port = 8870)

