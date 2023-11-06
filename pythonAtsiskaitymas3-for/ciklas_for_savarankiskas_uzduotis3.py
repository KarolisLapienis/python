# Karolis Lapienis JavaScriptPro
# ciklas for savarankiskas uzduotis 1
# Parašykite programą simpatiškajai eilutei 7 + 77 + 777 + ... apskaičiuoti. Pradinis duomuo – paskutinio nario septynetų skaičius.


paskNarioSkaicius= int(input("Iveskite paskutinio nario septynetu skaiciu: "))  #
nariuSuma = 0  # suma

for narioSkaicius in range(1, paskNarioSkaicius + 1):
    nariuSuma += int("7" * narioSkaicius)

print("Simpatisksios eilutes nariu suma:", nariuSuma)