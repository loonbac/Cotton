# telar/arduino_display.py
import serial
import time

class ArduinoDisplay:
    def __init__(self, puerto_com, baudrate=9600):
        self.puerto_com = puerto_com
        self.conexion = None
        self.conectado = False
        try:
            self.conexion = serial.Serial(puerto_com, baudrate, timeout=1)
            time.sleep(2)  # Esperar a que Arduino se inicialice
            self.conectado = True
            print(f"✅ Conectado al Arduino en {puerto_com}")
        except Exception as e:
            print(f"⚠️ No se pudo conectar al Arduino: {e}")
            print("ℹ️ El programa continuará sin pantalla LCD")
    
    def enviar_mensaje(self, linea1, linea2):
        """Envía dos líneas al Arduino LCD"""
        if not self.conectado:
            return
        try:
            mensaje = f"{linea1}\n{linea2}\n"
            self.conexion.write(mensaje.encode('utf-8'))
            self.conexion.flush()
        except Exception as e:
            print(f"⚠️ Error al enviar a Arduino: {e}")
    
    def mostrar_inicio(self, host, sockets):
        """Muestra pantalla de inicio"""
        self.enviar_mensaje("TELAR INICIANDO", f"Host:{host[:10]}")
        time.sleep(2)
        self.enviar_mensaje(f"Sockets: {sockets}", "Preparando...")
        time.sleep(1)
    
    def mostrar_ataque(self, iteracion, sockets_activos, cerrados):
        """Muestra estado del ataque en tiempo real"""
        linea1 = f"Iter:{iteracion} Act:{sockets_activos}"
        linea2 = f"Cerrados: {cerrados}"
        self.enviar_mensaje(linea1, linea2)
    
    def mostrar_resumen(self, iteraciones, prom_cerrados, resistencia):
        """Muestra resumen final"""
        self.enviar_mensaje("=== RESUMEN ===", f"Iters: {iteraciones}")
        time.sleep(3)
        self.enviar_mensaje(f"Prom.Cerr: {prom_cerrados:.0f}", "")
        time.sleep(3)
        
        # Mostrar nivel de resistencia
        if "Alta" in resistencia:
            self.enviar_mensaje("RESISTENCIA:", "ALTA")
        elif "Moderada" in resistencia:
            self.enviar_mensaje("RESISTENCIA:", "MODERADA")
        else:
            self.enviar_mensaje("RESISTENCIA:", "BAJA")
        time.sleep(3)
        self.enviar_mensaje("Ataque", "Finalizado!")
    
    def cerrar(self):
        """Cierra la conexión con Arduino"""
        if self.conexion and self.conectado:
            self.conexion.close()
            print("🔌 Conexión con Arduino cerrada")