
'''
shape_window.py

Description:
    Creates control icons for rigging

How to run:

import OG_MayaTools.shape_window as sw
reload(sw)
sw.gui()


'''

import pymel.core as pm
import maya.cmds as cmds
import string
__green__ = 14
__red__ = 13
__blue__ = 6

isNotPersistent = True
sendToOrigin = True


def toast(message):
    cmds.headsUpMessage(message)


def togglePersistence(*args):
    global isNotPersistent
    isNotPersistent = windowPersistence.getValue()


def togglePlacement(*args):
    global sendToOrigin
    sendToOrigin = snapToLocale.getValue()


def validateShape(shapeName):
    shapeName = shapeName.strip()

    # Check for numerics and bad characters

    if shapeName[0] in string.ascii_letters:
        return shapeName
    else:
        return ""


def currentlySelectedItemCoords():
    selectedItems = pm.ls(sl=True)
    if len(selectedItems) < 1:
        toast('There are no items selected.')
        pos = [0, 0, 0]
        return pos
    baseItem = selectedItems[0]
    pX = baseItem.tx.get()
    pY = baseItem.ty.get()
    pZ = baseItem.tz.get()
    return [pX, pY, pZ]


def moveObject(
    objectIdentifier,
    posX,
    posY,
    posZ,
    ):

    objectIdentifier.tx.set(posX)
    objectIdentifier.ty.set(posY)
    objectIdentifier.tz.set(posZ)


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
    return pm.curve(name=shapeTitle, p=[(0.5, 0, 0.5), (-0.5, 0, 0.5),
                    (-0.5, 0, -0.5), (0.5, 0, -0.5), (0.5, 0, 0.5)],
                    k=[0, 1, 2, 3, 4], d=1)


def create_2darrow(shapeTitle):
    return pm.curve(name=shapeTitle, p=[(-0.5, 0, 0), (0, 0, -0.5), (0, 0,
        -0.25), (0.5, 0, -0.25), (0.5, 0, 0.25), (0, 0, 0.25), (0, 0, 0.5),
    (-0.5, 0, 0)], k=[0, 1, 2, 3, 4, 5, 6, 7], d=1)


def create_3darrow(shapeTitle):
    return pm.curve(p=[(-0.5, 0, 0), (0, 0, -0.5), (0, 0, -0.25), (0.5, 0,
        -0.25), (0.5, -4.47035e-08, -4.47035e-08), (0.5, 0.25, 0), (0, 0.25,
        0), (0, 0.5, 0), (-0.5, 0, 0), (0, 0, 0.5), (0, 0, 0.25), (0.5, 0,
        0.25), (0.5, -4.47035e-08, -4.47035e-08), (0.5, -0.25, 0), (0, -0.25,
        0), (0, -0.5, 0), (-0.5, 0, 0)], k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16], d=1)


def create_cube(shapeTitle):
    return pm.curve(name=shapeTitle, p=[(0.5, 0.5, -0.5), (0.5, 0.5, 0.5),
        (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5,
            -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5),
        (-0.5, -0.5, 0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5,
            0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5)],
        k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], d=1)


