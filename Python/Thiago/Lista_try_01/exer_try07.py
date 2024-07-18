# 40. Faça um programa que some os números ímpares contidos em um intervalo definido pelo 
# usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo e o programa 
# deve somar todos os números ímpares contidos neste intervalo. Caso o usuário digite um 
# intervalo inválido (começando por um valor maior que o valor final) deve ser escrito uma 
# mensagem de erro na tela, “Intervalo de valores invalido” e o programa´ termina. Exemplo de 
# tela de saída:
# Digite o valor inicial e valor final: 5
# 10
# Soma dos ímpares neste intervalo: 21
try:
    inicial = int(input("INICIAL: "))
    final = int(input("FINAL"))
except:
    print("Entrada inválida!!!!!")
soma = 0

if inicial > final:
    print("INTERVALO VÁLIDO: ")
else:
    while inicial <= final:
        if inicial % 2 == 1:
            soma += inicial
        inicial += 1
    print("Soma dos ímpares neste intervalo: ",soma)    