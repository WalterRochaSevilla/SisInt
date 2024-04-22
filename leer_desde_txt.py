
def leer_estado_cubo_desde_txt(file_path):
    with open(file_path, 'r') as file:
        lineas = file.readlines()
        estado_cubo = {}

        # Crear instancias de cara
        for i, linea in enumerate(lineas, start=1):
            # Eliminar espacios en blanco y caracteres de formato
            linea = linea.strip().replace('[', '').replace(']', '').replace(',', '')

            # Dividir la línea en piezas
            piezas = linea.split()

            # Encontrar el número de la cara según la pieza 5
            numero_cara = None
            for idx, pieza in enumerate(piezas, start=1):
                if 'pieza5' in pieza:
                    numero_cara = idx
                    break

            # Crear el estado de la cara si se encuentra el número de la cara
            if numero_cara is not None:
                estado_cubo[numero_cara] = []

                # Crear piezas
                for j, pieza in enumerate(piezas, start=1):
                    # Determinar el tipo de pieza (esquina o arista)
                    if j in [1, 3, 7, 9]:
                        tipo_pieza = 'Esquina'
                    else:
                        tipo_pieza = 'Arista'

                    # Agregar la pieza al estado de la cara
                    estado_cubo[numero_cara].append((tipo_pieza, j, i))

    return estado_cubo