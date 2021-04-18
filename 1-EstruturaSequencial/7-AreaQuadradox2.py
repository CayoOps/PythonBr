#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("================================================================")
print("Bem vindo ao caculador de área de quadrados!")
print("Se der erro não é um número!!")
print("================================================================")
lado1 = float(input("Digite o tamanho da base do quadrado: "))
lado2 = float(input("Digite o tamanho da altura do quadrado: "))
print("================================================================")
area = lado1 * lado2

print("A área do quadrado é, %.1f" %area)

dobro = area * 2
print("================================================================")
print("O dobro da área é, %.1f" %dobro)
print("================================================================")
