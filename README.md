#Render module for complex script rendering

This package is designed for [Silpa-Flask](https://github.com/libindic/Silpa-Flask)
but can also be run as a standalone python module.

It contains a wiki to pdf converter based on pypdflib and also a text to image
renderer based on pango cairo.

You will need to have pango and cairo installed on your system along with
pycairo. You will probably have them if you have pygtk on  your system.

pycairo does not install in virtualenvs,so use your distributions package manger
to install pycairo or use pip to install pycairo system wide. Also try
installing pygtk if you can't find pycairo or pango in your distributions
repositories.

pycairo does not install in virtualenvs,so use you distributions package manger to
install  pycairo or use  pip to install pycairo system wide. Also try
installing pygtk if you can't find pycairo or pango in your distributions
repositories.

Run tests with `python tests/render_test.py`

You can find the documentaion [here](http://render.readthedocs.org/en/latest/).

## Dependencies for development
Scriptrender requires certain packages to be installed on your system for
development.

**On Ubuntu**

```shell
sudo apt-get install libxml-dev libxslt-dev python-dev build-essential libz-dev libjpeg-dev libpango1.0-dev pythongtk2-dev
```

If you are using a virtualenv, initialise virtualenv with the
`--system-site-packages` option to use pycairo, pango and cairo
