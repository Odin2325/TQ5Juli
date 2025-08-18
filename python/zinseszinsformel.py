print("Zinsenszinformel")
print("=====================================")
K0 = float(input("Geben Sie K0: "))
p = float(input("Geben Sie p: "))
n = int(input("Geben Sie n: "))
K = K0 * (1+p/100)**n
print("Endkapital K:", K)
print("=====================================")
