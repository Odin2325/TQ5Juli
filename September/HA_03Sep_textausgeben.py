def PythonFragentxt_lesen():
    print("Das sind meine Fragen: \n")    
    fragen = open("./September/PythonFragen.txt", "r", encoding="utf-8")               #r Bedeutet in diese Methode 'lese' modus
    print(fragen.read())
    fragen.close()

PythonFragentxt_lesen()