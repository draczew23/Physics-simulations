mport numpy as np
import matplotlib.pyplot as plt
import random


class circle():
    def __init__(self):
        self.x = np.random.rand(1)
        self.y = np.random.rand(1)
        self.v = random.random()
        self.r = 0.05


circle_num = 16
gas = []

while len(gas) < circle_num:
    new = circle()

    if any(pow(particle.r - new.r, 2) <=
           pow(particle.x - new.x, 2) + pow(particle.y - new.y, 2) <=
           pow(particle.r + new.r, 2)
       for particle in gas):
        continue

    gas.append(new)

plt.figure(figsize=(6, 6), dpi=300)
plt.grid(True)

ax = plt.gca()
ax.set_aspect("equal", adjustable="box")

for g in gas:
    c = plt.cm.summer(g.v)
    circle = plt.Circle((g.x, g.y), g.r, color=c)
    ax.add_artist(circle)

plt.show()
