from Cara import Cara
from corner_piece import Arista, Centro, Esquina

class CuboRubik:
    def __init__(self):
        self.caras = self.inicializar_caras()
        self.piezas_registradas = {'Centro': {}, 'Arista': {}, 'Esquina': {}}
        self.inicializar_piezas_legales()

    def inicializar_caras(self):
        # Inicializar la lista de listas para representar las caras del cubo
        caras = []
        for _ in range(6):
            caras.append([None] * 9)  # Cada cara tiene 9 piezas inicialmente vacías
        return caras

    def inicializar_piezas_legales(self):
        # Inicializar las combinaciones legales de piezas
        self.colores_centros = {'amarillo', 'rojo', 'verde', 'naranja', 'azul', 'blanco'}
        self.combinaciones_aristas = {('amarillo', 'rojo'), ('amarillo', 'naranja'), ('amarillo', 'azul'),
                                       ('amarillo', 'verde'), ('blanco', 'rojo'), ('blanco', 'naranja'),
                                       ('blanco', 'azul'), ('blanco', 'verde'), ('rojo', 'verde'), ('rojo', 'azul'),
                                       ('naranja', 'verde'), ('naranja', 'azul')}
        self.combinaciones_esquinas = {('amarillo', 'rojo', 'azul'), ('amarillo', 'verde', 'rojo'),
                                        ('amarillo', 'naranja', 'azul'), ('amarillo', 'verde', 'naranja'),
                                        ('blanco', 'rojo', 'azul'), ('blanco', 'rojo', 'verde'),
                                        ('blanco', 'azul', 'naranja'), ('blanco', 'verde', 'naranja')}
        # Marcar las combinaciones legales como presentes en los diccionarios
        for color in self.colores_centros:
            self.piezas_registradas['Centro'][color] = 0
        for combinacion in self.combinaciones_aristas:
            self.piezas_registradas['Arista'][combinacion] = 0
        for combinacion in self.combinaciones_esquinas:
            self.piezas_registradas['Esquina'][combinacion] = 0

    def crear_pieza(self, tipo, colores):
        if tipo not in {'Centro', 'Arista', 'Esquina'}:
            raise ValueError("Tipo de pieza no válido")

        # Verificar si la combinación de colores es legal
        if tipo == 'Centro':
            if colores not in self.colores_centros:
                raise ValueError("Combinación de colores de centro no válida")
            diccionario = self.piezas_registradas['Centro']
        elif tipo == 'Arista':
            if tuple(sorted(colores)) not in self.combinaciones_aristas:
                raise ValueError("Combinación de colores de arista no válida")
            diccionario = self.piezas_registradas['Arista']
        elif tipo == 'Esquina':
            if tuple(sorted(colores)) not in self.combinaciones_esquinas:
                raise ValueError("Combinación de colores de esquina no válida")
            diccionario = self.piezas_registradas['Esquina']

        # Verificar si la pieza ya existe
        if diccionario[colores] > 0:
            raise ValueError("Ya existe una pieza con esta combinación de colores")

        # Marcar la pieza como presente en el diccionario
        diccionario[colores] += 1

        # Crear la pieza y devolverla
        if tipo == 'Centro':
            return Centro(colores)
        elif tipo == 'Arista':
            return Arista(colores)
        elif tipo == 'Esquina':
            return Esquina(colores)

    def obtener_pieza(self, numero_cara, numero_pieza):
        # Obtener la pieza en la posición (numero_cara, numero_pieza)
        return self.caras[numero_cara][numero_pieza]

    def asignar_pieza(self, numero_cara, numero_pieza, pieza):
        # Asignar una pieza en la posición (numero_cara, numero_pieza)
        self.caras[numero_cara][numero_pieza] = pieza

    def girar_cara(self, numero_cara, sentido_horario=True):
        # Girar una cara en sentido horario o antihorario
        if sentido_horario:
            self.caras[numero_cara].girar_sentido_horario()
        else:
            self.caras[numero_cara].girar_sentido_antihorario()

    def actualizar_caras_derecha(self):
        # Actualizar estados de las caras adyacentes a la cara azul después de un movimiento R
        estado_derecha = [fila[-1] for fila in self.caras[2].obtener_estado()]
        estado_abajo = [fila[::-1] for fila in self.caras[6].obtener_estado()]
        estado_izquierda = [fila[0] for fila in self.caras[5].obtener_estado()]
        estado_arriba = [fila[::-1] for fila in self.caras[1].obtener_estado()]

        self.caras[2].actualizar_estado(
            list(zip(*self.caras[2].obtener_estado()[:2], estado_arriba)))
        self.caras[6].actualizar_estado(
            list(zip(*self.caras[6].obtener_estado()[:2], estado_derecha)))
        self.caras[5].actualizar_estado(
            list(zip(estado_abajo, *self.caras[5].obtener_estado()[1:])))
        self.caras[1].actualizar_estado(
            list(zip(estado_izquierda, *self.caras[1].obtener_estado()[1:])))

    def actualizar_caras_izquierda(self):
        # Actualizar estados de las caras adyacentes a la cara azul después de un movimiento L
        estado_derecha = [fila[-1] for fila in self.caras[2].obtener_estado()]
        estado_abajo = [fila[::-1] for fila in self.caras[6].obtener_estado()]
        estado_izquierda = [fila[0] for fila in self.caras[5].obtener_estado()]
        estado_arriba = [fila[::-1] for fila in self.caras[1].obtener_estado()]

        self.caras[2].actualizar_estado(
            list(zip(estado_arriba, *self.caras[2].obtener_estado()[1:])))
        self.caras[6].actualizar_estado(
            list(zip(estado_derecha, *self.caras[6].obtener_estado()[1:])))
        self.caras[5].actualizar_estado(
            list(zip(*self.caras[5].obtener_estado()[:2], estado_abajo)))
        self.caras[1].actualizar_estado(
            list(zip(*self.caras[1].obtener_estado()[:2], estado_izquierda)))

    def R(self):
        # Movimiento R (sentido horario)
        self.girar_cara(3)
        self.actualizar_caras_derecha()

    def R_prime(self):
        # Movimiento R' (sentido antihorario)
        self.R()
        self.R()
        self.R()

    def L(self):
        # Movimiento L (sentido horario)
        self.girar_cara(3, sentido_horario=False)
        self.actualizar_caras_izquierda()

    def L_prime(self):
        # Movimiento L' (sentido antihorario)
        self.L()
        self.L()
        self.L()

    def U(self):
        # Movimiento U (sentido horario)
        self.R_prime()
        self.girar_cara(4)

    def U_prime(self):
        # Movimiento U' (sentido antihorario)
        self.R()
        self.girar_cara(4, sentido_horario=False)

    def D(self):
        # Movimiento D (sentido horario)
        self.L_prime()
        self.girar_cara(5)

    def D_prime(self):
        # Movimiento D' (sentido antihorario)
        self.L()
        self.girar_cara(5, sentido_horario=False)

    def F(self):
        # Movimiento F (sentido horario)
        self.U()
        self.R()
        self.D_prime()

    def F_prime(self):
        # Movimiento F' (sentido antihorario)
        self.U_prime()
        self.R_prime()
        self.D()

    def B(self):
        # Movimiento B (sentido horario)
        self.U_prime()
        self.L_prime()
        self.D()

    def B_prime(self):
        # Movimiento B' (sentido antihorario)
        self.U()
        self.L()
        self.D_prime()

    def mover(self, movimiento):
        # Ejecutar un movimiento del cubo
        if movimiento == 'R':
            self.R()
        elif movimiento == 'R\'':
            self.R_prime()
        elif movimiento == 'L':
            self.L()
        elif movimiento == 'L\'':
            self.L_prime()
        elif movimiento == 'U':
            self.U()
        elif movimiento == 'U\'':
            self.U_prime()
        elif movimiento == 'D':
            self.D()
        elif movimiento == 'D\'':
            self.D_prime()
        elif movimiento == 'F':
            self.F()
        elif movimiento == 'F\'':
            self.F_prime()
        elif movimiento == 'B':
            self.B()
        elif movimiento == 'B\'':
            self.B_prime()

        # Actualizar caras después del movimiento
        if movimiento in {'R', 'R\'', 'L', 'L\''}:
            self.actualizar_caras_derecha()
        elif movimiento in {'U', 'U\'', 'D', 'D\''}:
            self.actualizar_caras_izquierda()

    def resolver(self, secuencia):
        # Resolver el cubo dado una secuencia de movimientos
        for movimiento in secuencia:
            self.mover(movimiento)