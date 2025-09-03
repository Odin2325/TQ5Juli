#Methode zum formattieren einer liste
# {234 - 54 - 61 - 87} in diese Form zurueckgibt

def sonderzeichen_entfernen(text:str):
    resultat = ''
    for zeichen in text:
        if zeichen.isdigit():
            resultat += zeichen
    return resultat

def vorwahl_entfernen(text:str):
    if len(text)==11 and text[0]=='1':
        return text[1:]
    elif len(text)==10:
        return text
    else:
        print('Fehler: Zu viele Zahlen in dieses String.')
        raise ValueError
    
def telefonnummer_extrahieren(text:str):
    return vorwahl_entfernen(sonderzeichen_entfernen(text))