import sys 
from form import *
from ppt import pipati as ppt
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QImageReader
import json
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
    ganadoC=0
    empateC=0
    perdidoC=0
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
        dato = self.s.recv(4096).decode()#Se recibe si eres J1(jugador 1) o J2(jugador 2)
        mensajeR=json.loads(dato)
        self.jugador=mensajeR[0]
        
        self.ganadoC=mensajeR[1]
        RgGan=str(self.ganadoC)
        self.empateC=mensajeR[2]
        RgEmp=str(self.empateC)
        self.perdidoC=mensajeR[3]
        RgPer=str(self.perdidoC)
        #Se establecen las señales de los botones y combobox
        self.ui.btnJugar.clicked.connect(self.BtonJugar)#Se conecta el boton de la interfaz con lo que hara
        #Dependiendo si se es J1 o J2 se bloquea la comboBox contraria
        if self.jugador=='J1':
            self.ui.seleccion1.activated.connect(self.MostrarImagenUser)#Se hace la conexion, si eliges tijera, te muestra la imagen
            self.ui.imgnUser2.setVisible(False)#Se bloquea la imagen del oponente
            self.ui.seleccion2.setVisible(False)#Se bloquea la comboBox del J2

            self.ui.RGganado2.setText(RgGan)
            self.ui.RGempate2.setText(RgEmp)
            self.ui.RGperdido2.setText(RgPer)
        if self.jugador=='J2':
            self.ui.seleccion2.activated.connect(self.MostrarImagenUser)
            self.ui.imgnUser1.setVisible(False)
            self.ui.seleccion1.setVisible(False)

            self.ui.RGganado.setText(RgGan)
            self.ui.RGempate.setText(RgEmp)
            self.ui.RGperdido.setText(RgPer)
        self.ui.btnSalir.clicked.connect(self.BtonSalir)#se establece la accion para el boton salir
        self.ui.btnJugar.setDisabled(True)#Al empezar, se tendrá bloqueada la opcion de jugar hasta que se seleccione algo
        #Visibilidad
        self.ui.btnContinuar.setVisible(False)#Se hace invisible el boton continuar de inicio, pues solo aparecerá cuando un jugador salga
        self.ui.btnContinuar.setDisabled(True)
   #Acciones Botones
    def BtonJugar(self):#La accion que hará el boton jugar cuando se presione
        print("listo para jugar")
        dato=[self.sel,self.ganadoG,self.empateG,self.perdidoG]
        dato1=json.dumps(dato)
        self.s.send(dato1.encode())
        mensajeR = self.s.recv(4096).decode()
        dato=json.loads(mensajeR)
        self.respuesta=dato[0]
        self.ui.msjJuego.setText(self.respuesta)
        if self.respuesta == 'Perdiste':
            self.perdidoA+=1
            self.perdidoG+=1
            self.ganadoC+=1
            gc=str(self.ganadoC)
            pa=str(self.perdidoA)
            pg=str(self.perdidoG)
            if self.jugador == 'J1':
                self.ui.RAperdido.setText(pa)
                self.ui.RGperdido.setText(pg)
                self.ui.RAganado2.setText(pa)
                self.ui.RGganado2.setText(gc)
            elif self.jugador == 'J2':
                self.ui.RAganado.setText(pa)
                self.ui.RGganado.setText(gc)
                self.ui.RAperdido2.setText(pa)
                self.ui.RGperdido2.setText(pg)
        elif self.respuesta == 'Ganaste':
            self.ganadoA+=1
            self.ganadoG+=1
            self.perdidoC+=1
            pc=str(self.perdidoC)
            ga=str(self.ganadoA)
            gg=str(self.ganadoG)
            if self.jugador == 'J1':
                self.ui.RAganado.setText(ga)
                self.ui.RGganado.setText(gg)
                self.ui.RAperdido2.setText(ga)
                self.ui.RGperdido2.setText(pc)
            elif self.jugador == 'J2':
                self.ui.RAperdido.setText(ga)
                self.ui.RGperdido.setText(pc)
                self.ui.RAganado2.setText(ga)
                self.ui.RGganado2.setText(gg)
        elif self.respuesta == 'Empate':
            self.empateA+=1
            self.empateG+=1
            self.empateC+=1
            ec=str(self.empateC)
            ea=str(self.empateA)
            eg=str(self.empateG)
            if self.jugador == 'J1':
                self.ui.RAempate.setText(ea)
                self.ui.RGempate.setText(eg)
                self.ui.RAempate2.setText(ea)
                self.ui.RGempate2.setText(ec)
            elif self.jugador == 'J2':
                self.ui.RAempate.setText(ea)
                self.ui.RGempate.setText(ec)
                self.ui.RAempate2.setText(ea)
                self.ui.RGempate2.setText(eg)

    def BtonSalir(self):#Lo que hará el boton salir cuando se presione
        print('Saliendo')
        dato=['salir',self.ganadoG,self.empateG,self.perdidoG]
        dato1=json.dumps(dato)
        self.s.send(dato1.encode())
        self.s.close()
        sys.exit()
    #Seleccion de imagen dependiendo de seleccion de usuario del combo box

    def MostrarImagenUser(self):
        if self.jugador=='J1':
            self.sel=self.ui.seleccion1.currentText()#se lee la seleccion
        elif self.jugador=='J2':
            self.sel=self.ui.seleccion2.currentText()

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
        if self.jugador=='J1':
            self.ui.imgnUser1.setPixmap(QPixmap.fromImage(imgn))#se establece la imagen dependiendo de la seleccion
            self.ui.imgnUser1.setVisible(True)#Se hace visible la imagen


            self.ui.btnJugar.setEnabled(True)#Una vez seleccionado algo, el botn jugar se habilita
            self.ui.msjJuego.clear()
        elif self.jugador=='J2':

            self.ui.imgnUser2.setPixmap(QPixmap.fromImage(imgn))
            self.ui.imgnUser2.setVisible(True)

            self.ui.btnJugar.setEnabled(True)
            self.ui.msjJuego.clear()

if __name__ == '__main__':

    app=QApplication()
    juego_ppt=PPTInterfaz()
    juego_ppt.show()
    sys.exit(app.exec_())