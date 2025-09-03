def formatierte_liste(liste:list):
    """
    Formats a list of strings into a single string with elements separated by ' - ' and enclosed in curly braces.

    Args:
        liste (list): A list of strings to format.

    Returns:
        str: A formatted string representation of the list, e.g., '{a - b - c}'.
    """
    resultat = '{'
    for element in liste:
        if element == liste[-1]:
            resultat += element
        else:
            resultat += element + ' - '
    resultat += '}'
    return resultat

def sonderzeichen_entfernen(text:str):
    """
    Entfernt alle Zeichen aus dem gegebenen Text, die keine Ziffern sind.

    Args:
        text (str): Der Eingabetext, aus dem Sonderzeichen entfernt werden sollen.

    Returns:
        str: Ein String, der nur die Ziffern aus dem Eingabetext enthält.
    """
    resultat = ''
    for zeichen in text:
        if zeichen.isdigit():
            resultat += zeichen
    return resultat

def vorwahl_entfernen(text:str):
    """
    Removes the leading '1' from an 11-digit phone number string, if present.

    Args:
        text (str): The phone number string to process.

    Returns:
        str: The phone number string without the leading '1' if it was present.

    Raises:
        ValueError: If the input string does not have 10 or 11 digits.
    """
    if len(text)==11 and text[0]=='1':
        return text[1:]
    elif len(text)==10:
        return text
    else:
        print('Fehler: Zu viele Zahlen in dieses String.')
        raise ValueError
    
def telefonnummer_extrahieren(text:str):
    return vorwahl_entfernen(sonderzeichen_entfernen(text))