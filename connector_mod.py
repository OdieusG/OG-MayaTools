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
import maya.cmds as cmds

windowWidth = 500
windowHeight=300
buttonWidth = 150
padObject = ""

def getSelected(dag=True):
	if dag==True:
		selectedItem=cmds.ls(sl=True, dag=True)
	else:
		selectedItem=cmds.ls(sl=True)
	return selectedItem

def closeWindow():
	pm.deleteUI(connector_window)

def selectItem(*args):
	padObject.setValue("test")

def padObject(*args):
	# Get the location of the object getting padded (xform)
	initialObject  = getSelected()
	initialTranslate = cmds.xform(initialObject[0], q=True, t=True)
	initialRotate = cmds.xform(initialObject[0], q=True, ro=True)
	print("Translate: " + str(initialTranslate) + "\nRotate: " + str(initialRotate))
	# Create group
	pm.group(em=True, n="newGroup")
	# Move group to location of object
	cmds.xform("newGroup", t=initialTranslate, ro=initialRotate)
	# Move object into group
	cmds.parent(initialObject[0], "newGroup")
	closeWindow()

def gui():
	connector_window = pm.window(title="Connector Window", width=windowWidth, height=windowHeight, sizeable=False)
	pm.scrollLayout()
	pm.frameLayout(collapsable=True, label="Pad Object", width=(windowWidth-10))
	pm.rowLayout(numberOfColumns=3, columnWidth=[(1, 150), (2, 200), (3, 150)], columnAlign=[(3, 'right')])
	pm.text(label="Choose an object to pad:")
	padObject = pm.text(label="<i>nothing selected</i>")
	pm.button(label="Choose item", command=pm.Callback(selectItem(padObject)))
	pm.setParent("..")
	pm.columnLayout()
	pm.button(label="Pad this", command=pm.Callback(padObject))
	pm.setParent("..")
	pm.checkBox("Automatically close window", value=True)

	pm.showWindow(connector_window)