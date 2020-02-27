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

backColor_gray = [.5, .5, .5]
debugMode=False
windowWidth = 520
windowHeight=350
buttonWidth = 150
keepAliveCheck = ""
windowKeepAlive=True
__green__ = 14
__red__ = 13
__blue__ = 6

if debugMode == True:
	phrases =  {
	"general_chooseJoint":"",
	"pad_chooseObjectText":"",
	"pad_chooseObjectBtn":"",
	"pad_append":"",
	"pad_button":"",
	"shapes_defaultShapeText":"",
	"shapes_defaultControlText":"",
	"shapes_chooseShape":"",
	"shapes_shapeName":"",
	"shapes_shapeSuffix":"",
	"shapes_placedOn":"",
	"shapes_button":"",
	"fkik_selectRootText":"",
	"fkik_selectEndText":"",
	"fkik_selectRootButton":"",
	"fkik_selectEndButton":"",
	"fkik_createControlsText":"",
	"fkik_createHierarchyText":"",
	"fkik_connectControlsText":"",
	"main_autocloseWindow":"",
	}
else:
	phrases =  {
	"general_chooseJoint":"Choose joint",
	"pad_chooseObjectText":"Choose an object to pad",
	"pad_chooseObjectBtn":"Choose Item",
	"pad_append":"Automatically append \"pad\" to end?",
	"pad_button":"Pad this",
	"shapes_defaultShapeText":"shape",
	"shapes_defaultControlText":"icon",
	"shapes_chooseShape":"Choose a shape",
	"shapes_shapeName":"Enter a name.\nLeave blank for default shape name.",
	"shapes_shapeSuffix":"Insert a suffix.\nLeave blank for default\n\"icon\" to be added",
	"shapes_placedOn":"Shape is placed on:",
	"shapes_button":"Create Shape",
	"fkik_selectRootText":"Select the root joint",
	"fkik_selectEndText":"Select the end joint\n(for IK creation)",
	"fkik_selectRootButton":"Select root",
	"fkik_selectEndButton":"Select end",
	"fkik_selectHandButton":"Select hand Joint",
	"fkik_createControl":"Create control on hand?",
	"fkik_createControlsText":"Create controls on respective joints?",
	"fkik_createHierarchyText":"Create controls in hierarchy?",
	"fkik_connectControlsText":"Connect controls on respective joints?",
	"main_autocloseWindow":"Automatically close window after operation",
	}


def toast(message):
    cmds.headsUpMessage(message)

def getSelected(niceName=False, dagOption=True):
	selectedItem = cmds.ls(sl=True, dag=dagOption)
	if niceName == True:
		return selectedItem[0]
	else:
		return selectedItem

def closeWindow():
	global connector_window, windowKeepAlive
	if windowKeepAlive==True:
		pm.deleteUI(connector_window)

def selectItem(*args):
	txt_jointField.setText(getSelected(True))

def autocloseWindowToggle(*args):
	windowKeepAlive = chk_keepAlive.getValue()

def wnd_rowTODO():
	pm.frameLayout(collapsable=False, label="TODO", width=500)

	pm.columnLayout(numberOfChildren=2, backgroundColor=backColor_gray)
	pm.text(label="<i>Things to work on</i>")
	todoList = "+Autosnapper\n"
	todoList = todoList + "+Joint connector\n"
	todoList = todoList + "+Shape maker integration\n"
	todoList = todoList + "-Joint orient tool\n"
	todoList = todoList + ""
	pm.text(label=todoList, align="left")
	pm.setParent("..")

	pm.setParent("..")
	
def wnd_rowPad():
	global txt_jointField, chk_appendPad
	pm.frameLayout(collapsable=True, label="Pad Object", width=500)

	pm.rowLayout(numberOfColumns=3, columnWidth=[(1, 150), (2, 200), (3, 100)])
	pm.text(label=phrases['pad_chooseObjectText'])
	txt_jointField = pm.textField(placeholderText=phrases['general_chooseJoint'], editable=False)
	pm.button(label=phrases['pad_chooseObjectBtn'], command=pm.Callback(selectItem))
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, columnWidth=[(1,350)])
	pm.text(phrases['pad_append'])
	chk_appendPad = pm.checkBox("appendPad", value=True, label="")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=3)
	pm.text(width=150, label="")
	pm.button(label=phrases['pad_append'], command=pm.Callback(padObject))
	pm.text(width=150, label="")
	pm.setParent("..")

	pm.setParent("..")

