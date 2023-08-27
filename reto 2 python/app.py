# Diccionario de productos
productos = [
    {
        'id': 123,
        'Nombre': 'libreta',
        'precio': 12.500,
        'id_cat': 1
    },
    {
        'id': 345,
        'Nombre': 'jabon',
        'precio': 10.500,
        'id_cat': 2
    }
]

# Diccionario de categorías
categorias = [
    {
        'id': 1,
        'nombre': 'utiles escolares'
    },
    {
        'id': 2,
        'nombre': 'aseo'
    }
]

# Crear un diccionario resultante
diccionario_resultante = []

# Iterar a través de los productos y buscar la categoría correspondiente
for producto in productos:
    for categoria in categorias:
        if producto['id_cat'] == categoria['id']:
            # Crear un nuevo diccionario con la información deseada
            producto_categoria = {
                'id': producto['id'],
                'Nombre': producto['Nombre'],
                'Categoria': categoria['nombre']
            }
            # Agregar el diccionario al resultado
            diccionario_resultante.append(producto_categoria)

# Imprimir el resultado
for item in diccionario_resultante:
    print(item)
