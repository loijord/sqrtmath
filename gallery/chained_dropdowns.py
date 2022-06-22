from dash import dcc, html, Input, Output, ctx, dash_table, callback
import pandas as pd

# SOURCE:
# double dropdown: https://github.com/plotly/dash-recipes/blob/master/multiple-city-chained-dropdown.py
# ctx.triggers: https://dash.plotly.com/advanced-callbacks

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

# AUTOMATE CREATION OF MULTIINDEX ENTRIES
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


# create a list of dropdowns
dropdown_ids = [f'dropdown-{i+1}' for i in range(df.index.nlevels)]
dropdown_items = []

for i in range(len(dropdown_ids)):
    if i == 0:
        dropdown_items.append(
            dcc.Dropdown(id=dropdown_ids[i],
                         options=[{'label': k, 'value': k} for k in df.index.unique(0)],
                         placeholder=f"Select {df.index.names[i]}",
                         disabled=False)
        )
    else:
        dropdown_items.append(
            dcc.Dropdown(id=dropdown_ids[i],
                         placeholder=f"Select {df.index.names[i]}",
                         disabled=True
                         ))

# create step by step callbacks dropdowns
for i in range(1, len(dropdown_ids)):
    @callback(
        [Output(dropdown_ids[i], 'disabled'),
         Output(dropdown_ids[i], 'options'),
         Output(dropdown_ids[i], 'value')
         ],
        [Input(dropdown, 'value') for dropdown in dropdown_ids[:i]],
        prevent_initial_call=True)
    def dropdown_options(*args, dropdown_id=dropdown_ids[i-1]):
        if ctx.triggered_id == dropdown_id:
            values = df.loc[tuple(args)].index.unique(0)
            return False, [{'label': i, 'value': i} for i in values], ""
        else:
            return True, [], ""

# display info about triggers of dropdowns
@callback(
    Output('container', 'children'),
    [Input(dropdown, 'value') for dropdown in dropdown_ids])
def set_display_children(*args):
    unnone_args = [n for n in args if n is not None]
    multiindex_info = html.P(f'Select entry of multiindex table: {" -> ".join(unnone_args)}')
    if unnone_args:
        #fixing pandas bugs...
        if None in args:
            sub_df = df.loc[tuple(unnone_args)]
        else:
            sub_df = pd.DataFrame(df.loc[tuple(args)]).T
        multiindex_values = dash_table.DataTable(sub_df.to_dict('records'),
                                                 [{"name": i, "id": i} for i in sub_df.columns],
                                                 style_table={'width':'40%'})
        info = [multiindex_info, multiindex_values]
    else:
        info = [multiindex_info]
    return html.Div(info)

content = html.Div([
    *dropdown_items,
    html.Div(id='container')
])