def padObject(*args):
	global chk_appendPad
	# Get the location of the object getting padded (xform)
	initialObject  = getSelected()
	initialTranslate = cmds.xform(initialObject[0], q=True, t=True)
	initialRotate = cmds.xform(initialObject[0], q=True, ro=True)
	# Create group
	padName = str(getSelected(True))
	if chk_appendPad.getValue() == True:
		padName = padName + "_pad"
	pm.group(em=True, n=padName)
	# Move group to location of object
	cmds.xform(padName, t=initialTranslate, ro=initialRotate)
	# Move object into group
	cmds.parent(initialObject[0], padName)
	#toast(windowKeepAlive.getValue)
	#if windowKeepAlive.getValue
	closeWindow()

def wnd_rowShapes():
	global opt_shapeOptions, txt_shapeName, txt_shapeSuffix
	global opt_placementOption
	pm.frameLayout(label="Shape Maker", width=500, collapsable=True)
	
	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]),
		width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label=phrases['shapes_chooseShape'])
	opt_shapeOptions = pm.optionMenu(width=100)
	pm.menuItem(label="Circle")
	pm.menuItem(label="Sphere")
	pm.menuItem(label="Square")
	pm.menuItem(label="Cube")
	pm.menuItem(label="2D Arrow")
	pm.menuItem(label="3D Arrow")
	pm.menuItem(label="Round Pointer")
	pm.menuItem(label="COG Circle")
	pm.menuItem(label="Compass")
	pm.setParent("..")
	
	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]),
		width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label=phrases['shapes_shapeName'])
	txt_shapeName = pm.textField(
		placeholderText=phrases['shapes_defaultShapeText'])
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]),
		width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label=phrases['shapes_shapeSuffix'])
	txt_shapeSuffix = pm.textField(
		placeholderText=phrases['shapes_defaultControlText'])
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]),
		width=450, columnWidth=([1, 200], [2, 250]))
	pm.text(label=phrases['shapes_placedOn'])
	opt_placementOption = pm.optionMenu(width=150)
	pm.menuItem(label="Origin")
	pm.menuItem(label="Currently Selected Object")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=3, columnWidth=([1,150], [2, 150]))
	pm.text(label="")
	pm.button(label=phrases['shapes_button'], command=pm.Callback(createShape,
		opt_shapeOptions, txt_shapeName, txt_shapeSuffix,
		opt_placementOption))
	pm.text(label="")
	pm.setParent("..")

	pm.setParent("..")

def create_circle(shapeTitle):
    return pm.circle(
        c=(0, 0, 0),
        ch=1,
        d=3,
        ut=0,
        sw=360,
        s=8,
        r=1,
        tol=0.01,
        nr=(0, 1, 0),
        name=shapeTitle,
        )

def create_square(shapeTitle):
    return pm.curve(name=shapeTitle, p=[
    	(0.5, 0, 0.5), 
    	(-0.5, 0, 0.5),
    	(-0.5, 0, -0.5), 
    	(0.5, 0, -0.5), 
    	(0.5, 0, 0.5)],
    	k=[0, 1, 2, 3, 4], d=1)

def create_2darrow(shapeTitle):
    return pm.curve(name=shapeTitle, p=[
    	(0, 0, 1), 
    	(1, 0, 0), 
    	(0.5, 0, 0),
    	(0.5, 0, -1), 
    	(-0.5, 0, -1), 
    	(-0.5, 0, 0), 
    	(-1, 0, 0), 
    	(0, 0, 1)],
    	k=[0, 1, 2, 3, 4, 5, 6, 7], d=1)

def create_3darrow(shapeTitle):
    return pm.curve(name=shapeTitle, p=[
    	(0, 0, 1), 
    	(1, 0, 0), 
    	(0.5, 0, 0),
    	(0.5, 0, -1), 
    	(0, 0, -1), 
    	(0, 0.5, -1), 
    	(0, 0.5, 0), 
    	(0, 1, 0),
    	(0, 0, 1), 
    	(-1, 0, 0), 
    	(-0.5, 0, 0), 
    	(-0.5, 0, -1), 
    	(0, 0, -1),
    	(0, -0.5, -1), 
    	(0, -0.5, 0), 
    	(0, -1, 0), 
    	(0, 0, 1)
    	],
    	k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], d=1)

