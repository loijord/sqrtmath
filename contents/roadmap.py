from dash import html, dcc

md_text = r'''
    # Release notes
    ## 2022-05-31
    Project $\large \sqrt{MATH}$ has spawned out! It lives in 
    [https://sqrtmath.herokuapp.com](https://sqrtmath.herokuapp.com)
    
    In its birth, it supports these features:
    * has a nice sidebar and content sections
    * able to navigate to other sidebars: like
    [https://sqrtmath.herokuapp.com/mokiniai](https://sqrtmath.herokuapp.com/mokiniai)
    * able to display some objects of `dash` library: 
      * [`dash_table.DataTable + dcc.Graph(figure=plotly.express.line)`](https://sqrtmath.herokuapp.com/mokiniai)
      * [`dash-cytoscape.Cytoscape`](https://sqrtmath.herokuapp.com/mokiniai/ieva)
      * `dcc.Markdown` with `mathjax` support like you see here
      * [`Error 404` notification](https://sqrtmath.herokuapp.com/mokiniai/mariukas)

    It's based on `dash` so there's going to be a lot more fun:
    
    * [`https://dash.plotly.com/`](https://dash.plotly.com/)
    * [`https://github.com/vizzuhq/ipyvizzu`](https://github.com/vizzuhq/ipyvizzu)
    * Other apps that are possible to integrate with `dash`?

    # Project Roadmap
    
    Šis projektas yra skirtas palengvinti matematikos mokymosi procesą. Jame bus talpinama įvairi medžiaga: 
    sąvokos, taisyklės, uždaviniai su sprendimais ir kt. Mokiniai galės pasirinkti specifinę temą/as, 
    pasitikrinti savo gebėjimus ir sužinoti, kokių tiksliai dalykų nemoka. Įsivertinus atsiranda galimybė kartoti 
    ne viską iš eilės, o tik tai, ką nemoka. Turėtų susitaupyti daug brangaus mokinių laiko, kurio matematika nuolat 
    stinga. Vėlesnėse projekto stadijose turėtų atsirasti:
    
    * Didelė visiškai skaitmeninė matematinės medžiagos bazė su galimu parsisiuntimu
    * Galimybė peržiūrėti kiekvieno uždavinio sprendimą pažingsniui
    * Galimybė vizualiai peržiūrėti, kaip stiprėja neuroninės jungtys tam tikroje srityje
    * Galimybė įvertinti, kiek tankiai sprendžiant uždavinius yra atliekamas tam tikras pasikartojantis žingsnis 
    ar žingsnių rinkinys
'''

content = html.Div(children=[dcc.Markdown(md_text, mathjax=True)])


