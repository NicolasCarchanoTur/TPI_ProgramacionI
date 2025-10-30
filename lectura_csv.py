import csv
import os
from typing import List, Dict
from utilidades import validar_int, formato_pais_valido

# Columnas esperadas en el CSV
CAMPOS_CSV = ['nombre', 'poblacion', 'superficie', 'continente']

# Lee los países desde un archivo CSV
def leer_paises_desde_csv(ruta: str) -> List[Dict]:
    paises = []

    #Si el archivo no existe, lo creamos automáticamente
    if not os.path.exists(ruta):
        print(f"\nArchivo '{ruta}' no encontrado. Se creará uno nuevo con datos de ejemplo.\n")
        crear_csv_ejemplo(ruta)

    try:
        with open(ruta, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')

            cabeceras = [h.strip().lower() for h in reader.fieldnames] if reader.fieldnames else []

            if any(c not in cabeceras for c in CAMPOS_CSV):
                raise ValueError(f"El CSV debe contener las columnas: {CAMPOS_CSV}. Encontrado: {cabeceras}")

            for i, row in enumerate(reader, start=2):
                try:
                    nombre = row.get('nombre', '').strip()
                    poblacion_raw = row.get('poblacion', '').strip()
                    superficie_raw = row.get('superficie', '').strip()
                    continente = row.get('continente', '').strip()

                    if not formato_pais_valido(nombre, continente):
                        print(f"Fila {i}: nombre o continente vacío. Se omite.")
                        continue

                    poblacion = validar_int(poblacion_raw)
                    superficie = validar_int(superficie_raw)

                    if poblacion is None or superficie is None:
                        print(f"Fila {i}: error en tipos numéricos. Se omite.")
                        continue

                    paises.append({
                        'nombre': nombre,
                        'poblacion': poblacion,
                        'superficie': superficie,
                        'continente': continente
                    })
                except Exception as e:
                    print(f"Error procesando fila {i}: {e}. Se omite.")

    except ValueError as ve:
        print(f"Error en formato del CSV: {ve}")
    except Exception as e:
        print(f"Error leyendo el CSV: {e}")
    
    return paises


#Crea un CSV base si no existe

def crear_csv_ejemplo(ruta: str):
    #Crea un archivo CSV de ejemplo con algunos países iniciales
    datos_ejemplo = [
        {'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'},
        {'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'},
        {'nombre': 'Alemania', 'poblacion': 83149300, 'superficie': 357022, 'continente': 'Europa'},
        {'nombre': 'Nigeria', 'poblacion': 206139589, 'superficie': 923768, 'continente': 'África'},
        {'nombre': 'Australia', 'poblacion': 25687041, 'superficie': 7692024, 'continente': 'Oceanía'},
    ]

    with open(ruta, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CAMPOS_CSV, delimiter=';')
        writer.writeheader()
        writer.writerows(datos_ejemplo)

    print(f"Archivo '{ruta}' creado exitosamente con {len(datos_ejemplo)} registros de ejemplo.\n")
