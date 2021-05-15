import os

def main():
    pasta = pede_pasta()
    calcula = calcula_tamanho_pasta(pasta)
    print(calcula)

def pede_pasta():
    while 1:
        path = input("Qual é o caminho da pasta?")
        if os.path.isdir(path):
            return path

def calcula_tamanho_pasta(pasta):
    soma = 0
    for file in os.listdir(pasta):
        path = os.path.join(pasta, file)
        if os.path.isfile(path):
            soma += os.stat(path).st_size
        if os.path.isdir(path):
            calcula_tamanho_pasta(path)
    return soma

if __name__ == "__main__":
    main()