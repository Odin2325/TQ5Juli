Abonnement = int(input("Abonnement: "))

if Abonnement <0:
        print("Your subscription has expired")
elif Abonnement <=1:
            print("Your subscription expires within a day!Renew now and save 20%!")
elif Abonnement <=5:
        print("Your subscription expires in [Abonnement] days. Renew now and save 10%!")
elif Abonnement <=10:
     print("Your subscription will expire soon. Renew now!")
else:
        print ("Keine Meldung")