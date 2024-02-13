import pandas as pd
import numpy as np


def hamming_distance(fall_a, fall_b):
    distance = sum(merkmal_a != merkmal_b for merkmal_a, merkmal_b in zip(fall_a, fall_b))
    return distance


def retrieve(fallbasis, neuer_fall, anzahl):
    # Entferne die Spalten 'Fallnummer' und 'Kino_besuch?' und konvertiere in numpy array
    ergebnis_spalte = fallbasis.columns[-1]  # Bestimme den Namen der letzten Spalte dynamisch
    fallbasis_merkmale = fallbasis.drop(['Fallnummer', ergebnis_spalte], axis=1).to_numpy()
    # Berechne die Hamming-Distanz zwischen dem neuen Fall und allen Fällen in der Fallbasis
    distanzen = [hamming_distance(neuer_fall, fall) for fall in fallbasis_merkmale]
    # Finde die Indizes der 'Anzahl' ähnlichsten Fälle
    aehnlichste_idxs = np.argsort(distanzen)[:anzahl]
    # Stelle sicher, dass aehnlichste_idxs eine Liste oder ein Array von ganzen Zahlen ist
    aehnlichste_idxs = list(aehnlichste_idxs)

    # Gib die ähnlichsten Fälle zurück
    return fallbasis.iloc[aehnlichste_idxs]


def reuse(aehnlichste_faelle):
    # Zähle die Häufigkeit der Ergebnisse in den ähnlichsten Fällen
    ergebnisse_haeufigkeit = aehnlichste_faelle['Kino_besuch?'].value_counts()

    # Wähle das häufigste Ergebnis als das Ergebnis für den neuen Fall
    neues_ergebnis = ergebnisse_haeufigkeit.idxmax()

    return neues_ergebnis


def revise(vorgeschlagenes_ergebnis):
    antwort = input(f"Ist das Ergebnis '{vorgeschlagenes_ergebnis}' korrekt? (ja/nein): ")
    return antwort.lower() == 'ja'


def retain(pfad, fallbasis, neuer_fall, neues_ergebnis):
    neue_fallnummer = fallbasis['Fallnummer'].max() + 1
    neuer_fall_df = pd.DataFrame([neuer_fall], columns=fallbasis.columns.drop(['Fallnummer', 'Kino_besuch?']))
    neuer_fall_df['Fallnummer'] = neue_fallnummer
    neuer_fall_df['Kino_besuch?'] = neues_ergebnis
    neue_fallbasis = fallbasis._append(neuer_fall_df, ignore_index=True)
    neue_fallbasis.to_csv(pfad, index=False)
    print(f"Neuer Fall wurde zur Fallbasis hinzugefügt: {neuer_fall_df.to_dict(orient='records')[0]}")
