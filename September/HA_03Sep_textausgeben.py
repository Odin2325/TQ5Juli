def PythonFragentxt_lesen(PythonFragen):
    try:
        with open(PythonFragen, 'r', encoding='utf-8') as datei:
            inhalt = datei.read()
            print("Inhalt der Datei:")
            print(inhalt)
    except FileNotFoundError:
        print(f"Die Datei '{dateipfad}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")