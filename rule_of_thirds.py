import os

def regra_de_tres(A, B, C):
    D = (C * B) / A
    return D

while True:
    try:
        # Obter os valores A, B e C do usuário
        A = float(input("Digite o valor de A: "))
        B = float(input("Digite o valor de B: "))
        C = float(input("Digite o valor de C: "))

        # Verificar se os valores são todos diferentes de zero
        if A == 0 or B == 0 or C == 0:
            print("Erro: pelo menos um dos valores informados é igual a zero. Por favor, tente novamente.")
            continue

        # Calcular o valor de D utilizando a função regra_de_tres
        D = regra_de_tres(A, B, C)

        # Exibir o resultado para o usuário
        print("O valor de D é:", D)

    except ValueError:
        # Caso o usuário digite um valor inválido, exibir mensagem de erro
        print("Erro: um ou mais valores informados não são numéricos. Por favor, tente novamente.")
        continue

    # Perguntar se o usuário deseja reiniciar o programa
    reiniciar = input("Deseja reiniciar o programa? (s/n): ")

    if reiniciar.lower() == "s":
        # Limpar a tela antes de reiniciar o programa
        os.system("cls" if os.name == "nt" else "clear")
    else:
        break
