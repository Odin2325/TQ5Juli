from datetime import datetime

# Klasse für eine Aufgabe
class Aufgabe:
    def __init__(self, beschreibung, faelligkeit, prioritaet, erledigt=False):
        self.beschreibung = beschreibung
        self.faelligkeit = faelligkeit
        self.prioritaet = prioritaet
        self.erledigt = erledigt

    def __str__(self):
        status = "✓" if self.erledigt else " "
        return f"[{status}] {self.beschreibung} | Fällig: {self.faelligkeit} | Priorität: {self.prioritaet}"


# Liste aller Aufgaben
task_liste = []


# Aufgabe hinzufügen
def aufgabe_hinzufuegen():
    beschreibung = input("Aufgabenbeschreibung: ")
    faelligkeit = input("Fälligkeitsdatum (YYYY-MM-DD): ")
    prioritaet = input("Priorität (1-5): ")
    task = Aufgabe(beschreibung, faelligkeit, int(prioritaet))
    task_liste.append(task)
    print("Aufgabe hinzugefügt.\n")


# Aufgaben anzeigen
def aufgaben_anzeigen():
    if not task_liste:
        print("Keine Aufgaben vorhanden.\n")
        return
    for i, aufgabe in enumerate(task_liste):
        print(f"{i + 1}. {aufgabe}")
    print()


# Aufgabe bearbeiten
def aufgabe_bearbeiten():
    aufgaben_anzeigen()
    try:
        nummer = int(input("Nummer der Aufgabe zum Bearbeiten: ")) - 1
        if 0 <= nummer < len(task_liste):
            beschreibung = input("Neue Beschreibung: ")
            faelligkeit = input("Neues Fälligkeitsdatum (YYYY-MM-DD): ")
            prioritaet = input("Neue Priorität (1-5): ")
            task_liste[nummer].beschreibung = beschreibung
            task_liste[nummer].faelligkeit = faelligkeit
            task_liste[nummer].prioritaet = int(prioritaet)
            print("Aufgabe bearbeitet.\n")
        else:
            print("Ungültige Nummer.\n")
    except ValueError:
        print("Ungültige Eingabe.\n")


# Aufgabe löschen
def aufgabe_loeschen():
    aufgaben_anzeigen()
    try:
        nummer = int(input("Nummer der Aufgabe zum Löschen: ")) - 1
        if 0 <= nummer < len(task_liste):
            del task_liste[nummer]
            print("Aufgabe gelöscht.\n")
        else:
            print("Ungültige Nummer.\n")
    except ValueError:
        print("Ungültige Eingabe.\n")


# Aufgabe als erledigt markieren
def aufgabe_erledigen():
    aufgaben_anzeigen()
    try:
        nummer = int(input("Nummer der Aufgabe zum Erledigen: ")) - 1
        if 0 <= nummer < len(task_liste):
            task_liste[nummer].erledigt = True
            print("Aufgabe als erledigt markiert.\n")
        else:
            print("Ungültige Nummer.\n")
    except ValueError:
        print("Ungültige Eingabe.\n")


# Aufgaben sortieren
def aufgaben_sortieren():
    print("Nach welchem Kriterium sortieren?")
    print("1. Fälligkeitsdatum")
    print("2. Priorität")
    auswahl = input("Auswahl (1/2): ")
    if auswahl == "1":
        try:
            task_liste.sort(key=lambda x: datetime.strptime(x.faelligkeit, "%Y-%m-%d"))
            print("Sortiert nach Fälligkeitsdatum.\n")
        except ValueError:
            print("Fehler beim Sortieren. Bitte gültige Datumsangaben verwenden.\n")
    elif auswahl == "2":
        task_liste.sort(key=lambda x: x.prioritaet)
        print("Sortiert nach Priorität.\n")
    else:
        print("Ungültige Auswahl.\n")


# Hauptmenü
def hauptmenue():
    while True:
        print("----- ToDo-Liste -----")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgabe bearbeiten")
        print("3. Aufgabe löschen")
        print("4. Aufgabe als erledigt markieren")
        print("5. Aufgaben anzeigen")
        print("6. Aufgaben sortieren")
        print("7. Beenden")

        auswahl = input("Bitte wählen: ")

        if auswahl == "1":
            aufgabe_hinzufuegen()
        elif auswahl == "2":
            aufgabe_bearbeiten()
        elif auswahl == "3":
            aufgabe_loeschen()
        elif auswahl == "4":
            aufgabe_erledigen()
        elif auswahl == "5":
            aufgaben_anzeigen()
        elif auswahl == "6":
            aufgaben_sortieren()
        elif auswahl == "7":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl.\n")


# Startpunkt
if __name__ == "__main__":
    hauptmenue()
