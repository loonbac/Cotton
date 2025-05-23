# 🧵 Telar – Herramienta DOS mediante prueba de estrés HTTP

**Telar** es una herramienta modular desarrollada en Python para realizar pruebas de estrés de bajo ancho de banda contra servidores web HTTP/S. Inspirada en el ataque Slowloris, Telar permite evaluar la resiliencia de un servidor ante múltiples conexiones persistentes e incompletas.

> ⚠️ Esta herramienta debe usarse exclusivamente con fines educativos, de investigación o en entornos controlados con autorización explícita.

---

## 🚀 Características

- ✅ Interfaz CLI interactiva paso a paso
- ✅ Modularizada y fácil de extender
- ✅ Soporte para:
  - HTTPS
  - Agentes de usuario aleatorios
  - Proxy SOCKS5
- ✅ Persistencia de configuración (`config_tel.json`)
- ✅ Registro de métricas (fase en desarrollo)

---

## 🧠 ¿Cómo funciona?

Telar mantiene abiertas múltiples conexiones al servidor objetivo y envía cabeceras HTTP de forma lenta e incompleta, forzando al servidor a mantener recursos ocupados. Este comportamiento coloca el host destino en denegación de servicio sin necesidad de tráfico volumétrico.

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Recomendado:
  - `pysocks` (`pip install pysocks`)

---

# 🧪 Ejecución

Clonar Repositorio, ingresar a la capeta telar y ejecutar:

#Modo Bash
-
python telar.py hostdestino -p80 -s500
-


#Modo Inteactivo
-
python interactivo.py
-




Telar es una herramienta de ciberseguridad. Su uso indebido puede violar leyes locales e internacionales.

❌ No la utilices contra redes, servidores o servicios que no sean de tu propiedad.

✅ Úsala únicamente con fines educativos, de auditoría ética, o en pruebas controladas con consentimiento.

⚖️ El autor y colaboradores no se responsabilizan por el uso indebido de esta herramienta.

---

⚠️ Descargo de Responsabilidad

Este software se proporciona con fines académicos y de prueba. Ni el autor ni los colaboradores se hacen responsables de los daños, interrupciones de servicio o consecuencias legales derivadas del uso de esta herramienta.

El uso de Telar implica la aceptación de que:

Es responsabilidad exclusiva del usuario garantizar que cualquier actividad realizada con esta herramienta se encuentra legal y éticamente justificada.

Esta herramienta no debe usarse en producción ni contra infraestructuras reales sin consentimiento explícito.

---

📜 Licencia

Este proyecto está licenciado bajo la MIT License.

---
Desarrollado por [WC] -
---
