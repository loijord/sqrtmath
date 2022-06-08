from dash import dcc, html

content = html.Div([
    dcc.Markdown(r"""# Duomenys ir jų parametrai
Norint atlikti kokybišką mokyklinio turinio analizę, 
įvertinti tam tikro moksleivio žinias ir paskirstyti mokomąjį turinį pagal jo gebėjimus,
reikia turėti """, mathjax=True, style={'width': '60%'})])