import sys 
from form import *
from ppt import pipati as ppt
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QImageReader

import socket
import sys

class PPTInterfaz(QMainWindow):
    respuesta=None
    jugador=None
    sel=None
    ganadoA=0
    perdidoA=0
    empateA=0
    ganadoG=0
    empateG=0
    perdidoG=0
    s = socket.socket()#Se inicia los puertos para la conexion como cliente
    server_host = 'localhost'
    server_port = 9999
    def __init__(self):
        super(PPTInterfaz,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ppt=ppt()#se inicializa la interfaz
        print("INICIANDO")
        self.s.connect((self.server_host, self.server_port))#se inicia la conexion con el server
        self.jugador = self.s.recv(4096).decode()#Se recibe si eres J1(jugador 1) o J2(jugador 2)
        
        #Se establecen las señales de los botones y combobox
        self.ui.btnJugar.clicked.connect(self.BtonJugar)#Se conecta el boton de la interfaz con lo que hara
        #Dependiendo si se es J1 o J2 se bloquea la comboBox contraria
        if self.jugador=='J1':
            self.ui.seleccion1.activated.connect(self.MostrarImagenUser)#Se hace la conexion, si eliges tijera, te muestra la imagen
            self.ui.imgnUser2.setVisible(False)#Se bloquea la imagen del oponente
            self.ui.seleccion2.setVisible(False)#Se bloquea la comboBox del J2
        if self.jugador=='J2':
            self.ui.seleccion2.activated.connect(self.MostrarImagenUser)
            self.ui.imgnUser1.setVisible(False)
            self.ui.seleccion1.setVisible(False)
        
        self.ui.btnSalir.clicked.connect(self.BtonSalir)#se establece la accion para el boton salir
        self.ui.btnJugar.setDisabled(True)#Al empezar, se tendrá bloqueada la opcion de jugar hasta que se seleccione algo
        #Visibilidad
        self.ui.btnContinuar.setVisible(False)#Se hace invisible el boton continuar de inicio, pues solo aparecerá cuando un jugador salga
        self.ui.btnContinuar.setDisabled(True)
   #Acciones Botones
    def BtonJugar(self):#La accion que hará el boton jugar cuando se presione
        print("listo para jugar")
        self.s.send(self.sel.encode())
        self.respuesta = self.s.recv(4096).decode()
        self.ui.msjJuego.setText(self.respuesta)
    def BtonSalir(self):#Lo que hará el boton salir cuando se presione
        print('Saliendo')
        self.s.send('Saliendo'.encode())
        self.s.close()
        sys.exit()
    #Seleccion de imagen dependiendo de seleccion de usuario del combo box

    def MostrarImagenUser(self):
        if self.jugador=='J1':
            self.sel=self.ui.seleccion1.currentText()#se lee la seleccion

            if self.sel=='Piedra':#dependiendo de la seleccion se mostrará la imgen correspondiente
                reader=QImageReader('.\Recursos\Piedra.png')
            elif self.sel=='Tijera':
                reader=QImageReader('.\Recursos\Tijera.png')
            elif self.sel=='Papel':
                reader=QImageReader('.\Recursos\Papel.png')
            else:
                self.ui.imgnUser1.setVisible(False)#de no moverse, la imagen se queda invisible
                return
        
            reader.setAutoTransform(True)
            imgn=reader.read()

            self.ui.imgnUser1.setPixmap(QPixmap.fromImage(imgn))#se establece la imagen dependiendo de la seleccion
            self.ui.imgnUser1.setVisible(True)#Se hace visible la imagen


            self.ui.btnJugar.setEnabled(True)#Una vez seleccionado algo, el botn jugar se habilita
            self.ui.msjJuego.clear()
            return self.sel
        elif self.jugador=='J2':
            self.sel=self.ui.seleccion2.currentText()

            if self.sel=='Piedra':
                reader=QImageReader('.\Recursos\Piedra.png')
            elif self.sel=='Tijera':
                reader=QImageReader('.\Recursos\Tijera.png')
            elif self.sel=='Papel':
                reader=QImageReader('.\Recursos\Papel.png')
            else:
                self.ui.imgnUser2.setVisible(False)
                return
        
            reader.setAutoTransform(True)
            imgn=reader.read()

            self.ui.imgnUser2.setPixmap(QPixmap.fromImage(imgn))
            self.ui.imgnUser2.setVisible(True)

            self.ui.btnJugar.setEnabled(True)
            self.ui.msjJuego.clear()
        
            return self.sel
        else:
            return self.sel

if __name__ == '__main__':

    # s = socket.socket()

    # server_host = 'localhost'
    # server_port = 9999

    # s.connect((server_host, server_port))
    # respuesta = s.recv(4096).decode()
    app=QApplication()
    juego_ppt=PPTInterfaz()
    juego_ppt.show()
    sys.exit(app.exec_())