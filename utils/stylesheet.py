from dash import html
import dash_bootstrap_components as dbc

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

# the styles for the main content position it to the right of the sidebar and add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# sidebar itself
def SIDEBAR(header, links):
    sidebar = html.Div(
        [
            html.H2(header), #className="display-4"
            html.Hr(),
            dbc.Nav(
                [dbc.NavLink(key, href=val, active="exact") for key, val in links.items()],
                vertical=True,
                pills=True,)],
        style=SIDEBAR_STYLE,
    )
    return sidebar