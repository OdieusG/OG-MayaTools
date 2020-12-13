'''

Connector mod

import maya.cmds as cmds
cmds.ikHandle(sj="joint2", ee="joint10", c="curve1")


Components:
 Joint auto-connector
 Auto-pad'der

 Usage:
    import OG_MayaTools.connector_mod as conmod
    reload(conmod)
    conmod.gui()
'''

import pymel.core as pm
import maya.mel as mel
import maya.cmds as cmds
import sys
import os.path
from os import path
import time

backColor_gray = [.5, .5, .5]
windowWidth = 520
windowHeight=500
buttonWidth = 150
keepAliveCheck = ""
windowKeepAlive=False
__green__ = 14
__red__ = 13
__blue__ = 6
optionAutoclose = True
optionLastSaved = 0
scriptPath = os.path.dirname(__file__)
# Determine if the file exists
try:
    # Initialize options
    print("Loading options")
    f = open(scriptPath + "/options.txt", "rt")
    # file is pipe delimited for readibility
    outputFile = f.read()
    f.close()
except IOError:
    print("Options are not existent")
try:
    f = open(scriptPath + "/todo.txt", "rt")
    todoList = f.read()
    f.close()
except IOError:
    print("TODO list does not exist")
# Break array into individual items
tempArr = outputFile.split("|")
# Set each variable
optionAutoclose = tempArr[0]
optionLastSaved = int(tempArr[1])


def saveOptions(*args):
    f = open(scriptPath + "/options.txt", "wt")
    outputString = str(optionAutoclose)
    outputString = outputString + "|" +  str(int(time.time()))
    f.write(outputString)
    f.close()
    print("Options saved")

def toast(message):
    cmds.headsUpMessage(message)

def sp():
    pm.setParent("..")

def getSelected(niceName=False, dagOption=True):
    selectedItem = cmds.ls(sl=True, dag=dagOption)
    if niceName == True:
        return selectedItem[0]
    else:
        return selectedItem

def closeWindow():
    if windowKeepAlive == True:
        pm.deleteUI(wnd_connector_window)
    else:
        return

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
    todoList = todoList + "+Joint orient tool\n"
    todoList = todoList + "+FK/IK Joint Automatic Creation Tool\n"
    todoList += "Flying hand syndrome with FK/IK\n"
    todoList = todoList + "Automatic SDK with FK/IK\n"
    todoList = todoList + "Repair broken selection items\n"
    todoList = todoList + "Create buttons to change the override colors on finalization\n"
    pm.text(label=todoList, align="left")
    pm.setParent("..")

    pm.setParent("..")
    
def wnd_rowPad():
    global txt_jointField, chk_appendPad
    pm.frameLayout(collapsable=True, label="Pad Object", width=500)

    pm.rowLayout(numberOfColumns=3, columnWidth=[(1, 150), (2, 200), (3, 100)])
    pm.text(label="Choose an object to pad")
    txt_jointField = pm.textField(placeholderText="Choose joint", editable=False)
    pm.button(label="Choose Item", command=pm.Callback(selectItem))
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=2, columnWidth=[(1,350)])
    pm.text("Automatically append \"pad\" to end?")
    chk_appendPad = pm.checkBox("appendPad", value=True, label="")
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=3)
    pm.text(width=150, label="")
    pm.button(label="Pad this", command=pm.Callback(padObject))
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
    pm.text(label="Choose a shape")
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
    pm.text(label="Enter a name.\nLeave blank for default shape name.")
    txt_shapeName = pm.textField(
        placeholderText="shape")
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]),
        width=450, columnWidth=([1, 200], [2, 250]))
    pm.text(label="Insert a suffix.\nLeave blank for default\n\"icon\" to be added")
    txt_shapeSuffix = pm.textField(
        placeholderText="icon")
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=2, columnAlign=([1, "left"], [2, "right"]),
        width=450, columnWidth=([1, 200], [2, 250]))
    pm.text(label="Shape is placed on:")
    opt_placementOption = pm.optionMenu(width=150)
    pm.menuItem(label="Origin")
    pm.menuItem(label="Currently Selected Object")
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=3, columnWidth=([1,150], [2, 150]))
    pm.text(label="")
    pm.button(label="Create Shape", command=pm.Callback(createShape,
        opt_shapeOptions, txt_shapeName, txt_shapeSuffix,
        opt_placementOption))
    pm.text(label="")
    pm.setParent("..")

    pm.setParent("..")

