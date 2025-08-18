# Wir programmieren jetzt mehrere Geschäftsregeln.
 
# 1. Ihr Code sollte nur eine Meldung anzeigen.
# 2. Wenn das Abonnement des Benutzers bzw. der Benutzerin in zehn Tagen oder weniger abläuft, zeigen Sie die folgende Meldung an:
#    Your subscription will expire soon. Renew now!
# 3. Wenn das Abonnement des Benutzers bzw. der Benutzerin in fünf Tagen oder weniger abläuft, zeigen Sie die folgenden Meldungen an:
#    Your subscription expires in _ days.
#    Renew now and save 10%!
# 4. Wenn das Abonnement des Benutzers bzw. der Benutzerin in einem Tag abläuft, zeigen Sie die folgenden Meldungen an:
#    Your subscription expires within a day!
#    Renew now and save 20%!
# 5. Wenn das Abonnement des Benutzers bzw. der Benutzerin abgelaufen ist, zeigen Sie die folgende Meldung an:
#    Your subscription has expired.
# 6. Wenn das Abonnement des Benutzers nicht in zehn Tagen oder weniger abläuft, zeigen Sie nichts an.

from random import *
daysUntilExpiration = randint(0,12)
discountPercentage = 0

print(f"Days until expiration: {daysUntilExpiration}")


# daysUntilExpiration = int(input("Bitte geben Sie die verbleibenden Tage bis zum Ablauf Ihres Abonnements ein: "))

if daysUntilExpiration <= 10 and daysUntilExpiration > 5:
    print("Your subscription will expire soon. Renew now!")
elif daysUntilExpiration <= 5 and daysUntilExpiration > 1:
    print(f"Your subscription expires in {daysUntilExpiration} days.")
    discountPercentage = 10
    print("Renew now and save 10%!")
elif daysUntilExpiration == 1:
    print("Your subscription expires within a day!")
    discountPercentage = 20
    print("Renew now and save 20%!")
elif daysUntilExpiration == 0:
    print("Your subscription has expired.")
else:
    pass