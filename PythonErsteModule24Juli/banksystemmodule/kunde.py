class Kunde:
    def __init__(self, vorname,nachname, adresse,telefonnummer):
        self.vorname=vorname
        self.nachname=nachname
        self.adresse=adresse
        self.telefonnummer=telefonnummer
        

    def details_kunde(self,zeige_alles):
       if zeige_alles:
         print(f"vorname:{self.vorname}\n nachnam:{self.nachname}\n adress:{self.adresse}\n telefonnummer:{self.telefonnummer}")
        
       else:
          return f"{self.vorname}\n{self.nachname}"
       