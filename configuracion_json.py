# telar/configuracion_json.py
import json
import os

CONFIG_ARCHIVO = "config_tel.json"

def guardar_configuracion(args):
    datos = {
        "host": args.host,
        "port": args.port,
        "sockets": args.sockets,
        "https": args.https,
        "usar_proxy": args.usar_proxy,
        "proxy_host": args.proxy_host,
        "proxy_port": args.proxy_port,
        "agente_aleatorio": args.agente_aleatorio,
        "tiempo_espera": args.tiempo_espera
    }
    with open(CONFIG_ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)
    print("✅ Configuración guardada en config_tel.json")

def cargar_configuracion(args):
    if not os.path.exists(CONFIG_ARCHIVO):
        return
    try:
        with open(CONFIG_ARCHIVO, "r") as f:
            datos = json.load(f)
            args.host = datos.get("host")
            args.port = datos.get("port", 80)
            args.sockets = datos.get("sockets", 150)
            args.https = datos.get("https", False)
            args.usar_proxy = datos.get("usar_proxy", False)
            args.proxy_host = datos.get("proxy_host", "127.0.0.1")
            args.proxy_port = datos.get("proxy_port", 8080)
            args.agente_aleatorio = datos.get("agente_aleatorio", False)
            args.tiempo_espera = datos.get("tiempo_espera", 15)
            print("📂 Configuración cargada desde config_tel.json")
    except Exception as e:
        print(f"⚠️ Error al cargar configuración: {e}")