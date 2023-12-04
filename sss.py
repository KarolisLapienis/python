smugiuKiekis = int
viniesIlgis = 16
smugioIlgis = 3


smugiuKiekis = (viniesIlgis // smugioIlgis)

if((viniesIlgis % smugiuKiekis) > 0):
   smugiuKiekis += 1

for i in range(smugiuKiekis):
    print(i)
