Line of Balance
=====================


Calculations and plotting of line of balance curve as taught by Dr. Ibrahim Odeh on `coursera <https://www.coursera.org/>`_.

`Course page <https://www.coursera.org/learn/construction-scheduling/home/welcome>`_


Usage
----------

1. Download and install `anaconda <https://www.continuum.io/downloads>`_ It comes at about 400MB so you might want to use a wifi connection.

2. After installation, go to start menu (windows), locate anaconda folder. Open anaconda prompt.

3. Install with ::

    pip install https://github.com/Parousiaic/line_of_balance/archive/master.zip
    
    
Optional Step
+++++++++++++++++
Creating a virtual environment



Generate the curve
++++++++++++++++++++

All steps are shown in this ...

1. Open the included "input.txt" file

2. Edit the entries on the right hand side of the equal sign ("=") for the given parameters. An "input.jpg" file has been included to show the format in which the program expects inputs. Please preserve the order and format of the inputs.



Disclaimer
-----------
This is just an experimental project. The results turned out very well for two data sets I have tried it on so far. In the event that it gives results which differ from that which you obtained by working on your own, the safest bet is that your result is the correct one, unless you have very good reasons to doubt your work.


License
------------

I don't really get the idea about licenses, but I do want this to be used freely, with acknowledgement

Code
-------

.. automodule :: line_of_balance.api
   :members:

.. automodule :: line_of_balance.illustrate
.. autoclass :: LineOfBalance
   :members:

.. automodule :: line_of_balance.lob
   :members:

.. automodule :: line_of_balance.utils
   :members:
