
import socket
import sys

s = socket.socket()

server_host = 'localhost'
server_port = 9999

s.connect((server_host, server_port))

respuesta = s.recv(4096).decode()
print(f'{respuesta}')

# print('Elija su opcion: [piedra, papel o tijera]')
while True:
    mensaje = input()
    if mensaje != 'adios': 
        s.send(mensaje.encode())
        respuesta = s.recv(4096).decode()
        print(f'SERVIDOR: {respuesta}')
    else: #si el mensaje es adios, lo envía al servidor y termina la conexion
        s.send(mensaje.encode())
        s.close()
        sys.exit()