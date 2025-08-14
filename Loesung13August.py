# Erstellen Sie zunächst drei Variablen: Ihr Lieblingsauto, Ihr Lieblingssport und Ihr Lieblingsgetränk.
mein_Lieblingsauto = input('Geben Sie Ihr Lieblingsauto ein: ')
mein_Lieblingsgetraenk = input('Geben Sie Ihr Lieblingsgetränk ein: ')
mein_Lieblingssport = input('Geben Sie Ihren Lieblingssport ein: ')

# Speichern Sie dies nun als formatierte Zeichenfolge (f-string) in einer Variablen, so dass es wie folgt aussieht:
# 'Wenn nur mein [mein_Lieblingsauto] [mein_Lieblingsgetränk] als Kraftstoff verwenden könnte, um [mein_Lieblingssport] auszuüben. Dann wäre ich zufrieden.'
resultat = f'Wenn nur mein {mein_Lieblingsauto} {mein_Lieblingsgetraenk} als Kraftstoff verwenden könnte, um {mein_Lieblingssport} auszuüben. Dann wäre ich zufrieden.'

# 1. Normale Variante ausgeben.
print(resultat)

# 2. Geben Sie nun diese Zeichenfolge unter Verwendung von eckigen Klammern vom 6. bis 16. inklusive Index aus.
print('Das mit dem Index habe ich nicht verstanden.')