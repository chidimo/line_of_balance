# Line-of-Balance
Calculation and plotting of line of balance diagram in project management

**Known parameters - scalar**

1. Number of sections to produce, $n$
2. Buffer time
3. Desired output rate, $r$
4. Hours of work per day
5. Days of work per week

**Known parameters - sequence**
1. Activity names
2. Manhours per unit required for each activity
3. Number of men per gang for each activity

**Parameters to be calculated**

1. Theoretical gang size required to complete each activity
2. Actual gang size required for each activity.
3. Actual output rate for each activity
4. Duration to complete a unit of each activity (activity duration per unit)
5. Time from start on first section to start on last section of each activity. This could also be interpreted as the time from end of first section to end of last section
6. Time of start on first section for each activity
7. Time of end on first section for each activity
8. Time of start on last section for each activity
9. Time of end on last section for each activity

**Calculations**

The actual gang size should be a multiple (at least 2) of the number of men per gang that is closest in value to the theoretical gang size

$
\text{actual_output_rate} = \text{desired_output_rate } * \frac{\text{actual_gang_size}}{\text{theoretical_gang_size}}\\
$

$
\text{start_on_first_section_to_last_section} = \text{desired_output_rate } * \frac{(\text{number_of_sections_to_produce } - 1) * \text{ days_per_week}}{\text{actual_output_rate}}
$

$
\text{theoretical_gang_size} = \frac{\text{desired_output_rate } * \text{ man_hours_per_unit}}{\text{hours_per_day } * \text{ days_per_week}}
$

$
\text{activity_duration_per_unit} = \frac{\text{ man_hours_per_unit}}{\text{men_per_gang} * \text{ hours_per_day}}
$

**Placement of Buffer time**

When drawing the bars for the different activities, compare the values of the actual output rate for each activity to determine where to place the buffer.

If the actual output rate of the activity under consideration is smaller than that of the preceding activity (meaning that the activity in consideration is slower), place the buffer at the bottom of the graph, by adding it to the value of the time to finish last section of the preceding activity.

Activity|man_hours_per_unit|men_per_gang|theoretical_gang_size|actual_gang_size|actual_output_rate|activity_duration_per_unit|start_on_first_section_to_last_section|start_on_first_section|end_on_first_section|start_on_last_section|end_on_last_section
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
1|2|3|4|5|6|7|8|9|10|11|12