def create_circle(shapeTitle, radius=1):
    return pm.circle(
        c=(0, 0, 0),
        ch=1,
        d=3,
        ut=0,
        sw=360,
        s=8,
        r=radius,
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

def create_cube(shapeTitle, newScale=1):
    newCurve = pm.curve(name=shapeTitle, p=[
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
    newCurve =pm.xform(shapeTitle, s=[float(newScale), float(newScale), float(newScale)])
    print "Rescaling " + str(newCurve)
    return newCurve

def create_COG(shapeTitle):
    # Make a base circle (16 segments), 2 mm wide
    cog = pm.circle(name=shapeTitle, c=[0,0,0], nr=[0,1,0], sw=360, r=1, d=3, tol=.01, ch=False, s=16)[0]
    # Scale in alternating CVs
    pm.xform(cog.cv[0::2], s=(.5, .5, .5))
    pm.xform(cog.cv[9], r=True, t=(0, 0, .5))


'''
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
            '''

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
    currently_selected_item = getSelected()
    if shapeName == "":
        shapeName = "shape"
    if shapeSuffix == "":
        shapeSuffix = "icon"
    shapeName = shapeName + "_" + shapeSuffix
    #determine which pulldown item is chosen
    #if build to appropriate function
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
    # Determine where the control will be placed
    if shapeLocation != "Origin":
        # Means it will be on the currently selected object
        print("Current selection is {0}".format(currently_selected_item[0]))
        # Get the translate of the selected object
        currentTranslate = cmds.xform(currently_selected_item[0], q=True, t=True)
        print("Current translate {0}".format(currentTranslate))
        # Get the rotate of the object
        currentRotate = cmds.xform(currently_selected_item[0], q=True, ro=True)
        # Move to translate and rotate
        cmds.xform(newShape, t=currentTranslate, ro=currentRotate)
    else:
        print("Sending to origin")
    closeWindow()

def wnd_rowFKIK():
    global txt_rootJoint, txt_endJoint, txt_handJoint, txt_handDrop
    global txt_handIconDist, txt_handIconRadius, txt_iconScale
    global chk_control_create, chk_control_hierarchy, chk_control_connect
    global chk_createHandControl, chk_arm_control
    global btn_selectHandControl, btn_selectWasteControl
    global sld_handIconDistance, sld_handIconRadius, sld_iconScale
    global opt_handOrient
    pm.frameLayout(collapsable=True, label="FK/IK")

    pm.rowLayout(numberOfColumns=3, width=500,
        columnWidth=([1, 200], [2, 150], [3, 150]))
    pm.text(label="Select the root joint")
    txt_rootJoint = pm.textField(
        placeholderText="Choose joint", editable=False)
    pm.button(label="Select root",
        command=pm.Callback(fkikSelectRoot), width=100)
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=3, width=500, columnWidth=([1, 200],[2, 150],
        [3, 150]))
    pm.text(label="Select the end joint\n(for IK creation)")
    txt_endJoint = pm.textField(
        placeholderText="Choose joint", editable=False)
    pm.button(label="Select end",
        command=pm.Callback(fkikSelectEnd), width=100)
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=2, width=450, columnWidth=([1, 350],
        [2, 150]))
    pm.text(label="Create controls on respective joints?")
    chk_control_create = pm.checkBox(label="", value=True,
        onCommand=pm.Callback(toggleJointCreation, True),
        offCommand=pm.Callback(toggleJointCreation, False))
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=3, columnWidth=([1, 150], [2, 200],
        [3, 150]))
    pm.text(label="Control Scale")
    sld_iconScale = pm.floatSlider(min=0, max=2, value=0.5, width=200, changeCommand=pm.Callback(scaleSliderChanged))
    txt_iconScale = pm.textField(editable=True, changeCommand=pm.Callback(txt_iconScaleChanged), text=sld_iconScale.getValue())
    pm.setParent("..")
    
    pm.rowLayout(numberOfColumns=2, width=450, columnWidth=([1, 350],
        [2, 150]))
    pm.text(label="Connect controls on respective joints?")
    chk_control_connect = pm.checkBox(label="", value=True)
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=2, width=450, columnWidth=([1, 350],
        [2, 150]))
    pm.text(label="Create arm control at IK handle")
    chk_arm_control = pm.checkBox(label="", value=True)
    pm.setParent("..")

    fkik_innerFrame = pm.frameLayout(label="Hand Connection", collapsable=True) # Embedded frame

    pm.rowLayout(numberOfColumns=2, columnWidth=([1, 350], [2, 150]))
    pm.text(label="Create control on hand?")
    chk_createHandControl = pm.checkBox(label="", value=True,
        changeCommand=pm.Callback(toggleHandConnection))
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=3, columnWidth=([1, 200], [2, 150],
        [3, 150]))
    pm.text(label="Hand Joint:")
    txt_handJoint = pm.textField(
        placeholderText="Choose joint", editable=False)
    btn_selectHandControl = pm.button(label="Select hand Joint",
        command=pm.Callback(fkikSelectHand))
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=3, columnWidth=([1, 200], [2, 150],
        [3, 150]))
    pm.text(label="Hand waste:")
    txt_handDrop = pm.textField(
        placeholderText="Choose joint", editable=False)
    btn_selectWasteControl = pm.button(label="Select secondary\nhand position (waste)",
        command=pm.Callback(fkikSelectHandIconPoint))
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=2, columnWidth=([1, 350], [2, 150]))
    pm.text(label="Left or right?")
    opt_handOrient = pm.optionMenu(width=150)
    pm.menuItem(label="Left")
    pm.menuItem(label="Right")
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=3, columnWidth=([1, 150], [2, 200],
        [3, 150]))
    pm.text(label="Hand icon distance")
    sld_handIconDistance = pm.floatSlider(min=0, max=10, value=5.0, width=200, changeCommand=pm.Callback(distanceSliderChanged))
    txt_handIconDist = pm.textField(editable=True, changeCommand=pm.Callback(txt_handDistanceChanged), text=sld_handIconDistance.getValue())
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=3, columnWidth=([1, 150], [2, 200],
        [3, 150]))
    pm.text(label="Hand icon radius")
    sld_handIconRadius = pm.floatSlider(min=0, max=5.0, value=1.0, width=200, changeCommand=pm.Callback(sliderRadiusChanged))
    txt_handIconRadius = pm.textField(editable=True, changeCommand=pm.Callback(txt_handRadiusChanged), text=sld_handIconRadius.getValue())
    pm.setParent("..")

    pm.setParent("..")

    pm.rowLayout(numberOfColumns=3, columnWidth=([1, 150], [3, 150]))
    pm.text(label="")
    pm.button(label="Generate Hand", width=150, command=pm.Callback(fkik_generateStuff))
    pm.text(label="")
    pm.setParent("..")

    pm.setParent("..")