def create_compass(shapeTitle): 
    newShape = pm.curve(name="Microedge1", p=[(-0.309017, 0, -0.951057),
        (-0.455125, 0, -0.882908), (-0.587785, 0, -0.809017), (-0.710365, 0,
            -0.710365), (-0.809017, 0, -0.587785), (-0.885102, 0, -0.457095),
        (-0.951057, 0, -0.309017)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece1 = newShape
    sidepiece_shape1 = sidepiece1.getShape();
    sidepiece_shape1.overrideEnabled.set(True)
    newShape = pm.curve(name="Microedge2", p=[(0.309017, 0, -0.951057),
        (0.457095, 0, -0.885102), (0.587785, 0, -0.809017), (0.709632, 0,
            -0.70902), (0.809017, 0, -0.587785), (0.885102, 0, -0.457095),
        (0.951057, 0, -0.309017)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece2 = newShape
    sidepiece_shape2 = newShape.getShape();
    sidepiece_shape2.overrideEnabled.set(True)
    newShape = pm.curve(name="Microedge3", p=[(0.951057, 0, 0.309017),
        (0.885102, 0, 0.457095), (0.809017, 0, 0.587785), (0.710365, 0,
            0.710365), (0.587785, 0, 0.809017), (0.455125, 0, 0.882908),
        (0.309017, 0, 0.951057)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece3 = newShape
    sidepiece_shape3 = newShape.getShape();
    sidepiece_shape3.overrideEnabled.set(True)
    newShape = pm.curve(name="Microedge4", p=[(-0.309017, 0, 0.951057),
        (-0.457095, 0, 0.885102), (-0.587785, 0, 0.809017), (-0.710365, 0,
            0.710365), (-0.809017, 0, 0.587785), (-0.882908, 0, 0.455125),
        (-0.951057, 0, 0.309017)], k=[0, 0, 0, 1, 2, 3, 4, 4, 4], d=3)
    sidepiece4 = newShape
    sidepiece_shape4 = newShape.getShape();
    sidepiece_shape4.overrideEnabled.set(True)
    microedge = pm.parent(shape="relative")
    backCompass = pm.curve(name="compassBack", p=[(0.309017, 0, 0.951057),
        (0.309017, 0, 1.296348), (0.548167, 0, 1.296348), (0, 0, 2),
        (-0.548167, 0, 1.296347), (-0.309017, 0, 1.296347), (-0.309017, 0,
            0.951057)], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    leftCompass = pm.curve(name="compassLeft", p=[(0.309017, 0, 0.951057),
        (0.309017, 0, 1.296348), (0.548167, 0, 1.296348), (0, 0, 2),
        (-0.548167, 0, 1.296347), (-0.309017, 0, 1.296347), (-0.309017, 0,
            0.951057)], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    forwardCompass = pm.curve(name="compassForward", p=[(0.309017, 0,
        0.951057), (0.309017, 0, 1.296348), (0.548167, 0, 1.296348), (0, 0,
        2), (-0.548167, 0, 1.296347), (-0.309017, 0, 1.296347), (-0.309017,
        0, 0.951057)], k=[0, 1, 2, 3, 4, 5, 6], d=1)
    rightCompass = pm.curve(name="compassRight", p=[(0.309017, 0, 0.951057),
        (0.309017, 0, 1.296348), (0.548167, 0, 1.296348), (0, 0, 2),
        (-0.548167, 0, 1.296347), (-0.309017, 0, 1.296347), (-0.309017, 0,
            0.951057)], k=[0, 1, 2, 3, 4, 5, 6], d=1)
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
        sidepiece_shape4, newGroup, s=True, r=True)
    pm.parent(forwardCompass_shape, backCompass_shape, leftCompass_shape,
        rightCompass_shape, newGroup, s=True, r=True)
    pm.makeIdentity(newGroup, n=0, s=1, r=1, t=1, apply=True, pn=1)
    pm.delete(sidepiece1, sidepiece2, sidepiece3, sidepiece4)
    pm.delete(forwardCompass, backCompass, leftCompass, rightCompass)
    shapeName = pm.rename(newGroup, shapeTitle)
    return newGroup



def makeShape(shapeName):

    global curveName, validName
    if snapToLocale.getValue():
        posX = 0
        posY = 0
        posZ = 0
    else:

        # Locate what is selected and get its coordinates

        updatedCoords = currentlySelectedItemCoords()
        posX = float(updatedCoords[0])
        posY = float(updatedCoords[1])
        posZ = float(updatedCoords[2])
    if not curveName.getText():
        shapeTitle = shapeName
    else:
        shapeTitle = curveName.getText()

    # Valiidate the shape

    shapeTitle = str(validateShape(shapeTitle))
    if len(shapeTitle) == 0:
        toast('Circle could not be created at this time. Check the name and try again.'
              )
        return
    if suffixEnable.getValue() is True:
        shapeTitle = shapeTitle + suffixName.getText()
    if shapeName == 'circle':
        newCurve = create_circle(shapeTitle)[0]
        toast('Circle created')
    elif shapeName == 'square':
        newCurve = create_square(shapeTitle)
        toast('Square')
    elif shapeName == 'cube':
        newCurve = create_cube(shapeTitle)
    elif shapeName == 'arrow2d':
        newCurve = create_2darrow(shapeTitle)
        return
    elif shapeName == 'arrow3d':
        newCurve = create_3darrow(shapeTitle)
        return
    elif shapeName == 'cog':
        toast("COG Control. Incomplete")
        return
    elif shapeName == 'compass':
        newCurve = create_compass(shapeTitle)
        return
    else:
        toast('Unknown shape.')
        return
    newCurve.tx.set(posX)
    newCurve.ty.set(posY)
    newCurve.tz.set(posZ)
    if isNotPersistent:
        closeWindow()


def closeWindow(*args):
    pm.deleteUI(shapeWindow)


def toggleSuffix(*args):
    suffixLabel.setEnable(suffixEnable.getValue())
    suffixName.setEnable(suffixEnable.getValue())


def gui():
    global windowPersistence, shapeWindow
    global snapToLocale, curveName
    global suffixEnable, suffixLabel, suffixName
    shapeWindow = pm.window(title='Shape Window')
    pm.columnLayout()
    button_width = 100
    pm.rowColumnLayout(nc=4)

    pm.button(label='Create Circle', width=button_width,
              command=pm.Callback(makeShape, 'circle'))
    pm.button(label='Create Square', width=button_width,
              command=pm.Callback(makeShape, 'square'))
    pm.button(label='Create Cube', width=button_width,
              command=pm.Callback(makeShape, 'cube'))
    pm.button(label='Create 2D Arrow', width=button_width,
              command=pm.Callback(makeShape, 'arrow2d'))
    pm.button(label='Create 3D Arrow', width=button_width,
              command=pm.Callback(makeShape, 'arrow3d'))
    pm.button(label='Create COG Circle', width=button_width,
              command=pm.Callback(makeShape, 'cog'))
    pm.button(label='Create Compass', width=button_width,
              command=pm.Callback(makeShape, 'compass'))
    pm.setParent('..')
    pm.text(label='Enter a name. Leave blank for default.')
    curveName = pm.textField(placeholderText='shape')
    suffixEnable = pm.checkBox(label='Insert suffix on creation?',
                               value=True, changeCommand=toggleSuffix)
    pm.rowLayout(nc=2)
    suffixLabel = pm.text(label='Suffix for curve after creation:',
                          enable=True)
    suffixName = pm.textField(text='_icon', enable=True)
    pm.setParent('..')
    windowPersistence = pm.checkBox(label='Window Closes Automatically',
                                    value=isNotPersistent,
                                    changeCommand=togglePersistence)
    snapToLocale = pm.checkBox(label='Place at origin',
                               value=sendToOrigin,
                               changeCommand=togglePlacement)
    pm.showWindow(shapeWindow)
