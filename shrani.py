import pandas as pd


def shrani_v_csv(macji_podatki):

    df = pd.DataFrame(macji_podatki)
    csv_filename = 'zajete_macke.csv'
    df.to_csv(csv_filename, index=False, encoding='utf-8')

    print(f"Podatki uspešno naloženi na '{csv_filename}'")