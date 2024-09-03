import datetime

def convertir_fecha(fecha_texto):
    # Mapeo de nombres de meses en español a números
    meses = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }

    # Dividir la fecha en día, mes, y año
    dia, _, mes, año = fecha_texto.split()

    # Convertir al formato "dd/mm/yyyy"
    fecha_formateada = f"{dia}/{meses[mes]}/{año}"

    return fecha_formateada