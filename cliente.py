import socket
import sys

s = socket.socket()

server_host = 'localhost'
server_port = 9999

s.connect((server_host, server_port))

respuesta = s.recv(4096).decode()
print(f'{respuesta}') #recibe si es jugador 1 o 2

# print('Elija su opcion: [piedra, papel o tijera]')
while True:
    mensaje = input() #espera a que el jugador elija su opcion
    if mensaje != 'salir': 
        s.send(mensaje.encode()) #envia la opcion al servidor
        respuesta = s.recv(4096).decode() #espera la respuesta del servidor
        print(f'SERVIDOR: {respuesta}') #el servidor responde si ganó o perdió la partida
    else: #si el mensaje es adios, lo envía al servidor y termina la conexion
        s.send(mensaje.encode())
        s.close()
        sys.exit()
    
