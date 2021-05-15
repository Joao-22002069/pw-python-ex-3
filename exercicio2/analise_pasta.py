import csv
import os
from matplotlib import pyplot as plt
from numpy import inf

def pede_pasta():
   while True:
       ficheiro = input("Introduza o nome da pasta: ")
       if os.path.isdir(f"{os.getcwd()}\\{ficheiro}"):
           return ficheiro

def faz_calculos(ficheiro):
    dic = {}
    dict = os.listdir(ficheiro)

    for a in dict:
        filename = f"tests\\{a}"
        if os.path.isfile(filename):
            tamanho = os.path.getsize(filename)
            split1 = filename.split(".")[-1]
            if not split1 in dic:
                dic[split1] = {}
                dic[split1]['quantidade'] = 1
                dic[split1]['size'] = tamanho
            else:
                dic[split1]['quantidade'] = dic[split1]['quantidade'] + 1
                dic[split1]['size'] = dic[split1]['size'] + tamanho
    return dic

def guarda_resultados(ficheiro):
    dados = faz_calculos(ficheiro)

    with open(ficheiro + '.csv', 'w', newline='') as file:
        campos = ['Extensao', 'Quantidade', 'Tamanho[kByte']
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        for extention, info in dados.items():
            writer.writerow({'Extensao': extention, 'Quantidade': info['quantidade'], 'Tamanho[kByte': info['size']})


def faz_grafico_queijos(titulo, ficheiro):
    dados = faz_calculos(ficheiro)
    lista_valores = []
    for i in dados.values():
        lista_valores.append(i['quantidade'])

    plt.pie(lista_valores, labels=dados.keys(), autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()


def faz_grafico_barras(titulo, nome_ficheiro):
    data = faz_calculos(nome_ficheiro)
    lista_valores = []
    for i in data.values():
        lista_valores.append(i['quantidade'])

    plt.bar(data.keys(), lista_valores)
    plt.title(titulo)
    plt.show()