"""Line of Balance illustrator

author: Chidi Orji
email: orjichidi95@gmail.com
github: https://github.com/Parousiaic
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
I bear no responsibility for anything you might break while using this script.
"""

import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np

def make_illustrator(ex1, ex2, ex3, ex4, ymin, ymax):
    """Generate plot from points"""

    fig = plt.figure(figsize=(10,8), facecolor='lightblue', edgecolor='g')

    label_x_position = (ex2 + ex3)//2
    label_y_position = (ymax + ymin)//2
    space = np.linspace(ymin, ymax, 5)
    plt.yticks(space)
    plt.ylabel("Number of units to produce")
    plt.xlabel("Project duration")
    # plt.tight_layout()

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
    plt.plot(x_vals, y_vals, 'b-')
    plt.fill(x_vals, y_vals, 'cyan')
    plt.text(label_x_position, label_y_position, "Activity")
    plt.plot([ex4, ex4], [ymin, ymax], 'r--')
    plt.title("Line of Balance Illustrator", color='k')

    # add annotations
    plt.annotate('Start on first section', xy=(ex1, ymin), xytext=(ex1, ymin+5),
                 arrowprops=dict(arrowstyle='->'), horizontalalignment='center')
    plt.annotate('End on first section', xy=(ex2, ymin), xytext=(ex2+5, ymin),
                 arrowprops=dict(arrowstyle='->'), verticalalignment='right')
    plt.annotate('Start on last section', xy=(ex3, ymax), xytext=(ex3, ymax+4),
                 arrowprops=dict(arrowstyle='->'), horizontalalignment='center')
    plt.annotate('End on last section', xy=(ex4, ymax), xytext=(ex4, ymax+2),
                 arrowprops=dict(arrowstyle='->'), horizontalalignment='center')

    axes = plt.gca()
    axes.title.set_color('red')

    axes.set_xlim(0, 1.1*ex4)
    axes.set_ylim(-0.1, 1.3*ymax)
    axes.spines['right'].set_visible(False)
    axes.spines['top'].set_visible(False)

    plt.savefig("output/line_of_balance_illustrator.pdf", facecolor=fig.get_facecolor(), dpi=100)
    plt.savefig("output/line_of_balance_illustrator.png", facecolor=fig.get_facecolor(), dpi=100)

    plt.show()

make_illustrator(5, 15, 35, 45, 0, 20)

if __name__ == "__main__":
    """Only for illustration"""
    pass
