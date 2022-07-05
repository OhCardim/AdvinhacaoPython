import random

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Ola! Bem Vindo ao jogo de Advinhação")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", end="\n")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000

print("Qual o nivel de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel==2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1,total_de_tentativas + 1):
    print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("\n Digite um número entre 1 e 100: ")


    #SEP = Espaço entre os textos, END = fim do texto
    #Input coleta a informação
    #Elif seria um else porém com um condicional
    #For funciona como um laço de repetição que automaticamente adiciona um, onde (começo, fim, passo), exemplo (1(começo),10(fim),3(passo)), porém o 10 nao vai ser impresso sendo exclusivo, então é bom adicionar 1 a mais


    print("\nVoce Digitou: ", chute_str, end="\n", sep=" ")
    chute = int(chute_str)
    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!! >:(")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("\nVocê acertou!!")
        print(f"Você fez {pontos} pontos!!")
        break
    else:
        if(maior):
            print("\nVocê errou... O seu chute foi maior do que o número secreto :(")
        elif(menor):
            print("\nVocê errou... O seu chute foi menor do que o número secreto :(")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("\n\nFim do Jogo!!")
print(f"\nO número era {numero_secreto}")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

