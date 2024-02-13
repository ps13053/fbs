from fbs import euklidische_distanz as ed
from fbs import allgemein as fbs


# Laden der Fallbasis
pfad = 'fallbasen/regenvorhersage.csv'
fallbasis = fbs.read_csv(pfad)

# Definieren eines neuen Falls (Beispiel)
neuer_fall = [23.0, 70, 1010, 12, 13.407,
              52.520]  # Temperatur, Luftfeuchtigkeit, Luftdruck, Windgeschwindigkeit, Längengrad, Breitengrad

# Die ähnlichsten Fälle finden
aehnlichste_faelle = ed.retrieve(fallbasis, neuer_fall, 3)
print(aehnlichste_faelle)
# Das Ergebnis für den neuen Fall bestimmen
ergebnis = ed.reuse(aehnlichste_faelle)

# Das Ergebnis überprüfen
if ed.revise(ergebnis):
    # Den neuen Fall an die Fallbasis anhängen
    ed.retain(pfad, fallbasis, neuer_fall, ergebnis)
