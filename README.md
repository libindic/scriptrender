#Render module for complex script rendering 

This package is designed for sipa-flask but can also be run as a standalone
python module.

It cintains a wiki to pdf converter based on pypdflib and also a text to image
renderer based on pango ccairo.

You will need to have pango and cairo installed on your system along woth pycairo.

pycairo does not install in virtualenvs,so use you distributions package manger to 
install  py cairo or use  pip to install pycairo system wide.
