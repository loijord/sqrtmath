from dash import html, dcc
import dash_bootstrap_components as dbc
import inspect
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

def nice_app_display(module):
    '''assume module has a content attribute and its not dash app, run it and display source code'''
    #https://dash.plotly.com/dash-core-components/markdown
    src = f'''```python
import dash
{inspect.getsource(module)}

app = dash.Dash(__name__)
app.layout = content
if __name__ == '__main__':
    app.run_server(debug=True)
    
```'''
    return html.Div([module.content,
                     html.Hr(),
                     dcc.Markdown('`source code:`'),
                     dcc.Markdown(src, style={"background-color": "purple", "border": "solid 1px black"})])




