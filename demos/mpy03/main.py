__author__      = "Ruben Acuna"
__copyright__   = "Copyright 2022, Ruben Acuna"

import matplotlib.pyplot as plt


#https://github.com/matplotlib/AnatomyOfMatplotlib/blob/master/AnatomyOfMatplotlib-Part1-Figures_Subplots_and_layouts.ipynb
fig = plt.figure(facecolor=(1, 0, 0, .1))
plt.show()

# what is format of color?
# axes is an object.
# fig contains axes contains axis+axis
# define to define: figure, axes, axis, and relationships between them.

fig = plt.figure(figsize=plt.figaspect(2.0), facecolor=(1, 0, 0, .1))
plt.show()

print(plt.figaspect(2.0)) # width, height


fig = plt.figure()
fig2 = plt.figure()
ax = fig.add_subplot(111) # We'll explain the "111" later. Basically, 1 row and 1 column.
ax2 = fig2.add_subplot(111)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
       ylabel='Y-Axis', xlabel='X-Axis')
ax2.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes 2',
       ylabel='Y-Axis', xlabel='X-Axis')
# set position?

# see note about the two different ways to do this.
# ^ that has exceptions though.
# For example, foo.set(bar='blah') would call foo.set_bar('blah').
#  For example, when calling plt.xlim(1, 10), pyplot calls ax.set_xlim(1, 10) on whichever Axes is "current".
plt.show()

#multi plot example
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0,0].set(title='Upper Left')
axes[0,1].set(title='Upper Right')
axes[1,0].set(title='Lower Left')
axes[1,1].set(title='Lower Right')
for ax in axes.flat:
    # Remove all xticks and yticks...
    ax.set(xticks=[], yticks=[])
plt.show()