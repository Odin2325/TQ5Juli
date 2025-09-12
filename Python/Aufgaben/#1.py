#1. Aktuelles Verzeichnis überprüfen
import os

# Aktuelles Verzeichnis ausgeben
print("Aktuelles Verzeichnis:", os.getcwd())

# Verzeichnis 'logs' erstellen, falls nicht vorhanden
if not os.path.exists("logs"):
    os.mkdir("logs")

# In das Verzeichnis wechseln
os.chdir("logs")
print("Neues Verzeichnis:", os.getcwd())


#2. Dateien und Ordner auflisten
import os

dateien = []
ordner = []

for eintrag in os.listdir("."):
    if os.path.isfile(eintrag):
        dateien.append(eintrag)
    elif os.path.isdir(eintrag):
        ordner.append(eintrag)

print("📄 Dateien:", dateien)
print("📂 Ordner:", ordner)

#3. Datei überprüfen
import os

dateiname = input("Dateiname eingeben: ")

if os.path.isfile(dateiname):
    print("Gefunden")
else:
    print("Nicht gefunden")

#4. Simulation: Temporäre Dateien löschen
import os

# Ordner 'temp' anlegen
if not os.path.exists("temp"):
    os.mkdir("temp")

# Testdateien erstellen
with open("temp/file1.tmp", "w") as f:
    f.write("Test1")
with open("temp/file2.tmp", "w") as f:
    f.write("Test2")
with open("temp/notes.txt", "w") as f:
    f.write("Notizen")

# Löschen aller .tmp-Dateien
for datei in os.listdir("temp"):
    if datei.endswith(".tmp"):
        os.remove(os.path.join("temp", datei))
        print("Gelöscht:", datei)

#5. Simulation: Logrotation
import os

# Testlogdatei erstellen, falls nicht vorhanden
if not os.path.exists("system.log"):
    with open("system.log", "w") as f:
        f.write("Alte Logdaten\n")

# Falls schon eine alte existiert, löschen
if os.path.exists("system.log.old"):
    os.remove("system.log.old")

# Umbenennen
os.rename("system.log", "system.log.old")

# Neue leere Datei erstellen
open("system.log", "w").close()

print("Logrotation abgeschlossen!")

#6. Verzeichnisbericht
import os

pfad = input("Verzeichnispfad eingeben: ")

if os.path.exists(pfad) and os.path.isdir(pfad):
    dateien = []
    ordner = []
    
    for root, dirs, files in os.walk(pfad):
        for d in dirs:
            ordner.append(os.path.join(root, d))
        for f in files:
            dateien.append(os.path.join(root, f))

    print("Gesamtanzahl Dateien:", len(dateien))
    print("Gesamtanzahl Ordner:", len(ordner))

    # Größte 5 Dateien
    groesste = sorted(dateien, key=lambda x: os.path.getsize(x), reverse=True)[:5]
    print("\nTop 5 größte Dateien:")
    for f in groesste:
        print(f, "-", os.path.getsize(f), "Bytes")
else:
    print("Ungültiger Pfad")

#7. Umgebungsvariablen bearbeiten
import os

print("Aktuelles PATH:")
print(os.environ.get("PATH"))

# Fake-Pfad hinzufügen
fake_path = "C:/fake/bin" if os.name == "nt" else "/usr/local/fake/bin"
os.environ["PATH"] = os.environ.get("PATH", "") + os.pathsep + fake_path

print("\nNeues PATH:")
print(os.environ["PATH"])

#8. Einfaches Backup-Skript
import os
import shutil

quelle = input("Verzeichnisname eingeben: ")

if os.path.exists(quelle) and os.path.isdir(quelle):
    ziel = quelle + "_backup"
    if os.path.exists(ziel):
        shutil.rmtree(ziel)  # Altes Backup löschen
    shutil.copytree(quelle, ziel)
    print(f"Backup erstellt: {ziel}")
else:
    print("Verzeichnis nicht gefunden")

#9. Bonus: Installierte Anwendungen auflisten
import os
import subprocess
import platform

system = platform.system()
befehl = None

if system == "Windows":
    befehl = ["wmic", "product", "get", "name"]
elif system == "Linux":
    befehl = ["dpkg", "--get-selections"]
elif system == "Darwin":  # macOS
    befehl = ["brew", "list"]

if befehl:
    try:
        result = subprocess.check_output(befehl, text=True, errors="ignore")
        with open("installed_apps.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("Installierte Anwendungen wurden in installed_apps.txt gespeichert")
    except Exception as e:
        print("Fehler beim Ausführen:", e)
else:
    print("Betriebssystem nicht unterstützt")