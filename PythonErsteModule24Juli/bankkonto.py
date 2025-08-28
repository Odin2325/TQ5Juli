class Bankkonto:
    def __init__(self,kontoinhaber,kontonummer,startguthaben=0):
        self.kontoinhaber = kontoinhaber
        self.kontonummer = kontonummer
        self.startguthaben = startguthaben
        self.Währung ='EUR'
        self.bankname ='sparkasse'

    def bank_detail(self):
        print(f"bankdetail:\n kontoinhab={self.kontoinhaber}\n kontonummer = {self.kontonummer}\n startguthaben ={self.startguthaben}\n wärung = {self.Währung}\n bankname={self.bankname}")   


mein_konto = Bankkonto('saba',34527799,53) 
mein_konto.bank_detail()