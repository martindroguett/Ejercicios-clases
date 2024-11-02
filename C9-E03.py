def leerArch (nombre_archivo): #lee el archivo
    lista = [] 
    arch = open(nombre_archivo)
    linea = arch.readline().strip()
    while linea != '':
        lista.append(linea) # agregamos el elemento a la lista
        linea = arch.readline().strip()
    return lista

def indice (elemento, lista):
    for i in range(len(lista)): # toma el tamaño de la lista
        if elemento == lista[i]: # lista en la posición i
            return i
    return -1 #forma de daclarar un error, puede ser otro valor declarado, necesitamos control de error
    # pero no va a pasar ya que está dentro de un if

# CÓDIGO PRINCIPAL 
nombres = leerArch ('texto.txt') # funcion para leer el archivo entregado

nombres_unicos = []

frecuencias = []

for i in nombres: # para verificar si está o no en la lista, ve la posición
    if i in nombres_unicos: # cuando el elemento si está en la lista, necesitamos que la frecuencia aumente
        ind = indice(i, nombres_unicos) # funcion para ver la posición del elemento
        frecuencias[ind] += 1 # se acumula 1 en la posicion correlativa en la lista de frecuencias
    else: # cuando el elemento no está
        nombres_unicos.append(i) # se agrega el nombre 
        frecuencias.append(1) # cuando no se repite el valor sólo es 1 
        

for i in range (len(frecuencias)): 
    print(nombres_unicos[i], frecuencias[i])

# otra forma de indice:
    # for i in nombres:
        # if i in nombres_unicos: 
    #     ind = nombres_unicos.index(i) 
    # utilizamos el elemento de la lista para ver la posicion, no necesita control de error manual :D