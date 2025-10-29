from typing import Optional

#Valida si un valor puede convertirse a entero positivo
def validar_int(valor: str) -> Optional[int]:
    try:
        valor = valor.replace(',', '').strip()  #Quita comas y espacios
        n = int(valor)
        if n < 0:  #No se aceptan números negativos
            return None
        return n
    except Exception:
        return None  #Si no se puede convertir, devuelve None

#Verifica que el nombre y continente no estén vacíos
def formato_pais_valido(nombre: str, continente: str) -> bool:
    return bool(nombre and continente)

#Pide un número entero con validación de rango
def pedir_entero(prompt: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        entrada = input(prompt).strip()  #Lee y limpia el texto
        if entrada == '':
            print("Entrada vacía. Intente nuevamente.")
            continue
        try:
            n = int(entrada)
            if minimo is not None and n < minimo:  #Verifica mínimo
                print(f"El valor debe ser >= {minimo}.")
                continue
            if maximo is not None and n > maximo:  #Verifica máximo
                print(f"El valor debe ser <= {maximo}.")
                continue
            return n
        except ValueError:
            print("Por favor ingrese un número entero válido.")  #Error si no es número

#Pide texto no vacío al usuario
def pedir_texto(prompt: str) -> str:
    while True:
        t = input(prompt).strip()
        if t == '':  #No permite cadenas vacías
            print("Entrada vacía. Intente nuevamente.")
            continue
        return t
