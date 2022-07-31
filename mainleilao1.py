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
nome= input("Qua o seu nome? \n")
lance= input("Qual o seu lance? \n")
continua = input("Mais alguém dara um lance? ").lower()



