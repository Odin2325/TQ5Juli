


class Bankkonto:
    def __init__(self,kontonummer,inhaber,saldo = 0):
        self.kontonummer = kontonummer
        self.inhaber = inhaber
        self.saldo = saldo
        self.dispo = 500.00
        self.zinsen = 0.15
        self.bank = "Commerzbank"
        self.region = "Flensburg"
        self.transaktionshistorie = []
    

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



konto1 = Bankkonto("40050012","Gottimperator",1200.00)
konto2 = Bankkonto("40050013","Leto II",2500.00)