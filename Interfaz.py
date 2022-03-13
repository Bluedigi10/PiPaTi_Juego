import sys 
from form import *
from ppt import pipati as ppt
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QImageReader

class PPTInterfaz(QMainWindow):
    jugador=0
    def __init__(self,jugador=0):
        super(PPTInterfaz,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ppt=ppt()
        self.jugador=jugador
        print("INICIANDO")
        #conexiones
        self.ui.btnJugar.clicked.connect(self.BtonJugar)
        self.ui.seleccion1.activated.connect(self.MostrarImagenUser1)
        self.ui.seleccion2.activated.connect(self.MostrarImagenUser2)
        self.ui.btnSalir.clicked.connect(self.BtonSalir)
        self.ui.btnJugar.setDisabled(True)
        #Visibilidad
        self.ui.btnContinuar.setVisible(False)
        self.ui.btnContinuar.setDisabled(True)
   #Acciones Botones
    def BtonJugar(self):
        print("listo para jugar")
        return True
    def BtonSalir(self):
        print("Saliendo")
        sys.exit()
    #Seleccion de imagen dependiendo de seleccion de usuario
    def MostrarImagenUser1(self):
        self.ui.imgnUser2.setVisible(False)
        self.ui.seleccion2.setVisible(False)
        sel=self.ui.seleccion1.currentText()

        if sel=='Piedra':
            reader=QImageReader('.\Recursos\Piedra.png')
        elif sel=='Tijera':
            reader=QImageReader('.\Recursos\Tijera.png')
        elif sel=='Papel':
            reader=QImageReader('.\Recursos\Papel.png')
        else:
            self.ui.imgnUser1.setVisible(False)
            return
        
        reader.setAutoTransform(True)
        imgn=reader.read()

        self.ui.imgnUser1.setPixmap(QPixmap.fromImage(imgn))
        self.ui.imgnUser1.setVisible(True)

        self.ppt.SetSeleccionUser1(sel.lower())

        self.ui.btnJugar.setEnabled(True)
        self.ui.msjJuego.clear()
    
    def MostrarImagenUser2(self):
        self.ui.imgnUser1.setVisible(False)
        self.ui.seleccion1.setVisible(False)
        sel=self.ui.seleccion2.currentText()

        if sel=='Piedra':
            reader=QImageReader('.\Recursos\Piedra.png')
        elif sel=='Tijera':
            reader=QImageReader('.\Recursos\Tijera.png')
        elif sel=='Papel':
            reader=QImageReader('.\Recursos\Papel.png')
        else:
            self.ui.imgnUser2.setVisible(False)
            return
        
        reader.setAutoTransform(True)
        imgn=reader.read()

        self.ui.imgnUser2.setPixmap(QPixmap.fromImage(imgn))
        self.ui.imgnUser2.setVisible(True)

        self.ppt.SetSeleccionUser2(sel.lower())

        self.ui.btnJugar.setEnabled(True)
        self.ui.msjJuego.clear()

if __name__ == '__main__':

    app=QApplication()
    juego_ppt=PPTInterfaz(1)
    juego_ppt.show()
    sel=juego_ppt.ui.seleccion1.currentText()
    
    print(sel)
    sys.exit(app.exec_())