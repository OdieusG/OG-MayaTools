import maya.OpenMaya as om
import maya.cmds as cmds
import maya.mel as mel
import math

"""

Author: Erik Qvarnstrom
Description: Creates PoleVector Object at correct position and rotation for a 3 bone IK-chain. 

Installation: 
Add this file to your maya scripts folder. 
In maya: 
Open up the maya script editor and create new Python script. 
Paste the following: 
_______________________________________________________________
import eq_createPV
eq_createPV.createPoleVector(cmds.ls(sl=1)))

_______________________________________________________________
Select and middlemouse drag the script to add it to your shelf. 

Select |Shoulder -> Elbow -> Hand| or equivalent for the legs in that order and run the code above.
A PoleVector constraint can then be added with no changed rotations on the constrained IK-chain. 

"""

# Vector Math to calculate pole vector position.
def findPvPos(jointList):
    shoulder = jointList[0]
    elbow = jointList[1]
    wrist = jointList[2]

    wa = createVector(shoulder)
    wb = createVector(elbow)
    wc = createVector(wrist)

    ab = wb-wa
    ac = wc-wa

    acNorm = ac.normal() * -1
    dot = acNorm * ab
    acDot = acNorm * dot
    pvFv = ab - acDot
    pvFvNorm = pvFv.normal()
    pvFvOffset = pvFvNorm * ac.length()/2 # PoleVector Distance
    pvPos = wb + pvFvOffset

    return pvPos

# Vector Math to calculate pole vector rotation.
def findPvRot(jointList):
    shoulder = jointList[0]
    elbow = jointList[1]
    wrist = jointList[2]

    wa = createVector(shoulder)
    wb = createVector(elbow)
    wc = createVector(wrist)

    ab = wb-wa
    ac = wc-wa

    acNorm = ac.normal() * -1
    dot = acNorm * ab
    acDot = acNorm * dot
    pvFv = ab - acDot
    pvFvNorm = pvFv.normal()

    upV = ac ^ ab
    upVNorm = upV.normal() * -1

    matrix = [pvFvNorm.x, pvFvNorm.y, pvFvNorm.z, 0,
              acNorm.x, acNorm.y, acNorm.z, 0,
              upVNorm.x, upVNorm.y, upVNorm.z, 0,
              0, 0, 0, 1]

    mMatrix = om.MMatrix()
    om.MScriptUtil_createMatrixFromList(matrix, mMatrix)
    mMatrix = om.MTransformationMatrix(mMatrix)
    pvRotPos = mMatrix.eulerRotation()

    return pvRotPos


def createPoleVector(jointList):
    if len(jointList) == 3:

        side = checkTx(jointList[1])

        pvPos = findPvPos(jointList)
        pvRotPos = findPvRot(jointList)

        object = create_PV_Object(pvPos, pvRotPos, side)

        createLineCurve(jointList[1], object)

        return object
    else:
        print 'You need to select a three object chain to calculate PoleVector Position'

# Check if chain is left or right.
def checkTx(object):
    if cmds.xform(object, q=True, worldSpace=True, translation=True)[0] > 0:
        return '_l'
    elif cmds.xform(object, q=True, worldSpace=True, translation=True)[0] < 0:
        return '_r'
    else:
        return ''

def createVector(node=None):
    pos = cmds.xform(node, query=True, worldSpace=True, translation=True)
    vector = om.MVector(pos[0], pos[1], pos[2])
    return vector

# Create a line going from the poleVector to the Knee.
def createLineCurve(knee, pv):
    points = [(0, 0, 0), (0, 0, 1)]
    line = cmds.curve(d=1, p=points, n=knee + '_to_' + pv + '_line')
    lineShape = cmds.listRelatives(line, shapes=True)[0]
    point1 = lineShape+'.controlPoints[0]'
    point2 = lineShape+'.controlPoints[1]'

    dec1 = cmds.createNode('decomposeMatrix', n=knee + '_pvLine_decomposeMatrix')
    mult1 = cmds.createNode('multMatrix', n=knee + '_pvLine_multMatrix')
    cmds.connectAttr(knee + '.worldMatrix[0]', mult1 + '.matrixIn[0]')
    cmds.connectAttr(lineShape + '.parentInverseMatrix[0]', mult1 + '.matrixIn[1]')
    cmds.connectAttr(mult1 + '.matrixSum', dec1 + '.inputMatrix')
    cmds.connectAttr(dec1+'.outputTranslate', point1)

    dec2 = cmds.createNode('decomposeMatrix', n=pv + '_pvLine_decomposeMatrix')
    mult2 = cmds.createNode('multMatrix', n=pv + '_pvLine_multMatrix')
    cmds.connectAttr(pv + '.worldMatrix[0]', mult2 + '.matrixIn[0]')
    cmds.connectAttr(lineShape + '.parentInverseMatrix[0]', mult2 + '.matrixIn[1]')
    cmds.connectAttr(mult2 + '.matrixSum', dec2 + '.inputMatrix')
    cmds.connectAttr(dec2+'.outputTranslate', point2)

    cmds.select(pv)
    mel.eval('parent -r -shape %s'%lineShape)
    cmds.delete(line)
    cmds.select(pv)

