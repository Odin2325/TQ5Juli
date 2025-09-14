from datetime import datetime
from random import randint
from kunde import Kunde
class Bankkonto:
    def __init__(self, kontoinhaber:Kunde, startguthaben=0,):

        self.kontoinhaber=kontoinhaber
        self.kontonummer= 'DE12346789012'
        
        
        self.bankname='sparda'
        self.stadt='münchen'
        self.währung='euro'
        self.kontostand=startguthaben
        self.pin=Bankkonto.pin_genrator()
        self.transaction_historie=[]
     
    def pin_genrator():
        neues_pin=''
        for i in range(0,4):
            neues_pin+=str(randint(0,9))
        print('das neu pin ist',neues_pin)
        return neues_pin

        
    def details(self):
        print('konto details')
        print("----------------")
        print(f"kontoinhaber::{self.kontoinhaber}\n adresse:{self.bankname}") 
        print(f'Kontonummer: {self.kontonummer}\nKontostand: {self.kontostand}\n stadt:{self.stadt}\n währung:{self.währung}\n')
        print('=======================================')   
    
    def einzahlen(self,betrag):
        if betrag>0:
         self.kontostand+=betrag
         self.transaction_historie.append(('einzahlen',betrag,self.kontostand,datetime.now()))
         print(f'kontostand wurde erhöht {betrag:.2f}{self.währung} eingezahlt.')
         return True

    def auszahlen(self,betrag):
        if betrag<= self.kontostand:
            self.kontostand-=betrag 
            self.transaction_historie.append(('auszahlen',betrag,self.kontostand,datetime.now()))
            print(f"betrag{betrag} wurde ausgezzahlt")
            return True
    def kontostand_ansehen(self):        
        print(f"kontostand wurd geleert {self.kontostand}")

    def zeige_transaction(self):
        print('--------start transaction-----------')
        for eintrag in self.transaction_historie:
            print(eintrag)
        print('-------------endtransaction------------')