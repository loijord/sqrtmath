from dash import html
from utils.utils import distinquish_sections

section1 = html.Div([html.H3('Kramtomoji guma, prilipusi prie dviračio rato'),
                       html.Iframe(width="630",
                                   height="354",
                                   src="https://www.youtube.com/embed/Io-HXZTepH4",
                                   title="YouTube video player",
                                   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture")])


section2 = html.Iframe(src="https://www.geogebra.org/classic/awdtfudz", width="1000px", height="1000px")

#scrolling="no", style="border:0px;"
content = distinquish_sections([section1, section2])



