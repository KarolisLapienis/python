# r
# a
# w

# f = open('01data.txt', 'w', encoding='utf-8')

# f.write('Pirmas kartas su failu\n')

# f.write ('čęąėŠĮŠŲ\n')

# a = [5, 8, 9, 7, 9]
# f.write(a)
# f.write(str(a))
# x = 5
# y = 8
# f.write(f'\n{x} + {y} = {x + y}\n')
# f.close()

# try:
#     f = open('01data1.txt', 'w', encoding='utf-8')
#     f.write('Pirmas kartas su failu\n')
#     f.write ('čęąėŠĮŠŲ\n')
#     a = [5, 8, 9, 7, 9]
#     f.write(str(a))
#     f.write(a)
#     x = 5
#     y = 8
#     f.write(f'\n{x} + {y} = {x + y}\n')
# finally:
#     f.close()


with open('01data1.txt', 'w', encoding='utf-8') as f:
    f.write('Pirmas kartas su failu\n')
    f.write ('čęąėŠĮŠŲ\n')
    a = [5, 8, 9, 7, 9]
    f.write(str(a))
    f.write(a)  # klaida
    x = 5
    y = 8
    f.write(f'\n{x} + {y} = {x + y}\n')