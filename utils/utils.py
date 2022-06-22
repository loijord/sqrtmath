from dash import html, dcc
import dash_bootstrap_components as dbc
import inspect
import json
import numpy as np
import pandas as pd
import dash_latex as dl

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

def multiindex_table(df,
                     table_style = {'border': '3px solid'},
                     header_section_style = {'border': '2px solid'},
                     body_section_style = {'border': '2px solid'},
                     body_index_cell_style = {'text-align': 'left',
                                              'border':'1px solid',
                                              'backgroundColor': 'rgb(210, 210, 255)',
                                              'valign':'top',
                                              'font-weight': 'bold'},
                     body_column_cell_style = {'text-align': 'right',
                                               'border':'1px solid grey',
                                               'backgroundColor': 'rgb(210, 255, 210)'},
                     header_index_cell_style = {'text-align': 'left',
                                                'border':'2px solid',
                                                'backgroundColor': 'rgb(165, 165, 255)',
                                                'valign':'top',
                                                'font-weight': 'bold'},
                     header_column_cell_style = {'text-align': 'right',
                                                 'border':'2px solid',
                                                 'backgroundColor': 'rgb(165, 255, 165)',
                                                 'font-weight': 'bold'}):
    # storing rowSpan values for every cell of index;
    # if rowSpan==0, html item is not going to be included
    pos = np.diff(df.index.codes, axis=1, prepend=-1)
    for row in pos:
        counts = np.diff(np.flatnonzero(np.r_[row, 1]))
        row[row.astype(bool)] = counts

    # filling up header of table;
    column_names = df.columns.values
    headTrs = html.Tr([html.Th(n, style=header_index_cell_style) for n in df.index.names] +
                      [html.Th(n, style=header_column_cell_style) for n in column_names])
    # filling up rows of table;
    bodyTrs = []
    for rowSpanVals, idx, col in zip(pos.T, df.index.tolist(), df.to_numpy()):
        rowTds = []
        for name, rowSpan in zip(idx, rowSpanVals):
            if rowSpan != 0:
                rowTds.append(html.Td(name, rowSpan=rowSpan, style=body_index_cell_style))
        for name in col:
            rowTds.append(html.Td(name, style=body_column_cell_style))
        bodyTrs.append(html.Tr(rowTds))

    table = html.Table([
        html.Thead(headTrs, style=header_section_style),
        html.Tbody(bodyTrs, style=body_section_style)
    ], style=table_style)
    return table

def nested_df(d):
    first_val = next(iter(d.values()))
    if type(first_val) is dict:
        return pd.concat([nested_df(val) for val in d.values()],
                          keys=d.keys())
    else:
        return pd.DataFrame(d).T

def force_multiline(lines, text_mode=True):
    if text_mode:
        mapper = lambda x: rf'\text{{{x}}}'
    else:
        mapper = lambda x: x
    latex = r'$\begin{array}{l}' + \
            r' \\ '.join([mapper(line) for line in lines]) + \
            r'\end{array}$'''
    return dl.DashLatex(latex)



