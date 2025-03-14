# microevaluacion5

# Configuración de Red en Cisco CLI

Este documento describe la configuración de una red en Cisco utilizando el CLI (Command Line Interface). La red consta de un router central, 4 routers conectados, switches y PCs. La dirección IP base utilizada es `200.30.40.0`.

---

## **1. División de la Red en Subredes**

La red `200.30.40.0/24` se dividió en 4 subredes:

- **Subred 1:** `200.30.40.0/26` (Rango: `200.30.40.1` - `200.30.40.62`)
- **Subred 2:** `200.30.40.64/26` (Rango: `200.30.40.65` - `200.30.40.126`)
- **Subred 3:** `200.30.40.128/26` (Rango: `200.30.40.129` - `200.30.40.190`)
- **Subred 4:** `200.30.40.192/26` (Rango: `200.30.40.193` - `200.30.40.254`)

---

## **2. Configuración del Router Central**

El router central tiene 4 interfaces, cada una conectada a un router diferente.

### **Comandos de Configuración:**

```bash
enable
configure terminal

! Configurar interfaces
interface GigabitEthernet0/0
ip address 200.30.40.1 255.255.255.192
no shutdown
exit

interface GigabitEthernet0/1
ip address 200.30.40.65 255.255.255.192
no shutdown
exit

interface GigabitEthernet0/2
ip address 200.30.40.129 255.255.255.192
no shutdown
exit

interface GigabitEthernet0/3
ip address 200.30.40.193 255.255.255.192
no shutdown
exit

! Configurar enrutamiento estático (opcional)
ip route 200.30.40.64 255.255.255.192 200.30.40.2
ip route 200.30.40.128 255.255.255.192 200.30.40.66
ip route 200.30.40.192 255.255.255.192 200.30.40.130
ip route 200.30.40.0 255.255.255.192 200.30.40.194

3. Configuración de los Routers Conectados
Cada router conectado tiene una interfaz hacia el router central y otra hacia el switch.

Comandos de Configuración:
Router 1:
bash
Copy
enable
configure terminal

! Configurar interfaz hacia el router central
interface GigabitEthernet0/0
ip address 200.30.40.2 255.255.255.192
no shutdown
exit

! Configurar interfaz hacia el switch
interface GigabitEthernet0/1
ip address 200.30.40.3 255.255.255.192
no shutdown
exit

! Configurar enrutamiento estático (opcional)
ip route 0.0.0.0 0.0.0.0 200.30.40.1

! Guardar configuración
write memory
Router 2:
bash
Copy
enable
configure terminal

! Configurar interfaz hacia el router central
interface GigabitEthernet0/0
ip address 200.30.40.66 255.255.255.192
no shutdown
exit

! Configurar interfaz hacia el switch
interface GigabitEthernet0/1
ip address 200.30.40.67 255.255.255.192
no shutdown
exit

! Configurar enrutamiento estático (opcional)
ip route 0.0.0.0 0.0.0.0 200.30.40.65

! Guardar configuración
write memory
Router 3:
bash
Copy
enable
configure terminal

! Configurar interfaz hacia el router central
interface GigabitEthernet0/0
ip address 200.30.40.130 255.255.255.192
no shutdown
exit

! Configurar interfaz hacia el switch
interface GigabitEthernet0/1
ip address 200.30.40.131 255.255.255.192
no shutdown
exit

! Configurar enrutamiento estático (opcional)
ip route 0.0.0.0 0.0.0.0 200.30.40.129

! Guardar configuración
write memory
Router 4:
bash
Copy
enable
configure terminal

! Configurar interfaz hacia el router central
interface GigabitEthernet0/0
ip address 200.30.40.194 255.255.255.192
no shutdown
exit

! Configurar interfaz hacia el switch
interface GigabitEthernet0/1
ip address 200.30.40.195 255.255.255.192
no shutdown
exit

! Configurar enrutamiento estático (opcional)
ip route 0.0.0.0 0.0.0.0 200.30.40.193

! Guardar configuración
write memory
4. Configuración de los Switches
Los switches no requieren configuración IP, ya que funcionan en modo "plug and play". Si se necesitan VLANs, se pueden configurar según sea necesario.

5. Configuración de las PCs
Cada PC debe tener una dirección IP dentro de la subred correspondiente al router al que está conectada.

PC	IP	Máscara	Gateway
PC1	200.30.40.4	255.255.255.192	200.30.40.3
PC2	200.30.40.68	255.255.255.192	200.30.40.67
PC3	200.30.40.132	255.255.255.192	200.30.40.131
PC4	200.30.40.196	255.255.255.192	200.30.40.195
6. Verificación de Conectividad
Para verificar la conectividad, utiliza el comando ping desde las PCs:

bash
Copy
ping 200.30.40.1  # Probar conexión al router central