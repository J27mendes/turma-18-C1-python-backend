'''I. Exercícios de If / Else / Elif'''
# 1. Par ou ímpar
num = int(input("escreva um numero, por favor! "))
print(num)
if(num % 2 == 1): print("Este numero é impar")
else:(print("este numero é par"))

# 2. Maioridade
idade = int(input("escreva sua idade por favor! "))
if(idade >= 18):print("você é maior de idade.")
else:(print("você é menor de idade!"))

# 3. Senha secreta
senha = "python123"
comparativo = input("Escreva sua senha, por favor! ")

if senha != comparativo:
    print(f"{comparativo} - Esta senha não é a senha correta")
else:
    print("Senha de acesso permitida!")

# 4. Nota escolar
nota = int(input("escreva qual foi sua nota! "))
if(nota >= 9): print("Excelente")
elif(nota >= 7): print("Bom")
elif(nota < 7): print("precisa melhorar")

# 5. Temperatura
temp = float(input("escreva a temperatura em celsius! "))
if(temp >= 30): print("Muito quente")
elif(temp < 15): print("Frio")
else: print("Clima agradável")

# 6. Dia da semana
numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Dia inválido")

# 7. Maior de três números
num1 = int(input("escreva o primeiro! "))
num2 = int(input("escreva o segundo numero! "))
num3 = int(input("escrava o terceiro numero! "))

if num1 > num2 and num1 > num3: print("o primeiro que digitou escreveu o maior numero!")
elif num2 > num1 and num2 > num3: print("o segundo que digitou escreveu o maior numero")
elif(num3 > num1 and num3 > num2): print("o terceiro que digitou escreveu o maior numero!")

# 8. Classificação etária
numero = int(input("digite sua idade! "))
if 0 <= numero <= 12:
    print("Criança")
elif 13 <= numero <= 17:
    print("Adolescente")
elif 18 <= numero <= 64:
    print("Adulto")
elif numero >= 65:
    print("Idoso")

# 9. Triângulo
lado1 = int(input("digite o primeiro lado! "))
lado2 = int(input("digite o segundo numero! "))
lado3 = int(input("digire o terceiro numero! "))

if lado1 == lado2 and lado2 == lado3: print("Equilátero")
elif lado1 != lado2 and lado2 == lado3: print("Isósceles")
elif lado1 == lado3 and lado3 != lado2: print("Isósceles")
elif lado1 == lado2 and lado2 != lado3: print("Isósceles")
else : print("Escaleno")

compra = float(input("Digite o valor da compra: R$ "))

# Aplica o desconto
if compra >= 500:
    desconto = 0.10  
elif compra >= 200:
    desconto = 0.05  
else:
    desconto = 0  

valor_final = compra * (1 - desconto)

print(f"Valor final da compra: R$ {valor_final:.2f}")

'''II. Exercícios de Laços de Repetição
(Loops)'''

# 1. Contar de 1 a 10
for i in range(1, 11):
    print(i)

# 2. Contar de 10 a 1
for i in range(10, 0, -1):
    print(i)

# 3. Somar números de 1 a 100
soma = 0
for i in range(1, 101):
    soma += i

print(f"A soma dos números de 1 a 100 é: {soma}")

# 4. Mostrar números pares de 0 a 50
for i in range(51): 
    if i % 2 == 0: 
        print(i)

#5. Mostrar números ímpares de 0 a 50
for i in range(1, 51, 2):
    print(i)

# 6. Tabuada do 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

#7. Tabuada personalizada
numero = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 8. Contagem regressiva
numero = 10
while numero >= 0:
    print(numero)
    numero -= 1 

soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    soma += numero  

print(f"A soma dos números informados é: {soma}")

# 10. Média de notas
soma = 0

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota  

media = soma / 3

print(f"A média das notas é: {media:.2f}")

# 11. Número positivo ou negativo
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    if numero >= 0:
        print(f"O {i+1}º número ({numero}) é positivo.")
    else:
        print(f"O {i+1}º número ({numero}) é negativo.")


# 12. Listar elementos de uma lista
nomes = ["Addrielly", "Maycon", "João", "Maria", "Luiz"]

for nome in nomes:
    print(nome)
    
# 13. Contar letras de uma palavra
palavra = input("Digite uma palavra: ")

contador = 0

for letra in palavra:
    contador += 1  

print(f"A palavra '{palavra}' tem {contador} letras.")

#14. Palíndromo
palavra = input("Digite uma palavra: ")

palindromo = True

# Verifica se a palavra é igual a ela mesma de trás pra frente
for i in range(len(palavra) // 2):
    if palavra[i] != palavra[len(palavra) - 1 - i]:
        palindromo = False
        break

if palindromo:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

# 15. Senha até acertar
senha_correta = "python123"

while True:
    senha = input("Digite a senha: ")
    
    if senha == senha_correta:
        print("Senha correta! Acesso permitido.")
        break  
    else:
        print("Senha incorreta. Tente novamente.")

# 16. Tabuada interativa
while True:
    numero = int(input("Digite um número para ver sua tabuada: "))
    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    
    resposta = input("Deseja ver outra tabuada? (s/n): ").lower()
    
    if resposta != 's':
        print("Programa encerrado. Até logo!")
        break

# 17. Soma de pares
soma_pares = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero % 2 == 0:
        soma_pares += numero 

print(f"A soma dos números pares é: {soma_pares}")

# 18. Contagem de vogais
frase = input("Digite uma frase: ")

contador_vogais = 0

vogais = "aeiouAEIOU"

for letra in frase:
    if letra in vogais:  
        contador_vogais += 1  

# Exibe o resultado
print(f"A frase contém {contador_vogais} vogais.")

# 19. Números primos até N
N = int(input("Digite um número N: "))

print(f"Números primos até {N}:")
for numero in range(2, N + 1):
    divisor = 2
    while divisor <= numero // 2:
        if numero % divisor == 0:
            break 
        divisor += 1
    else:
        print(numero)

# 20. Jogo de adivinhar número
import random

numero_aleatorio = random.randint(1, 10)

tentativas = 0

while True:
    tentativa = int(input("Tente adivinhar o número entre 1 e 10: "))
    tentativas += 1
    
    if tentativa < numero_aleatorio:
        print("O número é maior. Tente novamente.")
    elif tentativa > numero_aleatorio:
        print("O número é menor. Tente novamente.")
    else:
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
        break