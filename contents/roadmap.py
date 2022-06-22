from dash import html, callback, Input, Output
from utils.stylesheet import SIDEBAR_STYLE, JUMBOTRON
import sidebars.roadmap
import contents.release_notes, contents.koncepcija, contents.part1, contents.part2

content_children=html.P("Ši skiltis skirta apžvelgti projekto koncepciją ir technines dalis")

sidebar = html.Div(children=sidebars.roadmap.sections, id="roadmap-sidebar", style=SIDEBAR_STYLE)
content = html.Div(children=content_children, id="roadmap-content")


@callback(Output('roadmap-sidebar', 'children'),
          Output('roadmap-content', 'children'),
          [Input('page-url', 'pathname')],
          prevent_initial_call=False)
def display_content(pathname):
    path = pathname.strip('/').split('/')
    if path[:2] == ["roadmap"]: return sidebar, content
    elif path[:2] == ["roadmap", "koncepcija"]: return sidebar, contents.koncepcija.content
    elif path[:2] == ["roadmap", "release_notes"]: return sidebar, contents.release_notes.content
    elif path[:2] == ["roadmap", "part1"]: return sidebar, contents.part1.content
    elif path[:2] == ["roadmap", "part2"]: return sidebar, contents.part2.content
    elif path[:2] == ["roadmap", "part3"]: return sidebar, contents.part3.content
    else: return sidebar, JUMBOTRON(pathname)