def create_cube(shapeTitle):
    return pm.curve(name=shapeTitle, p=[
    	(0.5, 0.5, -0.5), 
    	(0.5, 0.5, 0.5),
        (0.5, -0.5, 0.5), 
        (0.5, -0.5, -0.5), 
        (0.5, 0.5, -0.5), 
        (-0.5, 0.5,  -0.5), 
        (-0.5, -0.5, -0.5), 
        (0.5, -0.5, -0.5), 
        (0.5, -0.5, 0.5),
        (-0.5, -0.5, 0.5), 
        (-0.5, -0.5, -0.5), 
        (-0.5, 0.5, -0.5), 
        (-0.5, 0.5, 0.5), 
        (-0.5, -0.5, 0.5), 
        (-0.5, 0.5, 0.5), 
        (0.5, 0.5, 0.5)
        ],
        k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], d=1)

def create_COG(shapeTitle):
        return pm.curve(name=shapeTitle, p=[
        	(-1.19209e-07, 0, 2), 
        	(-0.382683, 0, 0.923879), 
        	(-1.414213, 0, 1.414213), 
        	(-0.923879, 0, 0.382683), 
        	(-2, 0, 0), 
        	(-0.923879, 0, -0.382683), 
        	(-1.414213, 0, -1.414214), 
        	(-0.382683, 0, -0.923879), 
        	(0, 0, -2), 
        	(0.382683, 0, -0.923879),
        	(1.414214, 0, -1.414213), 
        	(0.92388, 0, -0.382683),
        	(2, 0,-1.19209e-07), 
        	(0.92388, 0, 0.382683),
        	(1.414214, 0, 1.414213), 
        	(0.382683, 0, 0.923879),
        	(-1.19209e-07, 0, 2)
        	],
        	k=[
        	0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 
        	13, 14, 14, 14
        	], d=3)

def create_sphere(shapeTitle):
        return pm.curve(name=shapeTitle, p=[
        	(0, 1, 0),
        	(0.25, 0.866025, 0.433013),
        	(0.5, 0.866025, 0),
        	(0.25, 0.866025, -0.433013),
        	(-0.25, 0.866025, -0.433013),
        	(-0.5, 0.866025, -7.45058e-08),
        	(-0.25, 0.866025, 0.433013),
        	(0.25, 0.866025, 0.433013),
        	(0.433013, 0.5, 0.75),
        	(-0.433013, 0.5, 0.75),
        	(-0.866025, 0.5, -1.29048e-07),
        	(-0.433013, 0.5, -0.75),
        	(0.433013, 0.5, -0.75),
        	(0.866025, 0.5, 0),
        	(0.433013, 0.5, 0.75),
        	(0.5, 0, 0.866025),
        	(-0.5, 0, 0.866025),
        	(-1, 0, -1.49012e-07),
        	(-0.5, 0, -0.866026), 
        	(0.5, 0, -0.866025), 
        	(1, 0, 0), 
        	(0.5, 0, 0.866025), 
        	(0.433013, -0.5, 0.75), 
        	(-0.433013, -0.5, 0.75), 
        	(-0.866025, -0.5, -1.29048e-07), 
        	(-0.433013, -0.5, -0.75), 
        	(0.433013, -0.5, -0.75), 
        	(0.866025, -0.5, 0), 
        	(0.433013, -0.5, 0.75),
        	(0.25, -0.866025, 0.433013), 
        	(-0.25, -0.866025, 0.433013), 
        	(-0.5, -0.866025, -7.45058e-08), 
        	(-0.25, -0.866025, -0.433013), 
        	(0.25, -0.866025, -0.433013), 
        	(0.5, -0.866025, 0), 
        	(0.25, -0.866025, 0.433013), 
        	(0, -1, 0), 
        	(-0.25, -0.866025, -0.433013), 
        	(-0.433013, -0.5, -0.75), 
        	(-0.5, 0, -0.866026), 
        	(-0.433013, 0.5, -0.75), 
        	(-0.25, 0.866025, -0.433013), 
        	(0, 1, 0), 
        	(-0.5, 0.866025, -7.45058e-08), 
        	(-0.866025, 0.5, -1.29048e-07), 
        	(-1, 0, -1.49012e-07), 
        	(-0.866025, -0.5, -1.29048e-07), 
        	(-0.5, -0.866025, -7.45058e-08), 
        	(0, -1, 0), (0.5, -0.866025, 0), 
        	(0.866025, -0.5, 0), 
        	(1, 0, 0), 
        	(0.866025, 0.5, 0), 
        	(0.5, 0.866025, 0), 
        	(0, 1, 0), 
        	(0.25, 0.866025, -0.433013), 
        	(0.433013, 0.5, -0.75), 
        	(0.5, 0, -0.866025), 
        	(0.433013, -0.5, -0.75), 
        	(0.25, -0.866025, -0.433013), 
        	(0, -1, 0), 
        	(-0.25, -0.866025, 0.433013), 
        	(-0.433013, -0.5, 0.75), 
        	(-0.5, 0, 0.866025), 
        	(-0.433013, 0.5, 0.75), 
        	(-0.25, 0.866025, 0.433013), 
        	(0, 1, 0)
        	], 
        	k=[
        	0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
        	16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
        	31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 
        	46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
        	61, 62, 63, 64, 65, 66
        	], d=1)

