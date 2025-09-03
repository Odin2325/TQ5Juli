# Aufgabe: Zahlen in Römische Zahlen umwandeln

Schreibe erstmal pseudocode, dann Struktogramm erstellen vom pseudocode, dann in programmcode umsetzten.

Schreibe eine Funktion, die normale Zahlen in **Römische Zahlen**
umwandelt.

Die Römer waren ein kluges Volk. Sie erfanden Beton, gerade Straßen und sogar Bikinis.\
Eine Sache, die sie jedoch nie entdeckten, war die Zahl **Null**. Das machte es etwas schwieriger, lange Chroniken zu schreiben und zu datieren. Dennoch wird das von ihnen entwickelte Zahlensystem bis heute verwendet. Zum Beispiel nutzt die BBC römische Zahlen, um ihre Programme zu datieren.

Die Römer schrieben Zahlen mit den Buchstaben:

-   **I, V, X, L, C, D, M**

Beispiele:

     1  => I
    10  => X
     7  => VII

Die größte Zahl, die mit diesem System dargestellt wird, ist **3.999**.

Laut Wikipedia schreibt man moderne römische Zahlen, indem man jede
Ziffer einzeln von links nach rechts ausdrückt und Nullen dabei
überspringt.

Beispiele:

-   **1990** in römischen Zahlen = **MCMXC**\
    (1000 = M, 900 = CM, 90 = XC)

-   **2008** in römischen Zahlen = **MMVIII**\
    (2000 = MM, 8 = VIII)

------------------------------------------------------------------------

## Deine Aufgabe

Schreibe in **Python** eine Funktion `to_roman(n: int) -> str`, die eine
Zahl `n` (1 ≤ n ≤ 3999) in eine römische Zahl umwandelt.

Beispielaufrufe:

``` python
print(to_roman(1))     # I
print(to_roman(7))     # VII
print(to_roman(1990))  # MCMXC
print(to_roman(2008))  # MMVIII
```
