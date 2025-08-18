x1 = input ("Gib ein Name x1 ein: ")
if x1[-1:] == "." or x1[-2:] == "r!":
    print ("treu")
elif x1[:5] == "Hallo":
    print ("Treu")
else:
    print ("false")
