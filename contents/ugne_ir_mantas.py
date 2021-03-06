import dash_cytoscape as cyto
from dash import html

#demo for adding urls: https://stackoverflow.com/a/69700675/3044825
cyto.load_extra_layouts() #dagre layout

P1 = {'data': {'id': 'p1', 'label': 'Use Bulb'}, 'grabbable': True, 'classes': 'process'}
P2 = {'data': {'id': 'p2', 'label': 'Prod. Bulb'}, 'grabbable': True, 'classes': 'process'}
P3 = {'data': {'id': 'p3', 'label': 'Prod. Elec', 'parent': 'm1'}, 'grabbable': True, 'classes': 'process'}
P4 = {'data': {'id': 'p4', 'label': 'Very long line for testing'}, 'grabbable': True, 'classes': 'process'}
P5 = {'data': {'id': 'p5', 'label': 'Prod. Glass'}, 'grabbable': True, 'classes': 'process'}
P6 = {'data': {'id': 'p6', 'label': 'Prod. Copper'}, 'grabbable': True, 'classes': 'process'}
P7 = {'data': {'id': 'p7', 'label': 'Prod. Fuel', 'parent': 'm1'}, 'grabbable': True, 'classes': 'process'}

E1 = {'data': {'id': 'e1', 'source': 'p7', 'target': 'p3', 'label': 'Fuel'}}
E2 = {'data': {'id': 'e2', 'source': 'p3', 'target': 'p6', 'label': 'Elec.'}}
E3 = {'data': {'id': 'e3', 'source': 'p3', 'target': 'p2', 'label': 'Elec.'}}
E4 = {'data': {'id': 'e4', 'source': 'p3', 'target': 'p5', 'label': 'Elec.'}}
E5 = {'data': {'id': 'e5', 'source': 'p3', 'target': 'p1', 'label': 'Elec.'}}
E6 = {'data': {'id': 'e6', 'source': 'p6', 'target': 'p2', 'label': 'Copper'}}
E7 = {'data': {'id': 'e7', 'source': 'p5', 'target': 'p2', 'label': 'Glass'}}
E8 = {'data': {'id': 'e8', 'source': 'p2', 'target': 'p1', 'label': 'Bulb'}}
E9 = {'data': {'id': 'e9', 'source': 'p4', 'target': 'p1', 'label': 'Waste Treatment'}}

nodes = [P1, P2, P3, P4, P5, P6, P7]
edges = [E1, E2, E3, E4, E5, E6, E7, E8, E9]


content = html.Div([
        #dcc.Location(id="ieva-content"), #This causes serious injuries
        cyto.Cytoscape(
            id='cytoscape',
            layout={'name': 'dagre', 'spacingFactor': 1.15},
            style={'width': '100%', 'height': '900px'},
            elements=nodes + edges,
            autounselectify=True
        )], style={'background-image': 'url(https://upload.wikimedia.org/wikipedia/commons/2/22/North_Star_-_invitation_background.png)',
                   'height': '200%'})
#layout = html.Div([dcc.Location(id="ieva-url"), sidebar, content])

#def display_content(pathname): print('im mantas', pathname)
#return html.Div([dcc.Location(id="mantas_ir_ugne"), sidebar, content])
