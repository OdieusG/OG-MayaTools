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
import sys

windowWidth = 500
windowHeight=300
buttonWidth = 150
padObject = ""

def toast(message):
    cmds.headsUpMessage(message)

def getSelected(niceName=False, dagOption=True):
	selectedItem = cmds.ls(sl=True, dag=dagOption)
	if niceName == True:
		return selectedItem[0]
	else:
		return selectedItem

def closeWindow():
	global connector_window
	pm.deleteUI(connector_window)

def selectItem(*args):
	# Break down the passed selected into
	#selItem = getSelected(False, True)
	pm.text("padObject", label=str(getSelected(True)), edit=True)

def padObject(*args):
	global appendPad
	# Get the location of the object getting padded (xform)
	initialObject  = getSelected()
	initialTranslate = cmds.xform(initialObject[0], q=True, t=True)
	initialRotate = cmds.xform(initialObject[0], q=True, ro=True)
	# Create group
	padName = str(getSelected(True))
	if appendPad.getValue() == True:
		padName = padName + "_pad"
	pm.group(em=True, n=padName)
	# Move group to location of object
	cmds.xform(padName, t=initialTranslate, ro=initialRotate)
	# Move object into group
	cmds.parent(initialObject[0], padName)
	closeWindow()

def createShape(*args):
	print("Create shapes")

def gui():
	global connector_window, appendPad
	connector_window = pm.window(title="Connector Window", width=windowWidth, height=windowHeight, sizeable=True)
	pm.columnLayout(numberOfChildren=2, columnAlign="left")
	mainTabs = pm.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

	tab_1 = pm.columnLayout(numberOfChildren=2)
	# Tab1 begin
	pm.text(label="<i>Things to work on</i>")
	pm.text(label="Autosnapper\nJoint connector\nShape maker integration", align="left")
	pm.setParent(mainTabs)
	# Tab1 end


	tab_2 = pm.scrollLayout(width=windowWidth-10, height=windowHeight-50)
	#Tab 2 begin
	pm.frameLayout(collapsable=True, label="Pad Object", width=(windowWidth-10))

	pm.rowLayout(numberOfColumns=3, columnWidth=[(1, 150), (2, 200), (3, 150)], columnAlign=[(3, 'right')])
	pm.text(label="Choose an object to pad:")
	pm.text("padObject", label="<i>nothing selected</i>")
	pm.button(label="Choose item", command=pm.Callback(selectItem))
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, columnWidth=[(1,350)])
	pm.text("Automatically append \"_pad\" to end?")
	appendPad = pm.checkBox("appendPad", value=True, label="")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=3)
	pm.text(width=150, label="")
	pm.button(label="Pad this", command=pm.Callback(padObject))
	pm.text(width=150, label="")
	pm.setParent("..")

	pm.setParent(mainTabs)
	#Tab 2 end

	tab_3 = pm.columnLayout(numberOfChildren=2, columnAlign="left")
	pm.frameLayout(label="Choose options:", width=450)
	
	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]), width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label="Choose a shape:")
	pm.optionMenu(width=100)
	pm.menuItem(label="Circle")
	pm.menuItem(label="Square")
	pm.menuItem(label="Cube")
	pm.menuItem(label="2D Arrow")
	pm.menuItem(label="3D Arrow")
	pm.menuItem(label="COG Circle")
	pm.menuItem(label="Compass")
	pm.setParent("..")
	
	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]), width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label="Enter a name.\nLeave blank for default shape name.")
	shapeName = pm.textField(placeholderText="shape")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]), width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label="Insert a suffix.\nLeave blank for default\n\"_icon\" to be added")
	shapeSuffix = pm.textField(placeholderText="_icon")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]), width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label="Shape is placed on:")
	pm.optionMenu(width=150)
	pm.menuItem(label="Origin")
	pm.menuItem(label="Currently Selected Object")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=1, columnAlign=([1, "center"]), width=450, columnWidth=([1,450]))
	pm.button(label="Create Shape", command=pm.Callback(createShape))
	pm.setParent("..")

	pm.setParent(mainTabs)
	#Tab 3 end

	pm.setParent("..")

	mainTabs.setTabLabel([tab_1, "TODO"])
	mainTabs.setTabLabel([tab_2, "Snapper"])
	mainTabs.setTabLabel([tab_3, "Shape Maker"])

	

	pm.checkBox("Automatically close window", value=True)

	pm.showWindow(connector_window)