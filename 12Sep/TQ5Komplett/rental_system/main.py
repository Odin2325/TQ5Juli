# Importiere die notwendigen Module
from controllers.user_controller import handle_login

def main():
    """
    Hauptfunktion, die den Programmablauf steuert.
    """
    print("Willkommen beim Fahrzeugvermietungs-System!")

    # Starte den Login-Prozess
    handle_login()

if __name__ == "__main__":
    main()