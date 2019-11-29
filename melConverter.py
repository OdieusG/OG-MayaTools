'''
Converter for MELScript to Pyton via window


Usage:

import OG_MayaTools.melConverter as melConvert
reload(melConvert)
melConvert.gui()

'''
import pymel.core as pm
import string
import pymel.tools.mel2py as mel2py

def gui():
    conversionWindow = pm.window(title="Converter Window")
    pm.columnLayout()
    pm.text(label="MEL Script To Convert:")
    melText = pm.textField(placeholderText="Insert Text Here")

