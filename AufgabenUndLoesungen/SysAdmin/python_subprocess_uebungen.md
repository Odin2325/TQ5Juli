# 🖥️ Python `subprocess` Modul Übungen (Systemadministrator Simulation)

## Einfache Aufgaben

### 1. Aktuelles Verzeichnis überprüfen
- Schreibe ein Programm, dass das aktuelle Arbeitsverzeichnis ausgibt.  
- Wechsle anschließend in ein Verzeichnis namens `logs` (erstelle es, falls es nicht existiert).  
- Gib danach erneut das aktuelle Arbeitsverzeichnis aus, um die Änderung zu prüfen.

---

### 2. Dateien und Ordner auflisten
- Erstelle ein Skript, das alle Dateien und Verzeichnisse im aktuellen Ordner auflistet.  
- Gib sie in zwei Gruppen aus: **Dateien** und **Ordner**.

---

### 3. Datei überprüfen
- Frage den Benutzer nach einem Dateinamen.  
- Prüfe, ob diese Datei im aktuellen Ordner existiert.  
- Gib `"Gefunden"` oder `"Nicht gefunden"` aus.

---

## Mittlere Aufgaben

### 4. Simulation: Temporäre Dateien löschen
- Lege in einem Ordner `temp` mehrere Testdateien an (z. B. `file1.tmp`, `file2.tmp`, `notes.txt`).  
- Schreibe ein Skript, das alle Dateien mit der Endung `.tmp` löscht.  
- Gib aus, welche Dateien gelöscht wurden.

---

### 5. Simulation: Logrotation
- Angenommen, es gibt eine Log-Datei `system.log`.  
- Schreibe ein Skript, das sie in `system.log.old` umbenennt.  
- Erstelle anschließend eine neue leere Datei `system.log`.  
- Dies simuliert eine typische Log-Rotation.

---

### 6. Verzeichnisbericht
- Schreibe ein Skript, das:  
  1. Den Benutzer nach einem Verzeichnispfad fragt.  
  2. Die **Gesamtanzahl der Dateien** und **Unterordner** darin ausgibt.  
  3. Die **5 größten Dateien** (nach Dateigröße) auflistet.

---

### 7. Umgebungsvariablen bearbeiten
- Schreibe ein Skript, das:  
  - Den aktuellen Wert der Umgebungsvariablen `PATH` ausgibt.  
  - Einen zusätzlichen (fiktiven) Pfad (`C:/fake/bin` oder `/usr/local/fake/bin`) anhängt.  
  - Den aktualisierten Wert erneut ausgibt.

---

### 8. Einfaches Backup-Skript
- Frage den Benutzer nach einem Verzeichnisnamen (z. B. `meinedaten`).  
- Erstelle eine Kopie dieses Verzeichnisses mit dem Namen `meinedaten_backup`.  
- Achte darauf, dass die Ordnerstruktur und Dateien mitkopiert werden.

---

## Bonusaufgabe: Installierte Programme auslesen

### 9. Installierte Anwendungen auflisten
- Schreibe ein Python-Skript, das alle installierten Programme auf dem Computer in einer Datei speichert.  
- Das Skript soll erkennen, auf welchem Betriebssystem es läuft:  
  - **Windows:** Befehl `wmic product get name`  
  - **Linux (Debian/Ubuntu):** Befehl `dpkg --get-selections`  
  - **macOS (Homebrew):** Befehl `brew list`  
- Das Ergebnis soll in die Datei `installed_apps.txt` geschrieben werden.  
- Gib eine Bestätigungsmeldung aus:  
  ```
  Installierte Anwendungen wurden in installed_apps.txt gespeichert
  ```
