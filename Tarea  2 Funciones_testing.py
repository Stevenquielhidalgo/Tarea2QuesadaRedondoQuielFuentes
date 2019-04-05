# Función: Determinar la cantidad de veces que se repite una cadena en un
# archivo
# Entradas: 2 cadenas de string
# Salidas: Un entero que indique la cantidad de veces
# que se repite la cadena en el archivo
# Restricciones: La primera cadena debe ser una dirección de memoria


def Lector(Direccion, Cadena):
    contl = 0  # Contador de letras
    contp = 0  # Contador de palabras
    file = open(Direccion, 'r')
    f1 = file.read()
    k = 0
    for i in f1:
        print(i, k, contl)
        if(i == Cadena[k]):
            print(i == Cadena[k])
            contl += 1
            k += 1
        else:
            if((i == Cadena[k-1]) & (k == 1)):
                contl += 1
            else:
                k = 0
                contl = 0
        if(contl == len(Cadena)):
            contp += 1
            contl = 0
            k = 0
    return contp
# Función: Crea una arreglo de 100 elementos
# Entradas: Enteros
# Salidas: El arreglo de 100 elementos
# Restricciones: El limite inical del arreglo debe ser menor
# y con una diferencia de 100 del limite superior


def Creador_array(val_min, val_max):
    arreglo = []
    if(val_max < val_min):
        print("ERROR: el valor maximo debe ser mayor que el incial")
    else:
        if((val_max - val_min) != 100):
            print("Debe existir una diferencia de 100")
        else:
            i = val_min
            while(i < val_max):
                arreglo.append(i)
                i += 1
            return(arreglo)
    return
# Función: Determinar si un numero es palindromo
# Entradas:enteros
# Salidas: True en caso de ser palindromo, false en caso contrario
# Restricciones: Numeros enteros >0


def Palind(n):
    z = n
    y = 0
    if(n < 0):
        print("El numero debe ser mayor o igual a cero")
    else:
        while n > 0:
            y = y * 10 + (n % 10)
            n = n // 10
        if(y == z):
            return(True)
        else:
            return(False)
    return


def test_1():
    assert Lector("C:\\Users\\kervinjosue\\Desktop\\Prueba.txt", "sss") == 3

    
def test_2():
    Creador_array(0, 100)


def test_3():
    assert (Palind(2332) == True)
