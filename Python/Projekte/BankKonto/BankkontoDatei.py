from random import randint
from datetime import datetime
from KundeDatei import Kunde

class Bankkonto:
    def __init__(self, kontoinhaber:Kunde, startguthaben=0):
        self.kontoinhaber = kontoinhaber
        self.kontostand = startguthaben
        self.bank = 'Deutsche Bank'
        self.region = 'Bayern'
        self.kontonummer = 'DE12346789012'
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
        print(f'Bank: {self.bank}\nRegion: {self.region}')
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