lista = [0,1]

for i in range(2, 16):
    soma = lista[i-1] + lista[i-2]
    lista.append(soma)

print(lista)