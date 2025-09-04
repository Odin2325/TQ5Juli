from random import randint
from KundeDatei import Kunde
from BankkontoDatei import Bankkonto

class Bank:
    def __init__(self, name, hauptstandort, region, land):
        self.kontos = []
        self.kunden = []
        self.name = name
        self.hauptstandort = hauptstandort
        self.region = region
        self.land = land

    def kunde_schon_existiert(self, vorname, nachname, adresse):
        for kunde in self.kunden:
            if kunde.vorname == vorname and kunde.nachname == nachname and kunde.adresse == adresse:
                return (True,kunde)
        return (False,None)
        #Rueckgabewert ist ein Tupel mit (bool,kunde) oder (bool,None)
    
    def kunde_erstellen(self, vorname, nachname, adresse, telefonnummer, email, alter):
        neuer_kunde = Kunde(vorname, nachname, adresse, telefonnummer, email, alter)
        if not self.kunde_schon_existiert(vorname, nachname, adresse)[0]:
            #0 ist der bool wert aus den Tupel 
            #den wir von die Methode kunde_schon_existiert 
            # bekommen.
            self.kunden.append(neuer_kunde)
            print('Kunde erfolgreich erstellt.')
            return True
        else:
            print('Kunde existiert schon.')
            return False

    def kunde_loeschen(self, vorname, nachname, adresse):
        kunde_existiert_tupel = self.kunde_schon_existiert(vorname,nachname,adresse)
        if kunde_existiert_tupel[0]: 
            #0 ist der bool wert aus den Tupel 
            #den wir von die Methode kunde_schon_existiert 
            # bekommen.
            self.kunden.remove(kunde_existiert_tupel[1]) #1 Ist der Kunde selbst
            print('Kunde erfolgreich geloescht.')
            return True
        else:
            print('Kunde konnte nicht gefunden werden.')
            return False
        
    def bankkonto_loeschen(self, kontonummer):
        for bankkonto in self.kontos:
            #print(bankkonto.kontonummer)
            if bankkonto.kontonummer == kontonummer:
                self.kontos.remove(bankkonto)
                print('Bankkonto erfolgreich geloescht.')
                return True
        print("Dieser Bankkonto konnte nicht gefunden werden.")
        return False

    def bankkonto_erstellen(self,kunde):
        tupel = self.freies_kontonummer_generieren()
        while not tupel[0]:
            tupel = self.freies_kontonummer_generieren()

        neuer_bankkonto = Bankkonto(kunde,tupel[1])
        self.kontos.append(neuer_bankkonto)

    #5-stelliges Kontonummer
    def freies_kontonummer_generieren(self):
        neue_kontonummer = self.fuenf_stellige_kontonummer_erstellen()
        for konto in self.kontos:
            if neue_kontonummer == konto.kontonummer:
                return (False,None)   
        return (True,neue_kontonummer)

    def fuenf_stellige_kontonummer_erstellen(self):
        resultat = ''
        for i in range(0,5):
            resultat += str(randint(0,9))
        return resultat
    
    def bank_details(self) -> str:
        """
       -- Gibt allgemeine Informationen über die Bank zurück
        --(Marketing/Werbung – keine vertraulichen Kundendetails).

        Returns:
            str: Übersicht über Bankname, Standort, Anzahl Kunden und Konten.
        """
        return (
            f" Willkommen bei {self.name}!\n"
            f" Hauptstandort: {self.hauptstandort}, {self.region}, {self.land}\n"
            f" Kundenanzahl: {len(self.kunden)}\n"
            f" Anzahl Konten: {len(self.kontos)}\n"
            f" Ihre zuverlässige Bank seit 1990!"
        )

    def konto_infos(self):
        """
        Gibt Informationen zu allen existierenden Bankkonten aus.
        Nutzt die details()-Methode von Bankkonto.
        """
        if not self.kontos:
            print("Es sind aktuell keine Bankkonten vorhanden.")
            return
        for konto in self.kontos:
            konto.details()

    def kunden_infos(self):
        """
        Gibt Informationen zu allen existierenden Kunden aus.
        Nutzt die detail_kunde(True)-Methode von Kunde.
        """
        if not self.kunden:
            print("Es sind aktuell keine Kunden vorhanden.")
            return
        for kunde in self.kunden:
            kunde.detail_kunde(True)

   
   
   
   
    def transaktion(self, von_konto_nummer: str, zu_konto_nummer: str, betrag: float) -> bool:
        """
        Führt eine Transaktion zwischen zwei Bankkonten durch,
        wenn beide in der Bank existieren.

        Args:
            von_konto_nummer (str): Kontonummer des Senders.
            zu_konto_nummer (str): Kontonummer des Empfängers.
            betrag (float): Betrag der Transaktion.

        Returns:
            bool: True, wenn erfolgreich, False sonst.
        """
        von_konto = None
        zu_konto = None

        # Konten suchen
        for konto in self.kontos:
            if konto.kontonummer == von_konto_nummer:
                von_konto = konto
            if konto.kontonummer == zu_konto_nummer:
                zu_konto = konto

        if not von_konto or not zu_konto:
            print("❌ Eines oder beide Konten existieren nicht.")
            return False

        # Transaktion ausführen
        return von_konto.transaktion(zu_konto, betrag)
