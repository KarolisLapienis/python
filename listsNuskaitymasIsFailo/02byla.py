with open('02data.txt', 'r+', encoding='utf-8') as f:
    txt = f.read()
    print(txt)
    f.seek(0)  # zymeklio sugrazinimas i bylos pradzia
    t1 = int(f.readline())
    t2 = int(f.readline())
    t3 = int(f.readline())
    s = t1 + t2 + t3
    f.write(f'\n{t1} + {t2} + {t3} = {s}\n')