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

fig, ax = plt.subplots()
ax.set(title='Growth Functions',
       ylabel='Number of Operations', xlabel='Problem Size')
plt.plot(n, 2 * n ** 2 + 3, label="$f(n)=2n^2+3$ (40 samples)")
plt.plot(n2, 2 * n2 ** 2 + 3, label=f"$f(n)=2n^2+3$ ({len(n2)} samples)")
plt.plot(n2, 3 * n2 + 10, "o", label="$f(n)=3n+10$ (dot plot)")  # see Format Strings
ax.legend()
fig.show()
fig.savefig("mpy03_demo_lineplot2.png")


################################################################################
# Line Plot (better visuals)
# new topics: subplots(figsize), suptitle (fontsize), xlim/ylim, line formatting, text (fontstyle, alpha)
# https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors

fig, ax = plt.subplots(figsize=(5, 4))
fig.suptitle('Growth Functions', fontsize=20, color="black")
ax.set(xlim=[0, 8], ylim=[0, 175],
       ylabel='Number of Operations', xlabel='Problem Size')
# alternative:
# ax.set_xlim([0, 8])
# ax.set_ylim([0, 175])
# ax.set_ylabel('Number of Operations')
# ax.set_xlabel('Problem Size')
ax.plot(n, 2 * n ** 2 + 3, "--g", label="$f(n)=2n^2+3$ (40 samples)")
ax.plot(n2, 2 * n2 ** 2 + 3, "cyan", label=f"$f(n)=2n^2+3$ ({len(n2)} samples)")
ax.plot(n2, 3 * n2 + 10, "*", label="$f(n)=3n+10$ (dot plot)")
ax.legend()
ax.text(1.75, 24, "intersection", fontstyle="italic", alpha=.5)
fig.show()
fig.savefig("mpy03_demo_lineplot3.png")

# FUTURE: manual axis ticks?
# FUTURE: adding annotation?
# FUTURE: color scale?


################################################################################
# TODO: multiple plot / multiple ax on same figure?


################################################################################
# Scatter plot (two variables)
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
# new topics: np.random.randn, np.random.randint, ax.scatter (x,y)

def sample_normal(mean, sigma, num):
    return mean + sigma * np.random.randn(num)


# variables used for positioning in space.
count = 100
sp_a = np.random.randint(0, 50, count)
sp_b = 2 * sp_a + sample_normal(0, 5, count)

fig, ax = plt.subplots()
ax.set(title='Scatter Plot (simple)',
       ylabel='Y-Axis (B)', xlabel='X-Axis (A)')
ax.scatter(sp_a, sp_b)
fig.show()
fig.savefig("mpy03_demo_scatterplot1.png")

# TODO: color scale?

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


################################################################################
# TODO: bar chart

################################################################################

################################################################################
# Pie Chart
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
# new topics: pie (*), axis

# TODO: pie chart
# top prog langs

# data from https://spectrum.ieee.org/top-programming-languages-2022
names = ["Python", "C", "C++", "C#", "Java", "LISP"]
values = [100, 96.8, 88.58, 86.99, 70.22, .77]
explode = (.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots()
ax.set(title='Top Programming Languages 2022 (IEEE)')
ax.pie(values, explode=explode, labels=names, autopct='%.2f%%', startangle=90)  # shadow=True
ax.axis('equal')
fig.show()
fig.savefig("mpy03_demo_piechart1.png")


################################################################################
# TODO: hist chart