Line of Balance
=====================


Calculations and plotting of line of balance curve as taught by Dr. Ibrahim Odeh on `coursera <https://www.coursera.org/>`_.

`Course page <https://www.coursera.org/learn/construction-scheduling/home/welcome>`_

Usage
================

1. `Download and install anaconda <https://www.continuum.io/downloads>`_ It comes at about 400MB so you might want to use a wifi connection.

2. After installation, go to start menu (windows), locate anaconda folder. Open anaconda prompt.

3. Install with ::

    pip install https://github.com/Parousiaic/line_of_balance/archive/master.zip
    
    
Create a virtual environment if you need to.

Generate the curve
++++++++++++++++++++++++

All steps are shown in this `video <https://www.youtube.com/watch?v=wNPupUVxNUo&feature=youtu.be>`_

1. Open the included "input.txt" file
2. Edit the entries on the right hand side of the equal sign ("=") for the given parameters. An "input.jpg" file has been included to show the format in which the program expects inputs. Please preserve the order and format of the inputs.
3. Type **python main.py** and click enter. A window pops up to show you what the plot looks like.
4. Check the output folder for the generated plot in png and pdf formats and the excel table for the calculations
5. The line of object is also returned for those who actually want to use it.


Disclaimer
-----------
This is just an experimental project. The results turned out very well for two data sets I have tried it on so far. In the event that it gives results which differ from that which you obtained by working on your own, the safest bet is that your result is the correct one, unless you have very good reasons to doubt your work.


License
-----------

I don't really get the idea about licenses, but I do want this to be used freely, with acknowledgement

Course Reminders
======================

Github doesn't render mathjax by default so you won't be able to see the mathematical equations if I included them in this readme. I have instead included a "readme.html" file which you can open in your browser on your computer.

You may also use view the same equations in the accompanying "readme.ipynb" jupyter notebook.

Known parameters - scalars
-----------------------------

1. Number of sections to produce
2. Buffer time
3. Desired output rate
4. Hours of work per day
5. Days of work per week

Known parameters - sequences
------------------------------

1. Activity names
2. Manhours per unit required for each activity
3. Number of men per gang for each activity

Parameters to be calculated
------------------------------

1. Theoretical gang size required to complete each activity
2. Actual gang size required for each activity.
3. Actual output rate for each activity
4. Duration to complete a unit of each activity (activity duration per unit)
5. Time from start on first section to start on last section of each activity. This could also be interpreted as the time from end of first section to end of last section
6. Time of start on first section for each activity
7. Time of end on first section for each activity
8. Time of start on last section for each activity
9. Time of end on last section for each activity
