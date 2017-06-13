"""Illustration of line of balance"""

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

    plt.show()

def generate_multiple_plots(set_of_points, ymin, ymax):
    """Generate plot from points"""

    # fig = plt.figure()

    for each in set_of_points:
        name = each[0]
        ex1 = each[1]
        ex2 = each[2]
        ex3 = each[3]
        ex4 = each[4]

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
        # calculate label position
        label_x_position = (ex2 + ex3)//2
        label_y_position = (ymax + ymin)//2

        # plot and fill control points and connecting lines
        x_vals, y_vals = zip(*path.vertices)
        plt.plot(x_vals, y_vals, 'b-', label=name)
        plt.fill(x_vals, y_vals, 'g')
        # add label
        plt.text(label_x_position, label_y_position, name)
        # draw dropdown
        plt.plot([ex4, ex4], [ymin, ymax], 'r--')

    space = np.linspace(0, 20, 5)
    plt.yticks(space)
    plt.ylabel("Number of units to produce")
    plt.xlabel("Project duration")
    plt.tight_layout()
    plt.savefig("line_of_balance_curve.pdf", dpi=100)
    plt.legend()
    plt.show()
