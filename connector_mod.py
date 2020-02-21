'''

Connector mod

Components:
 Joint auto-connector
 Auto-pad'der

 Usage:
 	import OG_MayaTools.connector_mod as conmod
	reload(conmod)
	conmod.gui()
'''

import pymel.core as pm

def getPosition(joint):
	print(joint)

def padObject(*args):
	print("padding object")

def gui():
	windowWidth = 300
	windowHeight=300
	buttonWidth = 150
	connector_window = pm.window(title="Connector Window", width=windowWidth, height=windowHeight)
	pm.columnLayout()
	pm.button(label="Pad this", width=buttonWidth,command=pm.Callback("padObject"))

	pm.showWindow(connector_window)