def create_roundpointer(shapeTitle):
        return pm.curve(name=shapeTitle, p=[
        	(7.78772e-08, 1.94693e-08, 1), 
        	(0, 1, 0), 
        	(0.707107, 0.707107, 0), 
        	(1, 0, 0), 
        	(0.707107, -0.707107, 0), 
        	(0, -1, 0), 
        	(-0.707107, -0.707107, 0), 
        	(-1, 0, 0), 
        	(-0.707107, 0.707107, 0), 
        	(0, 1, 0), 
        	(0, 0.923879, -0.382683), 
        	(0.653281, 0.653281, -0.382683), 
        	(0.92388, 0, -0.382683), 
        	(0.653281, -0.653281, -0.382683), 
        	(0, -0.923879, -0.382683), 
        	(-0.653281, -0.653281, -0.382683), 
        	(-0.923879, 0, -0.382683), 
        	(-0.653281, 0.653281, -0.382683), 
        	(0, 0.923879, -0.382683), 
        	(0, 0.707107, -0.707107), 
        	(0.5, 0.5, -0.707107), 
        	(0.707107, 0, -0.707107), 
        	(0.5, -0.5, -0.707107), 
        	(0, -0.707107, -0.707107), 
        	(-0.5, -0.5, -0.707107), 
        	(-0.707107, 0, -0.707107), 
        	(-0.5, 0.5, -0.707107), 
        	(0, 0.707107, -0.707107), 
        	(0, 0.382683, -0.92388), 
        	(0.270598, 0.270598, -0.92388), 
        	(0.382683, 0, -0.92388), 
        	(0.270598, -0.270598, -0.92388), 
        	(0, -0.382683, -0.92388), 
        	(-0.270598, -0.270598, -0.92388), 
        	(-0.382683, 0, -0.92388), 
        	(-0.270598, 0.270598, -0.92388), 
        	(0, 0.382683, -0.92388), 
        	(0, 0, -1), 
        	(0, -0.382683, -0.92388), 
        	(0, -0.707107, -0.707107), 
        	(0, -0.923879, -0.382683), 
        	(0, -1, 0), 
        	(7.78772e-08, 1.94693e-08, 1), 
        	(0.707107, -0.707107, 0), 
        	(0.653281, -0.653281, -0.382683), 
        	(0.5, -0.5, -0.707107),
        	(0.270598, -0.270598, -0.92388), 
        	(0, 0, -1), 
        	(-0.270598, 0.270598, -0.92388), 
        	(-0.5, 0.5, -0.707107), 
        	(-0.653281, 0.653281, -0.382683), 
        	(-0.707107, 0.707107, 0), 
        	(7.78772e-08, 1.94693e-08, 1), 
        	(0.707107, 0.707107, 0), 
        	(0.653281, 0.653281, -0.382683), 
        	(0.5, 0.5, -0.707107), 
        	(0.270598, 0.270598, -0.92388), 
        	(0, 0, -1), 
        	(-0.270598, -0.270598, -0.92388), 
        	(-0.5, -0.5, -0.707107), 
        	(-0.653281, -0.653281, -0.382683), 
        	(-0.707107, -0.707107, 0), 
        	(7.78772e-08, 1.94693e-08, 1)
        	], k=[
        	0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 
        	16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
        	31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 
        	46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
        	61, 62
        	], d=1)

