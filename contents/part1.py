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
dcc.Markdown(r"""Dar vėliau paaiškėjo, kad šis modelis nėra toks lankstus, kaip atrodo. 
Nors jis ir leidžia matyti duotus duomenis ir taikomas taisykles, tačiau dažnai yra sunku atskirti, 
kaip reiktų užrašyti faktus ir taisyklę. Pvz. jei $a+b=2$ ir gavome, jog $a=1$, tai pagal tam tikrą taisyklę $b=1$. 
Faktai tampa užrašomais sudėtingai: $\begin{cases} a+b=2 \\ a=1 \end{cases}$. 
Jei tokių faktų susidaro daug, schema tampa perpildyta. Būna, kad dalis teiginių gali 
priklausyti vienam faktui, o dalis kitam. Be to, minėtas faktas taptų suprantamas daug paprasčiau, jei sprendžiantysis 
mąsto apie tam tikrą situaciją, pvz. apie šalį, kurioje yra du didmiesčiai ($a+b=2$), o prie jūros yra vienas iš jų ($a=1$).

2022 metais radau lankstesnį būdą pavaizduoti uždavinių sprendimui. 
Kaip pavyzdį nagrinėjau geometrijos uždavinį, kuriame reikia įrodyti, kad sujungus bet kurio keturkampio gretimų 
kraštinių vidurio taškus gausime lygiagretainį:""", mathjax=True, style={'width': '60%'}),
html.Img(src=Image.open("assets/netgraph_demo.jpg"), style={'width': '40%'}),
dcc.Markdown("""Ankstesnėje schemoje rodyklės kartais būdavo nukreipiamos į kitas rodykles taip parodant, 
kad norint pritaikyti tam tikrą sudėtingesnę taisyklę reikia žinoti tam tikrus nesudėtingus teiginius 
ar paprastesnes taisykles. Šiame modelyje rodyklės gali eiti tik iš vieno teiginio į kitą. 
Visos į tam tikrą teiginį einančios rodyklės nurodo būtinąsias sąlygas pritaikyti jam pagrįsti.
Kiekvieno uždavinio sprendimą siūloma aprašinėti kaip kryptinį grafą, kurio viršūnių pavadinimai 
yra tarpiniai teiginiai, o briaunų pavadinimai atitinka taikomų taisyklių pavadinimus.

Taip pat 2022 metais pavyko atrasti būdą tokius grafus interaktyviai vaizduoti naudojant Python
(*žr. App Gallery -> Interactive Graphs*). Grafai yra plačiai naudojama duomenų struktūra, 
žadanti daug galimybių, tame tarpe ir automatinį sprendimo generavimą naudojant kelio iš duotų duomenų į 
ieškomus duomenis paiešką. Štai taip atrodo automatiškai iš pateikto grafo sugeneruotas sprendimas""",
             mathjax=True, style={'width': '60%'}),
html.Img(src=Image.open("assets/solution_demo.jpg"), style={'width': '60%'}),
dcc.Markdown('''Kitoje dalyje nagrinėsim, kas turėtų įeiti į šią duomenų struktūrą, 
kad ji būtų pakankama aprašyti mokyklinės matematikos mokomąją medžiagą ir kuo 
tiksliau nustatyti moksleivių gebėjimus''', mathjax=True, style={'width': '60%'})])