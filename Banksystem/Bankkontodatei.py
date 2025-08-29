import datetime
import random
from random import randint
from Kundendatei import Kundenklasse as Kunde
#from Bankdatei import Bankklasse as Bank

class Bankkontoklasse:
    def __init__(self, kontonummer, inhaber:Kunde, saldo = 0):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self.iban = f"DE65 {self.bank.BLZ}{self.kontonummer}"
        self.pin = Bankkontoklasse.pin_generator()
        self.saldo = saldo
        self.dispo = 500.00
        self.bank = "Commerzbank"
        self.transaktionshistorie = []

    def pin_generator():
        neuer_pin = ""
        for i in range(0,4):
            neuer_pin += str(randint(0,9))
        print("Das neue Pin ist:",neuer_pin)
        return neuer_pin
    
    def einzahlen(self,betrag):
        self.saldo += betrag
        self.transaktionshistorie.append(("Einzahlung:" ,betrag,self.saldo))
        print(f"Neuer Kontostand nach Einzahlung: {self.saldo}")

    def abheben(self,betrag):
        if betrag > self.saldo + self.dispo:
            print("Nicht genug Guthaben auf dem Konto")
        else:
            self.saldo -= betrag
            self.transaktionshistorie.append(("Abhebung:" ,betrag,self.saldo)) 
            print(f"Neuer Kontostand nach Abhebung: {self.saldo}")

    def konto_details(self):
        print(f"Kontonummer: {self.kontonummer}\nInhaber: {self.inhaber}\nSaldo: {self.saldo}")
    
    def guthaben_details(self):
        print(f"Saldo: {self.saldo}\nDispo: {self.dispo}")   

    def Transaktionen(self):
        print("Transaktionshistorie:")
        for eintrag in self.transaktionshistorie:
            print(eintrag)

#kunde1 = Kunde("Paul", "Atreides", "01.01.2000", "Wüstenplanet Arrakis", "0123456789", "PA@so.wa")

#konto1 = Bankkontoklasse("40050012",kunde1.Kundendetails,1200.00)
#konto2 = Bankkonto("40050013","Leto II",2500.00))

