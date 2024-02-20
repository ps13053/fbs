from fbs import hamming_distanz as hd
from fbs import allgemein as fbs

# Laden der Fallbasis
fallbasis_path = 'fallbasen/kino.csv'
fallbasis = fbs.einlesen_csv(fallbasis_path)

neuer_fall = [0, 1, 1, 0, 0, 0, 1, 0, 0, 1]
aehn_faelle = hd.selektieren(fallbasis, neuer_fall, 3)
ergebnis = fbs.wiederverwenden(aehn_faelle, 'Kino_besuch?')
if fbs.ueberpruefen(ergebnis):
    fbs.aufnehmen(fallbasis_path, fallbasis, neuer_fall, ergebnis)






