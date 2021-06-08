"""
Uso: Buscar Hosts
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 06 Junio 2021
"""

import getpass
import shodan

api = getpass.getpass("Introduce tu API key: ")
sites = []
shodan = shodan.Shodan(api)
resultados = shodan.search('port: 21 Anonymous user logged in')
print("Número de hosts encontrados ", len(resultados['matches']))
for match in resultados['matches']:
    if match['ip_str'] is not None:
        print(match['ip_str'])
        sites.append(match['ip_str'])
