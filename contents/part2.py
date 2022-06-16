from dash import dcc, html, dash_table
from utils.utils import Markdown, star_ranking, add_spacing
import pandas as pd
from PIL import Image

d = {'Known': {'n':1, 'fr':2, 'to':3, 'by':4},
     'Unknown': {'n':1, 'fr':2, 'to':3, 'by':4},
     'Ifthen': {'n':1, 'fr':2, 'carrier':3, 'by':4, 'to':5, 'ask':6, 'background':7}}

new = []
for level0, level1 in d.items():
    for key, val in level1.items():
        new.append([level0, key, val])

df = pd.DataFrame(new, columns=['Klasė', 'Parametras', 'Paaiškinimas'])

df_table = dash_table.DataTable(data=df.to_dict('records'),
                                columns=[{"name": str(i), "id": str(i)} for i in df.columns],
                                style_data={'whiteSpace': 'normal', 'height': 'auto'},
                                fill_width=True)

content = html.Div([
    html.H1('Duomenų bazės kūrimas'),
    Markdown(r"""## Tikslas
Norint naudotis ankstesnėje sekcijoje minėtais privalumais, reikia apibrėžti kokius 
parametrus įsivesime aprašinėdami įvairią mokymosi medžiagą"""),
    Markdown(r"""## Kiek pasiektas tikslas:"""),
    star_ranking((1, 1, 1, 0, 0)),
    html.Br(),
    Markdown(r"""## Kas nuveikta:
* 2021 m. pavasarį su trim moksleiviais išbandytas interaktyvus uždavinių sprendimas
* Buvo naudojama primityvi sprendimo žingsnių ir moksleivio gebėjimo juos atlikti duomenų bazė
* Uždavinių sprendimų įvedinėjimas, kėlimas į internetą ir klaidų taisymas kode buvo daug atimantis procesas, 
ko pasekoje projektas buvo sustabdytas
* Nepaisant to, liko neprižiūrimas kodas su daug iliustracijų, rodančių, kokių rezultatų reikėtų siekti, 
jei projektas būtų valdomas 
* 2022 metų pavasarį atsirado minčių, kaip patobulinti sprendimams aprašyti naudojamą duomenų struktūrą
* Taip pat atradus Python `Dash` biblioteką atsirado ir žinių, kaip naudojant HTML skriptus būtų galima supaprastinti 
sprendimų užrašymo procesą ir platformą atverti kiekvienam norinčiam
* Belieka tęsti!"""),
    dcc.Markdown(r"""### Primityvi duomenų bazė
2021 m. naudotoje duomenų bazėje buvo aprašinėjami stojamieji į licėjų ir VBE. Uždavinio sprendimo struktūra buvo tokia:
* Sąlyga
* Rankomis įvestas pilnas sprendimas
* Atskiri sprendimo žingsniai:
  * Atitikmuo - klausimas, į kurį reikia atsakyti
  * Sprendimas - rankomis įvestas atsakymas į klausimą, kuriame nurodytas veiksmas ir 
kartais paaiškinta, kokia taisykle remiamasi
  * Gebėjimas - kompetencija, kurios reikia norint atsakyti į klausimą"""),
    Markdown(r""" **Naudota sprendimo struktūra:**"""),
    add_spacing(html.Img(src=Image.open("assets/part2_ex1.png"))),
dcc.Markdown(r"""### Paprasčiausios duomenų bazės užklausos
Prijungus informaciją apie moksleivio rezultatus buvo galima pateikti, kokių kompetencijų reikia tam tikram testui ir 
kaip moksleivis jas atitinka:"""),
html.Img(src=Image.open("assets/part2_ex2.png")),
dcc.Markdown(r"""### Patobulinta versija

Pagal atnaujintą 2022 metų modelį uždavinių sprendimų aprašymas turėtų teikti detalesnių žinių 
apie teste esančių uždavinių sandarą, nei rankomis įvesti gebėjimų pavadinimai. Planuojama atsisakyti kompetencijų pavadinimų ir 
vietoj jų naudoti apibrėžimus, taisykles ir kt., kas paimta iš viešai prieinamos rodyklės. Tuomet sprendimo žingsniai atrodytų taip:"""
),
add_spacing(html.Img(src=Image.open("assets/solution_demo.jpg"))),
dcc.Markdown(r"""Grafui aprašyti panaudotas kodas:

```python
pr = Problem(
task='Sujungus keturkampio kraštinių vidurio taškus gautas lygiagretainis. Raskite jo perimetrą, jei viena jo įstrižainė lygi $x$, o kita $y$',
picture='my_draw.png',
data=(
    Known(n=0, fr='$X$ - atkarpos $AB$ vidurio taškas'),
    Known(n=1, fr='$Y$ - atkarpos $BC$ vidurio taškas'),
    Known(n=2, fr='$Z$ - atkarpos $CD$ vidurio taškas'),
    Known(n=3, fr='$T$ - atkarpos $DA$ vidurio taškas'),
    Known(n=4, fr='Viena lygiagretainio įstrižainė lygi $x$', to='$AC=x$', by=Assign('įstrižainė', '$x$')),
    Known(n=5, fr='Kita lygiagretainio įstrižainė lygi $y$', to='$BD=y$', by=Assign('įstrižainė', '$y$')),
    Unknown(n=6, fr='Raskite lygiagretainio perimetrą', to='$P_{XYZT}$')),
steps=(
    IfThen(n=7, fr=(0, 1), carrier=r'$XY$ yra $\bigtriangleup ABC$ vidurio linija',
           by=Def('Vidurio linija'), ask='Kokia savybe pasižymi atkarpa $XY$?'),

    IfThen(n=8, fr=(2, 3), carrier=r'$ZT$ yra $\bigtriangleup ACD$ vidurio linija',
           by=Def('Vidurio linija'), ask='Kokia savybe pasižymi atkarpa $ZT$?'),

    IfThen(n=9, fr=(1, 2), carrier=r'$YZ$ yra $\bigtriangleup ABD$ vidurio linija',
           by=Def('Vidurio linija'), ask='Kokia savybe pasižymi atkarpa $YZ$?'),

    IfThen(n=10, fr=(0, 3), carrier=r'$XT$ yra $\bigtriangleup BCD$ vidurio linija',
           by=Def('Vidurio linija'), ask='Kokia savybe pasižymi atkarpa $XT$?'),

    IfThen(n=11, fr=(7, 4), carrier=r'$XY = \frac{x}{2}$',
           by=Rule('Vidurio linijos savybė'), ask='$XY$', background=(Rule('deassign'), 4)),

    IfThen(n=12, fr=(8, 4), carrier=r'$ZT = \frac{x}{2}$',
           by=Rule('Vidurio linijos savybė'), ask='$ZT$', background=(Rule('deassign'), 4)),

    IfThen(n=13, fr=(9, 5), carrier=r'$YZ = \frac{y}{2}$',
           by=Rule('Vidurio linijos savybė'), ask='$YZ$', background=(Rule('deassign'), 5)),

    IfThen(n=14, fr=(10, 5), carrier=r'$XT = \frac{y}{2}$',
           by=Rule('Vidurio linijos savybė'), ask='$XT$', background=(Rule('deassign'), 5)),

    IfThen(n=15, fr=(11, 12, 13, 14),
           carrier=r'$P_{XYZT}=XY+ZT+XY+ZT=\frac{x}{2}+\frac{x}{2}+\frac{y}{2}+\frac{y}{2}=x+y$',
           to=r'$P_{XYZT}=x+y$',
           by=Def('Perimetras'),
           ask='$P_{XYZT}$',
           background=(Rule('trupmenų su vienodais vardikliais sudėtis'), Rule('deassign'), 11, 12, 13, 14))),

analogies=[(0, 1, 2, 3), (4, 5), (7, 8, 9, 10), (11, 12, 13, 14)],
conclusion='Lygiagretainio, gauto sujungus keturkampio kraštinių vidurio taškus, perimetras lygus to keturkampio įstrižainių sumai',
author='vadovėlis gimnazijų 1 ir 2 klasėms',
name='Uždavinys 99')
```"""),
dcc.Markdown(r"""### Patobulintos versijos analizė
Sprendimams aprašyti buvo naudojamos prieš tai apibrėžtos klasės, kiekviena sudaryta iš tam tikro parametrų rinkinio. 
Klasės `Assign`, `Rule` ir `Def` skirtos apibūdinti matematiniams žymėjimams, taisyklėms ir apibrėžimams. 
Jos skiriasi tik tuo, kad naudoja skirtingas rodykles: 
`Assign` klasė rodyklių nenaudoja, `Rule` naudoja taisyklių sąrašą, o `Def` - apibrėžimų.   
Klasės `Known`, `Unknown`, `Ifthen` taip pat panašios, tik pagal savo naudojamus atributus: 
* `n` - sprendimo žingsnio numeris, 
* `fr`- teiginys arba jų grupė, naudojami atlikti sprendimo žingsniui
* `to`- teiginys, išvestas sprendimo žingsnyje
* `by`- taisyklė ar teiginys, kurį taikant išvedimas yra galimas
             
"""),
df_table
])

