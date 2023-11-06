# Karolis Lapienis JavaScriptPro
# ciklas for savarankiskas uzduotis 1
# 1. Vienu smūgiu stalius įkala vinį į k cm gylį. Parašykite programą, kuri išspausdintu plaktuko dūžį "Tuk!" su kiekvienu smūgiu, šalia smūgio numerį ir kiek vinies ilgio dar liko neįkaltos. Kalamos vinies ilgis n cm. Baigus kalti vinį, pranešama "Vinis įkalta".


import math

viniesIlgis = int(input("Įveskite vinies ilgį centimetrais: "))
smugioGylis = int(input("Įveskite vieno smugio gylį centimetrais: "))
smugiuKiekis = math.ceil(viniesIlgis/smugioGylis)
likoNeikaltos = viniesIlgis

for smugis in range(1, smugiuKiekis + 1):
    likoNeikaltos = viniesIlgis - (smugis * smugioGylis)
    if likoNeikaltos > 0:
        print(f"Smūgis {smugis}: Tuk! Liko neįkaltos {likoNeikaltos} cm.")
    else:
        print(f"Smūgis {smugis}: Tuk! Vinis įkalta.")