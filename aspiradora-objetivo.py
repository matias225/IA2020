#!/usr/bin/python3
import random

# Estado de las baldosas
limpio = ' '
sucio = 'x'
poco = '+'
permanente = '#'
pared = '?'
pasillo = []
suciedad = [limpio, sucio, poco, permanente]

# Creando el pasillo aleatoriamente
tamanio_piso = random.randrange(1, 16)
# Pared del principio
pasillo.append(pared)
for i in range(0, tamanio_piso):
    pasillo.append(random.choice(suciedad))
# Pared del final
pasillo.append(pared)


class Aspiradora:
    posicion = random.randrange(1, len(pasillo)-1)
    direccion = ''
    giros = 0
    movimientos = 0
    condicion_piso = [0] * len(pasillo)


    def update_condicion_piso(self):
        self.condicion_piso[self.posicion] = self.condicion_piso[self.posicion] + 1


    def avanzar(self):
        self.movimientos += 1
        if self.direccion == 'izquierda':
            self.posicion -= 1
        elif self.direccion == 'derecha':
            self.posicion += 1
        print('Avance \n')


    def girar_izquierda(self):
        self.movimientos += 1
        self.giros += 1
        self.direccion = 'izquierda'
        print('Gire a la izquierda \n')


    def girar_derecha(self):
        self.movimientos += 1
        self.giros += 1
        self.direccion = 'derecha'
        print('Gire a la derecha \n')


    def limpiar(self):
        self.movimientos += 1
        if pasillo[aspiradora.posicion] == poco:
            pasillo[aspiradora.posicion] = limpio
        elif pasillo[aspiradora.posicion] == sucio:
            pasillo[aspiradora.posicion] = poco
        print('Limpie \n')


    def revisar_suciedad(self):
        self.movimientos += 1
        print('Limpie \n')


    def mostrar_aspiradora(self):
        cadena=''
        for i in range(0, len(pasillo)):
            if i == self.posicion:
                cadena = cadena + '|A|'
            else:
                cadena = cadena + '| |'
        print(cadena+'\n')


def mostrar_piso():
    cadena = ''
    for i in range(0, len(pasillo)):
        cadena = cadena + '|' + pasillo[i] + '|'
    print(cadena)


if __name__ == '__main__':
    aspiradora = Aspiradora()
    # Mitad del pasillo
    mitad = len(pasillo)/2
    if not mitad.is_integer():
        mitad = mitad + 0.5
    # La aspiradora decide en que dirección avanzar inicialmente
    if aspiradora.posicion >= mitad:
        aspiradora.direccion = 'derecha'
    else:
        aspiradora.direccion = 'izquierda' 
    print("Aspiradora comienza con dirección:", aspiradora.direccion)
    print("Posición inicial: ")
    mostrar_piso()
    aspiradora.mostrar_aspiradora()
    while aspiradora.giros < 2:
        if pasillo[aspiradora.posicion] == pared:
            if aspiradora.direccion == 'derecha':
                aspiradora.girar_izquierda()
                aspiradora.avanzar()
            elif aspiradora.direccion == 'izquierda':
                aspiradora.girar_derecha()
                aspiradora.avanzar()
        aspiradora.update_condicion_piso()
        for i in range(0, 2):
            if pasillo[aspiradora.posicion] != limpio:
                aspiradora.limpiar()
        mostrar_piso()
        aspiradora.mostrar_aspiradora()
        if aspiradora.giros == 2:
            print("Ya recorri todo el piso. Apagando...")
            print('Cantidad de movimientos totales:', aspiradora.movimientos)   
            break
        aspiradora.avanzar()
    