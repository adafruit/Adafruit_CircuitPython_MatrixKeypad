# SPDX-FileCopyrightText: 2018 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_matrixkeypad`
====================================================

CircuitPython library for matrix keypads

* Author(s): ladyada

Implementation Notes
--------------------

**Hardware:**

* Flexible 3x4 Matrix Keypad <https://www.adafruit.com/product/419>
* Phone-style 3x4 Matrix Keypad <https://www.adafruit.com/product/1824>

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

# imports
from digitalio import Direction, Pull

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_MatrixKeypad.git"


class Matrix_Keypad:
    """Driver for passive matrix keypads - any size"""

    def __init__(self, row_pins, col_pins, keys):
        """Initialise the driver with the correct size and key list.

        :param list row_pins: a list of DigitalInOut objects corresponding to the rows
        :param list col_pins: a list of DigitalInOut objects corresponding to the colums
        :param list keys: a list of lists that has the corresponding symbols for each key
        """
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
        """An array containing all detected keys that are pressed from the initalized
        list-of-lists passed in during creation"""
        # make a list of all the keys that are detected
        pressed = []

        # set all pins pins to be inputs w/pullups
        for pin in self.row_pins + self.col_pins:
            pin.direction = Direction.INPUT
            pin.pull = Pull.UP

        for row, row_pin in enumerate(self.row_pins):
            # set one row low at a time
            row_pin.direction = Direction.OUTPUT
            row_pin.value = False
            # check the column pins, which ones are pulled down
            for col, val in enumerate(self.col_pins):
                if not val.value:
                    pressed.append(self.keys[row][col])
            # reset the pin to be an input
            row_pin.direction = Direction.INPUT
            row_pin.pull = Pull.UP
        return pressed
