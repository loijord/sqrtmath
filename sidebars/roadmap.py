from utils.utils import nav
from dash import html

sections = [html.H2("Projekto planas"), html.Hr(),
           nav({"🏠 Home": "/",
                "Koncepcija": "/roadmap/koncepcija",
                "Release notes": "/roadmap/release_notes",
                "Part 1: uždavinių aprašymas": "/roadmap/part1",
                "Part 2: duomenų bazės kūrimas": "/roadmap/part2"})]