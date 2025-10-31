from typing import List, Dict

#Funciones auxiliares para las claves de ordenamiento
def clave_nombre(pais: Dict) -> str:
    return pais['nombre'].lower()

def clave_poblacion(pais: Dict) -> int:
    return pais['poblacion']

def clave_superficie(pais: Dict) -> int:
    return pais['superficie']

#Ordena los países por nombre
def ordenar_por_nombre(paises: List[Dict], descendente: bool = False) -> List[Dict]:
    return sorted(paises, key=clave_nombre, reverse=descendente)  #Orden alfabético

#Ordena los países por población
def ordenar_por_poblacion(paises: List[Dict], descendente: bool = False) -> List[Dict]:
    return sorted(paises, key=clave_poblacion, reverse=descendente)  #Orden por cantidad de habitantes

#Ordena los países por superficie
def ordenar_por_superficie(paises: List[Dict], descendente: bool = False) -> List[Dict]:
    return sorted(paises, key=clave_superficie, reverse=descendente)  #Orden por tamaño del país
