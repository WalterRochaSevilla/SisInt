from corner_piece import Arista, Centro, Esquina


class CuboRubik:
    def __init__(self):
        self.piezas = self.crear_piezas()

    def crear_piezas(self):
        piezas = []

        # Centros
        colores_centros = ['amarillo', 'rojo', 'verde', 'naranja', 'azul', 'blanco']
        for color in colores_centros:
            piezas.append(Centro(color))

        # Esquinas
        combinaciones_esquinas = [
            ('amarillo', 'rojo', 'azul'), ('amarillo', 'verde', 'rojo'),
            ('amarillo', 'naranja', 'azul'), ('amarillo', 'verde', 'naranja'),
            ('blanco', 'rojo', 'azul'), ('blanco', 'rojo', 'verde'),
            ('blanco', 'azul', 'naranja'), ('blanco', 'verde', 'naranja')
            
        ]
        for colores in combinaciones_esquinas:
            piezas.append(Esquina(colores))

        # Aristas
        combinaciones_aristas = [
            ('amarillo', 'rojo'), ('amarillo', 'naranja'), 
            ('amarillo', 'azul'), ('amarillo', 'verde'),
            ('blanco', 'rojo'), ('blanco', 'naranja'),
            ('blanco', 'azul'), ('blanco', 'verde'),
            ('rojo', 'verde'),('rojo', 'azul'),
            ('naranja','verde'),('naranja', 'azul')
        ]
        for colores in combinaciones_aristas:
            piezas.append(Arista(colores))

        return piezas