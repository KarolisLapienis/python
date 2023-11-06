# Karolis Lapienis JavaScriptPro
# ciklas for savarankiskas uzduotis 9
# Paskutinis knygos puslapis pažymėtas skaičiumi 710. Kiek reikia skaitmenų knygos puslapiams sunumeruoti (numeracija pradedama nuo vieneto)?


paskutinisPuslapis = 710
puslapiuSkaitmenuKiekis = 0

for puslapioNumeris in range(1, paskutinisPuslapis + 1):
    puslapiuSkaitmenuKiekis += len(str(puslapioNumeris))

print(puslapiuSkaitmenuKiekis)