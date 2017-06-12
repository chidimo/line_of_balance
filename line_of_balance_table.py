"""Illustration of line of balance"""

import matplotlib.pyplot as plt
import openpyxl as OP
from line_of_balance import default_lob

def generate_plot_from_points(x1, x2, x3, x4):
    """Generate plot from points"""
    vertical_1x = [x1, x3]
    vertical_2x = [x2, x4]
    horizontal_1x = [x1, x2]
    horizontal_2x = [x3, x4]
    drop_line = [x4, x4]

    join_1y = [0, 100]
    join_2y = [0, 0]
    join_3y = [100, 100]

    plt.figure()

    plt.plot(vertical_1x, join_1y, 'k-')
    plt.plot(vertical_2x, join_1y, 'k-')
    plt.plot(horizontal_1x, join_2y, 'k-')
    plt.plot(horizontal_2x, join_3y, 'k-')
    plt.plot(drop_line, join_1y, 'r--')

    plt.show()

def pyplot_table(headings, cell_values):
    """Draw the line of balance table"""

    num_rows = len(cell_values[0])
    num_cols = len(cell_values)
    cell_width = 2.5
    cell_height = 0.3
    fig_width = cell_width * num_cols
    fig_height = cell_height * (num_rows + 1) # plus 1 for heading

    fig = plt.figure(figsize=(fig_width, fig_height))
    ax = fig.add_subplot(111)
    ax.axis('off')
    lob_table = plt.table(cellText=cell_values,
                          colLabels=headings,
                          loc='center',
                          bbox=[0, 0, 1, 0.5])

    lob_table.auto_set_font_size(False)
    lob_table.set_fontsize(5)
    lob_table.scale(2, 2)
    fig.savefig('lob.png', bbox_inches='tight', bbox_extra_artists=[lob_table])
    plt.show()

def excel_table(headings, cell_values):
    """Table as excel file"""

    book = OP.Workbook()
    sheet = book.active
    sheet.title = "lineOfBalance"

    for idx, item in enumerate(headings):
        sheet.cell(row=1, column=idx+1, value=item)
    i = 2
    for each in cell_values:
        for idx, item in enumerate(each):
            sheet.cell(row=i, column=idx+1, value=item)
        i += 1
    book.save('line_of_balance.xlsx')

def create_pyplot_table():
    """View the table"""
    lob_object = default_lob()
    headers = lob_object.column_headings()
    vals = lob_object.arrange_values()
    pyplot_table(headers, vals)

def create_excel_table():
    """Docstring"""
    lob_object = default_lob()
    headers = lob_object.column_headings()
    vals = lob_object.arrange_values()
    excel_table(headers, vals)
    