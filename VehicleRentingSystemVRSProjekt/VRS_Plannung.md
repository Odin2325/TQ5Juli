# Planungsaufgaben für das Projekt Fahrzeugvermietung

Bevor du mit dem Programmieren beginnst, überlege dir, wie das System aufgebaut sein soll.  
Bearbeite die folgenden Aufgaben:

---

## Aufgabe A – Pseudocode und Struktogramme
Schreibe Pseudocode für mind. 4 Funktionen **„Fahrzeug mieten“**.  
Dein Pseudocode soll die einzelnen Schritte des Prozesses enthalten, z. B.:

```
function rent_vehicle(customer_id, vehicle_id, start_date, end_date):
    prüfe ob Fahrzeug verfügbar
    wenn nicht verfügbar → Fehlermeldung
    prüfe ob Kunde bereits aktives Mietobjekt hat
    wenn ja → Fehlermeldung
    berechne Mietzeitraum und geschätzte Kosten
    erstelle neuen Eintrag in Rental-Tabelle
    setze Fahrzeugstatus auf "Rented"
    gib Bestätigung zurück
```
Danach auch mind. 4 Struktogramme erstellen für deine in Pseudocode definierten Funktionen. Mit strukt.io.

---

## Aufgabe B – Aktivitätsdiagramm
Erstelle mindestens 5 **Aktivitätsdiagramme** für verschiedene Prozesse. Ein Beispiel: **„Fahrzeug zurückgeben“**.  
Es soll u. a. folgende Schritte zeigen:
- Kunde bringt Auto zurück  
- Kilometerstand eingeben  
- Rechnungsbetrag berechnen  
- Zahlung erfassen  
- Fahrzeugstatus auf „Available“ setzen  

---

## Aufgabe C – Klassendiagramm
Entwirf ein **Klassendiagramm** für das System.  
Folgende Klassen könnten vorkommen:  
- `User`  
- `Customer`  
- `Vehicle`  
- `Rental`  
- `Payment`  

Überlege dir Attribute (z. B. `name`, `email`, `daily_rate`) und Methoden (z. B. `rent_vehicle()`, `return_vehicle()`).  
