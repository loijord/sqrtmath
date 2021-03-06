from dash import dcc, html
from dash_latex import DashLatex as DL
from utils.utils import Markdown, star_ranking, add_spacing, \
    multiindex_table, nested_df, force_multiline
from PIL import Image

#force_multiline([r'\text{Pirma}',r'\text{Antra } x^2+y^2',r'\text{Trečia}'], text_mode=False)

d = {'Known': {'n':('Teiginio, kuris yra duotas sąlygoje, id', 'Numeriai nuo 1 iki 5'),
               'fr':(r'Pradinė teiginio forma', 'Viena lygiagretainio įstrižainė lygi x'),
               'to':(r'Galutinė teiginio forma, rašoma sprendime', 'AB = x'),
               'by':(r'Priskyrimas, pagal kurį pradinė teiginio forma susiveda į galutinę', 'Formos "A lygu B" sakinys užrašomas: A = B')},
     'Unknown': {'n': ('Duomens, kurį reikia rasti, id', 'Numeris 6'),
                 'fr': ('Pradinė duomens, forma', 'Rakite lygiagretainio perimetrą'),
                 'to': ('Galutinė duomens forma, rašoma sprendime', DL('$P_{XYZT}$')),
                 'by': ('Priskyrimas, pagal kurį pradinė teiginio forma susiveda į galutinę', DL('Figūros $X$ perimetras žymimas: $P_X$'))},
     'Ifthen': {'n': ('Sprendimo žingsnio numeris', 'Numeriai nuo 7'),
                'fr': ('Teiginių grupė, naudojama atlikti sprendimo žingsniui','(11, 12, 13, 14)'),
                'carrier':('Nuoseklus sprendimo žingsnio užrašymas', DL(r'$P_{XYZT}=XY+ZT+XY+ZT=\frac{x}{2}+\frac{x}{2}+\frac{y}{2}+\frac{y}{2}=x+y$')),
                'by':('Teiginys, kurį taikant išvedimas yra galimas', 'Perimetro apibrėžimas'),
                'to':('Teiginys, išvestas sprendimo žingsnyje', DL('P_{XYZT} = x + y')),
                'ask':('Klausimas, į kurį reikia atsakyti, norint užrašyti sprendimo žingsnį','Kam lygus lygiagretainio XYZT perimetras?'),
                'background':('Papildomos taisyklės, per lengvos kitų taisyklių kontekste, kad būtų įtrauktos į planą arba nebūtinos taikyti', 'Trupmenų su vienodais vardikliais sudėtis')}}

df = nested_df(d)
df.index.set_names(['Klasė', 'Parametras'], inplace=True)
df.columns = ['Kam skirtas parametras', 'Naudojimo pavyzdžiai']
dash_multitable = multiindex_table(df,
    body_column_cell_style = {
    'text-align': 'left',
    'border': '1px solid grey',
    'font-size': '12px',
    'backgroundColor': 'rgb(210, 255, 210)'})



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
apie teste esančių uždavinių sandarą ir moksleivių gebėjimus, nei rankomis įvesti gebėjimų pavadinimai. Kompetencijų pavadinimų įvedinėjimas rankomis 
turės būti pakeistas iš apibrėžimų, taisyklių ir kt., pasirinkimu iš viešai prieinamos rodyklės. 
Tuomet sprendimo žingsniai atrodytų taip:"""
),
add_spacing(html.Img(src=Image.open("assets/solution_demo.jpg"))),
Markdown(r"""### Patobulintos versijos analizė
Norint pasiekti tikslą, reiktų pradėti nuo bent vieno veikiančio kodo pavyzdžio analizės. 
Pavaizduotam sprendimui pateikti buvo pasinaudota kodu:

```python
pr = Problem(
task='Sujungus keturkampio kraštinių vidurio taškus gautas lygiagretainis. Raskite jo perimetrą, jei viena jo 
įstrižainė lygi $x$, o kita $y$',
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
conclusion='Lygiagretainio, gauto sujungus keturkampio kraštinių vidurio taškus, perimetras lygus to keturkampio 
įstrižainių sumai',
author='vadovėlis gimnazijų 1 ir 2 klasėms',
name='Uždavinys 99')
```

