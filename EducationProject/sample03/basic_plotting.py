import matplotlib.pyplot as plt

views = [534, 689, 258, 401, 724, 689, 350]
days = range(1, 8)

plt.plot(days, views, label='Youtube')
plt.xlabel('Day')
plt.ylabel('Views')
plt.legend(loc='upper left')
plt.title('Hello')
plt.show()
