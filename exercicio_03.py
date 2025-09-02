print("Operação - Adição")

while 1:

    valor1 = int(input("Digite um numero: "))
    valor2 = int(input("Digite outro numero: "))

    print(f"{valor1} + {valor2} = {valor1+valor2}")

    continuar = input("Deseja realizar mais uma soma: ")

    if continuar == "sim":
        continue
    else:
        break

