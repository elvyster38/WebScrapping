import requests
from bs4 import BeautifulSoup
from Formatdate import convertir_fecha
import re

# URL de la página web que quieres hacer scraping
url = 'https://www.yelu.do/leidsa/results/loto-mas'

# Realizar la petición HTTP
response = requests.get(url)

def calcular_promedios(lista_anidada):
    # Obtener el número de elementos en cada sublista
    num_elementos = len(lista_anidada[0])
    
    # Inicializar listas para las sumas y contadores
    sumas = [0] * num_elementos
    contadores = [0] * num_elementos
    
    # Sumar los valores y contar los elementos
    for sublista in lista_anidada[1:]:
        for i, valor in enumerate(sublista):
            sumas[i] += valor
            contadores[i] += 1
    
    # Calcular los promedios
    promedios = [suma / contador for suma, contador in zip(sumas, contadores)]
    
    return promedios


# Verificar si la petición fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

     # Abrir el archivo en modo escritura dentro del bloque with
    with open('Resultado.txt', 'w', encoding='utf-8') as file:
    
        # Buscar todas las filas de la tabla dentro del div con clase "desc"
        rows = soup.select('div.desc tr')
        #Creamos lista vacia para luego guardar los resultados de cada fila, esto resultaria en una lista anidada
        listas = []
        for row in rows:
            # Obtener el td con title="Fecha del Sorteo"
            fecha_td = row.select_one('td[title="Fecha del Sorteo"]')
            
            # Verificar que exista el td y obtener el contenido
            if fecha_td:
                fecha_texto = fecha_td.decode_contents().strip()
                
                # Obtener todos los span dentro del row con title
                spans = row.select('span[title]')
                for span in spans:
                    span_text = span['title']

                    #creating a list from text using "-" or "+" for splitting
                    numeros = re.findall(r'\d+', span_text)
                    # Convertimos los resultados a enteros
                    numeros = list(map(int, numeros))
                    texto = ",".join(map(str, numeros))
                    fecha_texto_formateada = convertir_fecha(fecha_texto.split('-')[0])
                    # Concatenar el contenido
                    resultado = f"{fecha_texto_formateada} , {fecha_texto.split('-')[1]} , {texto} "
                    # Escribir el resultado en el archivo
                    file.write(resultado + '\n')        
                    listas.append(numeros)
                    print(resultado)

    print(calcular_promedios(listas))
    print(listas)
    
                    
else:
    print(f"Error al acceder a la página: {response.status_code}")
