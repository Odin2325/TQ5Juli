from KundeDatei import Kunde
from random import randint
from datetime import datetime

class Bankkonto:
    def __init__(self, kontoinhaber:Kunde, kontonummer, startguthaben=0):
        self.kontoinhaber = kontoinhaber
        self.kontostand = startguthaben
        self.kontonummer = kontonummer
        self.pin = Bankkonto.pin_generator()
        self.transaktions_historie = []

    def pin_generator():
        neues_pin = ''
        for i in range(0,4):
            neues_pin += str(randint(0,9))
        print('Das neue Pin ist:',neues_pin)
        return neues_pin

    def details(self):
        print('Konto Details')
        print('=======================================')
        print(f'Kontoinhaber: {self.kontoinhaber.detail_kunde(False)}')
        print(f'Kontonummer: {self.kontonummer}\nKontostand: {self.kontostand}')
        print('=======================================')

    def einzahlen(self, betrag):
        if betrag <= 0:
            print('0 und Negative Betraege sind nicht erlaubt.')
            return False
        self.kontostand += betrag
        self.transaktions_historie.append(('einzahlen',betrag,self.kontostand,datetime.now()))
        print('Einzahlung erfolgreich.')
        return True
        
    def auszahlen(self, betrag):
        if betrag <= 0:
            print('0 und Negative Betraege sind nicht erlaubt.')
            return False
        self.kontostand -= betrag
        self.transaktions_historie.append(('auszahlen',betrag,self.kontostand,datetime.now()))
        print('Auszahlung erfolgreich')
        return True
    
    def kontostand_ansehen(self):
        print('Dein Aktueller Kontostand betraegt:',self.kontostand)

    def kontoauszug(self):
        print('==========Transaktionshistorie==========')
        print('(operation,betrag,kontostand,timestamp)')
        for eintrag in self.transaktions_historie:
            print(eintrag)
        print('==========EndeHistorie==========')


    def transaktion(self, anderen_konto: "Bankkonto", betrag: float) -> bool:
        """
        Führt eine Transaktion von diesem Konto zu einem anderen Bankkonto durch.

        Args:
            anderen_konto (Bankkonto): Das Zielkonto.
            betrag (float): Der Betrag, der überwiesen werden soll.

        Returns:
            bool: True, wenn die Transaktion erfolgreich war, sonst False.
        """
        if betrag <= 0:
            print("❌ Ungültiger Betrag. Nur positive Werte erlaubt.")
            return False

        if self.kontostand < betrag:
            print("❌ Nicht genügend Guthaben für die Transaktion.")
            return False

        # Geld abbuchen
        self.kontostand -= betrag
        self.transaktions_historie.append(("überweisung_ab", betrag, self.kontostand, datetime.now()))

        # Geld gutschreiben
        anderen_konto.kontostand += betrag
        anderen_konto.transaktions_historie.append(("überweisung_zu", betrag, anderen_konto.kontostand, datetime.now()))

        print(f"✅ Erfolgreich {betrag} EUR an Konto {anderen_konto.kontonummer} überwiesen.")
        return True
