a = []
for cont in range (20):
    a.append(int(input('digite um valor: ')))
b = []
for i in a:
    if i % 2 == 0:
        b.append(i * 3)
    else:
        b.append(i/2)
    i += 1

print(f'A - {a}')
print(f'B - {b}')
