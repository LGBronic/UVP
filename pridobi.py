import requests

headers = {"User-Agent": "Mozilla/5.0"}
BASE_URL = 'https://www.nawt.org.uk'

def pridobi_htmlje(st_strani):
    for x in range(1, st_strani + 1):

        url = 'https://www.nawt.org.uk/rehoming/cats/?page='
        odgovor = requests.get(url+str(x), headers = headers)
        #print(odgovor.content)

        if odgovor.status_code != 200:
            print("Napaka", x)
            continue

        vsebina = odgovor.text
        with open(f"stran{x}.html", "w", encoding = 'utf-8') as dat:
            dat.write(vsebina)

