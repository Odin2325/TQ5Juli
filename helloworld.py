import json

# Dem text eine variable zuweisen
inhalt = "Berschreibung"

#Variable für den  JSON inhalt erstellen
json_inhalt = json.dumps(inhalt)

# Den JSON inhalt in eine Datei schreiben
with open("output.json", "w") as json_file:
    json_file.write(json_inhalt)
