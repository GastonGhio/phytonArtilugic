"""
def devuelve(*ciudades): #se avisa con * q el numero va a ser variable o sea indeterminado
    for elemento in ciudades:
        yield elemento
"""   
        
def devuelve(*ciudades): #aca con YIELD FROM permite crear un objeto dentro de otro objeto
    for elemento in ciudades:   
        yield from elemento
        
ciudadesDevueltas = devuelve("buenos", "salta", "tucuman")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
