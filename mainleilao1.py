import os
from art import logo



def juiz(dicionario_final):
    maior_valor = 0
    for participante in dicionario_final:
        valor = dicionario_final[participante]  # NO LOPP A VARIAVEL VALOR VAI RECEBER O VALOR QUE ESTÁ PERCORRENDO. POR ISSO ADIONAMOS UMA VARIAVEL PARA RECEBER O MAIOR VALOR E ELA COMOÇA COM 0 E ENTÃO COMPARAMOS SE É MAIOR OU MENOR > <.
        if valor > maior_valor:
            maior_valor = valor #VARIAVEL VAI RECEBER O MAIOR VALOR.
            vencedor = participante  #NÃO PRECISAMOS FAZER UM NOVO LOOP PARA SABER QUEM VENCEU BASTA QUE OUTRA VARIVEL RECEBA O NOME DO PARTIPANTE EM QUE O LOOP ESTÁ PASSANDO E TENDO MAIOR LANCE
    os.system("cls")
    print(f"O vencedor da licitação é {vencedor} com o lance R${maior_valor}!")

   
    
print(logo)
print("\nBem vindo ao programa de leilões secretos!\n")

dicionario = {}

parar = False
while parar == False:
    nome= input("Qua o seu nome?: \n")
    lance= int(input("Qual o seu lance?: R$ \n"))
    dicionario[nome] = lance     #ADIONANDO OS VALORES AO dicionario :     NOME DO DICIONARIO[CHAVE] = RECEBE VALOR. FICANDO ASSIM:  dicionario{ "NOME": VALOR,}
    continua = input("Mais alguém dara um lance? Digite 's' ou 'n': \n").lower()
    if continua == "n":
        parar = True
        juiz(dicionario)
    else: os.system("cls")



