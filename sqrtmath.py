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
from dash import Input, Output, dcc, html
import subpages.savokos
import subpages.taisykles
import subpages.uzdaviniai
import subpages.sprendimai
import subpages.atvejai
import subpages.kursas

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Sąvokos", href="/savokos", active="exact"),
                dbc.NavLink("Taisyklės", href="/taisyklės", active="exact"),
                dbc.NavLink("Uždaviniai", href="/uzdaviniai", active="exact"),
                dbc.NavLink("Sprendimai", href="/sprendimai", active="exact"),
                dbc.NavLink("Atvejai", href="/atvejai", active="exact"),
                dbc.NavLink("Kursas", href="/kursas", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("Tai - pirmoji testinė puslapio, skirto studijuoti matematikai, versija!")
    elif pathname == "/savokos": return subpages.savokos.create_view()
    elif pathname == "/taisykles": return subpages.taisykles.create_view()
    elif pathname == "/uzdaviniai": return subpages.uzdaviniai.create_view()
    elif pathname == "/sprendimai": return subpages.sprendimai.create_view()
    elif pathname == "/atvejai": return subpages.atvejai.create_view()
    elif pathname == "/kursas": return subpages.kursas.create_view()
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

