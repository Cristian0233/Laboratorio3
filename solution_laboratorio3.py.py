def es_bisiesto(ano):
    # Verifica si el año es bisiesto según las reglas dadas.
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def validar_fecha(fecha):
    # Separa los elementos de la fecha
    dia, mes, anio = map(int, fecha.split())

    # Verifica el rango del mes
    if mes < 1 or mes > 12:
        return "Fecha incorrecta"

    # Verifica el rango del día según el mes
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Ajusta febrero para años bisiestos
    if es_bisiesto(anio):
        dias_por_mes[2] = 29
    
    if dia < 1 or dia > dias_por_mes[mes]:
        return "Fecha incorrecta"
    
    return "Fecha correcta"

# Ejemplos de uso
print(validar_fecha("30 11 1971"))  # Fecha correcta
print(validar_fecha("29 2 2001"))   # Fecha incorrecta
