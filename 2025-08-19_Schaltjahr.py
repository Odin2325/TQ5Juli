jahreszahl = int(input("Bitte gib eine Jahreszahl ein: "))

# Ohne Verschachtelung:
if jahreszahl % 4 == 0 and (jahreszahl % 100 != 0 or jahreszahl % 400 == 0):
    print(f"{jahreszahl} ist ein Schaltjahr.")
else:
    print(f"{jahreszahl} ist kein Schaltjahr.")


# Mit Verschachtelung:
if jahreszahl % 4 == 0:
    if jahreszahl % 100 == 0:
        if jahreszahl % 400 == 0:
            print(f"{jahreszahl} ist ein Schaltjahr.")
        else:
            print(f"{jahreszahl} ist kein Schaltjahr.")
    else:
        print(f"{jahreszahl} ist ein Schaltjahr.")
else:
    print(f"{jahreszahl} ist kein Schaltjahr.")