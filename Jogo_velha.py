## Jogo da velha!

import os 
import random 
from colorama import Fore, Back, Style

jogar_novamente = 's'
jogaveis = 0
prox_jogador = 2
max_jogadas = 9
vit = "n"

velha = [

    [" ", " "," "],
    [" ", " "," "],
    [" ", " "," "]

]

def tela():

    global velha
    global jogaveis
    os.system('cls')
    print("    0   1   3")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   ---------------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   ---------------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("   ---------------")
    print("Jogadas: " + Fore.GREEN + str(jogaveis) + Fore.RESET)

def jogador_joga():
    global jogaveis
    global prox_jogador
    global vit
    global max_jogadas

    if prox_jogador == 2 and jogaveis < max_jogadas:
        l = int(input("Linha..:  "))
        c = int(int("Coluna.:  "))

        while velha[1][c] != " ":
            l = int(input("Linha..:  "))
            c = int(int("Coluna.:  "))
        
        try:
            velha[1][c] = 'X'
            prox_jogador = 1
            jogaveis+=1
        
        except:
            print("Linha e coluna invalida")
            vit = "n"
        
def cpu_joga(): 
    global jogaveis
    global prox_jogador
    global vit
    global max_jogadas

    if prox_jogador == 1 and jogaveis < max_jogadas:
        l = random.randrange(0,3)
        c = random.randrange(0,3)

        while velha[1][c] != " ":
            l = random.randrange(0,3)
            c = random.randrange(0,3)
        velha[1][c] = "0"
        jogadas+=1
        prox_jogador = 2
     

while True: 
    tela()
    jogador_joga()
    cpu_joga()

    