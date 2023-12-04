def skaitytiDuom():
    with open('08data.txt', 'r', encoding='utf-8') as f:
        txt = []
        while True:
            eil = f.readline()
            if eil:
                txt.append(eil)
            else:
                break
    return txt




print(skaitytiDuom())

visiDuom = skaitytiDuom()
skaiciai = []
skaiciai = []
for eil in visiDuom:
    eilSk = [int(x) for x in eil.split(' ') if x!= '\n']
    print(eilSk)
    if len(eilSk) != 0:
        skaiciai.append(eilSk)
print(skaiciai)
print(skaiciai[0][0])