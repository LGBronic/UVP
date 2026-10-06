# ANALIZA MAČK V ANGLEŠKIH ZAVETIŠČIH
## OPIS
Program zajame podatke s spletne strani https://www.nawt.org.uk, kjer so objavljene živali v zavetiščih, ki iščejo svoj dom, jih shrani in analizira. Iz več strani izlušči osnovne podatke o vsaki mački, pri čemer si pomaga s knjižnico BeautifulSoup. Podatke shrani v datoteko, ki jo uporabi za nadaljnjo analizo. 
## STRUKTURA
1. pridobi.py - prenese shrani HTML strani s seznama mačk (`requests`) in jih shrani
2. izlusci.py - prebere shranjene strani in z `BeautifulSoup` izlušči podatke o vsaki mački(ime, lokacija (zavetišče), starost, spol, pasma, posvojitev v paru, razpoložljivost). Za vsako mačko obišče še njeno podstran in doda velikost ter podatek, ali živi z otroki. Te podatke zbere v seznam.
3. shrani.py - vzame seznam in ga pretvori v `pandas` tabelo, ki jo shrani v datoteko zajete_macke.csv
4. main.py - glavna datoteka, preko katere se projekt sploh zažene (po vrsti opravi zgornje korake). Zažene se z ukazom python main.py.
### REZULTATI ANALIZE
Rezultati analize, pojasnila in ugotovitve se nahajajo v datoteki analiza.ipynb.
### UPORABLJENE KNJIŽNICE
Pred zagonom je treba nemestiti uporabljene knjižnice:
pip install requests beautifulsoup4 pandas matplotlib jupyter.
