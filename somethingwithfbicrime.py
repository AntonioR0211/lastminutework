import matplotlib.pyplot as plt
import numpy as np

crimes_list = []
with open("ViolentCrimes.txt", 'r') as f:
    for l in f:
        crimes_list.append(int(l))

dates = range(2000, 2020)
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(4)
plt.plot(dates, crimes_list, 'o:r', color="Purple")
plt.title("Violent Crimes Throughout the 21st Century")
plt.xlabel("Time (Years)")
plt.ylabel("Crimes (Millions)")
fig, axs = plt.subplots(2)
fig.suptitle('2 Plots Because Why Not')
axs[0].plot(x, y)
axs[1].plot(-x, -y)
plt.show()
