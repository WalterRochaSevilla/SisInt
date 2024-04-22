from cubo import CuboRubik
from leer_desde_txt import leer_estado_cubo_desde_txt

if __name__ == "__main__":
    # Leer estado del cubo desde el archivo de texto
    estado_cubo = leer_estado_cubo_desde_txt('estado_cubo.txt')

    # Crear instancia de CuboRubik
    cubo = CuboRubik()

    # Asignar piezas al cubo
    for numero_cara, piezas in estado_cubo.items():
        for tipo_pieza, numero_pieza, numero_cara_pieza in piezas:
            if tipo_pieza == 'Esquina':
                cubo.caras[numero_cara].estado[numero_cara_pieza][numero_pieza] = 'Esquina'
            else:
                cubo.caras[numero_cara].estado[numero_cara_pieza][numero_pieza] = 'Arista'

    # Validar el cubo
    if cubo.validar_cubo():
        print("El cubo de Rubik es válido.")
    else:
        print("El cubo de Rubik no es válido.")