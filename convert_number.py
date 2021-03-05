# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 20:09:16 2021

@author: tob10
"""

import doctest

def test_for_integer_argument(f):
    def dekorator_function(*args):
        for value in args:
            if type(value) != int:
                print("Expected an integer value.")
                return -1
        return f(*args)
    return dekorator_function

units = ['null', 'eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun']
teens = ['elf', 'zwölf', 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn']
tens = ['einhundert', 'zehn', 'zwanzig', 'dreißig', 'vierzig', 'fünfzig', 'sechzig', 'siebzig', 'achtzig', 'neunzig']

@test_for_integer_argument
def convert(number):
    """
    Convert numbers to words.
    
    Parameters
    ----------
    number : integer
        
    Returns
    -------
    string
        
    >>> convert(5)
    'fünf'
    >>> convert(17)
    'siebzehn'
    >>> convert(42)
    'zweiundvierzig'
    >>> convert(-1)
    Traceback (most recent call last):
    ValueError: Expected an integer number between 0 and 100.
    """
    if number < 0 or number > 100:
        raise ValueError("Expected an integer number between 0 and 100.")
    
    if number == 100:
        return tens[0]
    elif 10 < number < 20:
        return teens[number % 10 - 1]
    elif number < 10:
        return units[number]
    elif number % 10 == 0:
        return tens[number // 10]
    else:
        return units[number % 10] + 'und' + tens[number // 10]

if __name__ == "__main__":
    doctest.testmod()