# Module und Bibliotheken in Python importieren

In Python gibt es verschiedene Möglichkeiten, Module oder Bibliotheken
zu importieren. Imports ermöglichen die Wiederverwendung von Code aus
Modulen, Bibliotheken oder ganzen Paketen.

------------------------------------------------------------------------

## 1. Einfacher `import`

``` python
import math
print(math.sqrt(16))  # 4.0
```

-   Importiert das gesamte Modul.
-   Funktionen/Klassen/Variablen müssen mit dem Modulnamen aufgerufen
    werden (`math.sqrt`).

------------------------------------------------------------------------

## 2. Import mit Alias (`as`)

``` python
import numpy as np
print(np.array([1, 2, 3]))
```

-   Gibt dem Modul einen Kurznamen (Alias).

------------------------------------------------------------------------

## 3. Spezifische Objekte importieren (`from ... import ...`)

``` python
from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793
```

-   Importiert nur die angegebenen Objekte.
-   Können direkt verwendet werden, ohne Präfix mit Modulnamen.

------------------------------------------------------------------------

## 4. Alles importieren (`from ... import *`)

``` python
from math import *
print(sqrt(16))
```

-   Importiert **alles** aus einem Modul in den aktuellen Namespace.
-   Nicht empfohlen, da Namenskonflikte entstehen können.

------------------------------------------------------------------------

## 5. Import aus einem Untermodul

Manche Module sind in **Paketen** (Ordner mit `__init__.py` oder
Namespace-Paketen) organisiert.\
Beispiel:

``` python
from tkinter.dnd import dnd_start
```

Bedeutung: - `tkinter` ist ein Paket (ein Ordner). - Darin befindet sich
das Untermodul `dnd`. - Aus diesem Untermodul wird die Funktion
`dnd_start` importiert.

Die allgemeine Struktur lautet also:\
**`from <paket>.<unterpaket/modul> import <objekt>`**

------------------------------------------------------------------------

## 6. Relative Imports (innerhalb von Paketen)

Wenn man **innerhalb eines Pakets** arbeitet, sind relative Importe
möglich:

``` python
from . import helper         # Importiert helper.py im gleichen Ordner
from ..utils import tools    # Importiert tools.py aus dem übergeordneten Ordner utils
```

-   Ein Punkt (`.`) = aktuelles Paket.
-   Zwei Punkte (`..`) = übergeordnetes Paket.

Relative Importe funktionieren nur **innerhalb von Paketen**.

------------------------------------------------------------------------

## 7. Dynamische Imports mit `importlib`

``` python
import importlib

math_module = importlib.import_module("math")
print(math_module.sqrt(25))  # 5.0
```

-   Nützlich, wenn der Modulname zur Laufzeit bestimmt wird.

------------------------------------------------------------------------

## 8. Bedingte Imports

``` python
try:
    import numpy as np
except ImportError:
    print("NumPy nicht installiert, benutze Fallback.")
```

-   Importiert ein Modul nur, wenn es vorhanden ist.

------------------------------------------------------------------------

# Zusammenfassung

-   `import modul` → ganzes Modul.\
-   `import modul as alias` → mit Alias.\
-   `from modul import name` → spezifische Funktionen/Klassen.\
-   `from modul import *` → alles (nicht empfohlen).\
-   `from paket.unterpaket import objekt` → Import aus einem
    Untermodul.\
-   `from . import etwas` → relative Imports.\
-   `importlib.import_module()` → dynamischer Import.

Beispiel `from tkinter.dnd import dnd_start`:\
- `tkinter` ist das Hauptpaket\
- `dnd` ist ein Untermodul darin\
- `dnd_start` ist die importierte Funktion
