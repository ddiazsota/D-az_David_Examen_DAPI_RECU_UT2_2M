def OrdenarLista():
    """Esta función recibe una lista de números enteros y lo escribe en un fichero
    .txt.
        Parámetros:
            -Una lista de numeros enteros
            -Ordenarlos de mayor a menor
        Salida:No tiene
    
    """
    lista_numeros = [1, 2, 3, 4, 5]
    with open("ListaOrdenada.txt", "w") as file:
        file.write(lista_numeros)
        
    for i in lista_numeros:
        print(f"numeros enteros">lista_numeros, str(len))
   

        

     
       
        
        


def NumeroPar():
    """Esta función abre un fichero en el que contiene una lista 
        ordenada de número, que lo lea y escriba en otro fichero.
            Parámetros:
                -Entrada:Fichero:ListaDePares.
            Salida: No tiene 

    """
    Pares = [2, 4, 6, 8, 10]
    with open("ListaOrdenada.txt","r")as file:
        file.readlines()
    with open("ListaOrdenadas.txt","w") as file:
        file.write("ListaDePares.txt")
        print(file)


        





