valores = []
qtd = int(input("Digite uma quantidade N de numero para saber qual é o maior: "))

for i in range(qtd):
    valor = int(input(f"Digite o {i+1}° valor: "))
    valores.append(valor)

if not valores:
    print('Nenhum valor informado.')
else:
    maior = menor = valores[0]
    for x in valores[0:]:
        if x > maior:
            maior = x
        if x < menor:
            menor = x

soma = maior + menor

print("maior", maior)
print("menor",menor)
print("Soma",soma)

