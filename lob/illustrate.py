"""Line of Balance illustrator"""

import matplotlib.pyplot as plt
import matplotlib.path as mpath
import numpy as np
from paths import OUT_PATH

def make_illustration(coord1, coord2, coord3, coord4, ymin, ymax):
    """Generate plot from points"""

    fig = plt.figure(figsize=(10, 8), facecolor='lightblue', edgecolor='g')

    label_x_position = (coord2 + coord3)//2
    label_y_position = (ymax + ymin)//2
    space = np.linspace(ymin, ymax, 5)
    plt.yticks(space)
    plt.ylabel("Number of units to produce")
    plt.xlabel("Project duration")
    # plt.tight_layout()

    Path = mpath.Path
    path_data = [
        (Path.MOVETO, (coord1, ymin)),
        (Path.LINETO, (coord3, ymax)),
        (Path.LINETO, (coord4, ymax)),
        (Path.LINETO, (coord2, ymin)),
        (Path.CLOSEPOLY, (coord1, ymin))
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)

    # plot and fill control points and connecting lines
    x_vals, y_vals = zip(*path.vertices)
    plt.plot(x_vals, y_vals, 'b-')
    plt.fill(x_vals, y_vals, 'cyan')
    plt.text(label_x_position, label_y_position, "Activity")
    plt.plot([coord4, coord4], [ymin, ymax], 'r--')
    plt.title("Line of Balance Illustrator", color='k')

    # add annotations
    plt.annotate('Start on first section', xy=(coord1, ymin), xytext=(coord1, ymin+5),
                 arrowprops=dict(arrowstyle='->'), horizontalalignment='center')
    plt.annotate('End on first section', xy=(coord2, ymin), xytext=(coord2+5, ymin),
                 arrowprops=dict(arrowstyle='->'), verticalalignment='right')
    plt.annotate('Start on last section', xy=(coord3, ymax), xytext=(coord3, ymax+4),
                 arrowprops=dict(arrowstyle='->'), horizontalalignment='center')
    plt.annotate('End on last section', xy=(coord4, ymax), xytext=(coord4, ymax+2),
                 arrowprops=dict(arrowstyle='->'), horizontalalignment='center')

    axes = plt.gca()
    axes.title.set_color('red')

    axes.set_xlim(0, 1.1*coord4)
    axes.set_ylim(-0.1, 1.3*ymax)
    axes.spines['right'].set_visible(False)
    axes.spines['top'].set_visible(False)

    plt.savefig(OUT_PATH + "/illustrator.pdf", facecolor=fig.get_facecolor(), dpi=100)
    plt.savefig(OUT_PATH + "/illustrator.png", facecolor=fig.get_facecolor(), dpi=100)

    plt.show()

if __name__ == "__main__":
    make_illustration(5, 15, 35, 45, 0, 20)
