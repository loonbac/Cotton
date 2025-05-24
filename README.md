# Telar – Herramienta DOS mediante estrés HTTP/s

**Telar** es una herramienta desarrollada en Python para realizar pruebas de estrés sobre servidores web HTTP/S. Inspirada en el ataque Slowloris, Telar permite evaluar la resiliencia de un servidor ante múltiples conexiones persistentes e incompletas.

⚠️ Esta herramienta debe usarse exclusivamente con fines educativos, de investigación o en entornos controlados con autorización explícita.


## Características

-   ✅ Interfaz CLI interactiva paso a paso
-   ✅ Soporte para:
    -   HTTPS
    -   Agentes de usuario aleatorios
    -   Proxy SOCKS5
-   ✅ Persistencia de configuración (`config_tel.json`)
-   ✅ Registro de métricas (proximamente)

## ¿Cómo funciona?

Telar mantiene abiertas múltiples conexiones al servidor objetivo y envía cabeceras HTTP de forma lenta e incompleta, forzando al servidor a mantener recursos ocupados. Este comportamiento coloca el host destino en denegación de servicio sin necesidad de tráfico volumétrico.

## Requisitos

-   Python 3.8 o superior
-   Recomendado:
    -   `pysocks`  (`pip install pysocks`)

## Ejecución mediante linea de comandos:

Clonar el repositorio, ingresar en la carpeta del proyecto y ejecutar:

    python telar.py hostdestino -p80 -s500

| Argumento                        | Descripción                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| `hostdestino`           | Dirección IP o dominio del servidor objetivo.                              |
| `-p`, `--port`                  | Puerto del servidor (por defecto: `80`).                                   |
| `-s`, `--sockets`               | Número de sockets a usar en la prueba (por defecto: `150`).                |
| `-v`, `--verbose`               | Muestra información detallada en consola.                                  |
| `-ua`, `--randuseragents`      | Usa un agente de usuario aleatorio por socket (simula múltiples clientes). |
| `-ue`, `--useproxy`            | Usa un proxy SOCKS5 para conectar los sockets.                             |
| `--proxy-host`                 | Dirección del proxy SOCKS5 (por defecto: `127.0.0.1`).                      |
| `--proxy-port`                 | Puerto del proxy SOCKS5 (por defecto: `8080`).                              |
| `--https`                      | Activa el uso de conexiones seguras (HTTPS).                               |
| `--sleeptime`                  | Tiempo entre envíos de cabeceras (en segundos, por defecto: `15`).         |

## Ejecución mediante interfaz amigable:
Clonar el repositorio, ingresar en la carpeta del proyecto y ejecutar:

    python interactivo.py


## Importante

Telar es una herramienta de ciberseguridad. Su uso indebido puede violar leyes locales e internacionales:

❌ No la utilices contra redes, servidores o servicios que no sean de tu propiedad.
✅ Úsala únicamente con fines educativos, de auditoría ética, o en pruebas controladas con consentimiento.

El autor y colaboradores no se responsabilizan por el uso indebido de esta herramienta.

## Descargo de Responsabilidad

Este software se proporciona con fines académicos y de prueba. Ni el autor ni los colaboradores se hacen responsables de los daños, interrupciones de servicio o consecuencias legales derivadas del uso de esta herramienta. El uso de Telar implica la aceptación de que:

Es responsabilidad exclusiva del usuario garantizar que cualquier actividad realizada con esta herramienta se encuentra legal y éticamente justificada.

Esta herramienta no debe usarse en producción ni contra infraestructuras reales sin consentimiento explícito


## Licencia

Este proyecto está licenciado bajo la MIT License.

## Autor
Walther Curo
