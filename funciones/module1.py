def imprimir():
    s = "soy una variable local"
    print(s)

s = "soy una variable global"


imprimir()
print(s)




def cadena_conmin(cadena):


    if cadena[0] == cadena[0].lower():
        respuesta = True
    return respuesta

cadena = "Hola "
respuesta = False

print(cadena_conmin(cadena))


