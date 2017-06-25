# Line-of-Balance
Calculations and plotting of line of balance curve as taught by Dr. Ibrahim Odeh on coursera.

[`Course page is here`](https://www.coursera.org/learn/construction-scheduling/home/welcome)

# How to use

## First step
1. Download this project as a zip file from github. Here is a direct [`link`](https://github.com/Parousiaic/Line-of-Balance/archive/master.zip)
2. Extract the contents of the zip file using either 7zip or winrar or whatever archiver of your choice.

### Follow these instructions if you do not have python, numpy and matplotlib installed
We will use the anaconda package to make life easier.
1. [`Download and install anaconda from here`](https://www.continuum.io/downloads). It comes at about 400MB so you might want to use a wifi connection.
2. Open command.exe and navigate to the root Line-of-balance folder; same folder where you have "main.py" file. A shortcut to do this is to navigate into the root Line-of-balance folder using windows explorer, then, hold down shift, and right click your mouse in a blank space. In the context menu you'll see "Open command window here". Click on it.

### You're now ready for the steps to generate the curve.
1. Open the included "input.txt" file
2. Edit the entries on the right hand side of the equal sign ("=") for the given parameters. An "input.jpg" file has been included to show the format in which the program expects inputs. Please preserve the order and format of the inputs.
3. Type **python main.py** and click enter. A window pops up to show you what the plot looks like.
4. Check the output folder for the generated plot in png and pdf formats and the excel table for the calculations
5. The line of object is also returned for those who actually want to use it.
6. Remember, this is just an experimental project. The results turned out very well for two data sets I have tried it on so far. In the event that it gives results which differ from that which you obtained by working on your own, the safest bet is that your result is the correct one.


**License**
I don't really get the idea about licenses, but I do want this to be used freely, with acknowledgement

## Course Reminders

Github doesn't render mathjax by default so you won't be able to see the mathematical equations if I included them in this readme. I have instead included a "readme.html" file which you can open in your browser on your computer.

You may also use view the same equations in the accompanying "readme.ipynb" jupyter notebook.

### Known parameters - scalars

1. Number of sections to produce
2. Buffer time
3. Desired output rate
4. Hours of work per day
5. Days of work per week

### Known parameters - sequences
1. Activity names
2. Manhours per unit required for each activity
3. Number of men per gang for each activity

### Parameters to be calculated

1. Theoretical gang size required to complete each activity
2. Actual gang size required for each activity.
3. Actual output rate for each activity
4. Duration to complete a unit of each activity (activity duration per unit)
5. Time from start on first section to start on last section of each activity. This could also be interpreted as the time from end of first section to end of last section
6. Time of start on first section for each activity
7. Time of end on first section for each activity
8. Time of start on last section for each activity
9. Time of end on last section for each activity
