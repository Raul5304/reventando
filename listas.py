#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe


lista = [11,22,33]
print(len(lista))

lista = list(range(1000))

for pos in range(len(lista)):
    print(pos)
    if pos == 0:
        pass
    else:
        lista[pos] += lista[pos-1]

print(lista)
