# 🛡️ Proyectos de Ciberseguridad con Golang y Python

Este listado está diseñado para ayudarte a aprender Golang desde cero y perfeccionar Python, desarrollando herramientas útiles en el mundo de la ciberseguridad. Los proyectos están ordenados de menor a mayor dificultad.

---

## 🟢 Nivel Básico

### 1. Escáner de Puertos
- **Descripción**: Detecta puertos abiertos en una IP objetivo.
- **Python**: `socket`, `argparse`
- **Golang**: `net`, `flag`

### 2. Generador de Contraseñas Seguras
- **Descripción**: Crea contraseñas aleatorias con criterios de seguridad.
- **Python**: `secrets`, `string`
- **Golang**: `crypto/rand`, `math/big`

### 3. Hashing de Archivos
- **Descripción**: Calcula hashes (MD5, SHA256) para verificar integridad.
- **Python**: `hashlib`
- **Golang**: `crypto/md5`, `crypto/sha256`

---

## 🟡 Nivel Intermedio

### 4. Sniffer de Red
- **Descripción**: Captura paquetes de red en tiempo real.
- **Python**: `scapy`, `socket`
- **Golang**: `gopacket`, `pcap`

### 5. Analizador de Logs
- **Descripción**: Detecta patrones sospechosos en archivos de logs.
- **Python**: `re`, `pandas`
- **Golang**: `regexp`, `bufio`

### 6. Cifrador/Descifrador de Archivos
- **Descripción**: Aplica cifrado simétrico (AES) a archivos.
- **Python**: `cryptography`, `pyAesCrypt`
- **Golang**: `crypto/aes`, `crypto/cipher`

### 7. Detector de Vulnerabilidades Web Básico
- **Descripción**: Escanea URLs en busca de fallos comunes (XSS, SQLi).
- **Python**: `requests`, `BeautifulSoup`
- **Golang**: `net/http`, `goquery`

---

## 🔴 Nivel Avanzado

### 8. Keylogger
- **Descripción**: Registra pulsaciones de teclado (solo para fines educativos).
- **Python**: `pynput`, `keyboard`
- **Golang**: `github.com/micmonay/keybd_event`

### 9. Botnet Simulada
- **Descripción**: Red de clientes controlados remotamente (modo laboratorio).
- **Python**: `socket`, `threading`
- **Golang**: `net`, `goroutines`

### 10. Firewall Personalizado
- **Descripción**: Filtra tráfico según reglas definidas.
- **Python**: `iptables` (via `subprocess`), `netfilterqueue`
- **Golang**: `github.com/google/nftables`

### 11. Sistema de Detección de Intrusos (IDS)
- **Descripción**: Detecta comportamientos anómalos en la red.
- **Python**: `scapy`, `sklearn`, `numpy`
- **Golang**: `gopacket`, `gonum`, `mlgo`

### 12. Plataforma de Pentesting Automatizado
- **Descripción**: Ejecuta múltiples pruebas de seguridad sobre un objetivo.
- **Python**: `nmap`, `paramiko`, `subprocess`
- **Golang**: `os/exec`, `github.com/Ullaakut/nmap`

---

## 🧠 Recomendaciones Finales

- Usa **Docker** para aislar cada herramienta.
- Documenta cada proyecto con README y ejemplos.
- Publica tus proyectos en GitHub con enfoque profesional.
- Añade pruebas unitarias y logs para destacar en entrevistas técnicas.

---

