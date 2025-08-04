# telar/telar.py
import sys
import os
import socket
from logica import ejecutar_telar
from configuracion import args
from configuracion_json import guardar_configuracion, cargar_configuracion

mensaje_estado = ""

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def es_ip_valida(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False

def menu():
    limpiar_pantalla()
    print("\n=== TELAR - Herramienta de Prueba de Estrés ===\n")
    if mensaje_estado:
        print(mensaje_estado)
        print("-" * len(mensaje_estado))
    print("1. Establecer host (actual: {})".format(args.host or "no definido"))
    print("2. Establecer puerto (actual: {})".format(args.port))
    print("3. Número de sockets (actual: {})".format(args.sockets))
    print("4. Activar HTTPS (actual: {})".format(args.https))
    print("5. Usar proxy SOCKS5 (actual: {})".format(args.usar_proxy))
    print("6. Activar agente de usuario aleatorio (actual: {})".format(args.agente_aleatorio))
    print("7. Establecer tiempo de espera (actual: {}s)".format(args.tiempo_espera))
    print("8. Ejecutar ataque")
    print("9. Guardar configuración actual")
    print("0. Salir")

def iniciar_menu():
    global mensaje_estado
    cargar_configuracion(args)
    mensaje_estado = "📂 Configuración cargada desde config_tel.json" if args.host else ""

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_host = input("Ingrese el host (IP o dominio): ").strip()
            if es_ip_valida(nuevo_host):
                args.host = nuevo_host
                mensaje_estado = "✅ Host actualizado."
            else:
                mensaje_estado = "❌ Host inválido. Intente nuevamente."
        elif opcion == "2":
            try:
                nuevo_puerto = int(input("Ingrese el puerto (1-65535): "))
                if 1 <= nuevo_puerto <= 65535:
                    args.port = nuevo_puerto
                    mensaje_estado = "✅ Puerto actualizado."
                else:
                    mensaje_estado = "❌ Puerto fuera de rango."
            except ValueError:
                mensaje_estado = "❌ Entrada inválida."
        elif opcion == "3":
            try:
                num = int(input("Ingrese número de sockets (mínimo 1): "))
                if num > 0:
                    args.sockets = num
                    mensaje_estado = "✅ Número de sockets actualizado."
                else:
                    mensaje_estado = "❌ Número inválido."
            except ValueError:
                mensaje_estado = "❌ Entrada inválida."
        elif opcion == "4":
            args.https = not args.https
            mensaje_estado = f"🔁 HTTPS {'activado' if args.https else 'desactivado'}."
        elif opcion == "5":
            args.usar_proxy = not args.usar_proxy
            mensaje_estado = f"🔁 Proxy {'activado' if args.usar_proxy else 'desactivado'}."
        elif opcion == "6":
            args.agente_aleatorio = not args.agente_aleatorio
            mensaje_estado = f"🔁 Agente aleatorio {'activado' if args.agente_aleatorio else 'desactivado'}."
        elif opcion == "7":
            try:
                espera = int(input("Tiempo entre headers (segundos): "))
                if espera >= 1:
                    args.tiempo_espera = espera
                    mensaje_estado = "✅ Tiempo de espera actualizado."
                else:
                    mensaje_estado = "❌ Debe ser al menos 1 segundo."
            except ValueError:
                mensaje_estado = "❌ Entrada inválida."
        elif opcion == "8":
            if not args.host:
                mensaje_estado = "❌ Debe establecer un host válido antes de ejecutar."
                continue
            print("\n⚠️ ¿Está seguro que desea ejecutar el ataque a {}:{} con {} sockets?".format(args.host, args.port, args.sockets))
            confirmar = input("Escriba 'SI' para continuar: ").strip().upper()
            if confirmar == "SI":
                limpiar_pantalla()
                ejecutar_telar()
                break
            else:
                mensaje_estado = "ℹ️ Ejecución cancelada."
        elif opcion == "9":
            guardar_configuracion(args)
            mensaje_estado = "✅ Configuración guardada correctamente."
        elif opcion == "0":
            confirmar = input("¿Desea guardar la configuración antes de salir? (s/N): ").strip().lower()
            if confirmar == "s":
                guardar_configuracion(args)
                print("✅ Configuración guardada. Saliendo...")
            else:
                print("Saliendo sin guardar...")
            break
        else:
            mensaje_estado = "❌ Opción inválida. Intente nuevamente."

if __name__ == "__main__":
    iniciar_menu()
