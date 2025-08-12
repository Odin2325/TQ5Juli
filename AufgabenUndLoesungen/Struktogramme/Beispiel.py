#UhrBegruessungs System

begruessung = ""
uhrzeit = input("Bitte geben Sie die Uhrzeit ein (0-23): ")

if uhrzeit < 12:
    begruessung = "Guten Morgen!"
elif uhrzeit < 18:
    begruessung = "Guten Tag!"
else:
    begruessung = "Guten Abend!"

print(begruessung)