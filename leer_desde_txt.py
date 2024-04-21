from corner_piece import Arista, Centro, Esquina


def leer_estado_cubo_desde_txt(file_path):
  with open(file_path, 'r') as file:
      lineas = file.readlines()
      estado_cubo = []
  
      for linea in lineas:
          colores = linea.strip().split(',')
          if len(colores) == 1:
              estado_cubo.append(Centro(colores[0]))
          elif len(colores) == 2:
              estado_cubo.append(Arista(colores))
          elif len(colores) == 3:
              estado_cubo.append(Esquina(colores))
  
  return estado_cubo