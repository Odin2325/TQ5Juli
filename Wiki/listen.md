# Python-Listen – Erklärung und wichtige Funktionen

Listen sind eine der wichtigsten Datenstrukturen in Python.  
Sie können mehrere Werte (Elemente) speichern und haben eine feste Reihenfolge.  
Die Elemente können verschiedene Datentypen haben (Zahlen, Strings, Booleans usw.).

---

## 1. Eine Liste erstellen

```python
zahlen = [1, 2, 3, 4, 5]
woerter = ["Apfel", "Banane", "Kirsche"]
gemischt = [1, "Hallo", True, 3.14]
```

➡️ Eine Liste wird mit **eckigen Klammern `[]`** erstellt.  
Man kann beliebig viele Elemente hineinschreiben, getrennt durch Kommata.

---

## 2. Elemente einer Liste ansprechen

- Der **Index** beginnt bei `0`.  
- Negative Indizes greifen von hinten zu (`-1` = letztes Element).

```python
zahlen = [10, 20, 30, 40]

print(zahlen[0])   # 10 (erstes Element)
print(zahlen[2])   # 30 (drittes Element)
print(zahlen[-1])  # 40 (letztes Element)
```

➡️ Mit `liste[index]` kann man ein bestimmtes Element auslesen.  
➡️ Mit `liste[index] = neuer_wert` kann man ein Element **ändern**.

---

## 3. Liste durchlaufen (Schleifen)

```python
fruechte = ["Apfel", "Banane", "Kirsche"]

for f in fruechte:
    print(f)
```

➡️ Die `for`-Schleife nimmt sich **jedes Element nacheinander** aus der Liste und führt den Schleifenblock damit aus.  

Mit Index (z. B. wenn man die Position wissen möchte):

```python
for i in range(len(fruechte)):
    print(i, fruechte[i])
```

➡️ `len(fruechte)` gibt die **Länge der Liste** zurück.  
➡️ `range(len(...))` erzeugt Zahlen von `0` bis zur Länge-1 → perfekt für Indizes.

---

## 4. Wichtige Funktionen und Methoden

### Länge einer Liste
```python
zahlen = [1, 2, 3, 4]
print(len(zahlen))  # 4
```
- **`len(liste)`** → gibt zurück, wie viele Elemente in der Liste sind.  
- Nützlich, wenn man die Größe nicht kennt (z. B. Eingaben vom Benutzer).

---

### Element hinzufügen
```python
zahlen = [1, 2, 3]
zahlen.append(4)
print(zahlen)  # [1, 2, 3, 4]
```
- **`append()`** fügt **ein Element am Ende** der Liste hinzu.  
- Verändert die Liste direkt.

---

### Mehrere Elemente hinzufügen
```python
zahlen = [1, 2]
zahlen.extend([3, 4, 5])
print(zahlen)  # [1, 2, 3, 4, 5]
```
- **`extend()`** hängt eine **ganze andere Liste** hinten an.  
- Unterschied zu `append`:  
  - `append([3,4,5])` → fügt eine Liste als ein Element hinzu → `[1, 2, [3,4,5]]`  
  - `extend([3,4,5])` → fügt jedes Element einzeln hinzu → `[1, 2, 3, 4, 5]`

---

### Element an bestimmter Stelle einfügen
```python
zahlen = [1, 2, 3]
zahlen.insert(1, 99)
print(zahlen)  # [1, 99, 2, 3]
```
- **`insert(index, wert)`** setzt ein Element an einer bestimmten Position ein.  
- Alles rechts vom Index rutscht eins nach hinten.

---

### Element entfernen
```python
zahlen = [1, 2, 3, 2]
zahlen.remove(2)
print(zahlen)  # [1, 3, 2]
```
- **`remove(wert)`** löscht **das erste Vorkommen** eines Elements.  
- Wenn der Wert nicht existiert → Fehlermeldung.

---

### Letztes Element entfernen
```python
zahlen = [1, 2, 3]
letztes = zahlen.pop()
print(letztes)   # 3
print(zahlen)    # [1, 2]
```
- **`pop()`** entfernt das letzte Element und gibt es zurück.  
- Praktisch, wenn man ein Element **herausnehmen und weiterverwenden** will.  
- Auch mit Index möglich: `pop(0)` entfernt das erste Element.

---

### Element suchen
```python
woerter = ["Hund", "Katze", "Maus"]
print(woerter.index("Katze"))  # 1
```
- **`index(wert)`** gibt den Index des ersten Vorkommens zurück.  
- Falls der Wert nicht existiert → Fehlermeldung.

---

### Zählen, wie oft ein Element vorkommt
```python
zahlen = [1, 2, 2, 3, 2, 4]
print(zahlen.count(2))  # 3
```
- **`count(wert)`** → zählt, wie oft ein Element in der Liste vorkommt.

---

### Liste sortieren
```python
zahlen = [4, 2, 7, 1]
zahlen.sort()
print(zahlen)  # [1, 2, 4, 7]
```
- **`sort()`** ordnet die Liste aufsteigend.  
- Mit `reverse=True` absteigend.  
- Achtung: verändert die Liste direkt!

---

### Liste umkehren
```python
zahlen = [1, 2, 3, 4]
zahlen.reverse()
print(zahlen)  # [4, 3, 2, 1]
```
- **`reverse()`** kehrt einfach die Reihenfolge der Liste um.

---

## 5. Nützliche Operationen mit eingebauten Funktionen

```python
zahlen = [3, 8, 1, 6]

print(min(zahlen))  # 1 (kleinstes Element)
print(max(zahlen))  # 8 (größtes Element)
print(sum(zahlen))  # 18 (Summe aller Elemente)
```

- **`min(liste)`** → gibt das kleinste Element zurück.  
- **`max(liste)`** → gibt das größte Element zurück.  
- **`sum(liste)`** → berechnet die Summe (nur für Zahlen).  

---

### Überprüfung, ob ein Element enthalten ist
```python
zahlen = [1, 2, 3]
if 3 in zahlen:
    print("3 ist in der Liste enthalten")
```
- **`in`** → prüft, ob ein Element in der Liste vorkommt.  
- Ergebnis ist `True` oder `False`.

---

## 6. Listen-Komprehension (fortgeschritten)

Kurzform, um neue Listen zu erstellen:

```python
quadrate = [x**2 for x in range(1, 6)]
print(quadrate)  # [1, 4, 9, 16, 25]
```

➡️ Liest man so: „Nimm jedes `x` aus `range(1,6)` und rechne `x**2`“.  
➡️ Besonders praktisch für schnelle Listen-Erstellungen oder Filterungen.

---

## Zusammenfassung

- Listen speichern mehrere Werte in einer festen Reihenfolge.  
- Elemente werden über Indizes angesprochen.  
- Typische Methoden: `append()`, `remove()`, `insert()`, `sort()`, `reverse()`.  
- Eingebaute Funktionen wie `len()`, `sum()`, `min()`, `max()` sind sehr nützlich.  
- Mit `for`-Schleifen kann man bequem über Listen iterieren.  
- Fortgeschritten: Listen-Komprehension für kompakte Schreibweise.
