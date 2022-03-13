class pipati:
    def __init__(self):
        self.user1=None
        self.user2=None
    
    def SetSeleccionUser1(self,seleccion):
        self.user1=seleccion
    def SetSeleccionUser2(self,seleccion):
        self.user2=seleccion
   
    def juego(self):
        msj=None

        if not self.user1 and not self.user2:
            return 'esperando'
        if self.user1 != self.user2:
            if self.user1 == 'piedra':
                if self.user2 == 'papel':
                    msj = 'Perdiste!'
                else:
                    msj = 'Ganaste!'

            elif self.user1 == 'papel':
                if self.user2 == 'tijera':
                    msj = 'Perdiste!'
                else:
                    msj = 'Ganaste!'

            elif self.user1 == 'tijera':
                if self.user2 == 'piedra':
                    msj = 'Perdiste!'
                else:
                    msj = 'Ganaste!'
        else:
            msj = 'Empate!'

        return msj