import datetime
import random
from Kundendatei import Kundenklasse as Kunde
#from Bankkontodatei import Bankkontoklasse as Bankkonto

class Bankklasse:
    def __init__(self, name, leiter, adresse, region, kontonummer):
        self.name = name
        self.leiter = leiter
        self.adresse = adresse
        self.region = region
        self.bankkonten = 0
        self.kontonummer = kontonummer
        self.BLZ = "08051990"
        self.kunden_liste = []
        self.konten_liste = []

    def konto_erstellen(self, kontonummer, inhaber:Kunde, saldo = 0):
        neues_konto = Bankkonto(kontonummer, inhaber, saldo)
        self.konten_liste.append(neues_konto)
        self.bankkonten += 1
        print(f"Neues Konto erstellt für {inhaber.name} mit Kontonummer {kontonummer}")
        return neues_konto

    def konto_löschen(self, kontonummer):
        for konto in self.konten_liste:
            if konto.kontonummer == kontonummer:
                self.konten_liste.remove(konto)
                self.bankkonten -= 1
                print(f"Konto mit Kontonummer {kontonummer} wurde gelöscht.")
                return True
        print(f"Konto mit Kontonummer {kontonummer} nicht gefunden.")
        return False

    def kontonummer_generator(self):
        import random
        kontonummer = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        print(f"Generierte Kontonummer: {kontonummer}")
        return kontonummer

    def kundennummer_generator(self):
        import random
        kundennummer = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        print(f"Generierte Kundennummer: {kundennummer}")
        return kundennummer