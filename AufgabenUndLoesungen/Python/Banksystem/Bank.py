from random import randint
from KundeDatei import Kunde
from BankkontoDatei import Bankkonto

class Bank:
    def __init__(self, name, hauptstandort, region, land):
        self.kontos = []
        self.kunden = []
        self.name = name
        self.hauptstandort = hauptstandort
        self.region = region
        self.land = land

    def kunde_schon_existiert(self, vorname, nachname, adresse):
        for kunde in self.kunden:
            if kunde.vorname == vorname and kunde.nachname == nachname and kunde.adresse == adresse:
                return (True,kunde)
        return (False,None)
        #Rueckgabewert ist ein Tupel mit (bool,kunde) oder (bool,None)
    
    def kunde_erstellen(self, vorname, nachname, adresse, telefonnummer, email, alter):
        neuer_kunde = Kunde(vorname, nachname, adresse, telefonnummer, email, alter)
        if not self.kunde_schon_existiert(vorname, nachname, adresse)[0]:
            #0 ist der bool wert aus den Tupel 
            #den wir von die Methode kunde_schon_existiert 
            # bekommen.
            self.kunden.append(neuer_kunde)
            print('Kunde erfolgreich erstellt.')
            return True
        else:
            print('Kunde existiert schon.')
            return False

    def kunde_loeschen(self, vorname, nachname, adresse):
        kunde_existiert_tupel = self.kunde_schon_existiert(vorname,nachname,adresse)
        if kunde_existiert_tupel[0]: 
            #0 ist der bool wert aus den Tupel 
            #den wir von die Methode kunde_schon_existiert 
            # bekommen.
            self.kunden.remove(kunde_existiert_tupel[1]) #1 Ist der Kunde selbst
            print('Kunde erfolgreich geloescht.')
            return True
        else:
            print('Kunde konnte nicht gefunden werden.')
            return False
        
    def bankkonto_loeschen(self, kontonummer):
        for bankkonto in self.kontos:
            #print(bankkonto.kontonummer)
            if bankkonto.kontonummer == kontonummer:
                self.kontos.remove(bankkonto)
                print('Bankkonto erfolgreich geloescht.')
                return True
        print("Dieser Bankkonto konnte nicht gefunden werden.")
        return False

    def bankkonto_erstellen(self,kunde):
        tupel = self.freies_kontonummer_generieren()
        while not tupel[0]:
            tupel = self.freies_kontonummer_generieren()

        neuer_bankkonto = Bankkonto(kunde,tupel[1])
        self.kontos.append(neuer_bankkonto)

    #5-stelliges Kontonummer
    def freies_kontonummer_generieren(self):
        neue_kontonummer = self.fuenf_stellige_kontonummer_erstellen()
        for konto in self.kontos:
            if neue_kontonummer == konto.kontonummer:
                return (False,None)   
        return (True,neue_kontonummer)

    def fuenf_stellige_kontonummer_erstellen(self):
        resultat = ''
        for i in range(0,5):
            resultat += str(randint(0,9))
        return resultat