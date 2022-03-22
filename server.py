from socket import AF_INET, SOCK_STREAM, socket
import json
s = socket()
host = 'localhost'
port = 9999

s.bind((host, port))
print('Esperando conexion')
s.listen(2)
datos1=['J1',0,0,0]
datos2=['J2',0,0,0]
while True:
    conn, addr = s.accept() #establecemos la conexion
    print('Jugador 1 ¡CONECTADO!')
    print(f'Direccion: {addr}')
    datoenv=json.dumps(datos1)
    conn.send(datoenv.encode())#envía un mensaje fijo#
    print('Esperando segundo jugador')
    conn2, addr2 = s.accept() #establecemos la conexion
    print('Jugador 2 ¡CONECTADO!')
    print(f'Direccion: {addr2}')
    datoenv2=json.dumps(datos2)
    conn2.send(datoenv2.encode())#envía un mensaje fijo
    
    while True:
        datorecv1 = conn.recv(4096).decode() #recibe el mensaje del jugador 1
        datos2=json.loads(datorecv1)
        mensajeRecibido1=datos2[0]
        print(f'Jugador 1: {mensajeRecibido1}')
        if mensajeRecibido1 == 'salir': #si el jugador 1 se desconecta
            conn.close()
            print('Esperando primer jugador')
            conn, addr = s.accept() #establecemos la conexion
            print('Jugador 1 ¡CONECTADO!')
            print(f'Direccion: {addr}') 
            datos1[0]='J1' 
            datoenv=json.dumps(datos1)
            conn.send(datoenv.encode())#envía un mensaje fijo#
            datorecv1 = conn.recv(4096).decode() #recibe el mensaje del jugador 1
            datos2=json.loads(datorecv1)
            mensajeRecibido1=datos2[0]
            print(f'Jugador 1: {mensajeRecibido1}')
        datorecv2 = conn2.recv(4096).decode() #recibe el mensaje del jugador 2
        datos1=json.loads(datorecv2)
        mensajeRecibido2=datos1[0]
        print(f'Jugador 2: {mensajeRecibido2}')
        if mensajeRecibido2 == 'salir': #si el jugador 2 se desconecta
            conn2.close()
            print('Esperando segundo jugador')
            conn2, addr2 = s.accept() #establecemos la conexion
            print('Jugador 2 ¡CONECTADO!')
            print(f'Direccion: {addr2}')
            datos2[0]='J2'  
            datoenv2=json.dumps(datos2)
            conn2.send(datoenv2.encode())#envía un mensaje fijo#
            datorecv2 = conn2.recv(4096).decode() #recibe el mensaje del jugador 2
            datos1=json.loads(datorecv2)
            mensajeRecibido2=datos1[0] #recibe el mensaje del jugador 2
            print(f'Jugador 2: {mensajeRecibido2}')
    
        if mensajeRecibido1 == mensajeRecibido2:
            datos1[0]='Empate'
            datoenv=json.dumps(datos1)
            datos2[0]='Empate'
            datoenv2=json.dumps(datos2)
            conn.send(datoenv.encode()) #se envía mensaje al jugador 1
            conn2.send(datoenv2.encode()) #se envía mensaje al jugador 2

        if mensajeRecibido1 == 'Piedra' and mensajeRecibido2 == 'Papel':  
            datos1[0]='Perdiste'
            datoenv=json.dumps(datos1)
            datos2[0]='Ganaste'
            datoenv2=json.dumps(datos2)
            conn.send(datoenv.encode()) #se envía mensaje al jugador 1
            conn2.send(datoenv2.encode()) #se envía mensaje al jugador 2  
            
        elif mensajeRecibido1 == 'Piedra' and mensajeRecibido2 == 'Tijera':
            datos1[0]='Ganaste'
            datoenv=json.dumps(datos1)
            datos2[0]='Perdiste'
            datoenv2=json.dumps(datos2)
            conn.send(datoenv.encode()) #se envía mensaje al jugador 1
            conn2.send(datoenv2.encode()) #se envía mensaje al jugador 2

        if mensajeRecibido1 == 'Papel' and mensajeRecibido2== 'Tijera':
            datos1[0]='Perdiste'
            datoenv=json.dumps(datos1)
            datos2[0]='Ganaste'
            datoenv2=json.dumps(datos2)
            conn.send(datoenv.encode()) #se envía mensaje al jugador 1
            conn2.send(datoenv2.encode()) #se envía mensaje al jugador 2  

        elif mensajeRecibido1 == 'Papel' and mensajeRecibido2 == 'Piedra':
            datos1[0]='Ganaste'
            datoenv=json.dumps(datos1)
            datos2[0]='Perdiste'
            datoenv2=json.dumps(datos2)
            conn.send(datoenv.encode()) #se envía mensaje al jugador 1
            conn2.send(datoenv2.encode()) #se envía mensaje al jugador 2

        if mensajeRecibido1 == 'Tijera' and mensajeRecibido2 == 'Piedra':
            datos1[0]='Perdiste'
            datoenv=json.dumps(datos1)
            datos2[0]='Ganaste'
            datoenv2=json.dumps(datos2)
            conn.send(datoenv.encode()) #se envía mensaje al jugador 1
            conn2.send(datoenv2.encode()) #se envía mensaje al jugador 2  

        elif mensajeRecibido1 == 'Tijera' and mensajeRecibido2 == 'Papel': 
            datos1[0]='Ganaste'
            datoenv=json.dumps(datos1)
            datos2[0]='Perdiste'
            datoenv2=json.dumps(datos2)
            conn.send(datoenv.encode()) #se envía mensaje al jugador 1
            conn2.send(datoenv2.encode()) #se envía mensaje al jugador 2
  
    # print(f'Desconectando al cliente 1: {addr}')
    # print(f'Desconectando al cliente 2: {addr2}')