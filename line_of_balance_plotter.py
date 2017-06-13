"""Illustration of line of balance"""

import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

def generate_single_plot(ex1, ex2, ex3, ex4, ymin, ymax):
    """Generate plot from points"""

    fig = plt.figure(figsize=(10,8), facecolor='lightblue', edgecolor='g')
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

    project_duration = set_of_points[-1][4] + 1

    fig = plt.figure(facecolor='lightblue', edgecolor='g')
    axes = plt.gca()

    axes.set_xlim(0, 1.1*project_duration)
    axes.set_ylim(-0.1, 1.3*ymax)
    axes.spines['right'].set_visible(False)
    axes.spines['top'].set_visible(False)

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
        plt.fill(x_vals, y_vals, 'cyan')
        # add label
        plt.text(label_x_position, label_y_position, name)
        # draw dropdown
        plt.plot([ex4, ex4], [ymin, ymax], 'r--')

    plt.title("Line of Balance Diagram")

    plt.annotate('Total project duration is\n{} days'.format(project_duration),
                 xy=(0, 0), xytext=(project_duration/2, 1.2*ymax),
                 horizontalalignment='center',
                 verticalalignment='top')

    space = np.linspace(0, 20, 5)
    plt.yticks(space)
    plt.ylabel("Number of units to produce")
    plt.xlabel("Project duration")

    plt.tight_layout()

    plt.savefig("line_of_balance_curve.pdf", facecolor=fig.get_facecolor(), dpi=100)
    plt.savefig("line_of_balance_curve.png", facecolor=fig.get_facecolor(), dpi=100)
    # plt.legend()
    plt.show()

def main():
    """Docstring"""
    pass
