from dash import html, dcc
import dash_bootstrap_components as dbc
import json

def nav(links):
    return dbc.Nav([dbc.NavLink(key, href=val, active="exact") for key, val in links.items()],
                   vertical=True, pills=True)

def render_ipynb(name):
    '''converts markdown contect of .ipynb to layout'''
    cells = json.load(open(name, 'r'))['cells']
    md_container = [c['source'] for c in cells if c['cell_type']=='markdown']
    div_container = []
    for i, md in enumerate(md_container):
        div_container.append(dcc.Markdown(md, mathjax=True, style={'width':'60%'}))
        if i != len(md_container) - 1:
            div_container.append(html.Hr())
    return html.Div(div_container)



