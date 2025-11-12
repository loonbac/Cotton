# Telar – Herramienta DOS mediante estrés HTTP/s

**Telar** es una herramienta desarrollada en Python para realizar pruebas de estrés sobre servidores web HTTP/S. Inspirada en el ataque Slowloris, Telar permite evaluar la resiliencia de un servidor ante múltiples conexiones persistentes e incompletas.

⚠️ Esta herramienta debe usarse exclusivamente con fines educativos, de investigación o en entornos controlados con autorización explícita.


Nota: este repositorio es un fork del proyecto original "Telar" (autor: Walther Curo). El fork se denomina "Cotton" y añade compatibilidad para mostrar información en una pantalla conectada por Arduino, además de otras mejoras. Se planea añadir otras funcionalidades extra en próximas versiones.

## Resumen de funcionalidades

- ✅ Interfaz CLI interactiva paso a paso
- ✅ Soporte para:
    - HTTPS
    - Agentes de usuario aleatorios
    - Proxy SOCKS5
- ✅ Persistencia de configuración (`config_tel.json`)
- ✅ Registro de métricas (ahora implementado)
- ✅ Integración con un display Arduino (opcional)

## Novedades implementadas en Cotton

- Integración con un display Arduino a través del módulo `arduino_display.py`.
    - Nueva clase `ArduinoDisplay` que se comunica por puerto serie y muestra en la pantalla estado de la ejecución, iteraciones y resumen.
    - Argumento CLI `--arduino-port` para configurar el puerto serie (por ejemplo `COM3` o `/dev/ttyUSB0`).
    - Envío en tiempo real de métricas al Arduino (iteraciones, sockets activos, sockets cerrados) desde `metricas.py`.
    - Persistencia de `arduino_port` en `config_tel.json` (funciones de guardar/cargar actualizadas).

Estas adiciones permiten monitorizar la ejecución en un display físico durante la prueba.

## ¿Cómo funciona?

Telar mantiene abiertas múltiples conexiones al servidor objetivo y envía cabeceras HTTP de forma lenta e incompleta, forzando al servidor a mantener recursos ocupados. Este comportamiento coloca el host destino en denegación de servicio sin necesidad de tráfico volumétrico.

## Requisitos

- Python 3.8 o superior
- Dependencias detectadas (mínimo):
    - `PySocks` (para proxy SOCKS5) — paquete PyPI: `pysocks` o `PySocks`
    - `pyserial` (para la integración con Arduino)

Recomendación: fijar versiones para reproducibilidad (por ejemplo `PySocks>=1.7.1`, `pyserial>=3.5`).

Contenido del archivo `requirements.txt` actual (estimado):

```
PySocks
pyserial
```

## Ejecución mediante linea de comandos

Clonar el repositorio, ingresar en la carpeta del proyecto y ejecutar:

```
python telar_shell.py hostdestino -p 80 -s 500
```

Parámetros principales:

| Argumento                        | Descripción                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| `hostdestino`           | Dirección IP o dominio del servidor objetivo.                              |
| `-p`, `--port`                  | Puerto del servidor (por defecto: `80`).                                   |
| `-s`, `--sockets`               | Número de sockets a usar en la prueba (por defecto: `150`).                |
| `-v`, `--verbose`               | Muestra información detallada en consola.                                  |
| `-ua`, `--randuseragents`       | Usa un agente de usuario aleatorio por socket (simula múltiples clientes). |
| `-ue`, `--useproxy`             | Usa un proxy SOCKS5 para conectar los sockets.                             |
| `--proxy-host`                  | Dirección del proxy SOCKS5 (por defecto: `127.0.0.1`).                     |
| `--proxy-port`                  | Puerto del proxy SOCKS5 (por defecto: `8080`).                             |
| `--https`                       | Activa el uso de conexiones seguras (HTTPS).                               |
| `--sleeptime`                   | Tiempo entre envíos de cabeceras (en segundos, por defecto: `15`).         |
| `--arduino-port`                | Puerto serie para conexión al Arduino (ej: `COM3` o `/dev/ttyUSB0`).       |

## Ejecución mediante interfaz amigable
Clonar el repositorio, ingresar en la carpeta del proyecto y ejecutar:

```
python telar.py
```

Si quieres usar el display Arduino, conecta el dispositivo al puerto serie y ejecuta con:

```
python telar.py --arduino-port COM3
```

(Asegúrate de instalar `pyserial` antes: `pip install pyserial`.)


## Notas importantes y seguridad

Telar es una herramienta de ciberseguridad. Su uso indebido puede violar leyes locales e internacionales:

❌ No la utilices contra redes, servidores o servicios que no sean de tu propiedad.
✅ Úsala únicamente con fines educativos, de auditoría ética, o en pruebas controladas con consentimiento.

El autor y colaboradores no se responsabilizan por el uso indebido de esta herramienta.

## Descargo de Responsabilidad

Este software se proporciona con fines académicos y de prueba. Ni el autor ni los colaboradores se hacen responsables de los daños, interrupciones de servicio o consecuencias legales derivadas del uso de esta herramienta. El uso de Telar implica la aceptación de que:

Es responsabilidad exclusiva del usuario garantizar que cualquier actividad realizada con esta herramienta se encuentra legal y éticamente justificada.

Esta herramienta no debe usarse en producción ni contra infraestructuras reales sin consentimiento explícito.


## Licencia

Este proyecto está licenciado bajo la MIT License.

## Autor y contribuciones

Basado en el proyecto original "Telar" (autor: Walther Curo).

Este repositorio, llamado "Cotton", es un fork que ha sido extendido por LoonBac21 con integración para displays Arduino, mejoras en métricas y otras funcionalidades. Se mantendrán y reconocerán las contribuciones del autor original.

