#Render module for complex script rendering 

This package is designed for sipa-flask but can also be run as a standalone
python module.

It contains a wiki to pdf converter based on pypdflib and also a text to image
renderer based on pango cairo.

You will need to have pango and cairo installed on your system along with pycairo.
You will probably have them if you have pygtk on  your system.

pycairo does not install in virtualenvs,so use you distributions package manger to 
install  pycairo or use  pip to install pycairo system wide. Also try
installing pygtk if you can't find pycairo or pango in your distributions
repositories.

Run tests with ```python setup.py test```

You can find the documentaion [here](http://render.readthedocs.org/en/latest/).
