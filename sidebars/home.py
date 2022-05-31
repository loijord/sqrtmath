from utils.dry import nav
from dash import html, dcc

sections = [dcc.Markdown(r'$\Huge \sqrt{MATH}$', mathjax=True), html.Hr(),
           nav({"🏠 Home":"/",
                "Mokiniai":"/mokiniai",
                "Mokesčiai":"/mokesciai",
                "Project Roadmap":"/roadmap"})]