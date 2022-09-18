import matplotlib.pyplot as plt
import numpy as np

__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"


def sample_normal(mean, sigma, num):
    return mean + sigma * np.random.randn(num)

# TODO: teach np.random.randn
# TODO: teach np.random.randint
# TODO: teach subplots()
# TODO: teach set()
# TODO: teach show()
# TODO: teach savefig()
# TODO: teach axis limits (anywhere)

#fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')

################################################################################
# Scatter plot (two variables)
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
# new topics: ax.scatter (x,y)

count = 100

# visualizing two variables with a scatter plot

# variables used for positioning in space.
sp_a = np.random.randint(0, 50, count)
sp_b = 2 * sp_a + sample_normal(0, 5, count)

fig, ax = plt.subplots()
ax.set(title='Scatter Plot (simple)',
       ylabel='Y-Axis (B)', xlabel='X-Axis (A)')
ax.scatter(sp_a, sp_b)
fig.show()
fig.savefig("mpy03_demo_scatterplot1.png")

# color scale?

################################################################################
# Scatter plot (four variables)
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
# new topics: ax.scatter (... s, c)

count = 100

# visualizing four variables with a scatter plot

# (new) variables encoded into "point" visualization.
sp_c = sample_normal(0, 1, count)
sp_d = sample_normal(60, 20, count) + 30

fig, ax = plt.subplots()
ax.set(title='Scatter Plot (less simple)',
       ylabel='Y-Axis (B)', xlabel='X-Axis (A)')
ax.scatter(sp_a, sp_b, c=sp_c, s=sp_d)
fig.show()
fig.savefig("mpy03_demo_scatterplot2.png")

# TODO: legend?
# TODO: color by classes?
# TODO: color scale?
