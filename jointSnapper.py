'''
Joint snapper
1.0

Snaps pads and controls to joint that alre already established

How to run:

import OG_MayaTools.jointSnapper as js
reload(js)
js.gui()
'''

import pymel.core as pm
import maya.cmds as cmds
import string



def gui():
	snapperWindow = pm.window()
	pm.columnLayout()
	pm.frameLayout(collapsable=True, label='Create padding')
	pm.button(label='Create pad on joint')
	pm.button(label='Pad control and joint')
	pm.button(label='Test button')
	pm.setParent('..')
	pm.frameLayout(collapsable=True, label='Snap to...')
	pm.scrollLayout(height=60)
	pm.text(label='field')
	pm.text(label='field')
	pm.text(label='field')
	pm.text(label='field')
	pm.text(label='field')
	pm.text(label='field')
	pm.text(label='field')
	pm.setParent('..')
	pm.button()


	snapperWindow.show()