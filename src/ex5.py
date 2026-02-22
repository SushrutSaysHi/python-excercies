import matplotlib.pyplot as plt

data=[1, 2, 3, 4, 5]
names = ['A', 'B', 'C', 'D', 'E']

plt.pie(data, labels=names, colors=['red', 'blue', 'green', 'orange', 'purple'])
plt.xlabel("Names")
plt.ylabel("Data")
plt.title("Pie Chart Example")
plt.show()

