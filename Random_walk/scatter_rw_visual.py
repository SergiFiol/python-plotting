import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

#Hace un camino aleatorio mientras el programa este activo

while True:
	rw = RandomWalk()
	rw.fill_walk()

	#Traza los puntos del camino
	plt.style.use("classic")
	fig, ax = plt.subplots()
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap="Blues",
		edgecolors="none", s=1)
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	#Enfatiza el primer y ultimo punto
	ax.scatter(0, 0,c="yellow", edgecolors="none", s=40)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c="green", edgecolors="none", s=40)


	plt.show()

	keep_runing = input("Generar otro camino? (y/n):")
	if keep_runing == "n" :
		break