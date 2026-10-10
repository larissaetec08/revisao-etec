# Aprendizagem e revisão da linguagem Python

# Comentario: descreva a intenção do trecho do codigo-fonte
print("ola,python!")
print("a soma é:",(3 + 5))
print("\n")

# Variaveis e tipos
nome = "Ana"
idade = 17
altura = 1.65
matriculado = True

for valor in [nome, idade, altura, matriculado]:
    print(valor,type(valor))

print("\n")

# Entrada de dados e conversão
nome = input("nome:")
idade = int(input("idade:"))
print(f"{nome} tera {idade+1} anos no proximo aniversario!")

print("tipo do nome:",type(nome))
print("tipo de idade:",type(idade))
print("\n")

# Operações aritmericas
a, b = 10,3
print((a+b),(a-b),(a*b))
print((a / b),( a // b),(a % b), (a ** b))
print("par?",12 % 2 == 0)

idade = 19
autorizado = True
print(idade >= 18 and autorizado)
print(idade < 18 or not autorizado)
print(idade == 19, idade != 19)
print("\n")

# Decisões com if,elif e else
nota = float(input("nota: "))
if nota >= 7:
    print("Aprovado,Parabens!")
elif nota >= 5:
    print("cuidado, recuperação!")
else:
    print("infelizmente foi reprovado")
print("\n")