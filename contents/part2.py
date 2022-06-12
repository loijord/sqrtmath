from dash import dcc, html
from PIL import Image

content = html.Div([
    dcc.Markdown(r"""# Duomenų bazės kūrimas
Norint atlikti kokybišką mokyklinio turinio analizę, 
vertinti moksleivių žinias ir paskirstyti mokomąjį turinį pagal jo gebėjimus,
reikia apibrėžti, kokius taisyklių ir uždavinių parametrus įsivesime.

### Pirminis variantas
2021 m. pavasarį su keletu moksleivių išbandžiau interaktyvų uždavinių sprendimą, 
taikydamas taip atrodančią uždavinių sprendimų duomenų bazę:""", mathjax=True, style={'width': '60%'}),
html.Img(src=Image.open("assets/part2_ex1.png"), style={'width': '60%'}),
    dcc.Markdown(r"""Kiekviename uždavinio sprendimo žingsnyje įvesdavau to žingsnio **sprendimą**, 
klausimą, į kurį reikia atsakyti (**atitikmenį**) ir **gebėjimą**, 
kurį moksleivis turi turėti, kad galėtų atsakyti. Remiantis šia duomenų baze buvo įmanoma vykdyti tam tikras duomenų bazės
užklausas, skirtas tirti, iš ko sudarytas stojamųjų į licėjų testas ir kaip tam tikras moksleivis yra jam pasiruošęs:""",
mathjax=True, style={'width': '60%'}),
html.Img(src=Image.open("assets/part2_ex2.png"), style={'width': '60%'}),
dcc.Markdown(r"""Daugiau duomenų bazės užklausų pavyzdžių pateiksiu kitoje dalyje""",
                 mathjax=True, style={'width': '60%'}),
dcc.Markdown(r"""### Patobulinta versija
Ankstesnis variantas yra pakankamas statistiniams tam tikros programos ar moksleivio gebėjimų vertinimams, 
tačiau neteikia tikslesnių žinių apie vidinę uždavinių struktūrą, sudėtingumą ir tam tikrų mąstymo būdų pasiskirstymą.
Vienintelis rodiklis, pagal kurį galima daryti panašias įžvalgas, būtų gebėjimai, duodantys tik miglotą vaizdą.
Panašus vaizdas susidaro nagrinėjant bendrojo ugdymo programas, egzaminų programas ar bet kurio vadovėlio temų sąrašą.

Pagal atnaujintą 2022 metų modelį uždavinių sprendimams aprašyti naudojami kryptiniai grafai. 
Norint aprašyti uždavinio sprendimą buvo pateiktas tokio grafo pavyzdys:""",
mathjax=True, style={'width': '60%'}),
html.Img(src=Image.open("assets/netgraph_demo.jpg"), style={'width': '40%'}),
dcc.Markdown(r"""Grafui aprašyti panaudotas kodas:

    ```
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
dcc.Markdown(r"""Kode naudojamos prieš tai apibrėžtos klasės su tam tikrais atributais:
             
|section a|section b
|:---:|:---|
|1|2|
|1|2|

""", mathjax=True, style={'width': '60%'})
])