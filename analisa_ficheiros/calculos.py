def calcula_linhas(name_file):
    count = 0
    with open(name_file, "r") as f:
        for line in f:
            if line != "\n":
                count += 1
    print(count)

def calcula_carateres(name_file):
    with open(name_file, "r") as f:
        print(len(name_file))

def calcula_ocorrencia_letras(name_file):
    dictionary = {}
    with open(name_file, "r") as f:
        for line in f:
            for c in line:
                if c == " " or c == "\n":
                    continue
                if dictionary.__contains__(c):
                    dictionary[c] += 1
                else:
                    dictionary[c] = 1
    sort_dict = sorted(dictionary.items())
    print(dictionary)
