def summe(liste):
    sum = 0
    for zahl in liste:
        sum += zahl
    return sum

# | 12 | 8.99 | 5.49 | 3.99 | 2.99 |
# Schleifen Durchlauf
# sum = 0 + 12 = 12
# sum = 12 + 8.99 = 20.99
# sum = 20.99 + 5.49 = 26.48
# sum = 26.48 + 3.99 = 30.47
# sum = 30.47 + 2.99 = 33.46

test_resultat = summe([12, 8.99, 5.49, 3.99, 2.99])
if test_resultat == 33.46:
    print("Test erfolgreich!")
else:
    print("Test fehlgeschlagen! Erwartet: 33.46, erhalten:", test_resultat)