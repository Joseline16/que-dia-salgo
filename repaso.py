#Tema 1: Listas
#creando una lista 
animales = ["perro","gato","conejo","loro"]
#ejercicios con listas 
print(animales[0])
print(animales[2])
print(animales[-1])
print(len(animales))
animales[1] = "tortuga"
print(animales)
animales.append("pez")
print(animales)

#Tema 2 : diccionarios 
libro = {"titulo":"El principito", "autor":"Saint-Exupéry", "paginas":96}

print(libro["titulo"])
print(libro["paginas"])
print(len(libro))
libro["paginas"] = 100
print(libro)
libro["leido"] = True
print(libro)
print(f'{libro["titulo"]} tiene {libro["paginas"]} paginas')

#Tema 3: Recorrer listas con for

notas = [7, 4, 9, 5, 3, 10]

for nota in notas:
    print(nota)

for nota in notas:
    print(f'Nota: {nota}')

total_nota = 0
for nota in notas:
    total_nota += nota
print(total_nota)

aprobadas = []
desaprobadas =[]
for nota in notas:
    if nota >= 5:
        aprobadas.append(nota)
    else:
        desaprobadas.append(nota)
print(aprobadas)
print(len(desaprobadas))

#Tema 4: Listas de diccionarios
peliculas = [
    {"titulo": "Coco", "año": 2017, "nota": 8.4},
    {"titulo": "Up", "año": 2009, "nota": 8.3},
    {"titulo": "Cars", "año": 2006, "nota": 7.2},
    {"titulo": "Soul", "año": 2020, "nota": 8.0},
]

print(peliculas[1]["titulo"])
print(peliculas[-1]["año"])

for pelicula in peliculas:
    print(f'{pelicula["titulo"]} ({pelicula["año"]})')

buenas = []
for pelicula in peliculas :
    if (pelicula["nota"]>= 8):
        buenas.append(pelicula["titulo"])
print (buenas)

suma_notas = 0
for pelicula in peliculas:
    suma_notas+= pelicula["nota"]
print(round(suma_notas/ len(peliculas), 2))


#Tema 5 : Funciones sencillas

def triple(numero):
    return numero*3

print(triple(4))

def saludar(nombre):
    return "Hola, " + nombre

print(saludar("Ana"))

def restar(a,b):
    return a - b

print(restar(10,3))

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False
    
print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))

def precio_con_iva(precio):
    total_iva = precio * 1.21
    return total_iva

print(precio_con_iva(100))

#Tema 6: Funciones con listas

def contar_elementos(lista):
    cuantos_hay = 0
    for elemento in lista:
        cuantos_hay+=1
    return cuantos_hay

print(contar_elementos(["a", "b", "c"]))

def media(numeros):
    return sum(numeros) / len(numeros)

print(media([4, 6, 8]))

def solo_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

print(solo_pares([1,2,3,4,5,6]))


def contar_aprobados(notas):
    aprobadas = []
    for nota in notas:
        if nota >= 5:
            aprobadas.append(nota)
    return len(aprobadas)

print(contar_aprobados([7,4,9,5,3]))

def maximo(numeros):
    mayor = numeros[0] 
    for numero in numeros:
        if numero> mayor:
            mayor = numero
    return mayor

print (maximo([3, 17, 8, 12]))
print(maximo([-5, -2, -9])) 

#Tema 7: Funciones con diccionarios

coche = {"marca": "Seat", "modelo": "Ibiza", "año": 2018, "km": 85000}

def nombre_completo(coche):
    marca = coche["marca"]
    modelo = coche["modelo"]
    return marca + " " + modelo 

print(nombre_completo(coche))

def antiguedad(coche,año_actual):
    antiguedad_coche = año_actual - coche["año"]
    return antiguedad_coche

print(antiguedad(coche,2026))

def necesita_revision(coche):
    return coche["km"] > 80000

print(necesita_revision(coche))

def sumar_km(coche, km_nuevos):
    coche["km"] += km_nuevos
    return coche["km"]

print(sumar_km(coche,500))

def ficha(coche):
    return f"{coche['marca']} {coche['modelo']} ({coche['año']}) - {coche['km']} km."

print(ficha(coche))

#tema 8: Funciones con listas de diccionarios


coches = [
    {"marca": "Seat", "modelo": "Ibiza", "año": 2018, "km": 85000},
    {"marca": "Toyota", "modelo": "Corolla", "año": 2022, "km": 20000},
    {"marca": "Renault", "modelo": "Clio", "año": 2012, "km": 160000},
    {"marca": "Kia", "modelo": "Ceed", "año": 2020, "km": 45000},
]

def marcas(coches):
    lista_marcas = []
    for coche in coches:
        lista_marcas.append(coche["marca"])
    return lista_marcas
print (marcas(coches))

def km_totales(coches):
    total = 0
    for coche in coches:
        total += coche["km"]
    return total

print (km_totales(coches))

def para_revision(coches):
    revisar = []
    for coche in coches: 
        if coche["km"]>80000:
            revisar.append(f'{coche["marca"]} {coche["modelo"]}')
    return revisar
    
print(para_revision(coches))

def mas_nuevo(coches):
    maximo = coches[0]
    for coche in coches:
        if coche["año"]> maximo["año"]:
            maximo = coche      
    return maximo

print(mas_nuevo(coches))


def contar_por_decada(coches):
    resultado = {"antes_2020": 0, "desde_2020": 0} 
    for coche in coches:
        if coche["año"]< 2020:
            resultado["antes_2020"]+=1
        else:
            resultado["desde_2020"]+=1
    return resultado

print(contar_por_decada(coches))
