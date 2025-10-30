#Importamos las funciones necesarias de los otros módulos del proyecto
from busquedas_filtros import (
    buscar_por_nombre, filtrar_por_continente, 
    filtrar_por_rango_poblacion, filtrar_por_rango_superficie
)
from ordenamientos import (
    ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie
)
from estadisticas import (
    pais_con_mayor_menor_poblacion, promedio_poblacion, 
    promedio_superficie, cantidad_por_continente
)
from utilidades import pedir_entero, pedir_texto


#Opción 1: Buscar país por nombre

def accion_buscar(paises, mostrar_paises):
    #Permite buscar un país por nombre o parte del nombre
    termino = pedir_texto('Ingrese nombre o parte del nombre: ')
    resultado = buscar_por_nombre(paises, termino)
    mostrar_paises(resultado)


#Opción 2: Filtrar países

def accion_filtrar(paises, mostrar_paises):
    #Permite filtrar países por continente, población o superficie
    print('\nFILTRAR')
    print('a. Por continente')
    print('b. Por rango de población')
    print('c. Por rango de superficie')
    
    sub = input('Elija filtro (a/b/c): ').strip().lower()

    match sub:
        #Filtro por continente
        case 'a':
            cont = pedir_texto('Ingrese continente (ej: América, Europa, Asia): ')
            mostrar_paises(filtrar_por_continente(paises, cont))

        #Filtro por rango de población
        case 'b':
            min_p = pedir_entero('Población mínima: ', minimo=0)
            max_p = pedir_entero('Población máxima: ', minimo=min_p)
            mostrar_paises(filtrar_por_rango_poblacion(paises, min_p, max_p))

        #Filtro por rango de superficie
        case 'c':
            min_s = pedir_entero('Superficie mínima (km²): ', minimo=0)
            max_s = pedir_entero('Superficie máxima (km²): ', minimo=min_s)
            mostrar_paises(filtrar_por_rango_superficie(paises, min_s, max_s))

        #Opción no válida
        case _:
            print('Opción inválida.')


#Opción 3: Ordenar países

def accion_ordenar(paises, mostrar_paises):
    #Permite ordenar los países por nombre, población o superficie
    print('\nORDENAR')
    print('a. Por nombre')
    print('b. Por población')
    print('c. Por superficie')
    
    sub = input('Elija criterio (a/b/c): ').strip().lower()
    sentido = input('Orden ascendente o descendente? (a/d): ').strip().lower()
    desc = True if sentido == 'd' else False  # True = descendente

    match sub:
        case 'a':
            mostrar_paises(ordenar_por_nombre(paises, desc))
        case 'b':
            mostrar_paises(ordenar_por_poblacion(paises, desc))
        case 'c':
            mostrar_paises(ordenar_por_superficie(paises, desc))
        case _:
            print('Opción inválida.')

#Opción 4: Estadísticas

def accion_estadisticas(paises):
    #Muestra distintas estadísticas sobre los países cargados
    
    #Obtiene el país con mayor y menor población
    mayor, menor = pais_con_mayor_menor_poblacion(paises)
    if mayor and menor:
        print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
        print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")

    #Calcula y muestra promedios de población y superficie
    print(f"Promedio de población: {promedio_poblacion(paises):.2f}")
    print(f"Promedio de superficie: {promedio_superficie(paises):.2f} km²")

    #Muestra la cantidad de países por continente
    conteo = cantidad_por_continente(paises)
    print('Cantidad de países por continente:')
    for c, n in conteo.items():
        print(f"- {c}: {n}")
