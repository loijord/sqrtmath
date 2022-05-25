from dash import html

# write connections only with args
data = {r'$ax+by+c=0$':
        {'ask': r'Duota pavidalo $ax+by+c=0$ lygtis, įvardykite du jos svarbesnius atskirus atvejus',
         'refers': 'tiesinė lygtis',
         'solution':
    ('Kai $a=0$, tai turime vieno kintamojo tiesinę lygtį $by+c=0$',
     'Kai $b=0$, tai turime vieno kintamojo tiesinę lygtį $ax+c=0$'),
         'by': 'zero-scenario',
         'scope': '1.9.5.1'},
        }

def create_view():
    return html.P("This is the first design of atvejai")