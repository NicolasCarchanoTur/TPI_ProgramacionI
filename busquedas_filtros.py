from typing import List, Dict  #Tipos para mayor claridad

#Busca países cuyo nombre contenga un término dado
def buscar_por_nombre(paises: List[Dict], termino: str) -> List[Dict]:
    t = termino.strip().lower()  #Limpia y pasa a minúsculas
    return [p for p in paises if t in p['nombre'].lower()]  #Devuelve coincidencias

#Filtra países por continente
def filtrar_por_continente(paises: List[Dict], continente: str) -> List[Dict]:
    c = continente.strip().lower()
    return [p for p in paises if c in p['continente'].lower()]

#Filtra países según rango de población
def filtrar_por_rango_poblacion(paises: List[Dict], min_pob: int, max_pob: int) -> List[Dict]:
    return [p for p in paises if min_pob <= p['poblacion'] <= max_pob]

#Filtra países según rango de superficie
def filtrar_por_rango_superficie(paises: List[Dict], min_sup: int, max_sup: int) -> List[Dict]:
    return [p for p in paises if min_sup <= p['superficie'] <= max_sup]
