"""API"""

# pylint: disable-msg=C0103

from .lob import LineOfBalance
from .utils import get_int_list, get_names_list

def plot_curve():
    """Generate curve for user input

    Returns
    --------
    Line of Balance object
    """
    with open("input.txt", "r") as input_handle:
        input_values = input_handle.readlines()

    activity_names = input_values[0].split('=')[1].strip()
    man_hours_per_unit = input_values[1].split('=')[1].strip()
    men_per_gang = input_values[2].split('=')[1].strip()


    buffer_time = int(input_values[3].split('=')[1].strip())
    productivity_rate = int(input_values[4].split('=')[1].strip())
    number_of_units_to_produce = int(input_values[5].split('=')[1].strip())
    hours_per_day = int(input_values[6].split('=')[1].strip())
    days_per_week = int(input_values[7].split('=')[1].strip())

    activity_names = get_names_list(activity_names)
    man_hours_per_unit = get_int_list(man_hours_per_unit)
    men_per_gang = get_int_list(men_per_gang)

    line_object = LineOfBalance(activity_names,
                                man_hours_per_unit,
                                men_per_gang,
                                buffer_time,
                                productivity_rate,
                                number_of_units_to_produce,
                                hours_per_day,
                                days_per_week)
    line_object.create_table()
    line_object.generate_curve()
    return line_object

if __name__ == "__main__":
    plot_curve()
