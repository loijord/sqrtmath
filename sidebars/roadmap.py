from utils.dry import nav
from dash import html

sections = [html.H2("Projekto planas"), html.Hr(),
           nav({"🏠 Home": "/",
                "Koncepcija": "/roadmap/koncepcija",
                "Release notes": "/roadmap/release_notes",
                "Part 1: uždavinių aprašymas": "/roadmap/part1"})]