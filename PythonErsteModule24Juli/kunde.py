class kunde:
    def __init__(self,vorname,nachname,adresse,telefonnummer):
        self.vorname=vorname
        self.nachname=nachname
        self.adresse=adresse
        self.telefonnummer=telefonnummer


    def kunde_deteil(self):
        print(f"kundedetail:\n vorname={self.vorname}\n nachname={self.nachname}\n adresse={self.adresse}\n telefonnummer={self.telefonnummer}")
        return True


erste_kunde=kunde('saba','farhan','reger str.112','0123456')
erste_kunde.kunde_deteil()