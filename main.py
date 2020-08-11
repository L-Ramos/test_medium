# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:47:09 2020

@author: laramos
"""

import numpy as np

def compute_bmi_cm(weight,height):
    height = height/100
    
    bmi = weight/(height**2)
    
    return bmi


weight = 65
height = 176
print(compute_bmi(weight,height))



    

