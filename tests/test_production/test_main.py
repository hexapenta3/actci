#%  usr/bin/env python
#%  -- coding: utf-8 --

"""
Test for main.py
"""


from actci.production import main


def test_main():
    """ test for main.py
    """
    numbers = main.get_numbers()
    print(numbers)
    assert numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]


