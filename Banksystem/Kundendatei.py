import datetime
import random
#from Bankkontodatei import Bankkontoklasse as Bankkonto
#from Bankdatei import Bankklasse as Bank

class Kundenklasse:
    def __init__(self, vorname, nachname, geburtsdatum, adresse, telefonnummer, email):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.alter = 35 #self.alter_berechnen()
        self.kundennummer = self.kundennummer_generator()
        self.adresse = adresse
        self.telefonnummer = telefonnummer
        self.email = email
        self.name = vorname + " " + nachname
        self.geschlecht = None

    def kundennummer_generator(self):
        kundennummer = "".join([str(random.randint(0, 9)) for _ in range(10)])
        print(f"Generierte Kundennummer: {kundennummer}")
        return kundennummer

    def alter_berechnen(self):
        heute = datetime.date.today()
        alter = heute.year - self.geburtsdatum.year
        # Prüfe, ob der Geburtstag in diesem Jahr schon war
        if (heute.month, heute.day) < (self.geburtsdatum.month, self.geburtsdatum.day):
            alter -= 1
        return alter

    def Kundendetails(self):
        print(f"Name: {self.name}\n Alter {self.alter}\nAdresse: {self.adresse}\nTelefonnummer: {self.telefonnummer}\n E-Mail: {self.email}\n Geschlecht: {self.geschlecht}")

