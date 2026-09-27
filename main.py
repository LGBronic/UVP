import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0"}

macji_podatki = []



for x in range(1, 3):

    url = 'https://www.nawt.org.uk/rehoming/cats/?page='
    odgovor = requests.get(url+str(x), headers = headers)
    #print(odgovor.content)
    soup = BeautifulSoup(odgovor.text, 'html.parser')
    #print(soup)
    rezultati = soup.find_all('div', class_=lambda c: c and 'page-cards__card' in c.split())
    #print(rezultati)
    print(f"Stran:{x}")
    print("Status:",odgovor.status_code)
    print("Končni URL:", odgovor.url)
    print("Št kartic:", len(rezultati))

    for rezultat in rezultati:
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




        macke_info = {
            'ime': ime,
            'na voljo': na_voljo,
            'lokacija': lokacija,
            'starost': meseci,
            'spol': spol,
            'pasma': pasma
        }
        macji_podatki.append(macke_info)
#print(macji_podatki)

print(f"Zajetih {len(macji_podatki)} mack.")

df = pd.DataFrame(macji_podatki)
csv_filename = 'zajete_macke.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8')

print(f"Podatki uspešno naloženi na '{csv_filename}'")