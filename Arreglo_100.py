def Creador_array(val_min,val_max):
    arreglo = []
    if (val_max<val_min):
        print("ERROR: el valor maximo debe ser mayor que el incial")
    else:
        if ((val_max-val_min) != 100):
            print ("Debe existir una diferencia de 100")
        else:
            i= val_min;
            while (i<val_max):
                arreglo.append(i)
                i+=1
            return (arreglo)
    return
def Lector(Direccion,Cadena):
    contl = 0 #Contador de letras
    contp = 0 #Contador de palabras
    file = open(Direccion,'r')
    f1 = file.read()
    k = 0 
    for i in f1:
        print (i, k,contl)
        if (i == Cadena[k]):
            print (i == Cadena[k])
            contl+=1
            k +=1
        else:
            if ((i== Cadena[k-1]) & (k==1)):
                contl+=1
                
            else:
                k=0;
                contl=0
        if (contl == len(Cadena)):
            contp+= 1
            contl = 0
            k= 0
            
    return contp
    
