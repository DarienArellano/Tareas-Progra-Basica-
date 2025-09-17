lista = [1, 2, 3, 4, 5,6,7,8,9,10]
ultimo = lista[-1]
for i in range(1, 11):
    lista.append(ultimo + i)
print("Lista final:", lista)
