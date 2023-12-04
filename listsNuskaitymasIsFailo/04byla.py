def sukurtiBylas(failas, tekstas):
    with open(failas, 'w', encoding='utf-8') as f:
        f.write(tekstas)


def nuskaitytiBylas(failas):
    with open(failas, 'r', encoding='utf-8') as f:
        info = f.readline()
    return info

for i in range(1, 21):
    sukurtiBylas(f'{i}byla.txt', f'{i} byloje irasyta informacija\n')

for i in range(1, 21):
    print(nuskaitytiBylas(f'{i}byla.txt'))

