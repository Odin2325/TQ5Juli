from controllers.user_controller import UserController

def main():
    print("=== Vehicle Rental System ===")
    user_controller = UserController()
    user = user_controller.login()

    if user:
        if user["Role"] == "Customer":
            print("👉 Kundenmenü laden...")
        elif user["Role"] == "Employee":
            print("👉 Mitarbeiter-Ansicht laden...")

if __name__ == "__main__":
    main()
