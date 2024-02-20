import pandas as pd


def einlesen_csv(datei_pfad):
    # unter Angabe eines Pfades(datei_pfad) wird die angegebene CSV-Datei als Pandas Dataframe eingelesen
    return pd.read_csv(datei_pfad)


def wiederverwenden(selektierte_faelle, ziel_spalte):
    # auf Basis der selektierten Fälle wird ein neues Ergebnis vorgeschlagen
    ergebnisse_haeufigkeit = selektierte_faelle[ziel_spalte].value_counts()
    # das neue Ergebnis ist das, welches am häufigsten unter den selektierten Fällen vorkam
    vorgeschlagenes_ergebnis = ergebnisse_haeufigkeit.idxmax()
    return vorgeschlagenes_ergebnis


def ueberpruefen(vorgeschlagenes_ergebnis):
    # manuelle Abfrage beim nutzer
    antwort = input(f"Soll der neue Fall mit dem bestimmten Ergebnis '{vorgeschlagenes_ergebnis}'"
                    f"der Fallbasis hinzugefügt werden? (ja/nein): ")
    # es wird True zurückgegeben, falls die Antwort "Ja" ist
    return antwort.lower() == 'ja'


def aufnehmen(datei_pfad, fallbasis, neuer_fall, neues_ergebnis):
    # die neue Fallnummer wird auf basis der höchsten existierenden Fallnummer bestimmt
    neue_fallnummer = fallbasis['Fallnummer'].max() + 1
    # Nimmt alle Spalten außer 'Fallnummer' und der letzten Spalte
    merkmale_spalten = fallbasis.columns[:-1].drop(['Fallnummer'])
    # Erstellen eines dataframes mit merkmale_spalten
    neuer_fall_df = pd.DataFrame([neuer_fall], columns=merkmale_spalten)
    neuer_fall_df['Fallnummer'] = neue_fallnummer
    # Zugriff auf den Namen der letzten Spalte und Setzen des Ergebnisses
    letzte_spalte_name = fallbasis.columns[-1]
    # setzen von dem neuen Ergebnis
    neuer_fall_df[letzte_spalte_name] = neues_ergebnis
    # hinzufügen des neuen Falls zur Fallbasis
    neue_fallbasis = fallbasis._append(neuer_fall_df, ignore_index=True)
    # speichern der neuen Fallbasis als CSV-datei
    neue_fallbasis.to_csv(datei_pfad, index=False)
    # Bestätigung, dass der Fall hinzugefügt wurde
    print(f"Neuer Fall wurde zur Fallbasis hinzugefügt: {neuer_fall_df.to_dict(orient='records')[0]}")


