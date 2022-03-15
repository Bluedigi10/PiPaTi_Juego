from socket import AF_INET, SOCK_STREAM, socket

s = socket()
host = 'localhost'
port = 9999

s.bind((host, port))
print('Esperando conexion')
s.listen(2)


while True:
    conn, addr = s.accept() #establecemos la conexion
    print('Jugador 1 ¡CONECTADO!')
    print(f'Direccion: {addr}')
    conn.send('J1'.encode())#envía un mensaje fijo#envía un mensaje fijo
    print('Esperano segundo jugador')
    conn2, addr2 = s.accept() #establecemos la conexion
    print('Jugador 2 ¡CONECTADO!')
    print(f'Direccion: {addr2}')
    conn2.send('J2'.encode())#envía un mensaje fijo
    
    while True:
        
        mensajeRecibido1 = conn.recv(4096).decode() #recibe el mensaje del jugador 1
        print(f'Jugador 1: {mensajeRecibido1}')        
        mensajeRecibido2 = conn2.recv(4096).decode() #recibe el mensaje del Jugador 2
        print(f'Jugador 2: {mensajeRecibido2}')

        if mensajeRecibido1 == mensajeRecibido2:    
            conn.send('Empate'.encode()) #se envía mensaje al jugador 1
            conn2.send('Empate'.encode()) #se envía mensaje al jugador 2

        if mensajeRecibido1 == 'Piedra' and mensajeRecibido2 == 'Papel':    
            conn.send('Perdiste'.encode()) #se envía mensaje al jugador 1
            conn2.send('Ganaste'.encode()) #se envía mensaje al jugador 2
        elif mensajeRecibido1 == 'Piedra' and mensajeRecibido2 == 'Tijera':
            conn.send('Ganaste'.encode()) #se envía mensaje al jugador 1
            conn2.send('Perdiste'.encode()) #se envía mensaje al jugador 2
    
        if mensajeRecibido1 == 'Papel' and mensajeRecibido2== 'Tijera':
            conn.send('Perdiste'.encode()) #se envía mensaje al jugador 1
            conn2.send('Ganaste'.encode()) #se envía mensaje al jugador 2
        elif mensajeRecibido1 == 'Papel' and mensajeRecibido2 == 'Piedra':
            conn.send('Ganaste'.encode()) #se envía mensaje al jugador 1
            conn2.send('Perdiste'.encode()) #se envía mensaje al jugador 2

        if mensajeRecibido1 == 'Tijera' and mensajeRecibido2 == 'Piedra':
            conn.send('Perdiste'.encode()) #se envía mensaje al jugador 1
            conn2.send('Ganaste'.encode()) #se envía mensaje al jugador 2
        elif mensajeRecibido1 == 'Tijera' and mensajeRecibido2 == 'Papel': 
            conn.send('Ganaste'.encode()) #se envía mensaje al jugador 1
            conn2.send('Perdiste'.encode()) #se envía mensaje al jugador 2
    
    #     continuar = input("¿Quiere seguir jugando? (s/n): ")
    #     if continuar=="n":
    #         break

    # print("Vuelva pronto")
            

        # if mensajeRecibido1 == 'adios': #si el mensaje es un adios, le envia un mensaje de hasta pronto jugador al cliente 1
        #     print('Hasta pronto Jugador 1')
        #     break
        # conn.send(input().encode()) #envía al cliente el mensaje ingresado por teclado
        
        # if mensajeRecibido2 == 'adios':
        #     print('Hasta pronto Jugador 2')
        #     break
        # conn2.send(input().encode()) #envía al cliente el mensaje ingresado por teclado
    
    # print(f'Desconectando al cliente 1: {addr}')
    # print(f'Desconectando al cliente 2: {addr2}')

    conn.close()
    conn2.close