# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:27:14 2016

@author: mayou

Main routine to run the analysis
"""

from raredecay.tools.dev_tool import play_sound
from raredecay.analysis.physical_analysis import run
from matplotlib.pyplot import show
import cProfile as profile
print "starting main"

run(1)
play_sound()
show()