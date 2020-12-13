from random import randint

def retornar_numero_rodadas(numero_opcao):
    rodadas = 5
    if numero_opcao == 1:
        rodadas = 20
    elif numero_opcao == 2:
        rodadas = 10

    return rodadas 

def retornar_tipo_pontuacao_por_rodada(rodadas):
    pontuacao = 0
    if rodadas == 20:
        pontuacao = 1000 / 20
    elif rodadas == 10:
        pontuacao = 1000 / 10
    else:
        pontuacao = 1000 / 5
    
    return pontuacao

def retornar_confirmacao_numero_secreto(numero, numero_secreto):
    mensagem = ""
    if numero == numero_secreto:
        mensagem = "Acertou!"
        return True, mensagem
    elif numero > numero_secreto:
        mensagem = "Número secreto é Menor!"
    else:
        mensagem = "Número secreto é Maior!"
    
    return False, mensagem


def jogar():

    print("***********************")
    print("* Jogo da Adivinhacao *")
    print("***********************")

    numero_secreto = randint(0, 100)
    pontuacao = 1000

    nivel_informado = int(input("\nInforme a dificuldade: 1-Fácil, 2-Médio, 3-Difícl:"))
    numero_rodadas = retornar_numero_rodadas(nivel_informado)
    reducao_pontucao = retornar_tipo_pontuacao_por_rodada(numero_rodadas)

    for rodada in range(1, numero_rodadas+1):
        print("\nPontuação: {}".format(pontuacao))
        print("\nTentativa {} de {}".format(rodada, numero_rodadas))
        chute = int(input("Informe o número secreto:"))

        confirmacao = retornar_confirmacao_numero_secreto(chute, numero_secreto)
        if confirmacao[0] == True:
            print("\n{}".format(confirmacao[1]))
            break
        else:
            pontuacao = pontuacao - reducao_pontucao
            print("\n{}".format(confirmacao[1]))

    print("\nFim de Jogo - Pontuação: {}".format(pontuacao))

