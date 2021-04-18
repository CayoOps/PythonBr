#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

print("================================================================")
print("Bem-vindo ao calculador de área de circunferência!!")
print("Se der erro não é um número!!")
print("================================================================")
raio = float(input("Digite o raio em metros da circunferência: "))

area = 3.14 * raio**2
print("================================================================")
print("A area da circunferência é %.2f Metros!" %area)
