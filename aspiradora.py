import random

# Estado de las baldosas

limpio = ' '
sucio = 'x'
poco = '+'
permanente = '#'
pared = '?'
piso = [pared, limpio, sucio, poco, permanente, limpio, limpio, pared]


class Aspiradora:
    posicion = random.randrange(len(piso))
    direccion = 'derecha'
    movimientos = 0


    def avanzar(self):
        self.movimientos += 1
        if self.direccion == 'izquierda':
            self.posicion -= 1
        elif self.direccion == 'derecha':
            self.posicion += 1
        print('Avance \n')


    def girar_izquierda(self):
        self.movimientos += 1
        self.direccion = 'izquierda'
        print('Gire a la izquierda \n')


    def girar_derecha(self):
        self.movimientos += 1
        self.direccion = 'derecha'
        print('Gire a la derecha \n')


    def limpiar(self):
        self.movimientos += 1
        print('Limpie \n')


    def revisar_suciedad(self):
        self.movimientos += 1
        print('Limpie \n')


    def mostrar_aspiradora(self):
        cadena=''
        for i in range(0,len(piso)):
            if i == self.posicion:
                cadena = cadena + '|A|'
            else:
                cadena = cadena + '| |'
        print(cadena)


def mostrar_piso():
    cadena = ''
    for i in range(0, len(piso)):
        cadena = cadena + '|' + piso[i] + '|'
    print(cadena)


if __name__ == '__main__':
    clean = False
    aspiradora = Aspiradora()
    for i in range(0, 100):
        if piso[aspiradora.posicion] == pared:
            if aspiradora.direccion == 'derecha':
                aspiradora.girar_izquierda()
                aspiradora.avanzar()
            elif aspiradora.direccion == 'izquierda':
                aspiradora.girar_derecha()
                aspiradora.avanzar()
        if piso[aspiradora.posicion] == poco:
            aspiradora.limpiar()
            piso[aspiradora.posicion] = limpio
        elif piso[aspiradora.posicion] == sucio:
            aspiradora.limpiar()
            piso[aspiradora.posicion] = poco
        elif piso[aspiradora.posicion] == permanente:
            aspiradora.limpiar()
        mostrar_piso()
        aspiradora.mostrar_aspiradora()
        aspiradora.avanzar()
