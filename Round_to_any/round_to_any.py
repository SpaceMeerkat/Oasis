#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 10:33:09 2019

@author: SpaceMeerkat
"""
#=============================================================================#
#///   IMPORT RELEVANT PACKAGES   ////////////////////////////////////////////#
#=============================================================================#

import numpy as np 

#=============================================================================#
#///   DEFINE THE ROUNDING CLASS   ///////////////////////////////////////////#
#=============================================================================#

class round_to_any:
        
        """ A class to round a single number to any interval element in a given
        start stop range. Users should pass the following elements to the 
        class:
                
                data: The number you wish to round
                start: Start number of an interval range
                stop: Final number of an interval range
                interval: The step-size between values in the interval range
        """
        
        def __init__(self,data,start,stop,interval):
                self.data = data
                self.start = start
                self.stop = stop
                self.interval = interval
                
                
        def interval_array(self):
                
                """ Defines the interval array into which the user wishes to 
                round their input data """
                
                _array = np.arange(self.start,self.stop,self.interval)
                return _array
        
        
        def round_data(self,decimals=None):
                
                """ Rounds the input data to the nearest element in the 
                interval array. If 'decimals' is passed, the output will be 
                rounded to the number of decimals provided """
                
                _array = self.interval_array()
                _diff = np.abs(_array-self.data)
                _rounded = _array[_diff.argmin()]
                if decimals is not None:
                        _rounded = np.around(_rounded,decimals=decimals)
                return _rounded
        
#=============================================================================#
#///   END OF SCRIPT   ///////////////////////////////////////////////////////#
#=============================================================================# 
                             
