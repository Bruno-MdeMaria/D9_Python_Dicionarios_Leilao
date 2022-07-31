import os
from art import logo

dict = {

}

def criar_dados (nome, lance):
    new =[{}]
    new["nome"]= nome
    new["lance"]= lance
    dict.append(new)
    
print(logo)
print("\nBem vindo ao programa de leilões secretos!\n")

parar = False
while parar == False:
    nome= input("Qua o seu nome? \n")
    lance= input("Qual o seu lance? \n")
    dict[nome] = lance     #ADIONANDO OS VALORES AO DICT :     NOME DO DICIONARIO[CHAVE] = RECEBE VALOR. FICANDO ASSIM:  DICT{ "NOME": VALOR,}
    continua = input("Mais alguém dara um lance? Digite 's' ou 'n' ").lower()
    if continua == "n":
        parar = True
    else: os.system("cls")

print(dict)

