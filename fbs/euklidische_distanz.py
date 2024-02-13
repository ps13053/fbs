import pandas as pd
import numpy as np


def euklidische_distanz(fall_a, fall_b):
    # Berechnet die Euklidische Distanz zwischen zwei Fällen
    return np.sqrt(np.sum((fall_a - fall_b) ** 2))


def retrieve(fallbasis, neuer_fall, anzahl):
    ergebnis_spalte = fallbasis.columns[-1]  # Bestimme den Namen der letzten Spalte dynamisch
    fallbasis_merkmale = fallbasis.drop(['Fallnummer', ergebnis_spalte], axis=1).to_numpy()
    distanzen = [euklidische_distanz(neuer_fall, fall) for fall in fallbasis_merkmale]
    aehnlichste_idxs = np.argsort(distanzen)[:anzahl]
    return fallbasis.iloc[aehnlichste_idxs]


def reuse(aehnlichste_faelle):
    ergebnisse_haeufigkeit = aehnlichste_faelle['Regen?'].value_counts()
    neues_ergebnis = ergebnisse_haeufigkeit.idxmax()
    return neues_ergebnis


def revise(vorgeschlagenes_ergebnis):
    antwort = input(f"Ist das Ergebnis '{vorgeschlagenes_ergebnis}' korrekt? (ja/nein): ")
    return antwort.lower() == 'ja'


def retain(pfad, fallbasis, neuer_fall, neues_ergebnis):
    neuer_fallnummer = fallbasis['Fallnummer'].max() + 1
    neuer_fall_df = pd.DataFrame([neuer_fall], columns=fallbasis.columns.drop(['Fallnummer', 'Regen?']))
    neuer_fall_df['Fallnummer'] = neuer_fallnummer
    neuer_fall_df['Regen?'] = neues_ergebnis
    neue_fallbasis = fallbasis._append(neuer_fall_df, ignore_index=True)
    neue_fallbasis.to_csv(pfad, index=False)
    print(f"Neuer Fall wurde zur Fallbasis hinzugefügt: {neuer_fall_df.to_dict(orient='records')[0]}")
