import numpy as np


def hamming_distance(fall_a, fall_b):
    # berechnen der hamming distanz zwischen zwei Fällen
    distance = sum(merkmal_a != merkmal_b for merkmal_a, merkmal_b in zip(fall_a, fall_b))
    return distance


def selektieren(fallbasis, neuer_fall, anzahl):
    # Bestimmung des Namens der letzten Spalte dynamisch
    ergebnis_spalte = fallbasis.columns[-1]
    # begrenzung auf Merkmale
    fallbasis_merkmale = fallbasis.drop(['Fallnummer', ergebnis_spalte], axis=1).to_numpy()
    # Berechne die Hamming-Distanz zwischen dem neuen Fall und allen Fällen in der Fallbasis
    distanzen = [hamming_distance(neuer_fall, fall) for fall in fallbasis_merkmale]
    # Finde die Indizes der 'Anzahl' ähnlichsten Fälle
    aehnlichste_idxs = np.argsort(distanzen)[:anzahl]
    # Stelle sicher, dass aehnlichste_idxs eine Liste oder ein Array von ganzen Zahlen ist
    aehnlichste_idxs = list(aehnlichste_idxs)
    # Gib die ähnlichsten Fälle zurück
    return fallbasis.iloc[aehnlichste_idxs]
