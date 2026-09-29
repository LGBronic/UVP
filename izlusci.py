from bs4 import BeautifulSoup
import re
import requests

headers = {"User-Agent": "Mozilla/5.0"}
BASE_URL = 'https://www.nawt.org.uk'

macji_podatki = []

def dobi_povezavo(rezultat):
    a = rezultat.find('a', class_='btn btn--secondary btn--med')
    if a is None:
        return None
    href = a.get('href')
    if href is None:
        return None
    return BASE_URL + href

def pridobi_podrobnosti(povezava):
    odgovor = requests.get(povezava, headers= headers)
    if odgovor.status_code != 200:
        return {'velikost': '',
                'živi z odraslimi': ''
                }
    
    vsebina = odgovor.text
    soup = BeautifulSoup(vsebina, 'html.parser')
    ena_macka = soup.find('div', class_ ='animal-stats')
    besedilo = ena_macka.get_text(separator = ' ', strip = False)
    besede = re.findall(r'\w+', besedilo)

    velikost = ''
    for i in range(len(besede)):
        if besede[i] == 'Small' or besede[i] == 'Medium' or besede[i] == 'Large':
            velikost = besede[i]

    živi_z_otroki = ''
    for i in range(len(besede)):
        if besede[i-1] == 'Adults':
            živi_z_otroki = 'ne'
        if besede[i-1] == 'children':
            živi_z_otroki = 'da'
    return {'velikost': velikost,
            'živi z otroki': živi_z_otroki
                }

    



def analiza_macke(rezultat):
    h3 = rezultat.find('h3')
    ime = h3.get_text(separator="", strip = False).replace("\n", "")

    p = rezultat.find('p')
    na_voljo = p.get_text(separator="", strip = False).replace("\n", "")

    l = rezultat.find('p', class_ = 'page-cards__category')
    lokacija = l.get_text(separator="", strip=False).replace("\n", "")

    vsi_p = rezultat.find_all('p')[2]
    podatki = vsi_p.get_text(separator=' ', strip = False)

        #print(podatki)
        #želimo ločiti besede v podatkih (torej loči z znaki, ki niso besede)
    besede = re.findall(r'\w+', podatki)
        #print(besede)

    leta = 0
    mesec = 0
    for i in range(len(besede)):
        if besede[i] == 'month' or besede[i] == 'months':
            mesec = besede[i-1]
        if besede[i] == 'years' or besede[i] == 'year':
            leta = besede[i-1]
    meseci = int(leta) * 12 + int(mesec)
     
    spol = ''
    if 'Female' in besede:
        spol = 'Female'
    if 'Male' in besede:
        spol = 'Male'
     
     
    pasma = ''
    for i in range(len(besede)):
        if besede[i] == 'Male' or besede[i] == 'Female':
            pasma = ' '.join(besede[i+1:])
     
    posvojitev_v_paru = 'ne'
    if '(' in ime or '&' in ime:
        posvojitev_v_paru = 'da'
        ime = ime.split()[0]

     
    return {
        'ime': ime,
        'na voljo': na_voljo,
        'lokacija': lokacija,
        'starost': meseci,
        'spol': spol,
        'pasma': pasma,
        'posvojitev v paru':posvojitev_v_paru
             }
     


def izlusci_podatke(st_strani):
    for x in range(1, st_strani + 1):
        with open(f"stran{x}.html", encoding='utf-8') as dat:
            vsebina = dat.read()
            soup =  BeautifulSoup(vsebina, 'html.parser')
            rezultati = soup.find_all('div', class_=lambda c: c and 'page-cards__card' in c.split())

            
            for rezultat in rezultati:
                macke_info = analiza_macke(rezultat)
                povezava = dobi_povezavo(rezultat)

                macke_info.update(pridobi_podrobnosti(povezava))
                macji_podatki.append(macke_info)
            print(f"Zajetih {len(macji_podatki)} mack.")
    return macji_podatki                                                          
