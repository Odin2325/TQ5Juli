class bank:
    def __init__(self,name,region):
        self.name = name
        self.region = region

    def  banksuchen_deteil(self,alle_anzeige):
        if  alle_anzeige:
            print({f"{self.name},{self.region}"})
        else:
            return f' {self.region}' 
        