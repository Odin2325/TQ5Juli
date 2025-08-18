# Aufgabe 1 Strings und Bedingungen.
 
# * Bestimme ob ein string der als input eingegeben wird
# * mit einem "." endet oder mit "r!".
# * Gebe True aus.
# * Zusaetzlich bestimme auch ob der string mit "Hallo" anfaengt.
# * Gebe True aus.
# * Wenn kein fall stimmen wuerde, gebe False aus.
# * Hinweis: ihr habt slices und indizes!
# * Hinweis2: Man darf negative Zahlen als index eingeben.

string = input("Bitte geben Sie einen String ein: ")

if string[-1] == "." or string[-2:] == "r!":
    ends_correctly = True
    print(ends_correctly)
elif string[0:5] == "Hallo":
    starts_correctly = True
    print(starts_correctly)
else:
    ends_correctly = False
    starts_correctly = False
    print = 'False'