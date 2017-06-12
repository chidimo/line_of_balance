"""Line of Balance"""
from line_of_balance_plotter import generate_multiple_plots
import matplotlib.pyplot as plt

class LineOfBalance(object):
    """LINE OF BALANCE"""

    def __init__(self,
                 activity_names,
                 man_hours_per_unit,
                 men_per_gang,
                 buffer_time,
                 productivity_rate,
                 number_of_units_to_produce,
                 hours_per_day,
                 days_per_week):

        """Create LineOfBalance() object"""
        self.activity_names = activity_names
        self.man_hours_per_unit = man_hours_per_unit
        self.men_per_gang = men_per_gang
        self.buffer_time = buffer_time
        self.productivity_rate = productivity_rate
        self.number_of_units_to_produce = number_of_units_to_produce
        self.hours_per_day = hours_per_day
        self.days_per_week = days_per_week
        self.number_of_activities = len(self.activity_names)

    def theoretical_gang_size(self):
        """Theoretical gang size"""
        return [(self.productivity_rate*each) /
                (self.hours_per_day*self.days_per_week)
                for each in self.man_hours_per_unit]

    def actual_gang_size(self):
        """Actual gang size"""
        actual_gang_size = [2 * x for x in self.men_per_gang]

        for idx, item in enumerate(actual_gang_size):
            old_gang_size = item

            for j in range(3, 6):
                new_gang_size = j * self.men_per_gang[idx]

                if abs(old_gang_size - self.theoretical_gang_size()[idx]) >=\
                abs(new_gang_size - self.theoretical_gang_size()[idx]):
                    old_gang_size = new_gang_size

            actual_gang_size[idx] = old_gang_size
        return actual_gang_size

    def actual_output_rate(self):
        """Actual output rate"""
        return [self.productivity_rate * (x/y)
                for x, y in zip(self.actual_gang_size(),
                                self.theoretical_gang_size())]

    def activity_duration_per_unit(self):
        """Actual duration per unit"""
        return [mhpu / (mpg * self.hours_per_day)
                for  mhpu, mpg in zip(self.man_hours_per_unit, self.men_per_gang)]

    def start_first_to_start_last(self):
        """Docstring"""
        return [(self.number_of_units_to_produce - 1) * self.days_per_week /
                each for each in self.actual_output_rate()]

    def start_end(self):
        """First section start and end"""
        start_first = [1]
        end_first = [self.activity_duration_per_unit()[0]]

        start_last = [self.start_first_to_start_last()[0]]
        end_last = [start_last[0] + end_first[0]]

        for i in range(1, self.number_of_activities):
            if self.actual_output_rate()[i] < self.actual_output_rate()[i-1]:
                # place buffer on bottom
                start_first.insert(i, end_first[i-1] + self.buffer_time)
                end_first.insert(i, start_first[i] + self.activity_duration_per_unit()[i])

                start_last.insert(i, start_first[i] +\
                self.start_first_to_start_last()[i])
                end_last.insert(i, start_last[i] + self.activity_duration_per_unit()[i])

            elif self.actual_output_rate()[i] > self.actual_output_rate()[i-1]:
                # place buffer at bottom
                start_last.insert(i, end_last[i-1] + self.buffer_time)
                end_last.insert(i, start_last[i] + self.activity_duration_per_unit()[i])

                start_first.insert(i, start_last[i] - \
                self.start_first_to_start_last()[i])
                end_first.insert(i, start_first[i] + self.activity_duration_per_unit()[i])
        return start_first, end_first, start_last, end_last

    def start_on_first_section(self):
        """Start on first section for activity"""
        return self.start_end()[0]

    def end_on_first_section(self):
        """End on first section for activity"""
        return self.start_end()[1]

    def start_on_last_section(self):
        """Start on last section for activity"""
        return self.start_end()[2]

    def end_on_last_section(self):
        """End on last section for activity"""
        return self.start_end()[3]

    def arrange_values(self):
        """Arrange the values in tabular format"""

        values = [[a, b, c, d, e, f, g, h, i, j, k, l]
                  for a, b, c, d, e, f, g, h, i, j, k, l in
                  zip(self.activity_names,
                      self.man_hours_per_unit,
                      self.men_per_gang,
                      self.theoretical_gang_size(),
                      self.actual_gang_size(),
                      self.actual_output_rate(),
                      self.activity_duration_per_unit(),
                      self.start_first_to_start_last(),
                      self.start_on_first_section(),
                      self.end_on_first_section(),
                      self.start_on_last_section(),
                      self.end_on_last_section())]
        return values

    def column_headings(self):
        """Column headings"""
        columns = ("Activity",
                   "Man hours per unit",
                   "Men per gang",
                   "Theoretical gang size",
                   "Actual gang size",
                   "Actual output rate",
                   "Activity duration per unit",
                   "Start on first section to start on last section",
                   "Start on first section",
                   "End on first section",
                   "Start on last section",
                   "End on last section")
        return columns

    def generate_plot_points(self):
        """Generate plot points"""
        # start_first = self.start_on_first_section()
        # end_first = self.end_on_first_section()
        # start_last = self.start_on_last_section()
        # end_last = self.end_on_last_section()

        return [(a, b, c, d) for a, b, c, d in
                zip(self.start_on_first_section(),
                    self.end_on_first_section(),
                    self.start_on_last_section(),
                    self.end_on_last_section())]

    def generate_diagram(self):
        """Generate the line of balance diagram"""
        points_to_plot = self.generate_plot_points()
        generate_multiple_plots(points_to_plot)

def default_lob():
    """Main with default arguments"""
    activity_names = ['A', 'B', 'C', 'D', 'E']
    man_hours_per_unit = [100, 350, 60, 200, 150]
    men_per_gang = [4, 6, 2, 5, 8]
    buffer_time = 5
    productivity_rate = 3
    number_of_units_to_produce = 20
    hours_per_day = 8
    days_per_week = 5

    return LineOfBalance(activity_names,
                         man_hours_per_unit,
                         men_per_gang,
                         buffer_time,
                         productivity_rate,
                         number_of_units_to_produce,
                         hours_per_day,
                         days_per_week)

def default_diagram():
    """Generate default diagram"""
    lob = default_lob()
    lob.generate_diagram()
