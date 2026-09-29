import pridobi
import izlusci
import shrani


STEVILO_STRANI = 3
pridobi.pridobi_htmlje(STEVILO_STRANI)
macji_podatki = izlusci.izlusci_podatke(STEVILO_STRANI)
shrani.shrani_v_csv(macji_podatki)