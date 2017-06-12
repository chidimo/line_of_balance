"""Illustration of line of balance"""

import matplotlib.pyplot as plt
import numpy as np

def generate_single_plot(x1, x2, x3, x4):
    """Generate plot from points"""
    vertical_1x = [x1, x3]
    vertical_2x = [x2, x4]
    horizontal_1x = [x1, x2]
    horizontal_2x = [x3, x4]
    drop_line = [x4, x4]

    join_1y = [0, 100]
    join_2y = [0, 0]
    join_3y = [100, 100]

    plt.plot(vertical_1x, join_1y, 'k-')
    plt.plot(vertical_2x, join_1y, 'k-')
    plt.plot(horizontal_1x, join_2y, 'k-')
    plt.plot(horizontal_2x, join_3y, 'k-')
    plt.plot(drop_line, join_1y, 'r--')

    plt.show()

def generate_multiple_plots(set_of_points):
    """Generate plot from points"""

    fig = plt.figure()

    for each in set_of_points:
        ex1 = each[0]
        ex2 = each[1]
        ex3 = each[2]
        ex4 = each[3]

        vertical_1x = [ex1, ex3]
        vertical_2x = [ex2, ex4]
        horizontal_1x = [ex1, ex2]
        horizontal_2x = [ex3, ex4]
        drop_line = [ex4, ex4]

        join_1y = [0, 20]
        join_2y = [0, 0]
        join_3y = [20, 20]

        plt.plot(vertical_1x, join_1y, 'k-')
        plt.plot(vertical_2x, join_1y, 'k-')
        plt.plot(horizontal_1x, join_2y, 'k-')
        plt.plot(horizontal_2x, join_3y, 'k-')
        plt.plot(drop_line, join_1y, 'r--')


    space = np.linspace(0, 20, 5)
    plt.yticks(space)
    plt.ylabel("Number of units to produce")
    plt.xlabel("Time")
    plt.tight_layout()
    plt.savefig("line_of_balance_curve.pdf", dpi=100)
    plt.show()
