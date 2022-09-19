import matplotlib.pyplot as plt
import numpy as np

__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"

# this file contains an outline for the code demonstrations in the slides. it is
# suggested that you load up this file at the start of lecture and then fill it
# out as the lecture progresses. use it to play with the specific features we
# discuss. this file is NOT graded.


################################################################################
# Blank Plot (two variables)
# new topics: subplots(), set (title, ylabel, xlabel), show, savefig

# TODO

################################################################################
# Line Plot
# new topics: np.arange, latex in label, plot
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

n = np.arange(0., 10, .2)

# TODO

################################################################################
# Line Plot (variants; show more data)
# new topics: np.linspace, default interpolation, multiple plots, legend, dots

n2 = np.linspace(0, 10, 5)

# TODO

################################################################################
# Line Plot (better visuals)
# new topics: subplots(figsize), suptitle (fontsize), xlim/ylim, line formatting, text (fontstyle, alpha)
# https://matplotlib.org/stable/api/colors_api.html#module-matplotlib.colors

# TODO

################################################################################
# Multiple Plots
# new topics: plt.subplots(nrows, ncols)
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

# TODO


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

# TODO

################################################################################
# Scatter plot (four variables)
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
# new topics: ax.scatter (... s, c)

count = 100

# (new) variables encoded into "point" visualization.
sp_c = sample_normal(0, 1, count)
sp_d = sample_normal(60, 20, count) + 30

# TODO


################################################################################
# Bar Chart (Plot)
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
# new topics: (bar)

languages = ['Java', 'None', 'C', 'Multiple', "C#", "Python"]
counts = [5, 1, 2, 2, 1, 2]

# TODO

################################################################################
# Pie Chart
# see https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
# new topics: pie (*), axis

# data from https://spectrum.ieee.org/top-programming-languages-2022
names = ["Python", "C", "C++", "C#", "Java", "LISP"]
values = [100, 96.8, 88.58, 86.99, 70.22, .77]
explode = (.1, 0, 0, 0, 0, 0)

# TODO

################################################################################
# Histogram
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# new topics: hist (*), grid

data = sample_normal(10, 1, 200)

# TODO
