from dash import dcc, html
from PIL import Image
#)

content = html.Div([
    dcc.Markdown(r"""# Duomenų sistema, aprašanti uždavinius
Spręsdami bet kokias iškilusias problemas žmonės yra linkę samprotauti pagal 
[Toulmino argumentacijos modelį](https://en.wikipedia.org/wiki/Stephen_Toulmin#The_Toulmin_model_of_argument):

![](https://owl.purdue.edu/owl/general_writing/academic_writing/historical_perspectives_on_argumentation/images/20190305Toulmin4.jpg)

Aprašinėjant matematinius sprendimus ant popieriaus pilnai pakanka iš tam tikrų faktų (facts) 
išvesti teiginius (claims) ir juos pagrįsti (warrants). Likusiais procesais (backing, rebuttal, qualifier) 
būtina operuoti prieš aprašant sprendimą. Trumpai tariant, sprendimo procesas susideda iš dviejų dalių:
* Euristinio samprotavimo - intuityvios mąstymo dalies, kuomet bandome sugalvoti sprendimo būdų
* Dedukcinio samprotavimo - mąstymo dalies, kai sprendimas apibūdinimas naudojant tvirtus nuoseklius 
tam tikrų teiginių pagrindimus.

2017/18 metais supratau, kad norint aprašyti bet kurio matematinio uždavinio sprendimą, 
iš esmės užtektų jį ,,sujungti" iš tokių dalių: 

$\boxed{\text{Vienas teiginys}} \stackrel{\begin{array}{c}\boxed{\text{Taisyklė}} \\ 
\big\downarrow \end{array}}{\longrightarrow} \boxed{\text{Kitas teiginys}}$

Kaip pavyzdį paėmiau nagrinėti Pitagoro teoremos įrodymą ir gavau tokią schemą:""",
                 mathjax=True, style={'width': '60%'}),
html.Img(src=Image.open("assets/pitagoro_demo.png"), style={'width': '60%'}),
dcc.Markdown(r"""Vėliau taip pat pagal šį modelį nubrėžiau lygybės 
$(a^n)^m = a^{nm}$ įrodymo schemą:""", mathjax=True, style={'width': '60%'}),
html.Img(src=Image.open("assets/laipsniu_demo.png"), style={'width': '60%'}),
dcc.Markdown(r"""Dar vėliau paaiškėjo, kad šis modelis nėra toks lankstus, kaip atrodo. Taikant siūlomą būdą aprašyti sprendimus kiekviename uždavinyje kildavo daug klausimų dėl 
teiginių ir taisyklių užrašymų. Keletas iškilusių sunkumų pavyzdžių: 
* Jei duota, kad $a+b=2$ ir $a=1$, tai pagal tam tikrą taisyklę gausime $b=1$. Šiuo atveju norint aprašyti tai, kas duota,
prireiktų naudoti komplikuotą teiginio užrašymą: $\begin{cases} a+b=2 \\ a=1 \end{cases}$. Jei taip aprašomų teiginių 
sprendime pasitaiko daug, schema tampa perpildyta. 
* Pasitaiko, kad dalis vieną teiginį sudarančių lygybių priklauso kitam kurioje nors sprendimo dalyje taikomam teiginiui. 
Tokiu atveju būtų neišvengiama pasikartojamumo
* Taisyklės taikymas pademonstruotam teiginiui gerokai supaprastėja, jei sprendžiantysis 
mąsto apie tam tikrą kontekstą, pvz. apie šalį, kurioje yra du didmiesčiai, iš kurių dalis yra uostamiesčiai ($a+b=2$), 
o jūra skalauja tik vieną iš jų ($a=1$). Tuomet lygčių arba lygčių sistemų sprendimas nebūtų reikalingas, užtektų teiginį
matyti kita forma, kaip tai įprasta pradinukams. Kyla natūralus klausimas, 
kurį iš šių sprendimo būdų verta rinktis aprašinėjant sprendimą, ir ar šiuos du sprendimo būdus laikyti skirtingais?

2021 m. kovo mėnesį viename iš 
[Matematikos švietimo centro](http://mif.vu.lt/lt3/mokslas/projektai/163-lt/institutai/matematikos#centro-veiklos) 
organizuojamų seminarų pristačiau savo tuometinę koncepciją apie mokyklinio matematikos turinio 
sudarymą ir nuoseklų išdėstymą remiantis taikant panašias struktūras surinkta informacija apie dedukcinį ryšį ir 
moksleivių pasiekimus. Skaidrės prieinamos adresu: 

[https://github.com/loijord/matematikos_pamokos/blob/master/kraitis/teorija_to_praktika/skaidruoles.pdf]
(https://github.com/loijord/matematikos_pamokos/blob/master/kraitis/teorija_to_praktika/skaidruoles.pdf)

Skaidrėse įvardijau ir kitus iššūkius:

* Uždavinių su keliais sprendimais aprašymas yra technologiškai kur kas sunkiau įgyvendinamas
* Kai kurie samprotavimo principai yra sunkiai aprašomi. Pavyzdžiui įrodymas prieštaros būdu arba 
*Modus Ponens* loginis principas
 
2022 metų balandį radau lankstesnį būdą pavaizduoti uždavinių sprendimui. 
Kaip pavyzdį nagrinėjau geometrijos uždavinį, kuriame reikia įrodyti, kad sujungus bet kurio keturkampio gretimų 
kraštinių vidurio taškus gausime lygiagretainį:""", mathjax=True, style={'width': '60%'}),
html.Img(src=Image.open("assets/netgraph_demo.jpg"), style={'width': '40%'}),
dcc.Markdown("""Ankstesnėje schemoje rodyklės kartais būdavo nukreipiamos į kitas rodykles taip parodant, 
kad norint pritaikyti tam tikrą sudėtingesnę taisyklę reikia taikyti kitus nesudėtingus teiginius 
ar paprastesnes taisykles. Šiame modelyje susitarta, kad rodyklės gali eiti tik iš vieno teiginio į kitą. 
Kiekvieno uždavinio sprendimą siūloma aprašinėti kaip kryptinį grafą, kurio viršūnių pavadinimai 
yra teiginiai, o briaunų, nukreiptų į tą pačią viršūnę, grupės atitinka, kažkurią vieną taisyklę.

Praėjus mėnesiui pavyko atrasti ir techninį būdą tokius grafus interaktyviai vaizduoti (*žr. Home -> App Gallery -> Interactive Graphs*). Grafai yra plačiai naudojama duomenų struktūra, 
žadanti daug galimybių, tame tarpe ir automatinį sprendimo generavimą naudojant kelio iš duotų duomenų į 
ieškomus duomenis paiešką. Norint taikyti tokius algoritmus būtina turėti tvarkingai aprašytus grafus. 
Štai taip atrodo automatiškai iš pateikto grafo sugeneruotas sprendimas:""",
             mathjax=True, style={'width': '60%'}),
html.Img(src=Image.open("assets/solution_demo.jpg"), style={'width': '60%'}),
dcc.Markdown('''Kitoje dalyje nagrinėsime, kas turėtų įeiti į duomenų bazę, 
pakankamą aprašyti mokyklinės matematikos mokomąją medžiagą ir teikti moksleiviams informaciją apie jų gebėjimus''',
             mathjax=True, style={'width': '60%'})])