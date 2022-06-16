from utils.utils import nav
from dash import html

sections = [html.H2("Mokiniai"), html.Hr(),
           nav({"🏠 Home": "/",
                "Ieva": "/mokiniai/ieva",
                "Ugnė ir Mantas": "/mokiniai/ugne_ir_mantas",
                "Pijus": "/mokiniai/pijus"})]