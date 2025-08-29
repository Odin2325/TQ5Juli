class Bank:
    def __init__(self, name, leiter, adresse, region):
        self.name = name
        self.leiter = leiter
        self.adresse = adresse
        self.region = region
        self.bankkonten = 0
        self.kunden_liste = []
        self.konten_liste = []
