valores = []
qtd = int(input("Digite uma quantidade N de numero para saber qual é o maior: "))
repeticao = 1

while repeticao <= qtd:

    for i in range(qtd):
        valor = int(input("Digite um valor entre 0 e 1000: "))

        if valor >= 0 and valor <= 1000:
            valores.append(valor)
            repeticao += 1
            break
        else:
            print("O valor digitado deve ser entre 0 e 1000: ")
            
maior = menor = valores[0]
for x in valores[0:]:
    
    if x > maior:
        maior = x

    if x < menor:
        menor = x

soma = maior + menor
print("maior", maior)
print("menor", menor)
print("Soma", soma)

            
        


