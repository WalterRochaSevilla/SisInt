class Cara:
  def __init__(self, numero):
      self.numero = numero
      self.estado = [None] * 9  # Inicializar la lista de piezas con valores None

  def __repr__(self):
      representacion = f"Cara {self.numero}:\n"
      for i in range(0, 9, 3):
          representacion += f"{self.estado[i:i+3]}\n"
      return representacion

  def obtener_estado(self):
      return self.estado

  def actualizar_estado(self, nuevo_estado):
      if len(nuevo_estado) != 9:
          raise ValueError("El nuevo estado debe tener 9 elementos")
      self.estado = nuevo_estado

  def girar_sentido_horario(self):
      self.estado = [self.estado[6], self.estado[3], self.estado[0],
                     self.estado[7], self.estado[4], self.estado[1],
                     self.estado[8], self.estado[5], self.estado[2]]

  def girar_sentido_antihorario(self):
      self.estado = [self.estado[2], self.estado[5], self.estado[8],
                     self.estado[1], self.estado[4], self.estado[7],
                     self.estado[0], self.estado[3], self.estado[6]]