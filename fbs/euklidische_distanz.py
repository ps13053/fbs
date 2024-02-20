import numpy as np


def euklidische_distanz(fall_a, fall_b):
    # Berechnet die Euklidische Distanz zwischen zwei Fällen
    return np.sqrt(np.sum((fall_a - fall_b) ** 2))


def selektieren(fallbasis, neuer_fall, anzahl):
    # Bestimmung des Namens der letzten Spalte dynamisch
    ergebnis_spalte = fallbasis.columns[-1]
    #  Begrenzung auf die Merkmale
    fallbasis_merkmale = fallbasis.drop(['Fallnummer', ergebnis_spalte], axis=1).to_numpy()
    # Berechnung der euklidischen Distanzen
    distanzen = [euklidische_distanz(neuer_fall, fall) for fall in fallbasis_merkmale]
    # bestimmung der ähnlichsten Fälle
    aehnlichste_idxs = np.argsort(distanzen)[:anzahl]
    return fallbasis.iloc[aehnlichste_idxs]
