# Karolis Lapienis JavaScriptPro
# ciklas for savarankiskas uzduotis 8
# Vasaros pradžioje prasideda braškių sezonas. Pirmąją dieną lysvėje prinoko b braškių. Kiekvieną kitą dieną prinoksta d braškių daugiau, negu prieš tai buvusią. Parašykite programą, skaičiuojančią, kiek prinokusių braškių k bus po n dienų. Pasitikrinkite: kai b =4, d = 5, n = 3, tuomet kompiuterio ekrane turi būti rodoma: Per 3 dienas prinoko 27 braškės.


b = int(input("Iveskite kiek braskiu prinoko pirmaja diena: "))
d = int(input("Iveskite kiek daugiau braskiu prinoksta kiekviena sekancia diena: "))
n = int(input("Iveskite dienu skaiciu: " ))
k = 0  # braskiu suma

for diena in range(1, n + 1):
    k += b + (d * (diena - 1))
      # print(diena, k)  # testas

print(f"Per {n} dienas prinoko {k} braskes.")