# 📘 Python: Das `os` Modul & Dateioperationen

Dieses Dokument erklärt die wichtigsten Funktionen des `os`-Moduls sowie typische Operationen zum **Lesen und Schreiben von Dateien** in Python.  
Zusätzlich werden **Konventionen** zur sauberen Strukturierung von Code vorgestellt.

---

## 🔹 Das `os` Modul in Python

Das `os`-Modul erlaubt es, mit dem Betriebssystem zu interagieren (Dateien, Ordner, Prozesse, Umgebungsvariablen).

### Häufig verwendete Funktionen

| Funktion | Beschreibung | Beispiel |
|----------|--------------|----------|
| `os.getcwd()` | Gibt das aktuelle Arbeitsverzeichnis zurück. | `print(os.getcwd())` |
| `os.chdir(pfad)` | Wechselt in ein anderes Verzeichnis. | `os.chdir("C:/Users")` |
| `os.listdir(pfad)` | Listet Dateien und Ordner in einem Verzeichnis auf. | `print(os.listdir("."))` |
| `os.mkdir(name)` | Erstellt ein neues Verzeichnis. | `os.mkdir("testordner")` |
| `os.makedirs(pfad)` | Erstellt verschachtelte Verzeichnisse. | `os.makedirs("a/b/c")` |
| `os.remove(datei)` | Löscht eine Datei. | `os.remove("alte_datei.txt")` |
| `os.rmdir(name)` | Löscht ein leeres Verzeichnis. | `os.rmdir("testordner")` |
| `os.rename(src, dst)` | Bennent Datei/Ordner um. | `os.rename("alt.txt", "neu.txt")` |
| `os.path.exists(pfad)` | Prüft, ob Datei/Ordner existiert. | `if os.path.exists("test.txt"):` |
| `os.path.isfile(pfad)` | Prüft, ob Pfad eine Datei ist. | `os.path.isfile("dokument.txt")` |
| `os.path.isdir(pfad)` | Prüft, ob Pfad ein Ordner ist. | `os.path.isdir("bilder")` |
| `os.environ` | Zugriff auf Umgebungsvariablen. | `print(os.environ["PATH"])` |

---

## 🔹 Dateien lesen und schreiben

Python bietet einfache Möglichkeiten, Dateien zu öffnen, zu lesen und zu schreiben.

### Datei öffnen
```python
# Datei im Lesemodus öffnen (Standard)
f = open("test.txt", "r")
```

### Datei lesen
```python
with open("test.txt", "r", encoding="utf-8") as f:
    inhalt = f.read()       # Ganze Datei lesen
    zeilen = f.readlines()  # Liste aller Zeilen
```

### Datei schreiben (überschreibt Datei!)
```python
with open("ausgabe.txt", "w", encoding="utf-8") as f:
    f.write("Hallo Welt\n")
```

### Datei anhängen (ohne Überschreiben)
```python
with open("ausgabe.txt", "a", encoding="utf-8") as f:
    f.write("Neue Zeile\n")
```

---

## 🔹 Typische Struktur eines Python-Skripts

Es ist gute Praxis, Python-Skripte nach bestimmten Konventionen zu strukturieren:

### Beispiel
```python
import os

def hauptfunktion():
    # Arbeitsverzeichnis ausgeben
    print("Aktuelles Verzeichnis:", os.getcwd())

    # Datei lesen
    with open("daten.txt", "r", encoding="utf-8") as f:
        daten = f.read()
    print("Inhalt:", daten)

    # Neue Datei schreiben
    with open("ausgabe.txt", "w", encoding="utf-8") as f:
        f.write("Datei erfolgreich erstellt!")

if __name__ == "__main__":
    hauptfunktion()
```

### Erklärung der Konventionen
1. **Imports am Anfang**: Zuerst alle benötigten Bibliotheken einbinden.  
2. **Funktionen definieren**: Wiederverwendbare Logik gehört in Funktionen.  
3. **`if __name__ == "__main__":`**: Damit wird das Skript nur ausgeführt, wenn es direkt gestartet wird – nicht beim Importieren.  
4. **Kontextmanager (`with`)**: Für Dateioperationen, da Dateien nach Nutzung automatisch geschlossen werden.

---

## ✅ Zusammenfassung
- `os`-Modul = Schnittstelle zum Betriebssystem.  
- Wichtige Funktionen: **Verzeichnisse wechseln, Dateien/Ordner erstellen, löschen, prüfen**.  
- Dateioperationen: `open()`, `read()`, `write()`, besser mit `with open(...)`.  
- Struktur: **Imports → Funktionen → Hauptprogramm**.  

