import plotly.express as px
from dash import html, dcc, dash_table
import pandas as pd
df = pd.DataFrame([[0, 0, 0, 17.39, 3.8, 1.26],
                   [0, 20.66, 0, 17.39, 6.54, 1.19],
                   [11.99, 32.19, 7.39, 17.39, 7.75, 1.89],
                   [42.97, 21.75, 7.39, 17.39, 9.42, 1.82],
                   [97.68, 17.94, 7.39, 17.39, 5.78, 1.19],
                   [141.32, 20.66, 3.43, 17.39, 10.35, 2.16],
                   [144.85, 24.03, 6.07, 17.39, 10.35, 2.16],
                   [151.24, 18.84, 6.07, 17.39, 7.68, 1.36],
                   [107.86, 36.77, 7.39, 17.39, 8.02, 1.36],
                   [92.46, 34.75, 10.82, 17.39, 6.85, 1.92]],
                  index=['rugpjūtis', 'rugsėjis', 'spalis', 'lapkritis', 'gruodis', 'sausis', 'vasaris', 'kovas', 'balandis', 'gegužė'],
                  columns=['šildymas', 'admin', 'vanduo', 'internetas', 'elektra', 'dujos'])

df['total'] = df.sum(axis=1).round(decimals=3)
df['9 praeitų mėn. average'] = df['total'].mean().round(decimals=2)
df['teorinis 12 mėn. average'] = round((df['total'].sum()+2*100)/12, 2)
df.reset_index(inplace=True)
df.rename(columns={"index":'mėnuo'}, inplace=True)
df_table = dash_table.DataTable(data=df.to_dict('records'),
                                columns=[{"name": i, "id": i} for i in df.columns],
                                style_data={
                                        'whiteSpace': 'normal',
                                        'height': 'auto',
                                    },
                                fill_width=True)

fig = px.line(df, x=df["mėnuo"], y=df.columns[[1,-3,-2,-1]], markers=True)
content = html.Div(children=[df_table, dcc.Graph(id='example', figure=fig)])

