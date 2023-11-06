  # Karolis Lapienis JavaScriptPro 
  # if uzduotis 7

print("staciakampis NR1.")
krastine1X = int(input("Irasykite X krastines ilgi: "))
krastine1Y = int(input("Irasykite Y krastines ilgi: "))
staciakampis1plotas = krastine1X * krastine1Y
print("Staciakampio NR1. plotas: ", staciakampis1plotas)

print("staciakampis NR2.")
krastine2X = int(input("Irasykite X krastines ilgi: "))
krastine2Y = int(input("Irasykite Y krastines ilgi: "))
staciakampis2plotas = krastine2X * krastine2Y
print("Staciakampio NR2. plotas: ", staciakampis2plotas)

print("staciakampis NR3.")
krastine3X = int(input("Irasykite X krastines ilgi: "))
krastine3Y = int(input("Irasykite Y krastines ilgi: "))
staciakampis3plotas = krastine3X * krastine3Y
print("Staciakampio NR3. plotas: ", staciakampis3plotas)

if (
    (staciakampis1plotas <= staciakampis2plotas <= staciakampis3plotas) 
    or (staciakampis1plotas > staciakampis2plotas > staciakampis3plotas)):
    rectAreaMid = staciakampis2plotas
  
# Pakeiciau i angliska varianta, nes labai sunkiai skambejo Lietuviskai :D
    
elif (
    (staciakampis2plotas <= staciakampis1plotas <= staciakampis3plotas) 
    or (staciakampis2plotas > staciakampis1plotas > staciakampis3plotas)):
    rectAreaMid = staciakampis2plotas

else:
    rectAreaMid = staciakampis3plotas

print("Vidutinio staciakampio plotas: ", rectAreaMid)
