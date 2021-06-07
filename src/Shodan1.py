"""
Uso: Buscar en Shodan
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 06 Junio 2021
"""

import getpass
import shodan

api = getpass.getpass("Introduce tu API key: ")
shodan = shodan.Shodan(api)
buscar = input("Qué vas a buscar? ")
resultados = shodan.search(buscar)
print(resultados['matches'][0])
