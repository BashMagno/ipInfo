import os
import ipinfo
import pprint
import sys
from colorama import Fore, Style, init

####################
# CREATED BY MANGO #
####################


# Inicializar colorama
init()

def get_ip_details(api_token, ip_address):
    handler = ipinfo.getHandler(api_token)
    details = handler.getDetails(ip_address)
    return details.all

if __name__ == '__main__':
    api_token = os.environ.get('IPINFO_API_TOKEN')
    
    if not api_token:
        print(f"{Fore.RED}La variable de entorno IPINFO_API_TOKEN no está configurada.{Style.RESET_ALL}")
        sys.exit(1)

    ip_address = input(f"{Fore.MAGENTA}Por favor, ingresa la dirección IP: {Fore.RESET}")

    details_all = get_ip_details(api_token, ip_address)
    
    # Imprimir los detalles en morado
    pprint.pprint(details_all, indent=4, width=80, color=Fore.MAGENTA)
