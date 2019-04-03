#Función: Determinar si un numero es palindromo
#Entradas:enteros
#Salidas: True en caso de ser palindromo, false en caso contrario
#Restricciones: Numeros enteros >0
n=int(input("Digite un numero"))
z=n
cont=0
multi=1
y=0
if n<0:
    print("El numero debe ser mayor o igual a cero")
else:
    while n>0:
            y=y*10+(n%10)
            n=n//10
    if y==z:
        
        print("True")
    else:
        print("False")

    

