import subprocess

def new_user():
    confirm = "N"
    while confirm != "Y":
        username = input("Gib den Namen des hinzuzufügenden Benutzers ein: ")
        print(f"Den Benutzernamen '{username}' verwenden? (Y/N)")
        confirm = input().upper()
    try:
          # 'Passwort123' is just a placeholder, set a real password
          subprocess.run(["net", "user", username, "Passwort123", "/add"], check=True, shell=True)
          print(f"Benutzer '{username}' wurde erfolgreich angelegt.")
    except subprocess.CalledProcessError:
          print("Fehler beim Anlegen des Benutzers. Vielleicht existiert er schon oder es fehlen Rechte.")

if __name__ == "__main__":
    new_user()