# Importación de funciones desde otros módulos del proyecto

from lectura_csv import leer_paises_desde_csv
from busquedas_filtros import buscar_por_nombre, filtrar_por_continente, filtrar_por_rango_poblacion, filtrar_por_rango_superficie
from ordenamientos import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie
from estadisticas import pais_con_mayor_menor_poblacion, promedio_poblacion, promedio_superficie, cantidad_por_continente
from utilidades import pedir_entero, pedir_texto

# Nombre del archivo CSV que contiene los datos de países
ARCHIVO = 'paises.csv'

def mostrar_paises(paises):
    # Si la lista está vacía, muestra un mensaje y sale
    if not paises:
        print('No hay países para mostrar.')
        return
    # Muestra el total de países y sus datos básicos
    print(f'\nListado de {len(paises)} países:')
    for p in paises:
        print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")

# Función principal que muestra el menú interactivo
def menu_principal():
    # Carga los datos de los países desde el archivo CSV
    paises = leer_paises_desde_csv(ARCHIVO)
    if not paises:
        print('No se cargaron países. Verifique el archivo CSV.')

    # Bucle principal del programa (se repite hasta elegir salir)
    while True:
        print('\nMENÚ PRINCIPAL') 
        print('1. Buscar país por nombre')
        print('2. Filtrar países')
        print('3. Ordenar países')
        print('4. Ver estadísticas')
        print('5. Mostrar todos los países')
        print('0. Salir')
        
        # Se pide al usuario una opción del menú
        opcion = input('Seleccione una opción: ').strip()
        
        # Se usa la estructura match-case para manejar las opciones del menú
        match opcion:
            
            # ---- OPCIÓN 1: Buscar país por nombre ----
            case '1':
                termino = pedir_texto('Ingrese nombre o parte del nombre: ')
                mostrar_paises(buscar_por_nombre(paises, termino))
            
            # ---- OPCIÓN 2: Filtrar países ----
            case '2':
                print('\nFILTRAR') 
                print('a. Por continente') 
                print('b. Por rango de población') 
                print('c. Por rango de superficie')
                sub = input('Elija filtro (a/b/c): ').strip().lower()
                # Submenú de filtros
                match sub:
                    # Filtro por continente
                    case 'a':
                        cont = pedir_texto('Ingrese continente (ej: América, Europa, Asia): ')
                        mostrar_paises(filtrar_por_continente(paises, cont))
                    
                    # Filtro por rango de población    
                    case 'b':
                        min_p = pedir_entero('Población mínima: ', minimo=0)
                        max_p = pedir_entero('Población máxima: ', minimo=min_p)
                        mostrar_paises(filtrar_por_rango_poblacion(paises, min_p, max_p))
                    
                    # Filtro por rango de superficie
                    case 'c':
                        min_s = pedir_entero('Superficie mínima (km²): ', minimo=0)
                        max_s = pedir_entero('Superficie máxima (km²): ', minimo=min_s)
                        mostrar_paises(filtrar_por_rango_superficie(paises, min_s, max_s))
                    
                    # Opción no válida
                    case _:
                        print('Opción inválida.')
            
            # ---- OPCIÓN 3: Ordenar países ----
            case '3':
                print('\nORDENAR') 
                print('a. Por nombre') 
                print('b. Por población') 
                print('c. Por superficie') 
                sub = input('Elija criterio (a/b/c): ').strip().lower()
                sentido = input('Orden ascendente o descendente? (a/d): ').strip().lower()
                desc = True if sentido == 'd' else False
                
                # Se ejecuta el ordenamiento correspondiente
                match sub:
                    case 'a':
                        mostrar_paises(ordenar_por_nombre(paises, desc))
                    case 'b':
                        mostrar_paises(ordenar_por_poblacion(paises, desc))
                    case 'c':
                        mostrar_paises(ordenar_por_superficie(paises, desc))
                    case _:
                        print('Opción inválida.')
            
            # ---- OPCIÓN 4: Ver estadísticas ----
            case '4':
                
                # Obtiene el país con mayor y menor población
                mayor, menor = pais_con_mayor_menor_poblacion(paises)
                if mayor and menor:
                    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})") 
                    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})") 
                
                # Muestra promedios de población y superficie    
                print(f"Promedio de población: {promedio_poblacion(paises):.2f}") 
                print(f"Promedio de superficie: {promedio_superficie(paises):.2f} km²") 

                # Muestra cuántos países hay por continente
                conteo = cantidad_por_continente(paises) 
                print('Cantidad de países por continente:') 
                for c, n in conteo.items(): 
                    print(f"- {c}: {n}")

            # ---- OPCIÓN 5: Mostrar todos los países ----
            case '5':
                mostrar_paises(paises)
            
            # ---- OPCIÓN 0: Salir del programa ----
            case '0':
                print('Salir')
                break
            
            # ---- Cualquier otra entrada ----
            case _:
                print('Opción inválida.')

# Punto de entrada principal del programa
if __name__ == '__main__':
    menu_principal()