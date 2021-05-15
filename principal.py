
import analisa_ficheiros as analisa
import json
import os

def main():
    path = os.getcwd() + "/test.txt"
    print(analisa.pede_nome())
    analisa.gera_nome()
    analisa.calcula_linhas(path)
    analisa.calcula_carateres(path)
    analisa.calcula_ocorrencia_letras(path)
    return

if __name__ == "__main__":
    main()