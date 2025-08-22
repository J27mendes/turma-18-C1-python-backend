'''nome = "Jessé"

idade = 35

while idade <= 40:
    print(f"{nome} com {idade} anos")
    idade += 1

print("fim!")   '''

''' numero = int(input("Digite um número inteiro positivo: "))

while numero >= 0:
    print(numero)
    numero -= 1

print("fim!") '''

'''num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2

controle = None

while controle != 0:
    try:
        controle = int(input("Digite 0 para ver a soma: "))
    
    except ValueError:
        print("Entrada inválida. Por favor, digite o número 0.")

print(f"A soma dos números é: {soma}")'''

'''for nome in "Jesse":
    print(nome)''' 

'''notas = []

for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("\nNotas dos alunos:", notas)
print(f"A média das notas é: {media:.2f}")'''