def fkik_generateStuff(*args):
    fkik_rootJoint = txt_rootJoint.getText()
    fkik_endJoint = txt_endJoint.getText()
    handIconDistance = txt_handIconDist.getText()
    handIconRadius = txt_handIconRadius.getText()
    iconScale = txt_iconScale.getText()
    handBind = txt_handJoint.getText()
    handDrop = txt_handDrop.getText();
    handIconDirection = opt_handOrient.getValue()
    createControlFlag = chk_control_create.getValue()
    inHierarchyFlag = True
    connectControlsFlag = chk_control_connect.getValue()
    createArmControl = chk_arm_control.getValue()
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
    # prep array for control creation
    arr_fk = []
    main_chain = cmds.ls(fkik_rootJoint, dag=True)
    # get the list from FK
    fk_chain = cmds.ls(fk_chain, dag=True)
    #get the list from IK
    ik_chain = cmds.ls(ik_chain, dag=True)
    arr_constraint = []
    # Parent the joints now
    for iter in main_chain:
        bind_joint = iter
        fk_joint = iter.replace("_bind", "_fk")
        fk_joint = fk_joint.replace("_waste", "_fk")
        ik_joint = iter.replace("_bind", "_ik")
        if iter.count("_waste") == 0:
            newConst = cmds.parentConstraint(fk_joint, ik_joint, bind_joint)
            arr_constraint.append(newConst)
        arr_fk.append(fk_joint)
    # check to see if the arm controls are to be made
    if createControlFlag == True:
        # Controls being made.
        for controlIndex in arr_fk:
            controlName = controlIndex.replace("_fk", "_icon")
            # send control to joint position
            controlTrans = cmds.xform(controlIndex, q=True, t=True, worldSpace=True)
            controlRot = cmds.xform(controlIndex, q=True, ro=True, worldSpace=True)
            control = create_circle(controlName, iconScale)
            freezeTransform(control)
            cmds.xform(controlName, t=controlTrans, ro=controlRot)
            controlPad = controlName.replace("_icon", "_pad")
            newGroup = cmds.group(em=True, n=controlPad)
            cmds.xform(newGroup, ro=controlRot, t=controlTrans)
            cmds.parent(controlName, controlPad)
            cmds.xform(controlName, ro=[0, 0, 90])
            freezeTransform(controlName)
    # Make IK handle
    ikBaseJoint = fkik_rootJoint.replace("_bind", "_ik")
    ikEndJoint = fkik_endJoint.replace("_bind", "_ik")
    ikEndJoint = ikEndJoint.replace("_waste", "_ik")
    armIKHandle = cmds.ikHandle(sj=ikBaseJoint, ee=ikEndJoint, sol="ikRPsolver", n=fkik_rootJoint + "_ikHandle")
    if createArmControl == True:
        # Make arm control
        armControl = fkik_rootJoint.replace("_bind", "_arm_icon")
        armIcon = create_cube(armControl, iconScale)
        freezeTransform(armControl)
        # Snap the icon to the end joint
        armPad = cmds.group(em=True, n=fkik_rootJoint.replace("_bind", "_arm_pad"))
        pivotTrans=cmds.xform(fkik_endJoint, q=True, t=True, worldSpace=True)
        pivotRot=cmds.xform(fkik_endJoint, q=True, ro=True, worldSpace=True)
        pm.xform(armControl, ro=pivotRot)
        pm.xform(armControl, t=pivotTrans)
        pm.xform(armPad, ro=pivotRot)
        pm.xform(armPad, t=pivotTrans)
        pm.parent(armControl, armPad)
    #Connect controls
    if connectControlsFlag == True:
        for iter in arr_fk:
            fk_joint = iter
            icon_name = iter.replace("_fk", "_icon")
            cmds.parentConstraint(icon_name, iter)
        if createArmControl == True:
            # Move the IK to the icon
            cmds.parent(fkik_rootJoint + "_ikHandle", armControl)
    if inHierarchyFlag == True:
        iter=0
        while iter < len(arr_fk)-1:
            # Iterate through fk_chain while replacing text
            parentIcon = arr_fk[iter].replace("_fk", "_icon")
            childPad = arr_fk[iter+1].replace("_fk", "_pad")
            cmds.parent(childPad, parentIcon)
            iter = iter + 1
        if onHand == True:
            iconName = "hand_icon"
            iconPad = iconName.replace("_icon", "_pad")
            # Create circle over waste
            strhandControl = create_circle(iconName, handIconRadius)
            # locate the waste location (rotate and translate)
            pm.group(n=iconPad, em=True)
            # get locations
            handTrans = pm.xform(handDrop, q=True, t=True, worldSpace=True)
            handRot = pm.xform(handDrop, q=True, ro=True, worldSpace=True)
            pm.xform(iconPad, t=handTrans)
            pm.xform(iconPad, ro=handRot)
            pm.xform(iconName, t=handTrans)
            pm.xform(icon_name, ro=handRot)
            pm.parent(iconName, iconPad)
            # Translate the icon in the Y direction
            if handIconDirection == "Left":
                iconDistance = float(handIconDistance)
            else:
                iconDistance = float(handIconDistance) * -1
            pm.xform(iconName, t=[float(0), float(iconDistance), float(0)])
            freezeTransform(iconName)
            # Snap pivot to hand base
            handBaseTra = pm.xform(handBind, q=True, t=True, worldSpace=True)
            snapToArray(iconPad, handBaseTra)
            snapToArray(iconName, handBaseTra)
            # constrain the control
            pm.parentConstraint(iconName, handBind)
            toast("Complete")

