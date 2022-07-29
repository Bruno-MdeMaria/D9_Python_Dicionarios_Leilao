cidades_vis = {
    "cidades": ["Paris", "Lion", "Saint Deni"]  # uma lista dentro de um dicionario 
}

viagem_dic = {
    "Franca": {cidades_vis},                   # uma forma de colocar um dicionario dentro de um dicionário
    "Brasil": {"cidades_visits":["Imbituba", "Itajai", "Floripa"]},  # outra forma de colocar um dicionario dentro de outro dicionario
    "Brasil": {"cidades_visits":["Imbituba", "Itajai", "Floripa"], "visitas": 12},  # acrescentando uma informação, neste caso a qunantidade de visitas
}

# um dicionario dentro de uma lista:

viagem_list = [
    
    {
        "País": "Brasil",                              #com concate4nação melhor forma de visualisar
        "cidades_visits":["Imbituba", "Itajai", "Floripa"], # este dicionario será a posisacão [0] na lista.
        "visitas": 5
    },
    
   {
        "País": "Franca",
        "cidades_visits": ["Paris", "Lion", "Saint Deni"] , 
        "visitas": 12,
   },
]