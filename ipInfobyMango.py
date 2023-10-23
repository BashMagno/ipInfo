import os
import ipinfo
import pprint
from colorama import Fore, Style, init

# Inicializar colorama
init()

def get_ip_details(api_token, ip_address):
    handler = ipinfo.getHandler(api_token)
    details = handler.getDetails(ip_address)
    return details.all

def scan_ip():
    api_token = os.environ.get('IPINFO_API_TOKEN')
    
    if not api_token:
        print(f"{Fore.RED}La variable de entorno IPINFO_API_TOKEN no está configurada.{Style.RESET_ALL}")
        return
    
    ip_address = input(f"{Fore.MAGENTA}Por favor, ingresa la dirección IP: {Fore.RESET}")

    details_all = get_ip_details(api_token, ip_address)
    
    # Imprimir los detalles en morado
    print(f"{Fore.MAGENTA}")
    pprint.pprint(details_all, indent=4, width=80)
    print(f"{Style.RESET_ALL}")

if __name__ == '__main__':
    while True:
        scan_ip()
        choice = input(f"{Fore.YELLOW}¿Deseas escanear otra IP? (s/n): {Fore.RESET}")
        if choice.lower() != 's':
            break
