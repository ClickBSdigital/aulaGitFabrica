# 14. Crie um programa que leia um número inteiro positivo par N 
# e imprima todos os números 
# pares de 0 até N em ordem crescente.
num = int(input("DIGITE UM NÚMERO: "))
cont = 0

while cont <= num:
    # if cont % 2 == 1: #se o resto da divisão for igual a 1 é impar
    if cont % 2 != 1: #se o resto da divisão for igual a 0 é par  
        print (cont)
    cont = cont + 1