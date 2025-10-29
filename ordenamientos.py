from typing import List, Dict

#Ordena los países por nombre
def ordenar_por_nombre(paises: List[Dict], descendente: bool = False) -> List[Dict]:
    return sorted(paises, key=lambda p: p['nombre'].lower(), reverse=descendente)  #Orden alfabético

#Ordena los países por población
def ordenar_por_poblacion(paises: List[Dict], descendente: bool = False) -> List[Dict]:
    return sorted(paises, key=lambda p: p['poblacion'], reverse=descendente)  #Orden por cantidad de habitantes

#Ordena los países por superficie
def ordenar_por_superficie(paises: List[Dict], descendente: bool = False) -> List[Dict]:
    return sorted(paises, key=lambda p: p['superficie'], reverse=descendente)  #Orden por tamaño del país
