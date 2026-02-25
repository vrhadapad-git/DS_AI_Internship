import matplotlib.pyplot as plt
plt.title("Monthly Revenue Growth")
months = [1, 2, 3, 4, 5,6]
revenue = [2000, 4500, 4000, 7500, 9000,10000]

plt.xlabel("months")
plt.ylabel("revenu")
plt.plot(months,revenue)
plt.show()