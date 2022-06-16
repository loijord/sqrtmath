from utils.utils import nav
from dash import html, dcc

sections = [dcc.Markdown(r'$\Huge \sqrt{MATH}$', mathjax=True), html.Hr(),
           nav({"🏠 Home":"/",
                "Mokiniai":"/mokiniai",
                "Project Roadmap":"/roadmap",
                "App Gallery":"/gallery"})]