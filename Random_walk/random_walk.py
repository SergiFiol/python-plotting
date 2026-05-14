from random import choice

class RandomWalk:
	"""Clase para generar caminos aleatorios"""

	def __init__(self, num_points=50000):
	    """Inicializa atributos de un camino"""
	    self.num_points = num_points

	    #Todos los caminos empiezan en 0
	    self.x_values = [0]
	    self.y_values = [0]

	def fill_walk(self):
		"""Calcula todos los puntos del camino"""

		#Sigue dando pasos hasta la longitud indicada
		while len(self.x_values) < self.num_points:

			#Decide en que dirección ir y cuanto avanzar
			x_direction = choice([-1, 1])
			x_distance = choice([0, 1, 2, 3, 4])
			x_step = x_direction * x_distance

			y_direction = choice([-1, 1])
			y_distance = choice([0, 1, 2, 3, 4])
			y_step = y_direction * y_distance

			if x_step and y_step == 0:
				continue 

			#Calcula la nueva posición
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)
