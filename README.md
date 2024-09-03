# Web Scraping de Resultados de Sorteos

Este proyecto realiza web scraping de una página web de sorteos Yelu.do para extraer y procesar información específica sobre sorteo de Leidsa Loto. Utiliza Python con las bibliotecas `requests` y `BeautifulSoup` para obtener y manipular el contenido HTML.

## Descripción

El script extrae:

- El texto dentro del atributo `title` de los elementos `span` que se encuentran dentro de un `div` con la clase `desc`.
- El contenido de las celdas (`td`) que tienen el atributo `title` igual a "Fecha del Sorteo".
- Luego, concatena el contenido del `span` con su correspondiente texto de la misma fila de la tabla y guarda el resultado en un archivo de texto llamado `Resultado.txt`.

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar el script:

- Python 3.x
- requests
- BeautifulSoup4

Puedes instalarlas con pip:

```bash
pip install requests beautifulsoup4
