'''
Converter for MELScript to Pyton via window
'''
import pymel.core as pm
import string
import pymel.tools.mel2py as mel2py

def gui():
    conversionWindow = pm.window(title="Converter Window")
    pm.columnLayout()
