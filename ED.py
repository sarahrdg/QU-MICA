# 1
#for i in range(0 , 21 , 2):
#    print(i)

#2
'''
num = int(input("Digite o número para que represente o início do intervalo:\n "))
numf = int(input("Digite o final do intervalo:\n"))

for i in range(num + 1 , numf):
    print(i) 
'''
#3
soma = 0

num = int(input("Digite o número para que represente o início do intervalo:\n "))
numf = int(input("Digite o final do intervalo:\n"))
  

for i in range(num + 1 , numf):
    if i % 2 != 0:
        soma = soma + i
print(soma)