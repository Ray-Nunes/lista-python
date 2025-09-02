valor = int(input("Digite um valor: "))
qtd = 0

if valor <= 1:
    print("Digite um valor positivo.")
else:
    for contador in range(1, valor + 1):
        if valor % contador == 0:
            qtd += 1

if qtd == 2:
    print(f"O numero {valor} é primo.")
else:
    print(f"O numero {valor} não é primo")
