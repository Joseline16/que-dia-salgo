frutas = ["manzana", "pera", "uva"]
persona = {"nombre": "Ana", "edad": 30}

print(frutas[1]) #pera
print(frutas[-1]) #uva
print(len(frutas)) # 3
print(persona["nombre"]) #ana
print(len(persona)) #2
print("pera" in frutas) #True
print("Ana" in persona) #false
print("edad" in persona)#True
#listas
numeros = [4, 8, 15, 16, 23, 42]
print(numeros[0], numeros[5])

numeros[2] = 100
print(numeros)

numeros.append(50)
print(numeros)
print()

for numero in numeros:
    print(2 * numero)
print()

pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

print()
#diccionarios
producto = {"nombre": "zapatillas", "precio": 60, "stock": 12}
print(producto["precio"])
producto["stock"]=10
print(producto)
producto["color"]= "azul"
print(producto)

for clave,valor in producto.items():
    print(f"{clave} -> {valor}")

if (producto["stock"]>0):
    print("Hay stock")
else: 
    print("Agotado")

print()   

#lista en diccionario

productos = [
    {"nombre": "zapatillas", "precio": 60, "stock": 12},
    {"nombre": "mochila", "precio": 25, "stock": 0},
    {"nombre": "botella", "precio": 8, "stock": 30},
]


print(productos[1]["nombre"])

print()
print()
for productoo in productos:
    print(productoo["nombre"])
print()
print()
agotados = []
for producto in productos:
    if (producto["stock"]==0):
        agotados.append(producto["nombre"])
print(agotados)
print()
print()

valor_almacen = 0

for producto in productos:
    x = producto["precio"]* producto["stock"]
    valor_almacen+=x

print(valor_almacen)

print()
print()