def create_compass(shapeTitle): 
    newShape = pm.curve(name="Microedge1", p=[
    	(-0.309017, 0, -0.951057),
        (-0.455125, 0, -0.882908), 
        (-0.587785, 0, -0.809017), 
        (-0.710365, 0, -0.710365), 
        (-0.809017, 0, -0.587785), 
        (-0.885102, 0, -0.457095),
        (-0.951057, 0, -0.309017)
        ], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece1 = newShape
    sidepiece_shape1 = sidepiece1.getShape();
    sidepiece_shape1.overrideEnabled.set(True)
    newShape = pm.curve(name="Microedge2", p=[
    	(0.309017, 0, -0.951057), 
    	(0.457095, 0, -0.885102), 
    	(0.587785, 0, -0.809017), 
    	(0.709632, 0, -0.70902), 
    	(0.809017, 0, -0.587785), 
    	(0.885102, 0, -0.457095),
        (0.951057, 0, -0.309017)
        ], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece2 = newShape
    sidepiece_shape2 = newShape.getShape();
    sidepiece_shape2.overrideEnabled.set(True)
    newShape = pm.curve(name="Microedge3", p=[
    	(0.951057, 0, 0.309017), 
    	(0.885102, 0, 0.457095), 
    	(0.809017, 0, 0.587785), 
    	(0.710365, 0, 0.710365), 
    	(0.587785, 0, 0.809017), 
    	(0.455125, 0, 0.882908),
        (0.309017, 0, 0.951057)
        ], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece3 = newShape
    sidepiece_shape3 = newShape.getShape();
    sidepiece_shape3.overrideEnabled.set(True)
    newShape = pm.curve(name="Microedge4", p=[
    	(-0.309017, 0, 0.951057),
        (-0.457095, 0, 0.885102), 
        (-0.587785, 0, 0.809017), 
        (-0.710365, 0, 0.710365), 
        (-0.809017, 0, 0.587785), 
        (-0.882908, 0, 0.455125),
        (-0.951057, 0, 0.309017)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece4 = newShape
    sidepiece_shape4 = newShape.getShape();
    sidepiece_shape4.overrideEnabled.set(True)
    microedge = pm.parent(shape="relative")
    backCompass = pm.curve(name="compassBack", p=[
    	(0.309017, 0, 0.951057),
        (0.309017, 0, 1.296348), 
        (0.548167, 0, 1.296348), 
        (0, 0, 2),
        (-0.548167, 0, 1.296347), 
        (-0.309017, 0, 1.296347), 
        (-0.309017, 0, 0.951057)
        ], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    leftCompass = pm.curve(name="compassLeft", p=[
    	(0.309017, 0, 0.951057),
        (0.309017, 0, 1.296348), 
        (0.548167, 0, 1.296348), 
        (0, 0, 2),
        (-0.548167, 0, 1.296347), 
        (-0.309017, 0, 1.296347), 
        (-0.309017, 0, 0.951057)
        ], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    forwardCompass = pm.curve(name="compassForward", p=[
    	(0.309017, 0, 0.951057), 
    	(0.309017, 0, 1.296348), 
    	(0.548167, 0, 1.296348), 
    	(0, 0, 2), 
    	(-0.548167, 0, 1.296347), 
    	(-0.309017, 0, 1.296347), 
    	(-0.309017, 0, 0.951057)
    	], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    rightCompass = pm.curve(name="compassRight", p=[
    	(0.309017, 0, 0.951057),
        (0.309017, 0, 1.296348), 
        (0.548167, 0, 1.296348), 
        (0, 0, 2),
        (-0.548167, 0, 1.296347), 
        (-0.309017, 0, 1.296347), 
        (-0.309017, 0, 0.951057)
        ], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    leftCompass.ry.set(90)
    backCompass.ry.set(180)
    rightCompass.ry.set(270)
    forwardCompass_shape = forwardCompass.getShape()
    backCompass_shape = backCompass.getShape()
    leftCompass_shape = leftCompass.getShape()
    rightCompass_shape = rightCompass.getShape()
    forwardCompass_shape.overrideEnabled.set(True)
    backCompass_shape.overrideEnabled.set(True)
    leftCompass_shape.overrideEnabled.set(True)
    rightCompass_shape.overrideEnabled.set(True)
    forwardCompass_shape.overrideColor.set(__green__)
    backCompass_shape.overrideColor.set(__green__)
    leftCompass_shape.overrideColor.set(__blue__)
    rightCompass_shape.overrideColor.set(__red__)
    pm.makeIdentity(sidepiece1, sidepiece2, sidepiece3, sidepiece4, n=0, s=1,
        r=1, t=1, apply=True, pn=1)
    pm.makeIdentity(leftCompass, rightCompass, forwardCompass, backCompass,
        n=0, s=1, r=1, t=1, apply=True, pn=1)
    newGroup = pm.group(name="microEdges", em=True)
    pm.parent(sidepiece_shape1, sidepiece_shape2, sidepiece_shape3,
        sidepiece_shape4, forwardCompass_shape, backCompass_shape, leftCompass_shape,
        rightCompass_shape, newGroup, s=True, r=True)
    pm.makeIdentity(newGroup, n=0, s=1, r=1, t=1, apply=True, pn=1)
    pm.delete(sidepiece1, sidepiece2, sidepiece3, sidepiece4)
    pm.delete(forwardCompass, backCompass, leftCompass, rightCompass)
    shapeName = pm.rename(newGroup, shapeTitle)
    return newGroup

def createShape(*args):
	shapeObject = args[0].getValue()
	shapeName = args[1].getText()
	shapeSuffix = args[2].getText()
	shapeLocation = args[3].getValue()
	if shapeName == "":
		shapeName = "shape"
	if shapeSuffix == "":
		shapeSuffix = "icon"
	shapeName = shapeName + "_" + shapeSuffix
	#determine which pulldown item is chosen
	#if build to appropriate functino
	if shapeObject == "Circle":
		newShape = create_circle(shapeName)
	elif shapeObject == "Sphere":
		newShape = create_sphere(shapeName)
	elif shapeObject == "Square":
		newShape = create_square(shapeName)
	elif shapeObject == "2D Arrow":
		newShape = create_2darrow(shapeName)
	elif shapeObject == "3D Arrow":
		newShape = create_3darrow(shapeName)
	elif shapeObject == "Round Pointer":
		newShape = create_roundpointer(shapeName)
	elif shapeObject == "Compass":
		newShape = create_compass(shapeName)
	elif shapeObject == "COG Circle":
		newShape = create_COG(shapeName)
	elif shapeObject == "Cube":
		newShape = create_cube(shapeName)
	else:
		print("Shape unidentified - " + str(shapeName))
		return


	#rename curve
	#move curve to desired locaiton, if not set to origin

def wnd_rowFKIK():
	global txt_rootJoint, txt_endJoint, txt_handJoint
	global chk_control_create, chk_control_hierarchy, chk_control_connect
	global chk_createHandControl
	global btn_selectHandControl
	global fkik_innerFrame
	pm.frameLayout(collapsable=True, label="FK/IK")

	pm.rowLayout(numberOfColumns=3, width=500,
		columnWidth=([1, 200], [2, 150], [3, 150]))
	pm.text(label=phrases['fkik_selectRootText'])
	txt_rootJoint = pm.textField(
		placeholderText=phrases['general_chooseJoint'], editable=False)
	pm.button(label=phrases['fkik_selectRootButton'],
		command=pm.Callback(fkikSelectRoot), width=100)
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=3, width=500, columnWidth=([1, 200],[2, 150],
		[3, 150]))
	pm.text(label=phrases['fkik_selectEndText'])
	txt_endJoint = pm.textField(
		placeholderText=phrases['general_chooseJoint'], editable=False)
	pm.button(label=phrases['fkik_selectEndButton'],
		command=pm.Callback(fkikSelectEnd), width=100)
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, width=450, columnWidth=([1, 350],
		[2, 150]))
	pm.text(label=phrases['fkik_createControlsText'])
	chk_control_create = pm.checkBox(label="", value=True,
		onCommand=pm.Callback(toggleJointCreation, True),
		offCommand=pm.Callback(toggleJointCreation, False))
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, width=450, columnWidth=([1, 350],
		[2, 150]))
	pm.text(phrases['fkik_createHierarchyText'])
	chk_control_hierarchy = pm.checkBox(label="", value=True)
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2, width=450, columnWidth=([1, 350],
		[2, 150]))
	pm.text(label=phrases['fkik_connectControlsText'])
	chk_control_connect = pm.checkBox(label="", value=True)
	pm.setParent("..")

	fkik_innerFrame = pm.frameLayout(label="Hand Connection", collapsable=True) # Embedded frame

	pm.rowLayout(numberOfColumns=2, columnWidth=([1, 350], [2, 150]))
	pm.text(label=phrases['fkik_createControl'])
	chk_createHandControl = pm.checkBox(label="", value=True,
		changeCommand=pm.Callback(toggleHandConnection))
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=3, columnWidth=([1, 200], [2, 150],
		[3, 150]))
	pm.text(label="Hand Joint:")
	txt_handJoint = pm.textField(
		placeholderText=phrases['general_chooseJoint'], editable=False)
	btn_selectHandControl = pm.button(label=phrases['fkik_selectHandButton'],
		command=pm.Callback(fkikSelectHand))
	pm.setParent("..")

	pm.setParent("..")

	pm.rowLayout(numberOfColumns=3, columnWidth=([1, 150], [3, 150]))
	pm.text(label="")
	pm.button(label="Generate", width=150, command=pm.Callback(fkik_generateStuff))
	pm.text(label="")
	pm.setParent("..")

def fkik_generateStuff(*args):
	global chk_control_connect, chk_control_create, chk_control_hierarchy, chk_createHandControl
	fkik_rootJoint = txt_rootJoint.getText()
	fkik_endJoint = txt_endJoint.getText()
	handJoint = txt_handJoint.getText()
	createControlFlag = chk_control_create.getValue()
	inHierarchyFlag = chk_control_hierarchy.getValue()
	connectControlsFlag = chk_control_connect.getValue()
	onHand = chk_createHandControl.getValue()
	activeSelection = cmds.ls(sl=True)
	#duplicate joint for FK
	fk_chain = cmds.duplicate(fkik_rootJoint, name=fkik_rootJoint.replace("_bind", "_fk"), rc=True)
	# now go through the rest and rename those
	inc = 0
	for fkInc in fk_chain:
		if (inc > 0):
			newName = fkInc.replace("_bind1", "_fk")
			newName = newName.replace("_waste1", "_fk")
			pm.rename(fkInc, newName)
		inc = inc + 1
	# duplicate again and do IK this time
	ik_chain = cmds.duplicate(fkik_rootJoint, name=fkik_rootJoint.replace("_bind", "_ik"), rc=True)
	# now go through the rest and rename those
	inc = 0
	for ikInc in ik_chain:
		if (inc > 0):
			newName = ikInc.replace("_bind1", "_ik")
			newName = newName.replace("_waste1", "_ik")
			pm.rename(ikInc, newName)
		inc = inc + 1
	main_chain = cmds.ls(fkik_rootJoint, dag=True)
	# get the list from FK
	fk_chain = cmds.ls(fk_chain, dag=True)
	#get the list from IK
	ik_chain = cmds.ls(ik_chain, dag=True)
	# prep array for control creation
	arr_fk = []
	# Parent the joints now
	for iter in main_chain:
		bind_joint = iter
		fk_joint = iter.replace("_bind", "_fk")
		fk_joint = fk_joint.replace("_waste", "_fk")
		ik_joint = iter.replace("_bind", "_ik")
		ik_joint = ik_joint.replace("_waste", "_ik")
		cmds.parentConstraint(fk_joint, ik_joint, bind_joint)
		arr_fk.append(fk_joint)
	# check to see if the arm controls are to be made
	if createControlFlag == True:
		# Controls being made.
		for controlIndex in arr_fk:
			controlName = controlIndex.replace("_fk", "_icon")
			# send control to joint position
			controlTrans = cmds.xform(controlIndex, q=True, t=True, worldSpace=True)
			controlRot = cmds.xform(controlIndex, q=True, ro=True, worldSpace=True)
			control = create_circle(controlName)
			cmds.xform(controlName, t=controlTrans, ro=controlRot)
			controlPad = controlName.replace("_icon", "_pad")
			newGroup = cmds.group(em=True, n=controlPad)
			cmds.xform(newGroup, ro=controlRot, t=controlTrans)
			cmds.parent(controlName, controlPad)
			cmds.xform(controlName, ro=[0, 0, 90])
			freezeTransform(controlName)
	# Make IK handle
	cmds.ikHandle(sj=fkik_rootJoint, ee=fkik_endJoint, sol="ikRPsolver", n=fkik_rootJoint + "_ikHandle")
	


def freezeTransform(objectName):
	pm.makeIdentity(objectName, n=0, s=1, r=1, t=1, apply=True, pn=1)
    
def orient_processJoints(*args):
	jointBeingManipulated = txt_orientJointBase.getText()
	freezeTransform(jointBeingManipulated)
	pm.joint(jointBeingManipulated, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='yup')

def toggleJointCreation(*args):
	chk_control_hierarchy.setEnable(chk_control_create.getValue())
	chk_control_connect.setEnable(chk_control_create.getValue())
	fkik_innerFrame.setEnable(chk_control_create.getValue())


def toggleHandConnection(*args):
	btn_selectHandControl.setEnable(chk_createHandControl.getValue())

def fkikSelectEnd(*args):
	txt_endJoint.setText(getSelected(True))

def fkikSelectRoot(*args):
	txt_rootJoint.setText(getSelected(True))

def fkikSelectHand(*args):
	txt_handJoint.setText(getSelected(True))

def orient_selectJoint(*args):
	txt_orientJointBase.setText(getSelected(True))

def btn_closeWindow(*args):
	global chk_keepAlive
	chk_keepAlive.setValue=False
	closeWindow()

def wnd_jointOrient():
	global txt_orientJointBase
	pm.frameLayout(collapsable=True, label="")

	pm.rowLayout(numberOfColumns=3, columnWidth=([1, 200], [2, 150],
		[3, 150]))
	pm.text(label="Select Joint")
	txt_orientJointBase = pm.textField(placeholderText=phrases['general_chooseJoint'], editable=False)
	pm.button(label="Select Joint", command=pm.Callback(orient_selectJoint))
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=3, columnWidth=([1, 150], [3, 150]))
	pm.text(label="")
	pm.button(label="Orient", width=150, command=pm.Callback(orient_processJoints))
	pm.text(label="")
	pm.setParent("..")
	
	pm.setParent("..")

def processButton():
	pm.rowLayout(numberOfColumns=3, columnWidth=([1, 150], [3, 150]))
	pm.text(label="")
	pm.button(label="", width=150)
	pm.text(label="")
	pm.setParent("..")

def wnd_row_default():
	pm.frameLayout(collapsable=True, label="")

	pm.rowLayout(numberOfColumns=1)
	pm.text(label="blank")
	#More layout in here
	pm.setParent("..")

	pm.setParent("..")

def gui():
	global wnd_connector_window, windowKeepAlive
	global chk_keepAlive
	wnd_connector_window = pm.window(title="Connector Window", widthHeight=(
		[windowWidth, windowHeight]), sizeable=True)

	pm.columnLayout(numberOfChildren=3)
	chk_keepAlive = pm.checkBox(phrases['main_autocloseWindow'],
		value=windowKeepAlive,
		changeCommand=pm.Callback(autocloseWindowToggle))

	pm.scrollLayout(width=windowWidth, height=windowHeight-50)
	wnd_rowTODO()
	wnd_rowPad()
	wnd_rowShapes()
	wnd_rowFKIK()
	wnd_jointOrient()
	pm.setParent("..")

	pm.setParent("..")

	pm.rowLayout(numberOfColumns=1)
	pm.button(label="Close Window/Cancel",
		command=pm.Callback(btn_closeWindow), height=30)
	pm.setParent("..")

	wnd_connector_window.setSizeable(False)

	pm.showWindow(connector_window)