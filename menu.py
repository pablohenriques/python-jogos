import adivinhacao
import forca

print("***********************")
print("*****Menu de Jogos*****")
print("***********************")

print("1. Adivinhação")
print("2. Força")
escolha = int(input("Qual jogo quer jogar? Digite um número: "))

if escolha == 1:
    adivinhacao.jogar()
elif escolha == 2:
    forca.jogar()