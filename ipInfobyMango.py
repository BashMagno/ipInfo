import os
import ipinfo
import pprint
import sys


####################
# CREATED BY MANGO #
####################


def get_ip_details(api_token, ip_address):
    handler = ipinfo.getHandler(api_token)
    details = handler.getDetails(ip_address)
    return details.all

if __name__ == '__main__':
    api_token = os.environ.get('IPINFO_API_TOKEN')
    
    if not api_token:
        print("ESP: La variable de entorno IPINFO_API_TOKEN no está configurada.")
        sys.exit(1)

    if len(sys.argv) != 2:
        print("ESP: Por favor, ingresa la dirección IP como argumento.")
        sys.exit(1)

    ip_address = sys.argv[1]
    details_all = get_ip_details(api_token, ip_address)
    pprint.pprint(details_all)
