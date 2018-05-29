# The MIT License (MIT)
#
# Copyright (c) 2018 ladyada for adafruit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_MatrixKeypad`
====================================================

.. todo:: Describe what the module does

* Author(s): ladyada

Implementation Notes
--------------------

**Hardware:**

.. todo:: Add links to any specific hardware product page(s), or category page(s). Use unordered list & hyperlink rST
   inline format: "* `Link Text <url>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
  
.. todo:: Uncomment or remove the Bus Device and/or the Register library dependencies based on the library's use of either.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports
import time
from digitalio import DigitalInOut, Direction, Pull
from micropython import const


__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_MatrixKeypad.git"

class Matrix_Keypad(object):
    def __init__(self, row_pins, col_pins, keys):
        if len(keys) != len(row_pins):
            raise RuntimeError("Key name matrix doesn't match # of colums")
        for row in keys:
            if len(row) != len(col_pins):
                raise RuntimeError("Key name matrix doesn't match # of rows")
        self.row_pins = row_pins
        self.col_pins = col_pins
        self.keys = keys

    @property
    def pressed_keys(self):

        # make a list of all the keys that are detected
        pressed = []
        
        # set all pins pins to be inputs w/pullups
        for pin in self.row_pins+self.col_pins:
            pin.direction = Direction.INPUT
            pin.pull = Pull.UP

        for row in range(len(self.row_pins)):
            # set one row low at a time
            self.row_pins[row].direction = Direction.OUTPUT
            self.row_pins[row].value = False
            # check the column pins, which ones are pulled down
            for col in range(len(self.col_pins)):
                if not self.col_pins[col].value:
                    pressed.append(self.keys[row][col])
            # reset the pin to be an input
            self.row_pins[row].direction = Direction.INPUT
            self.row_pins[row].pull = Pull.UP
        return pressed