# Create object under a buffer group and moves it to specified position and rotation.
def create_PV_Object(pos, rot, side):
    name = "poleVector_anim%s" % side

    group = cmds.group(empty=True, name=name + '_grp')

    # Create a nice looking nurb sphere.
    points = [(0, 3.21, 0), (0, 2.96, 1.23), (0, 2.27, 2.27), (0, 1.23, 2.96), (0, 0, 3.21), (0, -1.23, 2.96), (0, -2.27, 2.27), (0, -2.97, 1.23), (0, -3.21, 0), (0, -2.96, -1.23), (0, -2.27, -2.27), (0, -1.23, -2.96), (0, 0, -3.21), (0, 1.23, -2.96), (0, 2.27, -2.27), (0, 2.96, -1.23), (0, 3.21, 0), (-0.87, 2.96, 0.97), (-1.60, 2.27, 1.60), (-2.09, 1.23, 2.09),
    (-2.27, 0, 2.27), (-2.09, -1.23, 2.09), (-1.60, -2.27, 1.60), (-0.87, -2.96, 0.87), (0, -3.21, 0), (0.87, -2.97, -0.87), (1.60, -2.27, -1.60), (2.09, -1.23, -2.09), (2.27, 0, -2.27), (2.09, 1.23, -2.09), (1.60, 2.27, -1.60), (0.87, 2.86, -0.87), (0, 3.21, 0), (-1.23, 2.97, 0), (-2.27, 2.27, 0), (-2.97, 1.23, 0), (-3.21, 0, 0), (-2.97, -1.23, 0),
    (-2.27, -2.27, 0), (-1.23, -2.96, 0), (0, -3.21, 0), (1.23, -2.97, 0), (2.27, -2.27, 0), (2.97, -1.23, 0), (3.21, 0, 0), (2.97, 1.23, 0), (2.27, 2.27, 0), (1.23, 2.97, 0), (0, 3.21, 0), (-0.87, 2.97, -0.87), (-1.60, 2.27, -1.60), (-2.09, 1.23, -2.09), (-2.27, 0, -2.27), (-2.09, -1.23, -2.09), (-1.60, -2.27, -1.60), (-0.87, -2.96, -0.87), (0, -3.21, 0),
    (0.87, -2.97, 0.87), (1.60, -2.27, 1.60), (2.09, -1.23, 2.09), (2.27, 0, 2.27), (2.09, 1.23, 2.09), (1.60, 2.27, 1.60), (0.87, 2.97, 0.87), (0, 3.21, 0), (1.23, 2.97, 0), (2.27, 2.27, 0), (2.97, 1.23, 0), (3.21, 0, 0), (2.27, 0, 2.27), (0, 0, 3.21), (-2.27, 0, 2.27), (-3.21, 0, 0), (-2.27, 0, -2.27), (0, 0, -3.21), (2.27, 0, -2.27), (3.21, 0, 0), (2.27, 0, 2.27), (0, 0, 3.21)]
    object = cmds.curve(d=1, p=points, name=name)
    cmds.setAttr(object+'.scale', 0.15, 0.15, 0.15)
    cmds.makeIdentity(object, t=0, r=0, s=1, apply=True)

    cmds.parent(object, group)
    cmds.xform(group, worldSpace=True, translation=[pos.x, pos.y, pos.z])
    r2d2 = 1/math.pi*180
    rot *= r2d2
    cmds.xform(group, worldSpace=True, rotation=[rot.x, rot.y, rot.z])
    return object