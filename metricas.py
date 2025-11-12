# telar/metricas.py
import os
import time
from datetime import datetime

ruta_log = "logs/metricas_tel.log"
inicio_global = time.time()
iteracion_actual = 0
suma_cerrados = 0
suma_nuevos = 0
suma_duracion = 0.0
arduino_display = None

def configurar_arduino(display):
    """Configura la instancia del display Arduino"""
    global arduino_display
    arduino_display = display

def iniciar_log_metricas():
    os.makedirs("logs", exist_ok=True)
    with open(ruta_log, "a") as f:
        f.write("\n=== Inicio de ejecución: {} ===\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

def registrar_iteracion(sockets_activos, sockets_cerrados, sockets_nuevos, duracion_ms, sleeptime):
    global iteracion_actual, suma_cerrados, suma_nuevos, suma_duracion
    iteracion_actual += 1
    suma_cerrados += sockets_cerrados
    suma_nuevos += sockets_nuevos
    suma_duracion += duracion_ms

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = (
        f"[{timestamp}] Iteración {iteracion_actual} | "
        f"Activos: {sockets_activos} | Cerrados: {sockets_cerrados} | "
        f"Nuevos: {sockets_nuevos} | Duración: {duracion_ms:.2f} ms | "
        f"Sleeptime: {sleeptime}s"
    )
    with open(ruta_log, "a") as f:
        f.write(mensaje + "\n")
    
    # Enviar a Arduino en tiempo real
    if arduino_display:
        arduino_display.mostrar_ataque(iteracion_actual, sockets_activos, sockets_cerrados)

def finalizar_log():
    duracion_total = time.time() - inicio_global
    promedio_cerrados = suma_cerrados / iteracion_actual if iteracion_actual else 0
    promedio_nuevos = suma_nuevos / iteracion_actual if iteracion_actual else 0
    promedio_duracion = suma_duracion / iteracion_actual if iteracion_actual else 0

    if promedio_cerrados > 350:
        resistencia = "Alta - La App cumple con las capas de seguridad básicas."
    elif promedio_cerrados > 150:
        resistencia = "Moderada - La App esta luchando, pero necesita mejorar"
    else:
        resistencia = "Deprimente - La App no tiene capas de protección bien implementadas."

    resumen = (
        f"\n=== Fin de ejecución. Tiempo total: {duracion_total:.2f} segundos ===\n"
        f"Resumen automático:\n"
        f"- Iteraciones: {iteracion_actual}\n"
        f"- Promedio de Sockets Cerrados: {promedio_cerrados:.2f}\n"
        f"- Promedio de Sockets Nuevos: {promedio_nuevos:.2f}\n"
        f"- Promedio de duración por iteración: {promedio_duracion:.2f} ms\n"
        f"- Nivel estimado de resistencia de tu Aplicacion Web: {resistencia}\n"
    )
    with open(ruta_log, "a") as f:
        f.write(resumen)
    
    # Mostrar resumen en Arduino
    if arduino_display:
        arduino_display.mostrar_resumen(iteracion_actual, promedio_cerrados, resistencia)
    
    return resumen