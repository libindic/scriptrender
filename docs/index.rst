.. render documentation master file, created by
   sphinx-quickstart on Tue Sep 17 01:53:46 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

``render`` - a complex script rendering utility based on pangocairo
====================================================================

This is an experimental python package for generating renderings of complex
scripts. This is based on pypdflib and pangocairo.

The module currently has two functions 

* a wiki to pdf generater 
* a complex script renderer

Installation
-----------

You will need to have pango and cairo installed on your system along with pycairo.
You will probably have them if you have pygtk on  your system.

pycairo does not install in virtualenvs,so use you distributions package manger to 
install  pycairo or use  pip to install pycairo system wide.

API reference
--------------

.. automodule:: render.core
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

