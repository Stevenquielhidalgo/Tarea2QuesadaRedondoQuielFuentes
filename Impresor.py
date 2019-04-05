# Función: Imprime los numeros en un rango de valores
# Entradas:enteros
# Salidas: Impresión a pantalla de los números
# Restricciones: Numeros enteros >0, el segundo valor debes ser mayor al primero
def Impresor(val_min, val_max):
    arreglo = []
    i = val_min
    if (val_max< val_min):
        print("ERROR: el valor maximo debe ser mayor que el incial")
    else:
       while i < val_max:
           print(i)
           i+=1
    return
    
