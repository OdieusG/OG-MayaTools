'''
Converter for MELScript to Pyton via window


Usage:

import OG_MayaTools.melConverter as melConvert
reload(melConvert)
melConvert.gui()

test string:
curve -d 1 -p -0.5 0 0 -p 0 0 -0.5 -p 0 0 -0.25 -p 0.5 0 -0.25 -p 0.5 -4.47035e-08 -4.47035e-08 -p 0.5 0.25 0 -p 0 0.25 0 -p 0 0.5 0 -p -0.5 0 0 -p 0 0 0.5 -p 0 0 0.25 -p 0.5 0 0.25 -p 0.5 -4.47035e-08 -4.47035e-08 -p 0.5 -0.25 0 -p 0 -0.25 0 -p 0 -0.5 0 -p -0.5 0 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 ;

'''
import pymel.core as pm
import string
import pymel.tools.mel2py as mel2py


def processSyntax(*args):
    melString = melText.getText();
    convertedString =  mel2py.mel2pyStr(melString)
    pythonCollected.setText(convertedString)


def gui():
    global melText, pythonCollected
    guiWidth = 300
    guiHeight = 300
    spacer=10
    conversionWindow = pm.window(title="Converter Window", width=guiWidth, height=guiHeight)
    pm.columnLayout(columnAlign="center")
    pm.text(label="MEL Script To Convert:")
    melText = pm.scrollField(wordWrap=True, width=guiWidth)
    pm.separator(style="doubleDash")
    pm.text(label="Converted text:")
    pythonCollected = pm.scrollField(wordWrap=True, width=guiWidth)
    pm.button(label="Convert", command=processSyntax)

    pm.showWindow(conversionWindow)