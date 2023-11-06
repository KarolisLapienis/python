# Karolis Lapienis JavaScriptPro
# ciklas for savarankiskas uzduotis 2
# 2. Keturženklis skaičius turi tokią įdomią savybę: (30 + 25)^2 = 3025. Reikia parašyti programą, kuri tikrintų ir išvestų visus keturženklius skaičius, pasižyminčius šia savybe, ir suskaičiuotų jų kiekį.


skaiciuKiekis = 0

for skaicius in range(1000, 10000):
    duPriekioSkaitmenys = int(str(skaicius)[:2])  # Atskiriame 2 pirmus skaitmenis
    duGaloSkaitmenys = int(str(skaicius)[2:])  # Atskiriame 2 skaitmenis nuo galo

    if (duPriekioSkaitmenys + duGaloSkaitmenys) ** 2 == skaicius:
        print(skaicius)
        skaiciuKiekis += 1

print(f"Rasti {skaiciuKiekis} skaičiai pasižymintys šia savybe")