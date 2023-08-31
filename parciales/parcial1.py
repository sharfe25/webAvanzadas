import math

def calcular_distancia(point1, point2):
    #Esta funcion es quien nos da loa distancia entre dos puntos del mismo eje
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def validar_datos(function):
    def validar(*args):
        
        n = len(args)
        #Validamos si tenemos la cantidad suficiente de datos para ejecutar la funcion
        if n < 1:
            return {
                "coordinateOne":None,
                "coordinateTwo":None,
                "distance":0
            }
        
        if n == 1:
            return {
                "coordinateOne":args[0],
                "coordinateTwo":None,
                "distance":0
            }
        
        resultado = function(*args)
        return resultado
    
    return validar
    
    
    
    
    
@validar_datos
def pares_cercanos(*args):
    #Convertimos los args en un array
    coordenadas = [coordinate for coordinate in args]
    #Ordenamos el array
    coordenadas.sort(key=lambda point: point[0])
    
    n = len(coordenadas)

    min_distancia = float('inf')
    point1, point2 = None, None
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            
            distancia = calcular_distancia(coordenadas[i], coordenadas[j])
            if distancia < min_distancia:
                min_distancia = distancia
                point1, point2 = coordenadas[i], coordenadas[j]
    
    return {
        "coordinateOne":point1,
        "coordinateTwo":point2,
        "distance":min_distancia
    }

def __init__():
    results = pares_cercanos((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))

    print(f"Los puntos mas cercanos son: {results['coordinateOne']} y {results['coordinateTwo']}")
    print(f"La distancia entre ellos es: {results['distance']}")

__init__()