def snapToArray(objectName, snapArray):
    print "Snapping " + objectName + " to " 
    print str(snapArray)
    pm.move(float(snapArray[0]), float(snapArray[1]), float(snapArray[2]), objectName + ".scalePivot", objectName + ".rotatePivot", rpr=1)

def freezeTransform(objectName):
    pm.makeIdentity(objectName, n=0, s=1, r=1, t=1, apply=True, pn=1)
    
def orient_processJoints(*args):
    jointBeingManipulated = txt_orientJointBase.getText()
    freezeTransform(jointBeingManipulated)
    pm.joint(jointBeingManipulated, zso=1, ch=1, e=1, oj='xyz', secondaryAxisOrient='yup')

def scaleSliderChanged(*args):
    txt_iconScale.setText(sld_iconScale.getValue())

def txt_iconScaleChanged(*args):
    sld_iconScale.setValue(float(txt_iconScale.getText()))   

def distanceSliderChanged(*args):
    txt_handIconDist.setText(sld_handIconDistance.getValue())

def txt_handDistanceChanged(*args):
    sld_handIconDistance.setValue(float(txt_handIconDist.getText()))

def sliderRadiusChanged(*args):
    txt_handIconRadius.setText(sld_handIconRadius.getValue())

def txt_handRadiusChanged(*args):
    sld_handIconRadius.setValue(float(txt_handIconRadius.getText()))

