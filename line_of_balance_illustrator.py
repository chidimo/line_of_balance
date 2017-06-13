"""Illustration of the various points in the line of balance
diagram"""

import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

def generate_single_plot(ex1, ex2, ex3, ex4, ymin, ymax):
    """Generate plot from points"""

    label_x_position = (ex2 + ex3)//2
    label_y_position = (ymax + ymin)//2
    space = np.linspace(ymin, ymax, 5)
    plt.yticks(space)
    plt.ylabel("Number of units to produce")
    plt.xlabel("Project duration")
    plt.tight_layout()

    Path = mpath.Path
    path_data = [
        (Path.MOVETO, (ex1, ymin)),
        (Path.LINETO, (ex3, ymax)),
        (Path.LINETO, (ex4, ymax)),
        (Path.LINETO, (ex2, ymin)),
        (Path.CLOSEPOLY, (ex1, ymin))
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)

    # plot and fill control points and connecting lines
    x_vals, y_vals = zip(*path.vertices)
    plt.plot(x_vals, y_vals, 'k-')
    plt.fill(x_vals, y_vals, 'g')
    plt.text(label_x_position, label_y_position, "Plot")
    plt.plot([ex4, ex4], [ymin, ymax], 'r--')
    # add annotations
    # plt.annotate()

    plt.show()

generate_single_plot(5, 15, 35, 45, 0, 20)
