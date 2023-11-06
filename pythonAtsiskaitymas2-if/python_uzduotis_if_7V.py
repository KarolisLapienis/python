# Karolis Lapienis JavaScriptPro
# python uzduotis 7V

ab = input("Iveskite kainas a ir b: ")
a, b = map(float, ab.split())
print("kaina a:", a, "kaina b:", b)

n1n2n3 = input("Iveskite kiekius n1, n2, n3: ")
n1, n2, n3 = map(int, n1n2n3.split())
print("kiekis n1:", n1, "kiekis n2:", n2, "kiekis n3:", n3)

k = float(input("Iveskite bandeles kaina: "))
print("bandeles kaina:", k)

if (k <= a):
    suma = round(n1*k, 2)
elif (a < k < b):
    suma = round(n2*k, 2)    # panaudojau round, kad nebutu 000000000000000000004
else:
    suma = round(n3*k, 2)

print("Uz bandeles bus sumoketa:", suma, "eur.")