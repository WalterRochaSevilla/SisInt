def leer_estado_cubo_desde_txt(file_path):
  with open(file_path, 'r') as file:
      lineas = file.readlines()
  
      estado_cubo = {}
  
      for numero_cara, linea in enumerate(lineas, start=1):
          linea = linea.strip().replace('[', '').replace(']', '').replace(',', '')
  
          estado_cubo[numero_cara] = []
  
          for idx, _pieza in enumerate(linea.split(), start=1):
              tipo_pieza = 'Esquina' if idx in [1, 3, 7, 9] else 'Arista'
              estado_cubo[numero_cara].append((tipo_pieza, idx, numero_cara))
  
  return estado_cubo