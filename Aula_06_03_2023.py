# nome = "João Pedro"
# sobrenome = "Nunes da Silva"
# idade = 21
# altura = 1.70
# peso = "70kg"
# maiordeidade = idade >= 18
# print (nome, sobrenome, sep=" ")
# print("Idade: " , idade)
# print("Altura: " , altura)
# print("Peso: ", peso)
# print ("É maior de idade: " , maiordeidade)

adicao = 2 + 2
substracao = 2-2
multiplicacao = 2*2
divisao = 10/3
divisao_inteiro=10//3 #pega o número inteiro, o resto da divisão ignora
modulo = 10 % 4
potencia = 2**3

print(adicao)
print(substracao)
print("A multiplicação é " , multiplicacao)
print("A divisao é ", divisao)
print("A divisao é ", divisao_inteiro)
print("O modulo é "), modulo
print("A potência é ", potencia)

unir = "João " + "Pedro"
print (unir)
cinco_vezes ="O Matheus, pode ser um pouco duro as vezes" * 5
print (cinco_vezes)

#format
a = "João Pedro"
b = 21
c = " anos"
texto = "O meu nome é: {nome}"
exibir = texto.format(nome=a)
print(exibir)

texto2 = "Tenho {0} {1}"
exibir2 = texto2.format(b,c)
print(exibir2)

# nome = input ("Qual o seu nome?")
# time = input ("Qual é o melhor time?")
# print(time)

# print (f"O melhor time é: {time}")

#condição

pergunta = input("Qual a sua cidade de nascimento? ")
if pergunta == "Ivaiporã":
    print("Você é Ivaiporãense")
else:
    print(~"Não pertence a cidade de Ivaiporã")