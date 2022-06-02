from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc

link_list = [
            dbc.NavLink("Home", href="/gallery/sidebar/home", active="exact"),
            dbc.NavLink("Page 1", href="/gallery/sidebar/page-1", active="exact"),
            dbc.NavLink("Page 2", href="/gallery/sidebar/page-2", active="exact"),
            ]

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": "2.05rem",
    "left": "19.05rem",
    "bottom": 0,
    "width": "16rem",
    "height": "19.9rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    "border": "solid 1px black"
}

# the styles for the main content position it to the right of the sidebar and add some padding.
CONTENT_STYLE = {"position": "fixed", "left": "34rem", "margin-left": "2rem",
                 "margin-right": "2rem", "padding": "2rem 1rem"}

def modify_test():
    link_list.append(dbc.NavLink("Page 3", href="/app_gallery/sidebar/page-3", active="exact"))

sidebar = html.Div([html.H2("Sidebar"),
                    html.Hr(),
                    html.P("A simple sidebar layout with navigation links"),
                    dbc.Nav(link_list, vertical=True, pills=True)],
                   id="playground-sidebar", style=SIDEBAR_STYLE)

cnt = html.Div(id="playground-content", style=CONTENT_STYLE)
content = html.Div([dcc.Location(id="playground-url"), sidebar, cnt], style={"height": "20rem", "border": "solid 1px black"})

fun_note = """Just a fun note: 

```
Styles of a SIDEBAR (located on the left side) and a CONTENT (located on the right side) 
forces them to behave in a different way than any other dash components. 
```
      
* The idea of this website has initially born 
after running my first [Sidebar on Dash](https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/) 
successfully! 
* Cheers!
"""

@callback(
    Output("playground-sidebar", "children"),
    Output("playground-content", "children"),
    Input("playground-url", "pathname"),
    prevent_initial_call=True
)
def render_page_content(pathname):
    if pathname == "/gallery/sidebar":
        return sidebar, html.Div([dcc.Markdown(fun_note, style={'width':'50%'}),
                                 html.Img(src="../assets/have_a_drink.jpg", style={'width': '30%'})],
                                 className="row")
    elif pathname == "/gallery/sidebar/home":
        return sidebar, html.P("This is the content of the home page!")
    elif pathname == "/gallery/sidebar/page-1":
        return sidebar, html.P("This is the content of page 1. Yay!")
    elif pathname == "/gallery/sidebar/page-2":
        return sidebar, html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message - a new version of outdated dbc.Jumbotron
    return sidebar, html.Div([
            html.H2("404: Not found", className="text-danger"),
            html.Hr(className="my-2"),
            html.P(f"The pathname {pathname} was not recognised..."),
            dbc.Button("Super button that does nothing", color="secondary", outline=True)],
            className="h-100 p-5 bg-light border rounded-3")