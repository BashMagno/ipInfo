# **Usage ipInfo** 

> *{Creado por Mango / Created by Mango}*

**Obtener API** 

 1. Iniciamos sesión en [IpInfo](https://ipinfo.io).
 2. Una vez iniciado sesión , accedemos al [home](https://ipinfo.io/account/home) y "scrolleamos" o bajamos hasta que encontremos donde pone **ACCES TOKEN**.
 3. Copiamos el token al portapapeles.

**Almacenar la API token en una variable de entorno:**

En tu sistema operativo, configura una variable de entorno que contenga tu API token. El proceso exacto puede variar según el sistema operativo que estés utilizando. Aquí hay un ejemplo para Linux y macOS:
Deberemos cambiar **'TU_API_TOKEN_AQUI'** por el token que acabamos de copiar.
  

> bash


```bash
export IPINFO_API_TOKEN='TU_API_TOKEN_AQUI'
``` 

Para Windows, puedes hacerlo desde la línea de comandos con el siguiente comando:


> cmd / powershell


```
setx IPINFO_API_TOKEN "TU_API_TOKEN_AQUI"
```

## Clonar repositorio

**Forma rápida (copy&paste)**
```bash
git clone https://github.com/BashMagno/ipInfo
cd ipInfo
pip install -r requirements.txt
python3 ipInfobyMango.py

``` 
**Forma detallada**
1. Copiamos el repositorio a nuestro equipo local.

```bash
git clone https://github.com/BashMagno/ipInfo
``` 

2. Entramos al repositorio 

```bash
cd ipInfo
``` 

3. Instalamos los requerimientos

```bash
pip install -r requirements.txt
``` 

4. Ejecutamos el programa
```bash
python3 ipInfobyMango.py
``` 
<hr>
