import math
print("=====================================")
print("Distanz zwischen zwei Punkten")

x1 = float(input("Geben Sie x1: "))
y1 = float(input("Geben Sie y1: "))
x2 = float(input("Geben Sie x2: "))
y2 = float(input("Geben Sie y2: "))

distanz = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print ("Distanz zwischen zwei Punkten:", distanz)
print("=====================================")