def toggleJointCreation(*args):
    sld_iconScale.setEnable(chk_control_create.getValue())
    txt_iconScale.setEnable(chk_control_create.getValue())
    chk_control_connect.setEnable(chk_control_create.getValue())
    chk_arm_control.setEnable(chk_control_create.getValue())
    chk_createHandControl.setValue(chk_control_create.getValue())
    btn_selectHandControl.setEnable(chk_createHandControl.getValue())
    btn_selectWasteControl.setEnable(chk_createHandControl.getValue())
    sld_handIconDistance.setEnable(chk_createHandControl.getValue())
    txt_handIconDist.setEnable(chk_createHandControl.getValue())
    sld_handIconRadius.setEnable(chk_createHandControl.getValue())
    txt_handIconRadius.setEnable(chk_createHandControl.getValue())
    
def toggleHandConnection(*args):
    btn_selectHandControl.setEnable(chk_createHandControl.getValue())
    btn_selectWasteControl.setEnable(chk_createHandControl.getValue())
    sld_handIconDistance.setEnable(chk_createHandControl.getValue())
    txt_handIconDist.setEnable(chk_createHandControl.getValue())
    sld_handIconRadius.setEnable(chk_createHandControl.getValue())
    txt_handIconRadius.setEnable(chk_createHandControl.getValue())

def fkikSelectEnd(*args):
    txt_endJoint.setText(getSelected(True))

def fkikSelectRoot(*args):
    txt_rootJoint.setText(getSelected(True))

def fkikSelectHand(*args):
    txt_handJoint.setText(getSelected(True))

def fkikSelectHandIconPoint(*args):
    txt_handDrop.setText(getSelected(True))

def orient_selectJoint(*args):
    txt_orientJointBase.setText(getSelected(True))

def btn_closeWindow(*args):
    global windowKeepAlive
    windowKeepAlive=True
    closeWindow()

def wnd_jointOrient():
    global txt_orientJointBase
    pm.frameLayout(collapsable=True, label="Reorient Joint")

    pm.rowLayout(numberOfColumns=3, columnWidth=([1, 200], [2, 150],
        [3, 150]))
    pm.text(label="Select Joint")
    txt_orientJointBase = pm.textField(placeholderText="Choose joint", editable=False)
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

def hairDeformerCompute(*args):
    # get the joit chain
    # get the coordinates of each joint center
    # create a CUBIC curve based from the coordinates of the joint chain
    print "incomplete"

def wnd_hair_deformers():
    global btn_hairDef1, btn_hairDef2
    global sb_hairStatusBar
    # hair deformer connector
    btn_hairDef1 = pm.button(label="Create Joints", command=pm.Callback(hairDeformer_createJointchain))
    btn_hairDef2 = pm.button(label="Make Curve On Newly Created Joints", enable=False, command=pm.Callback(hairDeformer_createCurve))
    pm.text(label="Create a cubic curve on the joints that are newly created")
    sb_hairStatusBar = pm.textField(text="Status Message Area", enable=False, width=windowWidth-50)

