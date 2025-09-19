# Zugriff auf `db_connection.py` von `user_model.py`

Angenommen, deine Projektstruktur sieht so aus:

    project_root/
    │── main.py
    │── database/
    │   └── db_connection.py
    │── models/
    │   └── user_model.py

Du möchtest `db_connection.py` innerhalb von `user_model.py` verwenden.

------------------------------------------------------------------------

## Schritt 1: `__init__.py` hinzufügen

Stelle sicher, dass sowohl `database/` als auch `models/` eine leere
Datei namens `__init__.py` enthalten, damit Python sie als Pakete
erkennt:

    database/
       ├── __init__.py
       └── db_connection.py
    models/
       ├── __init__.py
       └── user_model.py

------------------------------------------------------------------------

## Schritt 2: Import mit absolutem Pfad

In `user_model.py`:

``` python
# user_model.py
from database.db_connection import Database

class User:
    def __init__(self, name):
        self.name = name

    def save(self):
        db = Database()
        db.connect()
        print(f"Benutzer {self.name} in Datenbank gespeichert")
```

------------------------------------------------------------------------

## Schritt 3: Beispiel `db_connection.py`

``` python
# db_connection.py
class Database:
    def connect(self):
        print("Datenbankverbindung hergestellt!")
```

------------------------------------------------------------------------

## Schritt 4: Ausführen vom Projekt-Root

Starte dein Skript **immer aus dem Root-Ordner**:

``` bash
cd project_root
python main.py
```

oder zum Testen direkt:

``` bash
python models/user_model.py
```

------------------------------------------------------------------------

 **Wichtig**: Wenn du versuchst, `user_model.py` direkt aus dem
`models/`-Ordner zu starten, schlägt der Import fehl
(`ModuleNotFoundError: No module named 'database'`).\
Das passiert, weil Python den aktuellen Ordner als Root setzt.\
**Lösung:** Immer vom obersten Verzeichnis (`project_root`) aus starten.

----------------------------------------------------------------------
