import sys 
from form import *
from ppt import pipati as ppt
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QImageReader

import time
import socket
import sys

class PPTInterfaz(QMainWindow):
    jugador1=None
    jugador2=None
    jugador=None
    sel=None
    seldef=None
    def __init__(self,jugador=None):
        super(PPTInterfaz,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ppt=ppt()
        self.jugador=jugador
        print("INICIANDO")
        #conexiones
        self.ui.btnJugar.clicked.connect(self.BtonJugar)
        
        if self.jugador=='J1':
            self.jugador1=self.jugador
            self.ui.seleccion1.activated.connect(self.MostrarImagenUser)
            self.ui.imgnUser2.setVisible(False)
            self.ui.seleccion2.setVisible(False)
        if self.jugador=='J2':
            self.jugador2=self.jugador
            self.ui.seleccion2.activated.connect(self.MostrarImagenUser)
            self.ui.imgnUser1.setVisible(False)
            self.ui.seleccion1.setVisible(False)
        
        self.ui.btnSalir.clicked.connect(self.BtonSalir)
        self.ui.btnJugar.setDisabled(True)
        #Visibilidad
        self.ui.btnContinuar.setVisible(False)
        self.ui.btnContinuar.setDisabled(True)
   #Acciones Botones
    def BtonJugar(self):
        print("listo para jugar")
        self.seldef=self.sel
        return True
    def BtonSalir(self):
        print("Saliendo")
        sys.exit()
    #Seleccion de imagen dependiendo de seleccion de usuario

    def MostrarImagenUser(self):
        if self.jugador=='J1':
            self.sel=self.ui.seleccion1.currentText()

            if self.sel=='Piedra':
                reader=QImageReader('.\Recursos\Piedra.png')
            elif self.sel=='Tijera':
                reader=QImageReader('.\Recursos\Tijera.png')
            elif self.sel=='Papel':
                reader=QImageReader('.\Recursos\Papel.png')
            else:
                self.ui.imgnUser1.setVisible(False)
                return
        
            reader.setAutoTransform(True)
            imgn=reader.read()

            self.ui.imgnUser1.setPixmap(QPixmap.fromImage(imgn))
            self.ui.imgnUser1.setVisible(True)


            self.ui.btnJugar.setEnabled(True)
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
    respuesta='J1'
    print(f'{respuesta}')
    app=QApplication()
    juego_ppt=PPTInterfaz(respuesta)
    juego_ppt.show()
    cont=1
    print(juego_ppt.seldef)
    sys.exit(app.exec_())