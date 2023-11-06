# Karolis Lapienis JavaScriptPro
# ciklas for savarankiskas uzduotis 4
# Kartais žmonėms būna sunku prisiminti, kokia šiandien yra savaitės diena, o ir kalendorius ne visada būna po ranka. Parašykite programą, kuri išspausdintų vieno mėnesio savaitės dienų sąrašą nuo a dienos iki b dienos, jei žinoma, kad mėnuo prasidėjo m-tąją savaitės dieną. Savaitės dienos numeruojamos taip: 1-pirmadienis, 2-antradienis ... 7 - sekmadienis.

pirmaMenesioDiena = int(input('Kokia savaites diena prasideda menuo? '))
dienuIntervalas = input("Iveskite menesio dienu intervala su tarpu: ")
intervaloPradzia, intervaloPabaiga = map(int, dienuIntervalas.split())

for diena in range(intervaloPradzia, intervaloPabaiga + 1):
    savaitesDiena = ((pirmaMenesioDiena + diena - 2) % 7) + 1
    print(f'{diena}-oji diena: {savaitesDiena}')