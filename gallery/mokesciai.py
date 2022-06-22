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
                  #index=['rugpjūtis', 'rugsėjis', 'spalis', 'lapkritis', 'gruodis', 'sausis', 'vasaris', 'kovas', 'balandis', 'gegužė'],
                  columns=['šildymas', 'admin', 'vanduo', 'internetas', 'elektra', 'dujos'])

df['mėnuo'] = pd.date_range(start='08-31-2021', periods=len(df), freq="M")
df['mėnuo'] = df['mėnuo'].dt.strftime('%m/%Y')
df = df.set_index('mėnuo').reset_index() #dash_table.DataTable has no index thus swap the order
df['total'] = df[['šildymas', 'admin', 'vanduo', 'internetas', 'elektra', 'dujos']].sum(axis=1).round(decimals=3)
df['average'] = df['total'].mean().round(decimals=2)
df_table = dash_table.DataTable(data=df.to_dict('records'),
                                columns=[{"name": i, "id": i} for i in df.columns],
                                fill_width=True)

#k. tarifas: https://chc.lt/lt/gyventojams/karsto-vandens-kainos/81/y2021
#š. tarifas: https://www.vv.lt/namams/paslaugu-kainos/
df2 = pd.DataFrame([[0.611, 37, 4.28*1.09, 1.32], #5
                    [3.936, 42, 4.69*1.09, 1.32], #5
                    [5.08, 44, 5.26*1.09, 1.32], #2
                    [6.536, 48, 6.04*1.09, 1.32], #4
                    [8.572, 52, 6.70*1.09, 1.32], #4
                    [11.706, 57, 7.30*1.09, 1.32], #5
                    [15.236, 61, 7.09*1.09, 1.32], #?
                    [17.980, 66, 6.71*1.09, 1.32]],
                   columns=['karštas', 'šaltas', 'k. tarifas', 'š. tarifas'])
df2['mėnuo'] = pd.date_range(start='11-25-2021', periods=len(df2), freq="M")
df2['mėnuo'] = df2['mėnuo'].dt.strftime('%m/%Y')
df2['k. tarifas'] = df2['k. tarifas'].round(decimals=5)
df2['š. tarifas'] = df2['š. tarifas'].round(decimals=2)
df2['karšto sunaudojimas'] = df2['karštas'].diff().round(decimals=3)
df2['šalto sunaudojimas'] = df2['šaltas'].diff().round(decimals=3)
df2['karšto suma'] = (df2['karšto sunaudojimas'] * df2['k. tarifas']).round(decimals=2)
df2['šalto suma'] = (df2['šalto sunaudojimas'] * df2['š. tarifas'] + 0.79).round(decimals=2)
df2 = df2.drop(['k. tarifas', 'š. tarifas'], axis = 1)
df2 = df2.set_index('mėnuo').reset_index()

df2_table = dash_table.DataTable(data=df2.to_dict('records'),
                                columns=[{"name": i, "id": i} for i in df2.columns],
                                fill_width=True)

fig = px.line(df, x=df["mėnuo"], y=['šildymas', 'total', 'average'], markers=True)
fig2 = px.line(df2, x=df2["mėnuo"], y=['šalto suma', 'karšto suma'], markers=True)
content = html.Div(children=[html.Label("Komunalai"), html.Hr(), df_table,
                             dcc.Graph(id='example', figure=fig),
                             html.Hr(),
                             html.Label("Numatomas mokėjimas pagal skaitiklių parodymus"),
                             html.Hr(),
                             df2_table,
                             dcc.Graph(id='example', figure=fig2)])

