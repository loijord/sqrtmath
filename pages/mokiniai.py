from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from utils.stylesheet import SIDEBAR, CONTENT_STYLE, SIDEBAR_STYLE
#import pages.ieva, pages.mantas_ir_ugne

#sidebar = SIDEBAR('Mokiniai', {"Ieva": "/mokiniai/ieva", "Mantas ir Ugnė": "/mokiniai/mantas_ir_ugne"})

sidebar = html.Div(
    [
        html.H2("Mokiniai", className="display-4"),
        html.Hr(),
        #html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav([dbc.NavLink("About", href="/mokiniai", active="exact"),
                dbc.NavLink("Ieva", href="/ieva", active="exact"),
                dbc.NavLink("Mantas ir Ugnė", href="/mantas_ir_ugne", active="exact")],
            vertical=True, pills=True,)],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="mokiniai-content")
layout = html.Div([dcc.Location(id="mokiniai-url"), sidebar, content])


'''
@callback(Output('mokiniai-dropdown', 'value'),
          [Input('mokiniai-url', 'n_clicks')],
          [State('mokiniai-dropdown', 'value')])
def drop_down(n_clicks, input1):
    if (n_clicks) >=1 :
        return(input1)
'''

@callback(Output('mokiniai-content', 'children'), Input('mokiniai-url', 'pathname'))
def display_content(pathname):
    front_layout = html.P("sqrtmath - vieta, kur mokosi, kas tik tik nori")
    if pathname == "/mokiniai":
        return front_layout
    elif pathname == "/ieva":
        ieva = html.P("sqrtmath - vieta, kur mokosi ieva")
        print(ieva)
        return ieva
    elif pathname == "/mantas_ir_ugne":
        mantas = html.P("sqrtmath - vieta, kur mokosi mantas")
        print(mantas)
        return mantas
        #return pages.mantas_ir_ugne.layout

