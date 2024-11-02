# A partir de un archivo de texto con muchos nombres, determinar nombres únicos presentes en el archivo.



def leerNombres(arch): #lee el archivo
    nombres = [] 
    linea = arch.readline().strip()
    while linea != '':
        nombres.append(linea) # agregamos el elemento a la lista
        linea = arch.readline().strip()
    return nombres

def esta(elemento, lista):
    for i in lista: # lista vacia
        if i == elemento: # si el valor de la lista es igual al elemento 
            return True
    return False # la primera vez retorna siempre falso ya que está vacia
    # cuando se comprueben todos los valores y ninguno coincida


def obtenerUnicos(nombres):
    # crear una lista nueva y empezar a recorrer la lista anterior, verificar si el elemento está en la lista vacía
    # si está no se agrega, así siempre existirá sólo uno de cada elemento 
    unicos = []
    for i in nombres:
        if not esta(i, unicos): # si no está i en la lista de unicos, con el not la funcion se vulve lo contrario
      # cuando retorna verdadero con el not se hace falso y no se ejecuta el append, termina el ciclo
            unicos.append(i) # se agrega el elemento de la lista
    return unicos
    
def printNombre(lista):
    for i in lista:
        print (i)

# CÓDIGO PRINCIPAL
arch = open('texto.txt', 'r')
nombres = leerNombres(arch) #utilizamos el arch como parámetro
nombres_unicos = obtenerUnicos(nombres)

printNombre(nombres_unicos)

        
# otra forma de obtener los unicos:
    # def obtenerUnicos (nombres)
    # unicos = []
    # for i in nombres:
        # if not i in unicos: verificamos que el elemento esté en la lista
            # unicos.append(i)
       # return unicos