from datetime import date


class Employee:
    """Employee class"""

    # Constructor
    def __init__(self, lname, fname):
        self.last_name = lname
        self.first_name = fname

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    def display(self):
        return "{}, {}".format(self.last_name, self.first_name)
