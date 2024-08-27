import math

def evaluar(a):
    if a < 0:
        raise TypeError("este es mensaje personalizado desde dentro de la funcion")

    else:
        b = math.sqrt(a)
    return b

nota= -4



try:
    c = evaluar(nota)
    print ("la raiz cuadrade de ", nota, " es ", c)
except TypeError as MensajeError:
    print("no hay raices de numeros negativos ", MensajeError)
print("fin del programa")


#CON TRY EXCEPT Y RAISE PODEMOS CREAR EXCEPCIONES PERSONALIZADAS, MUCHO POTENCIAL

# con raise y except  CREAMOS OTRA CAMINO DE LA FUNCION, Q VIAJA POR LAS EXCEPCIONES Y NO POR LA FUNCION MISMA, LA CUAL SE DETIENE