from cubo import CuboRubik
from leer_desde_txt import leer_estado_cubo_desde_txt


def main():
    # Definir la ruta del archivo de texto
    ruta_archivo = "ejemplo.txt"

    # Leer el estado del cubo desde el archivo de texto
    estado_cubo = leer_estado_cubo_desde_txt(ruta_archivo)

    # Crear una instancia del cubo con el estado inicial
    cubo = CuboRubik(estado_cubo)

    # Resolver el cubo y obtener la serie de pasos para resolverlo
    pasos_para_resolver = cubo.resolver()

    print("Pasos para resolver el cubo:")
    print(pasos_para_resolver)

if __name__ == "__main__":
    main()