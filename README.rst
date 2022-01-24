Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-matrixkeypad/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/matrixkeypad/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_MatrixKeypad/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_MatrixKeypad/actions/
    :alt: Build Status

This simple helper library lets you create objects that will scan and detect keypresses on passive matrix keypads

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-matrixkeypad/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-matrixkeypad

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-matrixkeypad

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-matrixkeypad

Usage Example
=============

.. code-block:: python

	import adafruit_matrixkeypad
	from digitalio import DigitalInOut
	import board

	# Classic 3x4 matrix keypad
	cols = [DigitalInOut(x) for x in (board.D2, board.D0, board.D4)]
	rows = [DigitalInOut(x) for x in (board.D1, board.D6, board.D5, board.D3)]
	keys = ((1, 2, 3),
		(4, 5, 6),
		(7, 8, 9),
		('*', 0, '#'))

	keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

	while True:
	    keys = keypad.pressed_keys
	    if keys:
		print("Pressed: ", keys)
	    time.sleep(0.1)


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/matrixkeypad/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/adafruit_CircuitPython_MatrixKeypad/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
