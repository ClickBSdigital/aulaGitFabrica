# 41. Crie um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos 
# pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário
# entre com um valor para resistência igual a zero.
#### JÁ COMEÇA ENTRANDO NO WHILE...........
while True:
    try:
        r1 = int(input("DIGITE R1: "))
        r2 = int(input("DIGITE O R2: "))
        if r1 == 0 or r2 == 0:
            break
        res = (r1 * r2) / (r1 + r2)
        print("O valor para resistência igual a: ",res)
    except:
        print("Entrada inválida, digite novamente!!!!")
print("PROGRAMA FINALIZADO!!")    