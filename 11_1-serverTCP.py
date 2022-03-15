
from socket import AF_INET, SOCK_STREAM, socket

s = socket()
host = 'localhost'
port = 9999

#declaración de contadores de record globales:
globalGanado1=globalPerdido2=0
globalPerdido1=globalGanado2=0
globalEmpatado=0
#declaración de contadores de record de partida actuales:
actualEmpatado=0
actualGanado1=actualPerdido2=0
actualPerdido1=actualGanado2=0

#funcion empate para enviar mensajes de empate e incrementar los contadores
def empate(): 
    conn.send('Empate'.encode()) #se envía mensaje al jugador 1
    conn2.send('Empate'.encode()) #se envía mensaje al jugador 2
    globalEmpatado+=1 #se incrementa el contador de record global en 1
    actualEmpatado+=1 #se incrementa el contador de rcord de partida actual en 1

#funcion para enviar mensajes de "Perdiste" a jugador 1 e incrementar los contadores
def pierdeJugador1():
    conn.send('Perdiste'.encode()) #se envía mensaje al jugador 1
    conn2.send('Ganaste'.encode()) #se envía mensaje al jugador 2
    globalPerdido1+=1 #se incrementa en 1 el contador global perdido para jugador 1
    globalGanado2+=1 #se incrementa en 1 el contador global ganado para jugador 2
    actualPerdido1+=1 #se incrementa en 1 el contador de partida actual de perdido para jugador 1
    actualGanado2+=1 #se incrementa en 1 el contador de partida actual de ganado para jugador 2

#funcion para enviar mensajes de "Ganaste" a jugador 1 e incrementar los contadores
def ganasteJugador1():
     conn.send('Ganaste'.encode()) #se envía mensaje al jugador 1
     conn2.send('Perdiste'.encode()) #se envía mensaje al jugador 2
     globalGanado1+=1 #se incrementa en 1 el contador global ganado para jugador 1
     globalPerdido2+=1 #se incrementa en 1 el contador global perdido para jugador 2
     actualGanado1+=1 #se incrementa en 1 el contador de partida actual de ganado para jugador 1
     actualPerdido2+=1 #se incrementa en 1 el contador de partida actual de perdido para jugador 2


s.bind((host, port))
print('Esperando conexion')
s.listen(2)

while True:
    conn, addr = s.accept() #establecemos la conexion
    print('Jugador 1 ¡CONECTADO!')
    print(f'Direccion: {addr}')
    conn.send('J1'.encode())#envía un mensaje fijo#
    print('Esperando segundo jugador')
    conn2, addr2 = s.accept() #establecemos la conexion
    print('Jugador 2 ¡CONECTADO!')
    print(f'Direccion: {addr2}')
    conn2.send('J2'.encode())#envía un mensaje fijo
    
    while True:
        mensajeRecibido1 = conn.recv(4096).decode() #recibe el mensaje del jugador 1
        print(f'Jugador 1: {mensajeRecibido1}')
        if mensajeRecibido1 == 'salir': #si el jugador 1 se desconecta
            print('Esperando primer jugador')
            conn, addr = s.accept() #establecemos la conexion
            print('Jugador 1 ¡CONECTADO!')
            print(f'Direccion: {addr}')  
            conn.send('J1'.encode())#envía un mensaje fijo#
            mensajeRecibido1 = conn.recv(4096).decode() #recibe el mensaje del jugador 1
            print(f'Jugador 1: {mensajeRecibido1}')
        
        mensajeRecibido2 = conn2.recv(4096).decode() #recibe el mensaje del jugador 2
        print(f'Jugador 2: {mensajeRecibido2}')
        if mensajeRecibido2 == 'salir': #si el jugador 2 se desconecta
            print('Esperando segundo jugador')
            conn2, addr2 = s.accept() #establecemos la conexion
            print('Jugador 2 ¡CONECTADO!')
            print(f'Direccion: {addr2}')  
            conn2.send('J2'.encode())#envía un mensaje fijo#
            mensajeRecibido2 = conn2.recv(4096).decode() #recibe el mensaje del jugador 2
            print(f'Jugador 2: {mensajeRecibido2}')
    
        if mensajeRecibido1 == mensajeRecibido2:    
            empate() #llamado a función empate()

        if mensajeRecibido1 == 'piedra' and mensajeRecibido2 == 'papel':    
            pierdeJugador1() #llamado a función pierdeJugador1()
        elif mensajeRecibido1 == 'piedra' and mensajeRecibido2 == 'tijera':
            ganasteJugador1() #llamado a función ganasteJugador1()
            
        if mensajeRecibido1 == 'papel' and mensajeRecibido2== 'tijera':
            pierdeJugador1() #llamado a función pierdeJugador1()
        elif mensajeRecibido1 == 'papel' and mensajeRecibido2 == 'piedra':
            ganasteJugador1() #llamado a función ganasteJugador1()

        if mensajeRecibido1 == 'tijera' and mensajeRecibido2 == 'piedra':
            pierdeJugador1() #llamado a función pierdeJugador1()
        elif mensajeRecibido1 == 'tijera' and mensajeRecibido2 == 'papel': 
            ganasteJugador1() #llamado a función ganasteJugador1()
  
    # print(f'Desconectando al cliente 1: {addr}')
    # print(f'Desconectando al cliente 2: {addr2}')

conn.close()
conn2.close
