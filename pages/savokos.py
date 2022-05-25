from dash import html

data = {'tiesinė lygtis': r'lygtis, kurios pavidalas yra $ax+by+c=0$, $a \neq 0$ ir $b\neq 0$',
        'kryptinė tiesinė lygtis': r'lygtis, kurios pavidalas yra $y=kx+m$'}

def create_view():
    return html.P("This is the first design of sąvokos")