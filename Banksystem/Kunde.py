import datetime


class Kunde:
    def __init__(self, vorname, nachname, geburtsdatum, adresse, telefonnummer, email):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.alter = self.alter_berechnen()
        self.adresse = adresse
        self.telefonnummer = telefonnummer
        self.email = email
        self.name = vorname + " " + nachname
        self.geschlecht = None


    def alter_berechnen(self):
        heute = datetime.date.today()
        alter = heute.year - self.geburtsdatum.year
        # Prüfe, ob der Geburtstag in diesem Jahr schon war
        if (heute.month, heute.day) < (self.geburtsdatum.month, self.geburtsdatum.day):
            alter -= 1
        return alter

    def Kundendetails(self):
        print(f"Name: {self.name}\n Alter {self.alter}\nAdresse: {self.adresse}\nTelefonnummer: {self.telefonnummer}\n E-Mail: {self.email}\n Geschlecht: {self.geschlecht}")

kunde1 = Kunde("Paul","Atreides",datetime.date(2000,5,15),"Wüstenplanet Arrakis","0123456789","PA@so.wa")