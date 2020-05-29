'''
Simple script for Technical Animation

Gabriel Perro

- USAGE

import TAScript as mainScript
reload(mainscript)
mainScript.gui()
'''
import pymel.core as pm


def renameJoints(*args):
	oriOpt = orient_option.getValue()
	baseName = txtName.getText()
	print baseName
	if oriOpt == "Left":
		oriPrefix = "lt"
	elif oriOpt == "Center":
		oriPrefix = "ct"
	else:
		oriPrefix = "rt"
	# Collect the joints into a DAG array
	currentCollection = pm.ls(sl=True, dag=True)
	print currentCollection
	i=0
	jointMax=len(currentCollection)
	for joint in currentCollection:
		i = i + 1
		print "increment " + str(i) + " of " + str(jointMax)
		if i<jointMax:
			suffix = txtBaseSuffix.getText()
		else:
			suffix = txtFinalSuffix.getText()
		newName = "{0}_{1}_{2:02d}_{3}".format(oriPrefix, baseName, i, suffix)
		print "renaming to " + newName
		pm.rename(joint, newName)
		


def fkikJoints(*args):
	print "FK/IK conversion for limbs"

def gui():
	global orient_option, txtName, txtBaseSuffix, txtFinalSuffix
	TAWindow = pm.window(title="Joint Renamer", width=300, height=300)
	pm.scrollLayout(verticalScrollBarAlwaysVisible=True)

	#Frame layout 1 begin
	pm.frameLayout(collapsable=True, label="Joint Renamer")

	pm.rowLayout(numberOfColumns=2)
	pm.text(label="Orientation")
	orient_option = pm.optionMenu(width=100)
	pm.menuItem(label="Left")
	pm.menuItem(label="Center")
	pm.menuItem(label="Right")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2)
	pm.text(label="Name")
	txtName = pm.textField(text="base")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2)
	pm.text(label="Common suffix")
	txtBaseSuffix = pm.textField(text="bind")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=2)
	pm.text(label="Final joint suffix")
	txtFinalSuffix = pm.textField(text="waste")
	pm.setParent("..")

	pm.rowLayout(numberOfColumns=1)
	pm.button(label="Apply", command=pm.Callback(renameJoints))
	pm.setParent("..")

	pm.setParent("..") # Frame layout 1 end

	# Frame layout 2 begin
	pm.frameLayout(collapsable=True, label="FK/IK Conversion")
	pm.rowLayout(numberOfColumns=2)
	pm.button(label="Convert")
	pm.setParent("..")

	pm.setParent("..") # Frame layout 2 end

	TAWindow.show()