from typing import List, Dict, Tuple
import statistics

#Función auxiliar: clave para comparar por población
def clave_poblacion(pais: Dict) -> int:
    return pais['poblacion']

#Devuelve el país con mayor y menor población
def pais_con_mayor_menor_poblacion(paises: List[Dict]) -> Tuple[Dict, Dict]:
    if not paises:  #Si la lista está vacía
        return None, None
    mayor = max(paises, key=clave_poblacion)  #País con más población
    menor = min(paises, key=clave_poblacion)  #País con menos población
    return mayor, menor

#Calcula el promedio de población
def promedio_poblacion(paises: List[Dict]) -> float:
    if not paises:
        return 0.0
    return statistics.mean([p['poblacion'] for p in paises])  #Promedio de poblaciones

#Calcula el promedio de superficie
def promedio_superficie(paises: List[Dict]) -> float:
    if not paises:
        return 0.0
    return statistics.mean([p['superficie'] for p in paises])  #Promedio de superficies

#Cuenta cuántos países hay por continente
def cantidad_por_continente(paises: List[Dict]) -> Dict[str, int]:
    conteo = {}
    for p in paises:
        c = p['continente']
        conteo[c] = conteo.get(c, 0) + 1  #Suma 1 por cada país del continente
    return conteo
