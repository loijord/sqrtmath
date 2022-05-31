import dash_bootstrap_components as dbc

def nav(links):
    return dbc.Nav([dbc.NavLink(key, href=val, active="exact") for key, val in links.items()],
                   vertical=True, pills=True)