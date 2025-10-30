#Importamos la función para leer el CSV y las acciones del menú
from lectura_csv import leer_paises_desde_csv
from acciones_menu import (
    accion_buscar, accion_filtrar, accion_ordenar, accion_estadisticas
)

#Nombre del archivo CSV con los datos
ARCHIVO = 'paises.csv'


#Función auxiliar: Mostrar países

def mostrar_paises(paises):
    """Muestra un listado con los países recibidos."""
    if not paises:
        print('No hay países para mostrar.')
        return

    print(f'\nListado de {len(paises)} países:')
    for p in paises:
        print(f"- {p['nombre']} | Población: {p['poblacion']} | "
            f"Superficie: {p['superficie']} km² | Continente: {p['continente']}")


#Función principal: Menú

def menu_principal():
    """Despliega el menú principal y gestiona la interacción con el usuario."""
    
    #Carga los datos desde el CSV
    paises = leer_paises_desde_csv(ARCHIVO)
    if not paises:
        print('No se cargaron países. Verifique el archivo CSV.')

    #Bucle principal
    while True:
        print('\nMENÚ PRINCIPAL')
        print('1. Buscar país por nombre')
        print('2. Filtrar países')
        print('3. Ordenar países')
        print('4. Ver estadísticas')
        print('5. Mostrar todos los países')
        print('0. Salir')

        opcion = input('Seleccione una opción: ').strip()

        #Estructura match-case
        match opcion:
            case '1':
                accion_buscar(paises, mostrar_paises)
            case '2':
                accion_filtrar(paises, mostrar_paises)
            case '3':
                accion_ordenar(paises, mostrar_paises)
            case '4':
                accion_estadisticas(paises)
            case '5':
                mostrar_paises(paises)
            case '0':
                print('Salir')
                break
            case _:
                print('Opción inválida.')


#Punto de entrada del programa

if __name__ == '__main__':
    menu_principal()
