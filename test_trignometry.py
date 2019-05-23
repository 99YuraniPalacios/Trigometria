#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test battery for Trigonometry package

Created on Thu Feb 28 13:26:45 2019

@author: jzuluaga
"""
import trigonometry as trig
import unittest

class Test(unittest.TestCase):

    def test_sin_between_one_and_minus_one(self):
        theta=trig.Angle(150.0,trig.Unit.DEG)
        if abs(trig.Sin(theta))>1:
            raise AssertionError("Trig. function is larger than 1")

    def test_sin_between_one_and_minus_one_2(self):
        theta=trig.Angle(150.0,trig.Unit.DEG)
        assert abs(trig.Sin(theta))<=1

    def test_sin_between_one_and_minus_one_3(self):
        theta=trig.Angle(150.0,trig.Unit.DEG)
        self.assertTrue(abs(trig.Sin(theta))<=1)

    """
    def test_sin_90(self):
        theta=trig.Angle(90.0,trig.Unit.DEG)
        self.assertEqual(trig.Sin(theta),1)
    """

    def test_sin_90(self):
        theta=trig.Angle(90.0,trig.Unit.DEG)
        self.assertTrue(abs(trig.Sin(theta)-1)<1e-5)

if __name__=="__main__":
    unittest.main()
    