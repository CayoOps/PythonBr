#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print("================================================================")
print("Bem-vindo!!")
print("Digite as notas dos bimestres!!")
print("================================================================")
print("Se der erro não é um número!!")
print("================================================================")
notab1 = float(input("Digite a nota do 1 Bimestre: "))
notab2 = float(input("Digite a nota do 2 Bimestre: "))
notab3 = float(input("Digite a nota do 3 Bimestre: "))
notab4 = float(input("Digite a nota do 4 Bimestre: "))
print("================================================================")

media = ( notab1 + notab2 + notab3 + notab4 ) / 4

print("Sua média é:" , media)
