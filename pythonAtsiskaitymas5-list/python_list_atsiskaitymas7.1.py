# Karolis Lapienis JavaScript pro
# Python list atsiskaitymas 
# Uzduotis 7.1

masyvas1 = [int(skaicius) for skaicius in input("Iveskite sveikuosius skaicius atskirtus tarpais: ").split()]

def sumuotiNeigiamusNelyginius(masyvas):
    suma = 0
    for skaicius in masyvas:
        if (skaicius < 0) and (skaicius % 2 != 0):
            suma += skaicius
    return suma

sumNegativeOdd1 = sumuotiNeigiamusNelyginius(masyvas1)  # angliskai, nes trumpiau

print(f"Pradiniai duomenys: {masyvas1}")
print(f"Neigiamu nelyginiu skaiciu suma sarase: {sumNegativeOdd1}")
