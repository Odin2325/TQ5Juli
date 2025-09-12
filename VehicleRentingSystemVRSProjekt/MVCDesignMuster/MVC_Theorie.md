

# Theorie: Das MVC-Designmuster

## 1. Was ist MVC?
**MVC** steht für **Model – View – Controller**.  
Es ist ein **Architekturmuster**, das Software in **drei klar getrennte Schichten** aufteilt:

1. **Model**  
   - Enthält die **Daten** und die **Logik**, wie diese Daten verarbeitet werden.  
   - Beispiel: Datenbanktabellen und Python-Funktionen/Klassen, die mit diesen Daten arbeiten (`VehicleModel`, `RentalModel` usw.).  

2. **View**  
   - Zuständig für die **Darstellung**.  
   - Zeigt Daten an und nimmt Eingaben vom Benutzer entgegen.  
   - Beispiel im Konsolenprojekt: Menüs, Textausgaben, Benutzereingaben.  

3. **Controller**  
   - Vermittelt zwischen **View** und **Model**.  
   - Nimmt Benutzeraktionen entgegen, ruft passende Methoden im Model auf und entscheidet, welche View angezeigt wird.  
   - Beispiel: `RentalController.rent_vehicle()` prüft Verfügbarkeit → erstellt Mietvertrag → gibt Rückmeldung an View.  

---

## 2. Warum MVC?
Das Ziel ist es, **klare Trennung der Verantwortlichkeiten** zu schaffen:  
- Model = Daten  
- View = Darstellung  
- Controller = Steuerung  

Dadurch bleibt der Code **übersichtlich, erweiterbar und testbar**.  

---

## 3. Vorteile von MVC

### Klare Trennung der Verantwortlichkeiten
- Änderungen im **Design (View)** haben keinen Einfluss auf die **Datenbanklogik (Model)**.  
- Änderungen im **Model** betreffen nicht die Darstellung.  

### Bessere Wiederverwendbarkeit
- Das Model kann auch in einer anderen Oberfläche wiederverwendet werden (z. B. später GUI oder Web-App).  

### Einfacheres Testen
- Man kann das **Model separat testen**, ohne sich um Benutzeroberfläche oder Eingaben kümmern zu müssen.  

### Bessere Teamarbeit
- Entwickler können parallel arbeiten:  
  - Einer am Model (z. B. SQLite-Anbindung),  
  - einer am Controller (Logik),  
  - einer an der View (Darstellung).  

### Erweiterbarkeit
- Neue Features lassen sich leichter einbauen, weil die Struktur klar ist.  

---

## 4. Beispiel im Fahrzeugvermietungs-Projekt
- **Model:** `RentalModel.create_rental(customer_id, vehicle_id, start, end)`  
- **Controller:** prüft, ob das Fahrzeug frei ist, und ruft `RentalModel` auf.  
- **View:** zeigt entweder *„Fahrzeug erfolgreich gemietet“* oder *„Fahrzeug nicht verfügbar“*.  


---

**Zusammenfassung:**  
Das MVC-Muster macht Programme **strukturierter, wartbarer und erweiterbarer**.  
Es ist ein Grundbaustein moderner Softwareentwicklung (z. B. in Django, ASP.NET, Rails, Spring).  
