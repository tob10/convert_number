# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:37:40 2021

@author: tob10
"""

import unittest
import convert_number

class convert_numberTest (unittest.TestCase):
    
    def setUp (self):
        self.elements = ((0,'null'), (5,'fünf'), (10,'zehn'), (17,'siebzehn'),
                         (20,'zwanzig'), (42,'zweiundvierzig'), 
                         (99,'neunundneunzig'), (100,'einhundert'))
        
    def testConvert (self):
        for (num, word) in self.elements:
            self.assertEqual(convert_number.convert(num), word)
        
    def testException (self):
        self.assertRaises(ValueError, convert_number.convert, -1)
        
    def tearDown (self):
        self.elements = None
        
        
if __name__ == "__main__":
    unittest.main()