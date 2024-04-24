
class CuboSolverAStar:
  def __init__(self, estado_inicial,cubo):
      self.estado_inicial = estado_inicial
      self.cubo = cubo

  def resolver(self):
      movimientos_necesarios = [] 
      # Almacena la secuencia de movimientos necesarios para resolver el cubo
      estado_actual = self.estado_inicial

      # Definir función heurística
      def heuristica(estado):
          # Usar distancia Manhattan como heurística
          return self.distancia_manhattan(estado)

      # Definir cola de prioridad para almacenar los estados a explorar
      cola_prioridad = [(heuristica(estado_actual), estado_actual, [])]

      # Definir conjunto para almacenar los estados ya visitados
      estados_visitados = set()

      # Algoritmo A*
      while cola_prioridad:
          _, estado_actual, movimientos = cola_prioridad.pop(0)

          # Verificar si el estado actual es el estado objetivo
          if self.es_estado_objetivo(estado_actual):
              movimientos_necesarios = movimientos
              break

          # Agregar el estado actual al conjunto de estados visitados
          hashable_estado_actual = tuple(sorted((key, tuple(value)) for key, value in estado_actual.items()))
          estados_visitados.add(tuple(hashable_estado_actual))

          # Generar los posibles movimientos y estados resultantes
          for movimiento in ['R', 'R\'', 'L', 'L\'', 'U', 'U\'', 'D', 'D\'', 'F', 'F\'', 'B', 'B\'']:
              nuevo_estado = self.aplicar_movimiento(estado_actual, movimiento)
              nuevo_movimientos = movimientos + [movimiento]

              # Si el nuevo estado no ha sido visitado, agregarlo a la cola de prioridad
              if nuevo_estado not in estados_visitados:
                  cola_prioridad.append((heuristica(nuevo_estado), nuevo_estado, nuevo_movimientos))

          # Ordenar la cola de prioridad según la heurística
          cola_prioridad.sort(key=lambda x: x[0])

      return movimientos_necesarios

  def es_estado_objetivo(self, estado):
      colores_esperados = {
          1: ['blanco'] * 9,
          2: ['rojo'] * 9,
          3: ['azul'] * 9,
          4: ['verde'] * 9,
          5: ['naranja'] * 9,
          6: ['amarillo'] * 9
      }

      # Verificar si cada cara tiene los colores esperados
      return all(colores == colores_esperados[cara] for cara, colores in estado.items())

  def aplicar_movimiento(self, estado, movimiento):
      # Copiar el estado actual para no modificarlo directamente
      nuevo_estado = estado.copy()

      # Lógica para aplicar el movimiento
      if movimiento == 'R':
          self.cubo.R()
      elif movimiento == 'R\'':
          self.cubo.R_prime()
      elif movimiento == 'L':
          self.cubo.L()
      elif movimiento == 'L\'':
          self.cubo.L_prime()
      elif movimiento == 'U':
          self.cubo.U()
      elif movimiento == 'U\'':
          self.cubo.U_prime()
      elif movimiento == 'D':
          self.cubo.D()
      elif movimiento == 'D\'':
          self.cubo.D_prime()
      elif movimiento == 'F':
          self.cubo.F()
      elif movimiento == 'F\'':
          self.cubo.F_prime()
      elif movimiento == 'B':
          self.cubo.B()
      elif movimiento == 'B\'':
          self.cubo.B_prime()

      # Devolver el nuevo estado del cubo
      return nuevo_estado

  def distancia_manhattan(self, estado_actual):
      # Definir la posición objetivo de cada pieza
      posiciones_objetivo = {
          1: [(0, 0)] * 9,  # centro blanco
          2: [(2, 1), (2, 0), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (1, 1)],  # cara roja
          3: [(2, 1), (2, 0), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (1, 1)],  # cara azul
          4: [(2, 1), (2, 0), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (1, 1)],  # cara verde
          5: [(2, 1), (2, 0), (2, 2), (1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (1, 1)],  # cara naranja
          6: [(0, 0)] * 9  # centro amarillo
      }

      # Calcular la distancia de Manhattan total
      distancia_total = 0
      for cara, estado in estado_actual.items():
          for i, _pieza in enumerate(estado):
              # Obtener las coordenadas de la pieza en el estado actual
              coordenadas_actual = (i, cara)

              # Obtener las coordenadas objetivo de la pieza
              coordenadas_objetivo = posiciones_objetivo[cara][i]

              # Calcular la distancia de Manhattan entre las coordenadas actual y objetivo
              distancia_total += abs(coordenadas_actual[0] - coordenadas_objetivo[0]) \
                                 + abs(coordenadas_actual[1] - coordenadas_objetivo[1])
      return distancia_total