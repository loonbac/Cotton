# telar/red.py
import random
import socket
from configuracion import args
from utilidades import enviar_linea, enviar_encabezado

socket.socket.enviar_linea = enviar_linea
socket.socket.enviar_encabezado = enviar_encabezado

if args.https:
    import ssl
    ssl.SSLSocket.enviar_linea = enviar_linea
    ssl.SSLSocket.enviar_encabezado = enviar_encabezado

if args.usar_proxy:
    import socks
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, args.proxy_host, args.proxy_port)
    socket.socket = socks.socksocket

agentes_usuario = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]

def iniciar_socket(ip: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)

    if args.https:
        contexto = ssl.create_default_context()
        contexto.check_hostname = False
        contexto.verify_mode = ssl.CERT_NONE
        s = contexto.wrap_socket(s, server_hostname=args.host)

    s.connect((ip, args.port))
    s.enviar_linea(f"GET /?{random.randint(0, 2000)} HTTP/1.1")

    agente = random.choice(agentes_usuario) if args.agente_aleatorio else agentes_usuario[0]
    s.enviar_encabezado("User-Agent", agente)
    s.enviar_encabezado("Accept-language", "en-US,en,q=0.5")
    return s