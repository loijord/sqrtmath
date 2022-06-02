import dash_bootstrap_components as dbc
from dash import html

left_jumbotron = dbc.Col(
    html.Div(
        [
            html.H2("404: Rojus nerastas", className="display-3"),
            html.Hr(className="my-2"),
            html.P(f"The pathname /gallery/jumbotron was not recognised..."),
            dbc.Button("Example Button", color="light", outline=True),
        ],
        className="h-100 p-5 text-white bg-dark rounded-3",
    ),
    md=6,
)

right_jumbotron = dbc.Col(
    html.Div(
        [
            html.H2("404: Rojus nerastas", className="display-3"),
            html.Hr(className="my-2"),
            html.P(f"The pathname /gallery/jumbotron was not recognised..."),
            dbc.Button("Example Button", color="secondary", outline=True),
        ],
        className="h-100 p-5 bg-light border rounded-3",
    ),
    md=6,
)

content = dbc.Row([left_jumbotron, right_jumbotron], className="align-items-md-stretch")
