productos = [
    {"nombre": "zapatillas", "precio": 60, "stock": 12},
    {"nombre": "mochila", "precio": 25, "stock": 0},
    {"nombre": "botella", "precio": 8, "stock": 30},
    {"nombre": "gorra", "precio": 15, "stock": 0},
]

alumnos = [
    {"nombre": "Lucía", "notas": [7, 8, 9]},
    {"nombre": "Marcos", "notas": [4, 5, 3]},
    {"nombre": "Sara", "notas": [10, 9, 8]},
]

def nombres(productos):
    lista_nombres = []
    for producto in productos:
        lista_nombres.append(producto["nombre"])
    return lista_nombres

print(nombres(productos))


def valor_almacen(productos):
    total = 0
    for producto in productos:
        total +=  producto["precio"] * producto["stock"]
    return total

print(valor_almacen(productos))


def hay_stock(productos):
    if productos["stock"]>0: 
        return True
    else:
        return False
print(hay_stock(productos[0]))
print(hay_stock(productos[1]))


def aplicar_descuento(producto, porcentaje):
    descuento = producto["precio"] * porcentaje/100
    return producto["precio"]-descuento

print(aplicar_descuento(productos[0],10))