# Klassen und Vererbung in Python

Python unterstützt die objektorientierte Programmierung (OOP). Mit
Klassen können eigene Datentypen erstellt werden, die Attribute (Daten)
und Methoden (Funktionen) enthalten.\
Ein zentrales Konzept dabei ist die **Vererbung**, bei der eine Klasse
Eigenschaften und Methoden einer anderen Klasse erbt.

------------------------------------------------------------------------

## 1. Eine einfache Klasse

``` python
class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def bellen(self):
        print(f"{self.name} bellt!")

# Instanz erzeugen
mein_hund = Hund("Bello", 3)
mein_hund.bellen()  # Ausgabe: Bello bellt!
```

-   `__init__` ist der **Konstruktor**, er wird beim Erstellen eines
    Objekts aufgerufen.
-   `self` verweist auf das aktuelle Objekt.

------------------------------------------------------------------------

## 2. Attribute und Methoden

``` python
class Auto:
    def __init__(self, marke, baujahr):
        self.marke = marke
        self.baujahr = baujahr

    def details(self):
        return f"Auto: {self.marke}, Baujahr: {self.baujahr}"

mein_auto = Auto("BMW", 2020)
print(mein_auto.details())
```

-   Attribute speichern Daten.
-   Methoden führen Aktionen mit diesen Daten aus.

------------------------------------------------------------------------

## 3. Vererbung (Grundlagen)

``` python
class Tier:
    def __init__(self, name):
        self.name = name

    def bewegen(self):
        print(f"{self.name} bewegt sich.")

class Hund(Tier):
    def bellen(self):
        print(f"{self.name} bellt!")

class Katze(Tier):
    def miauen(self):
        print(f"{self.name} miaut!")

hund = Hund("Bello")
hund.bewegen()  # geerbt von Tier
hund.bellen()

katze = Katze("Minka")
katze.bewegen()  # geerbt von Tier
katze.miauen()
```

-   `Hund` und `Katze` erben von `Tier`.
-   Beide haben Zugriff auf die Methode `bewegen`.

------------------------------------------------------------------------

## 4. Methoden überschreiben

``` python
class Tier:
    def __init__(self, name):
        self.name = name

    def laut(self):
        print(f"{self.name} macht ein Geräusch.")

class Hund(Tier):
    def laut(self):  # überschreibt die Methode
        print(f"{self.name} bellt laut!")

tier = Tier("Tierchen")
tier.laut()

hund = Hund("Bello")
hund.laut()  # überschreibt die geerbte Methode
```

-   Kindklassen können geerbte Methoden **überschreiben**.

------------------------------------------------------------------------

## 5. `super()` verwenden

``` python
class Tier:
    def __init__(self, name):
        self.name = name

class Hund(Tier):
    def __init__(self, name, rasse):
        super().__init__(name)  # ruft den Konstruktor der Elternklasse auf
        self.rasse = rasse

    def info(self):
        print(f"Hund: {self.name}, Rasse: {self.rasse}")

hund = Hund("Bello", "Labrador")
hund.info()
```

-   Mit `super()` kann man auf Methoden der Elternklasse zugreifen.

------------------------------------------------------------------------

## 6. Mehrfachvererbung

``` python
class Schwimmer:
    def schwimmen(self):
        print("Kann schwimmen.")

class Läufer:
    def laufen(self):
        print("Kann laufen.")

class Triathlet(Schwimmer, Läufer):
    pass

athlet = Triathlet()
athlet.schwimmen()
athlet.laufen()
```

-   Eine Klasse kann von mehreren Klassen erben.
-   Python löst Konflikte mit der **MRO (Method Resolution Order)**.

------------------------------------------------------------------------

## 7. Abstrakte Klassen (Blueprints)

``` python
from abc import ABC, abstractmethod

class Tier(ABC):
    @abstractmethod
    def laut(self):
        pass

class Hund(Tier):
    def laut(self):
        print("Wuff!")

class Katze(Tier):
    def laut(self):
        print("Miau!")

tiere = [Hund(), Katze()]
for t in tiere:
    t.laut()
```

-   Mit dem Modul `abc` können abstrakte Klassen erstellt werden.
-   Sie definieren **Methoden, die implementiert werden müssen**.

------------------------------------------------------------------------

# Zusammenfassung

-   Klassen sind Baupläne für Objekte.
-   Vererbung ermöglicht Wiederverwendung von Code.
-   Methoden können überschrieben werden.
-   `super()` erlaubt Zugriff auf Elternmethoden.
-   Mehrfachvererbung ist möglich.
-   Abstrakte Klassen dienen als Vorlagen.

Beispiel:\
Eine Klasse `Tier` definiert die Basisfunktionalitäten.\
`Hund` und `Katze` erben von `Tier` und fügen eigenes Verhalten hinzu.
