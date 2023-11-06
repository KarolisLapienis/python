# Karolis Lapienis JavaScriptPro
# python uzduotis 7S

abc = input("Iveskite trikampio krastiniu ilgius a, b, c: ")
a, b ,c = map(int, abc.split())
print(a, b, c)



if (a == b == c):
    triangleType = "Trikampis yra lygiakrastis"

elif (a == b or b == c or a == c):
    triangleType = "Trikampis yra lygiasonis"

elif (
    (a**2 + b**2 == c**2) 
    or (b**2 + c**2 == a**2) 
    or (a**2 + c**2 == b**2)):
    triangleType = "Trikampis yra statusis"

elif ((a + b <= c) or (a + c <= b) or (b + c <= a)):
    triangleType = "Trikampio sudaryti negalima"

else:
        triangleType = "Trikampis yra ivairiakrastis"

print(triangleType)