# Funktionen in Python

Funktionen sind wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe
erfüllen. Sie helfen dabei, Programme übersichtlicher und modularer zu
gestalten.

------------------------------------------------------------------------

## 1. Eine einfache Funktion

``` python
def hallo():
    print("Hallo, Welt!")

hallo()  # Aufruf der Funktion
```

-   Definiert wird eine Funktion mit dem Schlüsselwort `def`.
-   Funktionen können beliebig oft aufgerufen werden.

------------------------------------------------------------------------

## 2. Funktionen mit Parametern

Parameter sind Eingabewerte für eine Funktion.

``` python
def begruessung(name):
    print(f"Hallo, {name}!")

begruessung("Anna")
begruessung("Tom")
```

-   Parameter (`name`) werden beim Aufruf mit Werten belegt.

------------------------------------------------------------------------

## 3. Mehrere Parameter

``` python
def addiere(a, b):
    print(a + b)

addiere(3, 5)   # 8
addiere(10, 2)  # 12
```

-   Funktionen können mehrere Parameter annehmen.

------------------------------------------------------------------------

## 4. Rückgabewerte (`return`)

Funktionen können Ergebnisse zurückgeben.

``` python
def quadrat(x):
    return x * x

ergebnis = quadrat(5)
print(ergebnis)  # 25
```

-   Mit `return` gibt die Funktion einen Wert zurück.
-   Ohne `return` gibt die Funktion automatisch `None` zurück.

------------------------------------------------------------------------

## 5. Standardwerte für Parameter

``` python
def begruessung(name="Gast"):
    print(f"Hallo, {name}!")

begruessung("Anna")  # Hallo, Anna!
begruessung()        # Hallo, Gast!
```

-   Parameter können Standardwerte haben.
-   Wenn kein Wert übergeben wird, wird der Standard genutzt.

------------------------------------------------------------------------

## 6. Benannte Argumente

``` python
def beschreibung(name, alter):
    print(f"{name} ist {alter} Jahre alt.")

beschreibung(alter=25, name="Lena")
```

-   Argumente können beim Aufruf explizit benannt werden.
-   Die Reihenfolge spielt dann keine Rolle.

------------------------------------------------------------------------

## 7. Variable Anzahl an Argumenten (`*args`, `**kwargs`)

``` python
def summiere(*zahlen):
    return sum(zahlen)

print(summiere(1, 2, 3))       # 6
print(summiere(5, 10, 15, 20)) # 50
```

-   `*args` = beliebig viele Positionsargumente (als Tupel).
-   `**kwargs` = beliebig viele benannte Argumente (als Dictionary).

Beispiel für `**kwargs`:

``` python
def info(**daten):
    for key, value in daten.items():
        print(f"{key}: {value}")

info(name="Anna", alter=22, ort="Berlin")
```

------------------------------------------------------------------------

## 8. Funktionen mit mehreren Rückgabewerten

``` python
def berechne(a, b):
    return a + b, a * b

summe, produkt = berechne(3, 4)
print("Summe:", summe)       # 7
print("Produkt:", produkt)   # 12
```

-   Eine Funktion kann mehrere Werte zurückgeben (als Tupel).

------------------------------------------------------------------------

## 9. Anonyme Funktionen (Lambda)

``` python
quadrat = lambda x: x * x
print(quadrat(6))  # 36
```

-   `lambda` erstellt kleine, anonyme Funktionen.
-   Nützlich für kurze Berechnungen.

------------------------------------------------------------------------

# Zusammenfassung

-   Funktionen werden mit `def` definiert.\
-   Parameter ermöglichen Eingaben.\
-   Mit `return` können Ergebnisse zurückgegeben werden.\
-   Es gibt Standardparameter, benannte Argumente und variable Parameter
    (`*args`, `**kwargs`).\
-   Funktionen können mehrere Rückgabewerte liefern.\
-   Mit `lambda` können kleine Funktionen schnell erstellt werden.
