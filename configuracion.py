# telar/configuracion.py
import argparse

parser = argparse.ArgumentParser(
    description="Telar, herramienta de prueba de estrés para sitios web"
)
parser.add_argument("host", nargs="?", help="Host para realizar la prueba de estrés")
parser.add_argument("-p", "--port", default=80, type=int, help="Puerto del servidor web, usualmente 80")
parser.add_argument("-s", "--sockets", default=150, type=int, help="Número de sockets a usar en la prueba")
parser.add_argument("-v", "--verbose", action="store_true", help="Activa el modo detallado")
parser.add_argument("-ua", "--randuseragents", dest="agente_aleatorio", action="store_true", help="Agentes de usuario aleatorios")
parser.add_argument("-ue", "--useproxy", dest="usar_proxy", action="store_true", help="Usar proxy SOCKS5")
parser.add_argument("--proxy-host", default="127.0.0.1", help="Host del proxy SOCKS5")
parser.add_argument("--proxy-port", default=8080, type=int, help="Puerto del proxy SOCKS5")
parser.add_argument("--https", action="store_true", help="Usar HTTPS")
parser.add_argument("--sleeptime", dest="tiempo_espera", default=15, type=int, help="Tiempo entre encabezados")

parser.set_defaults(verbose=False, agente_aleatorio=False, usar_proxy=False, https=False)
args = parser.parse_args()