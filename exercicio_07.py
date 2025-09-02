imformacoes = [
    [" ","Nome tem 3 caracteres", "Nome maior que 3 caracteres", "Nome menor que 3 caracteres"],
    [" ", "Idade menor que 0", "Idade está entre 0 e 150", "Idade maior que 150"],
    [" ", "Salario menor que 0", "Salario maior que 0"],
    [" ", "F", "M"],
    [" ", "S", "C", "V", "D",]
]

perguntas = [
    "Qual o seu nome: ",
    "Qual a sua idade: ",
    "Qual o seu salario: ",
    "Qual o seu sexo: ",
    "Qua o seu estado civil: "
]

for i in range(5):
    imformacoes[i][0] = input(perguntas[i])

nome = imformacoes[0][0]
if len(nome) == 3:
    print(imformacoes[0][1])
elif len(nome) > 3:
    print(imformacoes[0][2])  
else:
    print(imformacoes[0][3])


idade = int(imformacoes[1][0])
if idade < 0:
    print(imformacoes[1][1])
elif idade > 0 and idade < 150:
    print(imformacoes[1][2])
else:
    print(imformacoes[1][3])


salario = float(imformacoes[2][0])
if salario < 0:
    print(imformacoes[2][1])
else:
    print(imformacoes[2][2])


sexo = imformacoes[3][0].upper()
if sexo == "F":
    print(imformacoes[3][1])
elif sexo == "M":
    print(imformacoes[3][2])
else:
    print("Sexo inválido!")


estado_civil = imformacoes[4][0].upper()
if estado_civil in imformacoes[4][1:]:
    print(f"Estado civil: {estado_civil}")
else:
    print("Estado civil inválido!")
