permission = input("What is your permission level? (admin/manager): ").strip().lower()
level = 55

role = ''.join(ch for ch in permission if ch.isalpha())

if role == "admin" or role == "administrator":
    if level > 55:
        print("Welcome, Super Admin user.")
    else:
        print("Welcome, Admin user.")
elif role == "manager":
    if level >= 20:
        print("Contact an Admin for access.")
    else:
        print("You do not have sufficient privileges.")
else:
    print("You do not have sufficient privileges.")