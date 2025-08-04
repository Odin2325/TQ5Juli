username = input("Bitte geben Sie Ihren Benutzernamen ein: ")
passwort = input("Bitte geben Sie Ihr Passwort ein: ")

if username == "user123" and passwort == "123456789":
    print("Login erfolgreich!")
else:
    print("Login fehlgeschlagen!")


if username == "user123":
    #weiters code
    if passwort == "123456789":
        print("Login erfolgreich!")
else:
    print("Login fehlgeschlagen!")