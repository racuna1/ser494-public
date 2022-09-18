import matplotlib.pyplot as plt
import numpy as np

__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"


################################################################################
# Blank Plot (two variables)
# new topics: subplots(), set (title, ylabel, xlabel), show, savefig

fig, ax = plt.subplots()
ax.set(title='Fancy Title',
       ylabel='Y-Axis Nothingness', xlabel='X-Axis Nothingness')
fig.show()
fig.savefig("mpy03_demo_blankplot.png")


################################################################################
# Line Plot
# new topics: np.arange, latex in label, plot
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

n = np.arange(0., 10, .2)

fig, ax = plt.subplots()
ax.set(title='Growth Function: $f(n)=2n^2+3$',
       ylabel='Number of Operations', xlabel='X-Axis Nothingness')
plt.plot(n, 2 * n ** 2 + 3)

fig.show()
fig.savefig("mpy03_demo_lineplot1.png")


################################################################################
# Line Plot (variants; show more data)
# new topics: np.linspace, default interpolation, multiple plots, legend, dots
n2 = np.linspace(0, 10, 5)

print(len(n2))
print(n2)

fig, ax = plt.subplots()
ax.set(title='Growth Functions',
       ylabel='Number of Operations', xlabel='X-Axis Nothingness')
plt.plot(n, 2 * n ** 2 + 3, label="$f(n)=2n^2+3$ (40 samples)")
plt.plot(n2, 2 * n2 ** 2 + 3, label=f"$f(n)=2n^2+3$ ({len(n2)} samples)")
plt.plot(n2, 3 * n2 + 10, "o", label="$f(n)=3n+10$ (dot plot)")  # see Format Strings
ax.legend()
fig.show()
fig.savefig("mpy03_demo_lineplot2.png")
exit()



################################################################################
# making look nice
# TODO: subplots(figsize)
# TODO: adding text on figure
# TODO: teach axis limits
# TODO: manual axis
# FUTURE: text formatting
# FUTURE: adding annotation?

# TODO: line styles (shape + color + dot)

# FUTURE: color scale?

################################################################################


def sample_normal(mean, sigma, num):
    return mean + sigma * np.random.randn(num)

# TODO: np.random.randn
# TODO: np.random.randint
# TODO: multiple ax on same figure?

# x = np.linspace(0, 2, 100)
# blank -> simple data -> add axis stuff + fig size
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

# FUTURE: color by classes?