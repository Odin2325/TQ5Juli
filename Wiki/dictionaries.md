# Python-Dictionaries – Erklärung und wichtige Funktionen

Ein **Dictionary** (Wörterbuch) ist eine Datenstruktur in Python, die Informationen als **Schlüssel-Wert-Paare** speichert.  
Man kann damit z. B. Namen mit Telefonnummern, Produkte mit Preisen oder Wörter mit Häufigkeiten verknüpfen.

---

## 1. Ein Dictionary erstellen

```python
telefonbuch = {
    "Anna": "1234",
    "Ben": "5678",
    "Clara": "9012"
}

leeres_dict = {}  # leeres Dictionary
```

➡️ Syntax: `{schlüssel: wert, ...}`  
➡️ Schlüssel müssen **eindeutig** sein.  
➡️ Schlüssel können verschiedene Datentypen haben (typisch: Strings, Zahlen).  

---

## 2. Werte auslesen und ändern

```python
print(telefonbuch["Anna"])  # "1234"

telefonbuch["Anna"] = "0000"  # Wert ändern
print(telefonbuch["Anna"])   # "0000"
```

➡️ Zugriff über den Schlüssel.  
➡️ Wenn der Schlüssel nicht existiert → **Fehler (`KeyError`)**.  

---

## 3. Werte sicher abrufen mit `get()`

```python
print(telefonbuch.get("Anna"))      # "1234"
print(telefonbuch.get("Max"))       # None
print(telefonbuch.get("Max", "Unbekannt"))  # "Unbekannt"
```

➡️ Vorteil: Kein Fehler, wenn der Schlüssel fehlt.  
➡️ Nützlich für **Standardwerte**.  

---

## 4. Einträge hinzufügen

```python
telefonbuch["David"] = "5555"
print(telefonbuch)  
# {"Anna": "0000", "Ben": "5678", "Clara": "9012", "David": "5555"}
```

➡️ Einfach über `dict[schlüssel] = wert`.  
➡️ Überschreibt, wenn Schlüssel schon vorhanden ist.  

---

## 5. Einträge entfernen

```python
del telefonbuch["Anna"]  # löscht einen Eintrag
print(telefonbuch)

nummer = telefonbuch.pop("Ben")  
print(nummer)          # "5678"
print(telefonbuch)     # {"Clara": "9012", "David": "5555"}
```

➡️ `del` → löscht einen Schlüssel ohne Rückgabe.  
➡️ `pop()` → löscht und gibt den Wert zurück.  
➡️ `pop(key, default)` → gibt `default` zurück, wenn Schlüssel fehlt.  

---

## 6. Über Schlüssel und Werte iterieren

```python
for name in telefonbuch:  # über Schlüssel
    print(name)

for nummer in telefonbuch.values():  # über Werte
    print(nummer)

for name, nummer in telefonbuch.items():  # über Schlüssel und Werte
    print(name, "->", nummer)
```

➡️ Wichtige Methoden:  
- `.keys()` → alle Schlüssel  
- `.values()` → alle Werte  
- `.items()` → Schlüssel-Wert-Paare  

---

## 7. Prüfen, ob ein Schlüssel enthalten ist

```python
if "Clara" in telefonbuch:
    print("Clara ist im Telefonbuch")
```

➡️ `in` prüft **nur die Schlüssel**, nicht die Werte.  

---

## 8. Nützliche Dictionary-Methoden

### Länge
```python
print(len(telefonbuch))  # Anzahl der Einträge
```

### Leeren
```python
telefonbuch.clear()
print(telefonbuch)  # {}
```

### Kopieren
```python
copy_dict = telefonbuch.copy()
```

### Standardwert setzen mit `setdefault()`
```python
zahlen = {}
zahlen.setdefault("eins", 1)   # {"eins": 1}
zahlen.setdefault("eins", 99)  # bleibt {"eins": 1}
```
➡️ Fügt Schlüssel mit Wert hinzu, wenn er fehlt.  
➡️ Wenn Schlüssel schon existiert, passiert nichts.  

### Update mit anderem Dictionary
```python
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}
a.update(b)
print(a)  # {"x": 1, "y": 3, "z": 4}
```
➡️ Überschreibt vorhandene Werte, fügt neue hinzu.  

---

## 9. Dictionary in Listen umwandeln

```python
personen = {"Anna": 25, "Ben": 30, "Clara": 20}

print(list(personen.keys()))    # ["Anna", "Ben", "Clara"]
print(list(personen.values()))  # [25, 30, 20]
print(list(personen.items()))   # [("Anna", 25), ("Ben", 30), ("Clara", 20)]
```

---

## 10. Dictionary-Komprehension (fortgeschritten)

Kurzform, um Dictionaries zu erzeugen:

```python
quadrate = {x: x**2 for x in range(1, 6)}
print(quadrate)  
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

➡️ Sehr nützlich für Umwandlungen und Filterungen.  

---

## Zusammenfassung

- Dictionaries speichern **Schlüssel-Wert-Paare**.  
- Zugriff über `dict[schlüssel]` oder sicher mit `.get()`.  
- Typische Methoden: `.keys()`, `.values()`, `.items()`, `.pop()`, `.update()`.  
- Iteration über Schlüssel, Werte oder Paare ist sehr häufig.  
- Dictionary-Komprehension erlaubt kompakte Erstellung.
