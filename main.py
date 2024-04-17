from corner_piece import Arista, Centro
from cubo import CuboRubik


def validar_cubo(piezas):
    # Verificar que no haya 2 centros del mismo color
    centros = [pieza for pieza in piezas if isinstance(pieza, Centro)]
    colores_centros = [centro.color for centro in centros]
    if len(colores_centros) != len(set(colores_centros)):
        return False

    # Verificar que haya exactamente 9 piezas de cada color
    contador_colores = {color: 0 for color in set(colores_centros)}
    for pieza in piezas:
        if isinstance(pieza, Centro):
            contador_colores[pieza.color] += 1
    if not all(contador == 9 for contador in contador_colores.values()):
        return False

    # Verificar que no hayan 2 aristas iguales
    aristas = [pieza for pieza in piezas if isinstance(pieza, Arista)]
    colores_aristas = [tuple(sorted(arista.colores)) for arista in aristas]
    if len(colores_aristas) != len(set(colores_aristas)):
        return False

    # Verificar que no falte ninguna arista
    combinaciones_aristas = {
        ('amarillo', 'rojo'), ('amarillo', 'azul'), ('amarillo', 'verde'), ('amarillo', 'blanco'),
        ('blanco', 'rojo'), ('blanco', 'azul'), ('blanco', 'verde'), ('rojo', 'verde'),
        ('rojo', 'azul'), ('verde', 'azul'), ('verde', 'naranja'), ('verde', 'blanco'),
        ('rojo', 'naranja'), ('azul', 'naranja'), ('naranja', 'blanco')
    }
    colores_presentes = set(colores_aristas)
    if colores_presentes != combinaciones_aristas:
        return False

    return True

if __name__ == "__main__":
    cubo = CuboRubik()
    piezas = cubo.piezas
    if validar_cubo(piezas):
        print("El cubo de Rubik es válido.")
    else:
        print("El cubo de Rubik no es válido.")