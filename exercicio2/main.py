
import analise_pasta as al

def main():
    foldername = al.pede_pasta()
    informacao = al.faz_calculos(foldername)
    print(informacao)
    al.guarda_resultados(foldername)
    al.faz_grafico_queijos("Requeijao", foldername)
    al.faz_grafico_barras("Barra de Ceriais", foldername)




if __name__ == "__main__":
     main()
