import csv
from datetime import datetime

import matplotlib.pyplot as plt 

filename = "temperature_2025.csv"
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	#Sets the values of the x and y axes
	rows = list(reader)
	dates = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").date() for row in rows]
	highs = [float(row[3]) for row in rows]
	lows = [float(row[2]) for row in rows]
	
	#Graph the maximum and minimum temperature functions
	fig, ax = plt.subplots()
	ax.plot(dates, highs, c="red", alpha=0.5)
	ax.plot(dates, lows, c="blue", alpha=0.5)
	plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

	plt.title("Temperature Variation in Menorca Throughout 2025", fontsize=10)
	plt.xlabel("", fontsize=8)
	fig.autofmt_xdate()
	plt.ylabel("Temperature(Cº)", fontsize=8)
	plt.tick_params(axis="both", which="major", labelsize=8)

	plt.show()