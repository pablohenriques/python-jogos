import random

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)    
    
    print(letras_acertadas)

    acertou = False
    enforcou = False
    erros = False

    while(not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
    
        print(letras_acertadas)
        
    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    print("Fim de Jogo!")


def imprime_mensagem_abertura():
    print("*************************")
    print("***** Jogo da Forca *****")
    print("*************************")


def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    letras_acertadas = ['_' for letra in palavra]
    return letras_acertadas


def imprime_mensagem_vencedor():
    print("Você ganhou!")


def imprime_mensagem_perdedor(palavra):
    print(f"Você perdeu! - Palavra-chave: {palavra}")


def pede_chute():
    chute = input('Informe uma letra: ')
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[posicao] = letra
        posicao += 1