Sprendimams aprašyti šiame kode buvo naudojamos prieš tai apibrėžtos klasės, kiekviena sudaryta iš tam 
tikro parametrų rinkinio. Klasės `Assign`, `Rule` ir `Def` skirtos apibūdinti matematiniams žymėjimams, taisyklėms 
ir apibrėžimams. Jos skiriasi tik tuo, kad naudoja skirtingas rodykles: `Assign` klasė rodyklių nenaudoja, 
`Rule` naudoja taisyklių sąrašą, o `Def` - apibrėžimų. Klasės `Known`, `Unknown`, `Ifthen` taip pat panašios pagal 
savo naudojamus atributus. `Ifthen` klasė skirta aprašinėti naujiems teiginiams, deklaruojamiems tam tikruose 
sprendimo žingsniuose, o likusios - pateiktiems ir ieškomiems duomenims.

Pateikto kodo variantas turės būti supaprastintas siekiant paprastumo ir lankstumo duomenų struktūros modifikavimui. 
Kol kas siekiant aiškiai apibrėžti kode naudojamus parametrus remsimės hierarchine lentele:"""),
add_spacing(dash_multitable),
Markdown(r"""* Kuriant tikslų duomenų bazės aprašymą vienas iš pagr. uždavinių - nustatyti kaip sudėtingesni parametrai priklauso nuo klasių. Pvz.:
  * `fr` gali atitikti nurodytą teiginį, nežinomąjį arba teiginių id grupę.
  * `ask` atitinka klausimą, į kurį reikia atsakyti, norint užrašyti sprendimo žingsnį. 
Tačiau sprendžiant tekstinius uždavinius būna sunku pastebėti ir užrašyti tam tikrą sąlygą. Dėl šios priežasties yra 
siūloma `ask` parametrą kiek galima dažniau įtraukti į `Known` klasę (kelti klausimą, kaip užrašyti sąlygoje 
nurodytus duomenys), tačiau ne visuose tekstiniuose uždaviniuose tai įmanoma įgyvendinti.
  * `carrier` parametras prasmingas tada, kai yra `ask` parametras. Jis skirtas parodyti nuoseklų atsakymo į 
tam tikrą klausimą procesą. Tačiau, jei reikia atsakyti į klausimą, kaip pažymėti sąlygoje nurodytus duomenis, žymėjimo
proceso aiškinimas nėra prasmingas, todėl `carrier` parametras tampa nebūtinas.
  * `background` parametro duomenys labai dažnai yra apibrėžiami tik intuityviai. Jei tikimasi, kad uždavinio sprendėjui
tam tikros sprendimo žingsnio dalys privalo būti akivaizdžios be išvedimo, tai į `background` dalį yra įvedamos tik 
taisyklių, kuriomis tos dalys remiasi, pavadinimai. Jei tikimasi kitaip, tai tuomet sprendimo žingsnis turėtų būti
skeliamas į daugiau dalių, tas taisykles priskiriant tų dalių `fr` atributams.
* Reikėtų daugiau pavyzdžių, kad būtų galima kategorizuoti išvedimo taisykles. Preliminarus kategorijų sąrašas:
  * **Taisyklė, savybė ar teorema**
  * **Išvada** iš anksčiau spręsto uždavinio
  * **Konstruktas**, pvz.:
    * Jei skaičius $y$ yra dvigubai didesnis už $x$, tai rašome: $y = 2x$
    * Jei teatre yra 20 eilių po 30 sėdimų vietų, tai teatre yra 600 eilių.
    * Kiti aritmetinių veiksmų subkonstruktai, apžvelgti įvairiuose šaltiniuose.
      * [Daugybos subkonstruktų apžvalga](https://roomtodiscover.com/meanings-of-multiplication/)
      * [Visų aritmetinių veiksmų apžvalga](https://talpykla.elaba.lt/elaba-fedora/objects/elaba:107118246/datastreams/MAIN/content)
  * **Žymėjimas**, pvz. jei kampas $A$ lygus $60^0$, tai žymime: $\angle A = 60^o$
  * **Procesas**, pvz. procedūrų rinkinys, taikomas iš tam tikros lygties gauti sprendinį
  * **Realaus pasaulio kontekstas**, pvz. jei iš skirtingų vietų pajudėję žmonės susitiko pusiaukelėje, 
  tai iki susitikimo jie užtruko vienodai laiko.
  
* Vėliau bus galima pasvarstyti ir apie duomenų bazių valdymo sistemų teorijoje naudojamą
esybių-ryšių diagramą ir duomenų bazės schemą. Šių diagramų pavyzdžius galima peržiūrėti MIF duomenų bazių valdymo 
sistemų laboratorinio darbo sprendime 
[GitHub nuorodoje](https://nbviewer.org/github/loijord/DBVS/blob/master/DBVS2.ipynb) """)
])

