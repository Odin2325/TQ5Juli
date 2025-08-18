# Aufgabe 1 Strings und Bedingungen.
 
# * Bestimme ob ein string der als input eingegeben wird
# * mit einem "." endet oder mit "r!".
# * Gebe True aus.
# * Zusaetzlich bestimme auch ob der string mit "Hallo" anfaengt.
# * Gebe True aus.
# * Wenn kein fall stimmen wuerde, gebe False aus.
# * Hinweis: ihr habt slices und indizes!
# * Hinweis2: Man darf negative Zahlen als index eingeben.

eingabe = input("Bitte geben Sie einen String ein: ")

if eingabe[-1] == "." or eingabe[-2:] == "r!":
    ends_correctly = True
    print(ends_correctly)
elif eingabe[0:5] == "Hallo":
    starts_correctly = True
    print(starts_correctly)
else:
    ends_correctly = False
    starts_correctly = False
    print("False")