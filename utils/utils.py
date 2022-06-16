from dash import html, dcc
import dash_bootstrap_components as dbc
import inspect
import json

class Markdown(dcc.Markdown):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mathjax=True
        self.dangerously_allow_html = True

def add_spacing(html_element):
    return html.Div([html.Br(), html_element, html.Br()])

def nav(links):
    return dbc.Nav([dbc.NavLink(key, href=val, active="exact") for key, val in links.items()],
                   vertical=True, pills=True)

def distinquish_sections(container):
    div_container = []
    for i, c in enumerate(container):
        div_container.append(c)
        if i != len(container) - 1:
            div_container.append(html.Hr())
    return html.Div(div_container)

def render_ipynb(name):
    '''converts markdown contect of .ipynb to layout'''
    cells = json.load(open(name, 'r'))['cells']
    md_container = [dcc.Markdown(c['source'], mathjax=True, style={'width': '60%'}) for c in cells if c['cell_type']=='markdown']
    return distinquish_sections(md_container)


def star_ranking(array, colors=('black', '#ffd700')):
    elements = []
    for n in array:
        elements.append(html.I(
            className="fa fa-star",
            style={'color': colors[n], 'font-size': '24px'}))
    return html.Div(elements)

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




