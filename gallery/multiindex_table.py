import pandas as pd
import numpy as np
from dash import html

# ADJUST STYLES
table_style = {'border': '3px solid'}
header_section_style = {'border': '2px solid'}
body_section_style = {'border': '2px solid'}
body_index_cell_style = {'text-align': 'left',
                    'border':'1px solid',
                    'backgroundColor': 'rgb(210, 210, 255)',
                    'valign':'top',
                    'font-weight': 'bold'}
body_column_cell_style = {'text-align': 'right',
                     'border':'1px solid grey',
                     'backgroundColor': 'rgb(210, 255, 210)'}
header_index_cell_style = {'text-align': 'left',
                    'border':'2px solid',
                    'backgroundColor': 'rgb(165, 165, 255)',
                    'valign':'top',
                    'font-weight': 'bold'}
header_column_cell_style = {'text-align': 'right',
                     'border':'2px solid',
                     'backgroundColor': 'rgb(165, 255, 165)',
                     'font-weight': 'bold'}

# CREATE TABLE MANUALLY (thanks to pd.to_html)
table = html.Table([
            html.Thead([
                html.Tr([
                    html.Th('Country', style=header_index_cell_style),
                    html.Th('Cultural Region', style=header_index_cell_style),
                    html.Th('Capital', style=header_column_cell_style),
                    html.Th('Avg. temperature', style=header_column_cell_style)
                ])
            ], style=header_section_style),
            html.Tbody([
                html.Tr([
                    html.Td('Lithuania', rowSpan=5, style=body_index_cell_style),
                    html.Td('Aukštaitija', style=body_index_cell_style),
                    html.Td('Panevėžys', style=body_column_cell_style),
                    html.Td('6.3°C', style=body_column_cell_style)
                    ]),
                html.Tr([
                    html.Td('Žemaitija', style=body_index_cell_style),
                    html.Td('Telšiai', style=body_column_cell_style),
                    html.Td('5.9°C', style=body_column_cell_style)
                    ]),
                html.Tr([
                    html.Td('Dzūkija', style=body_index_cell_style),
                    html.Td('Alytus', style=body_column_cell_style),
                    html.Td('6.4°C', style=body_column_cell_style)
                ]),
                html.Tr([
                    html.Td('Suvalkija', style=body_index_cell_style),
                    html.Td('Marijampolė', style=body_column_cell_style),
                    html.Td('No data', style=body_column_cell_style)
                ]),
                html.Tr([
                    html.Td('Mažoji Lietuva', style=body_index_cell_style),
                    html.Td('Tilžė', style=body_column_cell_style),
                    html.Td('8.2°C', style=body_column_cell_style)
                ]),
                html.Tr([
                    html.Td('Latvia', rowSpan=4, style=body_index_cell_style),
                    html.Td('Kurzeme', style=body_index_cell_style),
                    html.Td('Jelgava', style=body_column_cell_style),
                    html.Td('7.1°C', style=body_column_cell_style)
                ]),
                html.Tr([
                    html.Td('Zemgale', style=body_index_cell_style),
                    html.Td('Jelgava', style=body_column_cell_style),
                    html.Td('7.1°C', style=body_column_cell_style)
                ]),
                html.Tr([
                    html.Td('Vidūmō', style=body_index_cell_style),
                    html.Td('Riga', style=body_column_cell_style),
                    html.Td('6.1°C', style=body_column_cell_style)
                ]),
                html.Tr([
                    html.Td('Latgale', style=body_index_cell_style),
                    html.Td('Daugavpils', style=body_column_cell_style),
                    html.Td('5.5°C', style=body_column_cell_style)
                ])
            ], style=body_section_style)
        ], style=table_style)

# AUTOMATE MANUAL CREATION
def multiindex_table(df):
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

# PREPARE YOUR DATA
d = {'Full':
    {'Lithuania':
         {'Aukštaitija': ('Panevėžys',	'6.3°C'),
          'Žemaitija': ('Telšiai', '5.9°C'),
          'Dzūkija': ('Alytus', '6.4°C'),
          'Suvalkija': ('Marijampolė', 'No data'),
          'Mažoji Lietuva': ('Tilžė', '8.2°C')},
     'Latvia':
         {'Kurzeme': ('Jelgava', '7.1°C'),
          'Zemgale': ('Jelgava', '7.1°C'),
          'Vidūmō': ('Riga', '6.1°C'),
          'Latgale': ('Daugavpils', '5.5°C')}
    },
    'Short':
    {'Lithuania':
         {'Aukštaitija': ('Panevėžys',	'6.3°C'),
          'Žemaitija': ('Telšiai', '5.9°C'),
          'Dzūkija': ('Alytus', '6.4°C'),
          'Suvalkija': ('Marijampolė', 'No data')},
     'Latvia':
         {'Kurzeme & Zemgale': ('Jelgava', '7.1°C'),
          'Vidūmō': ('Riga', '6.1°C'),
          'Latgale': ('Daugavpils', '5.5°C')}
    },
    }

# CREATE NESTED DF MANUALLY
def nested_df_demo(d):
    return pd.concat([pd.concat([pd.DataFrame(d2).T for d2 in d1.values()],
                                keys=d1.keys()) for d1 in d.values()],
                     keys=d.keys())

# AUTOMATE MANUAL CREATION
def nested_df(d):
    first_val = next(iter(d.values()))
    if type(first_val) is dict:
        return pd.concat([nested_df(val) for val in d.values()],
                          keys=d.keys())
    else:
        return pd.DataFrame(d).T

df = nested_df(d)
df.index.set_names(['Portion', 'Country', 'Cultural Region'], inplace=True)
df.columns = ['Capital', 'Average Temperature']

content = html.Div([html.H4('pd.DataFrame to html by pandas'),
                    html.Iframe(width="800",
                                height="500",
                                sandbox='',
                                srcDoc=df.to_html()),
                    html.H4('pd.DataFrame to html in a custom way'),
                    multiindex_table(df),
                    ])
