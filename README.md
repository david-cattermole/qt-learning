# Qt Learning
User Interfaces written with the Qt framework using various techniques as a journey of self-discovery and to learn the best practices of working with Qt.

This project can be considered a constant work in progress, it is used for experimentation and testing with no functional goal in sight; only the goal of learning.

Take a look at the various [window screenshots](https://github.com/david-cattermole/qt-learning/blob/master/docs/windows.md).

# Installation

Dependencies:
- Qt4
- Python 2.7.x
- PyQt4 or PySide
- [Qt.py 0.6.9](https://github.com/mottosso/Qt.py/releases/tag/0.6.9)

Optional Dependencies:
- Autodesk Maya

To install, run this:
```commandline
$ cd <project root> 

$ su
# Enter password here.

$ python setup.py install
``` 

Or, if you have virtualenv installed:
```commandline
$ cd <project root> 

$ mkdir virtenv

$ virtualenv virtenv

$ virtenv/bin

$ source activate

$ cd ../..

$ pip install Qt.py

$ pip install python-pyqt5

# Optional, required for running tests only.
$ pip install coverage

$ python setup.py install

# Use package as needed.

# Clean up when you're done.
$ deactivate
``` 

# Usage and Testing

Here is an example usage:
```commandline
$ python runStandalone.py
```

Or if you'd like to use the widgets inside your own UIs, try this:
```python
# do stuff here
```

To open all the UIs in this project for testing, run the following command:
```commandline
$ python runStandalone.py
```


# Development

## Convention

- PEP8 Python convention for code.
- All UIs are first created in Qt Designer.
- UIs are always saved into ./ui directory.  

## Design

- All UI pieces must be re-usable 
