# telar/utilidades.py
def enviar_linea(self, linea):
    linea = f"{linea}\r\n"
    self.send(linea.encode("utf-8"))

def enviar_encabezado(self, nombre, valor):
    self.enviar_linea(f"{nombre}: {valor}")
