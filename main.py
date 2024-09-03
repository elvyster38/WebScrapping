import requests
from bs4 import BeautifulSoup
from Formatdate import convertir_fecha
import re

# URL de la página web que quieres hacer scraping
url = 'https://www.yelu.do/leidsa/results/loto-mas'

# Realizar la petición HTTP
response = requests.get(url)

# Verificar si la petición fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

     # Abrir el archivo en modo escritura dentro del bloque with
    with open('Resultado.txt', 'w', encoding='utf-8') as file:
    
        # Buscar todas las filas de la tabla dentro del div con clase "desc"
        rows = soup.select('div.desc tr')
        
        for row in rows:
            # Obtener el td con title="Fecha del Sorteo"
            fecha_td = row.select_one('td[title="Fecha del Sorteo"]')
            
            # Verificar que exista el td y obtener el contenido
            if fecha_td:
                fecha_texto = fecha_td.decode_contents().strip()
                
                # Obtener todos los span dentro del row
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

                    print(resultado)
else:
    print(f"Error al acceder a la página: {response.status_code}")
