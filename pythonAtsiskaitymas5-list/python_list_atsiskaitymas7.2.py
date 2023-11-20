# Karolis Lapienis JavaScript pro
# Python list atsiskaitymas 
# Uzduotis 7.2

prekiuKiekiai1 = [int(kiekis) for kiekis in input("Iveskite turimu prekiu kiekius atskirtus tarpais: ").split()]

prekiuParduota1 = [int(kiekis) for kiekis in input("Iveskite kiek prekiu parduota per para, kiekius atskirkite tarpais: ").split()]

def prekiuLikucioSkaiciavimas(prekiuKiekiai, prekiuParduota):
    likusiosPrekes = []
    for kiekis in range(len(prekiuKiekiai)):
        likusiosPrekes.append(prekiuKiekiai[kiekis] - prekiuParduota[kiekis])
    return likusiosPrekes

prekiuLikutis1 = prekiuLikucioSkaiciavimas(prekiuKiekiai1, prekiuParduota1)
prekesNumeris = 1

print(f"Pradiniai duomenys. prekiuKiekiai1: {prekiuKiekiai1}, prekiuParduota1: {prekiuParduota1}")
for kiekis in prekiuLikutis1:
    print(f"Prekes NR.{prekesNumeris} likutis: {kiekis}.")
    prekesNumeris +=1
