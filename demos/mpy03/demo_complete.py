import matplotlib.pyplot as plt
import numpy as np

__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"

# this file contains all the code from the slides already typed in. it is
# suggested that you use it as a reference and instead start by viewing
# demo_template.py.

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
# FUTURE: different scales?

################################################################################
# Multiple Plots
# new topics: plt.subplots(nrows, ncols)
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

fig, axs = plt.subplots(2, 2)
fig.suptitle('Multiple Plots', fontsize=20)
axs[0, 0].plot(n, 2 * n ** 2 + 3, "--g")
axs[1, 0].plot(n2, 2 * n2 ** 2 + 3, "cyan")
axs[0, 1].plot(n2, 3 * n2 + 10, "*")
axs[1, 1].plot(n, 2 * n ** 2 + 3, "--g", label="(40 samples)")
axs[1, 1].plot(n2, 2 * n2 ** 2 + 3, "cyan", label=f"({len(n2)} samples)")

for row in axs:
    for col in row:
        col.set(xlim=[0, 8], ylim=[0, 175])

axs[1, 1].legend()

fig.show()
fig.savefig("mpy03_demo_multiples.png")


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

# FUTURE: color scale?

################################################################################
# Scatter plot (four variables)
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
# new topics: ax.scatter (... s, c)

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
# Bar Chart (Plot)
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
# new topics: bar

languages = ["Java", "None", "C", "Multiple", "C#", "Python"]
counts = [5, 1, 2, 2, 1, 2]

fig, ax = plt.subplots()
ax.set(title='Number of Times Languages Are Used in SER Courses',
       ylabel='Count', xlabel='Language')
ax.bar(languages, counts)
fig.show()
fig.savefig("mpy03_demo_barchart.png")


################################################################################
# Pie Chart
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
# new topics: pie (*), axis

# data from https://spectrum.ieee.org/top-programming-languages-2022
names = ["Python", "C", "C++", "C#", "Java", "LISP"]
values = [100, 96.8, 88.58, 86.99, 70.22, .77]
explode = (.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots()
ax.set(title='Top Programming Languages 2022 (IEEE)')
ax.pie(values, explode=explode, labels=names, autopct='%.2f%%', startangle=90)
# could have used a shadow=True... but?
ax.axis('equal')
fig.show()
fig.savefig("mpy03_demo_piechart1.png")


################################################################################
# Histogram
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# new topics: hist (*), grid

data = sample_normal(10, 1, 200)

fig, ax = plt.subplots()
ax.set(title=r'Samples from Normal Distribution with $\mu=10$ and $\sigma=1$',
       ylabel='Probability', xlabel='Value')
ax.hist(data, bins=10, density=True)  # bins=4
# ax.grid(True)  # could have done this, but...?
plt.show()
fig.savefig("mpy03_demo_histogram1.png")
