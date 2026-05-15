import matplotlib.pyplot as plt 

from die import Die

#Creates a die
sides = int(input("How many sides have the die?"))
rolls = int(input("How many rolls?"))
die_1 = Die(sides)


#Make a number of rolls and save them in a list
results = [die_1.roll() for roll_num in range(rolls)]

#Analyze the results
x_values = list(range(1, sides +1))
frequencies = [results.count(value) for value in range(1, sides + 1)]

print(frequencies)

#Visualize results
plt.bar(x_values, frequencies, color="skyblue", edgecolor="navy", linewidth=1.5, alpha=0.7)

plt.xticks(range(min(x_values), max(x_values)+1))
plt.yticks(range(0, max(frequencies)+1))
plt.xlabel("Result")
plt.ylabel("Frequency")
plt.title(f"Result of rolling a D{sides}  {rolls} times")


plt.show()
