# 🌍 Proyecto: Gestor de Países en Python

## 📘 Descripción del Programa

El **Gestor de Países** es una aplicación de consola desarrollada en Python que permite **leer, organizar, filtrar y analizar información de países** almacenada en un archivo CSV.  
Su propósito es facilitar el manejo de datos geográficos y demográficos mediante un **menú interactivo** y **funciones modulares**, promoviendo el aprendizaje de conceptos como:

- Lectura y validación de archivos CSV.
- Uso de estructuras de datos (listas y diccionarios).
- Ordenamientos y filtrados personalizados.
- Cálculo de estadísticas simples.
- Buenas prácticas de modularidad y reutilización de código.

---

## ⚙️ Instrucciones de Uso

### 🧩 1. Requisitos previos

- Tener instalado **Python 3.8 o superior**.
- Todos los archivos `.py` y el archivo `paises.csv` deben estar en la **misma carpeta**.

### 📁 2. Archivos del proyecto

| Archivo            | Descripción                                                                          |
| ------------------ | ------------------------------------------------------------------------------------ |
| `acciones_menu.py` | Contiene las acciones principales del menú (buscar, filtrar, ordenar, estadísticas). |
| `lectura_csv.py`   | Carga y valida los datos desde el archivo CSV. Si no existe, crea uno de ejemplo.    |
| `ordenamientos.py` | Funciones para ordenar países por nombre, población o superficie.                    |
| `estadisticas.py`  | Calcula promedios, mayores/menores valores y conteos por continente.                 |
| `utilidades.py`    | Funciones auxiliares para pedir y validar datos del usuario.                         |
| `paises.csv`       | Archivo de datos con la información de los países.                                   |

---

### ▶️ 3. Ejecución

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta el archivo principal:
   ```bash
   python acciones_menu.py
   ```
3. Seguí las instrucciones en pantalla para interactuar con el menú.

---

### 🧭 4. Navegación del Menú

```
=== MENÚ PRINCIPAL ===
1. Buscar país
2. Filtrar países
3. Ordenar países
4. Ver estadísticas
5. Mostrar todos los paises
0. Salir
```

Cada opción ejecuta una funcionalidad distinta, permitiendo explorar o analizar los datos de manera dinámica.

---

## 💡 Ejemplos de Entradas y Salidas

### 🔹 Ejemplo 1: Búsqueda por nombre

**Entrada:**

```
Seleccione una opción: 1
Ingrese nombre o parte del nombre: arg
```

**Salida:**

```
Resultados encontrados:
- Argentina | Población: 45376763 | Superficie: 2780400 km² | Continente: América
```

---

### 🔹 Ejemplo 2: Filtrado por rango de población

**Entrada:**

```
Seleccione una opción: 2
Elija filtro (a/b/c): b
Población mínima: 30000000
Población máxima: 90000000
```

**Salida:**

```
Países entre 30 y 90 millones de habitantes:
- Alemania | 83149300 habitantes
- Argentina | 45376763 habitantes
```

---

### 🔹 Ejemplo 3: Ordenamiento descendente por superficie

**Entrada:**

```
Seleccione una opción: 3
Elija criterio (a/b/c): c
Orden ascendente o descendente? (a/d): d
```

**Salida:**

```
Países ordenados por superficie (mayor a menor):
1. Australia — 7,692,024 km²
2. Argentina — 2,780,400 km²
3. Nigeria — 923,768 km²
4. Alemania — 357,022 km²
5. Japón — 377,975 km²
```

---

### 🔹 Ejemplo 4: Estadísticas generales

**Entrada:**

```
Seleccione una opción: 4
```

**Salida:**

```
País con mayor población: Nigeria (206139589)
País con menor población: Australia (25687041)
Promedio de población: 97401538.40
Promedio de superficie: 2420981.80 km²
Cantidad de países por continente:
- América: 1
- Asia: 1
- Europa: 1
- África: 1
- Oceanía: 1
```

---

## 🧮 Ejemplo del archivo `paises.csv`

El archivo debe estar en formato **CSV con punto y coma (;)** y tener las siguientes columnas:

```csv
nombre;poblacion;superficie;continente
Argentina;45376763;2780400;América
Japón;125800000;377975;Asia
Alemania;83149300;357022;Europa
Nigeria;206139589;923768;África
Australia;25687041;7692024;Oceanía
```

> 💡 Si el archivo no existe, el programa lo creará automáticamente con datos de ejemplo.

---

## 👥 Participación de los Integrantes

| Integrante | Rol / Aporte |

| **Nicolás Exequiel Carchano** | Desarrolló los archivos `main.py` y `acciones_menu.py`, integrando los distintos módulos del proyecto. También colaboró en la redacción y mejora de los comentarios del código. |

| **Santino Cárdenas** | Creó las funciones principales de los módulos lógicos (ordenamientos, filtros, estadísticas y utilidades). Además, colaboró en la documentación y comentarios del código. |

---

## 🧠 Objetivos de Aprendizaje

- Comprender la **modularización de código en Python**.
- Practicar la **lectura y escritura de archivos CSV**.
- Aplicar **funciones de ordenamiento, filtrado y búsqueda** en estructuras de datos.
- Implementar **interacción con el usuario** mediante entrada y validación de datos.
- Calcular **estadísticas básicas** sobre conjuntos de información.

---

## LINK GOOGLE DRIVE PARA VIDEO E INFORME: https://drive.google.com/drive/folders/1zFNjJZoEDEZl3dcgygd7_u04tF8QUGwn?usp=sharing
