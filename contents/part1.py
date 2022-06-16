from dash import dcc, html
import dash_bootstrap_components as dbc
from utils.utils import Markdown, star_ranking, add_spacing #force to use mathjax by default
from PIL import Image
#)
content = html.Div([
    html.H1('Duomenų sistema, aprašanti uždavinius'),
    Markdown(r"""## Tikslas
***Įvertinti, kokia duomenų struktūra būtų tinkamiausia aprašinėti teoremų įrodymams, 
procedūrų ir taisyklių paaiškinimams bei uždavinių sprendimams.***"""),
    Markdown(r"""## Kiek pasiektas tikslas:"""),
    star_ranking((1, 1, 1, 1, 0)),
    html.Br(),
    Markdown(r"""## Kas nuveikta:
* 2017/18 metais išbandytas struktūra, paremta, supaprastintą Toulmino argumentacijos modeliu
* Paaiškėjo, kad ši struktūra nepakankamai lanksti norint ja remtis kuriant duomenų bazes
* Vėliau buvo apsiribota atskirų sprendimo žingsnių užrašinėjimu rankomis
* 2022 metų balandį pavyko realizuoti kitokią struktūrą, reprezentuojamą kryptiniais grafais"""),
    html.Hr(),
    Markdown(r"""### Toulmino argumentacijos modelis
Spręsdami bet kokias iškilusias problemas žmonės yra linkę samprotauti pagal 
[Toulmino argumentacijos modelį](https://en.wikipedia.org/wiki/Stephen_Toulmin#The_Toulmin_model_of_argument):

![](https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/images/20190305Toulmin4.jpg)

Aprašinėjant matematinius sprendimus ant popieriaus pilnai pakanka iš tam tikrų faktų (Grounds) 
išvesti teiginius (Claims) ir įvardyti, kaip jie grindžiami (Warrants). Likę procesai (Backing, Rebuttal, Qualifier) 
sprendimo užrašyme dažniausiai neatsispindi, tačiau yra svarbi samrotavimo dalis. Apibendrinus:

* $[\text{Backing} +\text{Rebuttal} + \text{Qualifier}] = \text{Euristinis samprotavimas}$ (artima matematinei intuicijai)
* $[\text{Grounds } \& \text{ Warrants} \longrightarrow \text{Claims}] = \text{Dedukcinis samprotavimas}$ (artima griežtam pagrindimui)."""),
    Markdown(r"""### Supaprastintas Toulmino argumentacijos modelis
Norint aprašyti bet kurio matematinio uždavinio sprendimą, iš esmės užtektų jį ,,sujungti" iš tokių dalių: 

$\boxed{\text{Vienas teiginys}} \stackrel{\begin{array}{c}\boxed{\text{Taisyklė}} \\ 
\big\downarrow \end{array}}{\longrightarrow} \boxed{\text{Kitas teiginys}}$"""),

    Markdown(r"""**Pavyzdys 1.** Pitagoro teoremos įrodymo pavaizdavimas remiantis šia struktūra:"""),
    add_spacing(html.Img(src=Image.open("assets/pitagoro_demo.png"))),
    Markdown(r"""**Pavyzdys 2.** Lygybės $(a^n)^m = a^{nm}$ įrodymo schema:"""),
    add_spacing(html.Img(src=Image.open("assets/laipsniu_demo.png"))),

    Markdown(r"""### Supaprastinto Toulmino argumentacijos modelio taikymas"""),
    Markdown(r"""Su laiku paaiškėjo, kad šis modelis nėra toks lankstus, kaip atrodo. 
Taikant siūlomą būdą aprašyti sprendimus kiekviename uždavinyje kildavo daug klausimų dėl 
teiginių ir taisyklių užrašymų. Keletas iškilusių sunkumų pavyzdžių: 
* Jei duota, kad $a+b=2$ ir $a=1$, tai pagal tam tikrą taisyklę gausime $b=1$. Šiuo atveju norint aprašyti tai, kas duota,
prireiktų naudoti komplikuotą teiginio užrašymą: $\begin{cases} a+b=2 \\ a=1 \end{cases}$. Jei taip aprašomų teiginių 
sprendime pasitaiko daug, `schema tampa perpildyta`. 
* Pasitaiko, kad dalis vieną teiginį sudarančių lygybių priklauso kitam kurioje nors sprendimo dalyje taikomam teiginiui. 
Tokiu atveju `schemoje neišvengiama pasikartojimų`.
* Taisyklės taikymas pademonstruotam teiginiui gerokai supaprastėja, jei sprendžiantysis 
mąsto apie tam tikrą kontekstą, pvz. apie šalį, kurioje yra du didmiesčiai, iš kurių dalis yra uostamiesčiai ($a+b=2$), 
o jūra skalauja tik vieną iš jų ($a=1$). Tuomet lygčių arba lygčių sistemų sprendimas nebūtų reikalingas, užtektų teiginį
matyti kita forma, kaip tai įprasta pradinukams. Tampa nelengva nuspręsti, `kada du sprendimo būdai laikomi skirtingais?`

2021 m. kovo mėnesį viename iš 
[Matematikos švietimo centro](http://mif.vu.lt/lt3/mokslas/projektai/163-lt/institutai/matematikos#centro-veiklos) 
organizuojamų seminarų pristačiau savo tuometines idėjas, kaip būtų galima sudaryti ir nuosekliai išdėstyti mokyklinį 
matematikos turinį remiantis matematinių taisyklių tarpusavio ryšiu pagal supaprastintą Toulmino modelį ir 
moksleivių gebėjimais taikyti schemose įtrauktas taisykles. Skaidrės prieinamos adresu: 

[https://github.com/loijord/matematikos_pamokos/blob/master/kraitis/teorija_to_praktika/skaidruoles.pdf]
(https://github.com/loijord/matematikos_pamokos/blob/master/kraitis/teorija_to_praktika/skaidruoles.pdf)

Skaidrėse įvardijau ir kitus iššūkius:

* Uždavinių su `keliais sprendimais` aprašymas yra technologiškai kur kas sunkiau įgyvendinamas
* `Sudėtingesni samprotavimo principai` yra sunkiau aprašomi. Pavyzdžiui įrodymas prieštaros būdu arba 
*Modus Ponens* loginis principas"""),
 
    Markdown(r"""Kryptinių grafų modelis
Dalis `paryškintų` problemų išsisprestų, jei kiekvieną sprendimo žingsnio taisyklę 
vaizduotume kaip kryptinio grafo briaunų rinkinį, išeinantį iš grupės teiginių ir nukreiptų į vienodą išvestinį teiginį.
Šioje struktūroje susitarta, kad rodyklės negali eiti į briaunas, o tik į viršūnes, 
todėl ją galima laikyti pilnaverčiu grafu"""),

    Markdown(r"""**Pavyzdys 3.** Reikia įrodyti, kad sujungus bet kurio keturkampio gretimų 
kraštinių vidurio taškus gausime lygiagretainį:"""),
add_spacing(html.Img(src=Image.open("assets/netgraph_demo.jpg"))),

    Markdown(r"""Sekcijoje (Home -> App Gallery -> Interactive Graphs) siūlomas sprendimas, kaip šį grafą pavaizduoti įskaitomiau."""),

    Markdown(r"""Ieškant būdų, kaip padėti moksleiviams išmokti tam tikrą temą, tvarkingas grafų aprašymas atvertų daug galimybių:
* Tiriant pasikartojančius pografius būtų galima nustatyti matematinių objektų, taisyklių ar jų rinkinių 
pasiskirstymą
* Leistų efektyviai identifikuoti moksleivio spragas
* Identifikavus spragas leistų automatiškai nukreipti į konkrečią mokymosi medžiagą.
* Uždavinių sprendimus generuoti automatiškai"""),
    Markdown(r"""**Pavyzdys 4.** Automatiškai sugeneruoto sprendimas:"""),
    add_spacing(html.Img(src=Image.open("assets/solution_demo.jpg")))
])