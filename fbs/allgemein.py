import pandas as pd


def read_csv(pfad):
    return pd.read_csv(pfad)


def reuse(aehnlichste_faelle, ziel_spalte):
    ergebnisse_haeufigkeit = aehnlichste_faelle[ziel_spalte].value_counts()
    neues_ergebnis = ergebnisse_haeufigkeit.idxmax()
    return neues_ergebnis


def revise(vorgeschlagenes_ergebnis):
    antwort = input(f"Soll der neue Fall mit dem bestimmten Ergebnis '{vorgeschlagenes_ergebnis}'"
                    f"der Fallbasis hinzugefügt werden? (ja/nein): ")
    return antwort.lower() == 'ja'


def retain(datei_pfad, fallbasis, neuer_fall, neues_ergebnis):
    neue_fallnummer = fallbasis['Fallnummer'].max() + 1
    # Nimmt alle Spalten außer 'Fallnummer' und der letzten Spalte
    merkmale_spalten = fallbasis.columns[:-1].drop(['Fallnummer'])
    neuer_fall_df = pd.DataFrame([neuer_fall], columns=merkmale_spalten)
    neuer_fall_df['Fallnummer'] = neue_fallnummer
    # Zugriff auf den Namen der letzten Spalte und Setzen des Ergebnisses
    letzte_spalte_name = fallbasis.columns[-1]
    neuer_fall_df[letzte_spalte_name] = neues_ergebnis
    neue_fallbasis = fallbasis._append(neuer_fall_df, ignore_index=True)
    neue_fallbasis.to_csv(datei_pfad, index=False)
    print(f"Neuer Fall wurde zur Fallbasis hinzugefügt: {neuer_fall_df.to_dict(orient='records')[0]}")