def hairDeformer_createJointchain(*args):
    # store into joint chain variable for processing later
    jointChain = cmds.JointTool()
    # Enable the next button
    btn_hairDef2.setEnable(True)
    sb_hairStatusBar.setText("Lay out your joints, and select the topmost joint that will have the hair deformation")

def hairDeformer_makeDynamicCurve(*args):
    #temporaryLink
    print "Nothing here"

def hairDeformer_createCurve(*args):
    hfCount = 0
    hfArr = []
    degree = 3
    # Get the selection, which should be the joint chain
    jointChain = getSelected()
    # assemble the joints to an array and get the coordinates of each
    for i in jointChain:
        jointTrans = pm.xform(i, q=True, t=True, worldSpace=True)
        tempX = jointTrans[0]
        tempY = jointTrans[1]
        tempZ = jointTrans[2]
        # Store the values in a base array
        hfArr.append ((tempX, tempY, tempZ))
        hfCount = hfCount + 1
    # Number of knots
    # = numPoints + degree (default of 3) - 1
    knotCount = degree + len(hfArr) - 1
    knots = []
    i=0
    while i < knotCount:
        knots.append(i)
        i = i + 1
    # assemble the statement now
    print "Output is"
    print "pm.curve(p=" + str(hfArr) + ", k=" + str(knots) + ", d=" + str(degree) + ")"
    hairCurve = pm.curve(p=hfArr, k=knots, d=degree)
    print mel.eval("makeCurvesDynamic 2 { \"1\", \"0\", \"1\", \"1\", \"0\"};")
    # toggle the point lock to just the base
    # assumed the hair system is "hairSystem1"
    # going off from default follicle design
    pm.setAttr("follicleShape1.pointLock", 1)
    # Take the established joint chain and unparent temporarily
    parentJoints = cmds.listRelatives(jointChain, parent=True)
    # separate the joint from the parent
    baseJoint = jointChain[0]
    endJoint = jointChain[len(jointChain) -1]
    print "Base joint:" + baseJoint
    print "End Joint:" + endJoint
    # Create spline handle on these joints now
    pm.ikHandle(sj=baseJoint, ee=endJoint, c=hairCurve)
    print "Hair system connection complete"
    
def gui():
    global wnd_connector_window, windowKeepAlive
    global chk_keepAlive

    if pm.window('connectorWindow', exists=1) :
        pm.deleteUI('connectorWindow')
    wnd_connector_window = pm.window("connectorWindow", title="Connector Window", widthHeight=(
        [windowWidth, windowHeight]), sizeable=True, resizeToFitChildren=True)
    pm.frameLayout('Connector Mod', width=windowWidth, height=windowHeight)

    pm.tabLayout('tabList')
    
    tab_Todo = pm.columnLayout('TODOList', h=200, w=200)
    wnd_rowTODO()
    pm.setParent("..")

    tab_Quicks = pm.columnLayout('QuickLinks', h=200, w=200)
    wnd_rowPad()
    wnd_rowShapes()
    pm.setParent("..")

    tab_FKIK = pm.columnLayout('FKIK', h=200, w=200)
    wnd_rowFKIK()
    pm.setParent("..")

    tab_Cloth = pm.columnLayout('Cloth', h=200, w=200)
    pm.text(label="In the works")
    pm.setParent("..")

    tabHair = pm.columnLayout('Hair', h=200, w=200)
    wnd_hair_deformers()
    pm.setParent("..")

    tabOptions = pm.columnLayout('Options')
    pm.checkBox(label="Automatically Close Window On Creation")
    pm.button(label="Save Options", command=pm.Callback(saveOptions))

    # back to main layout
    pm.setParent("..")
    # Lay out the tab list
    pm.tabLayout('tabList', edit=1, tabLabel=[
        (tab_Quicks, "Quick Creates"), 
        (tab_FKIK, "FKIK"), 
        (tab_Cloth, "Cloth Deformers"),
        (tabHair, "Hair Deformers"),
        (tab_Todo, "TODO"), 
        (tabOptions, "Options")
        ])
    pm.setParent("..")

    pm.rowLayout(numberOfColumns=1)
    pm.button(label="Close Window/Cancel",
        command=pm.Callback(btn_closeWindow), height=30)
    pm.setParent("..")

    
    wnd_connector_window.setSizeable(False)

    pm.showWindow(wnd_connector_window)