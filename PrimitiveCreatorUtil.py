import maya.cmds as cmds

def doCreateObject(result, name):
	if result == "cone":
		cmds.polyCone(name = '{name}'.format(name=name))
	elif result == "cube":
		cmds.polyCube(name = '{name}'.format(name=name))
	elif result == "sphere":
		cmds.polySphere(name = '{name}'.format(name=name))
	elif result == "torus":
		cmds.polyTorus(name = '{name}'.format(name=name))
	else :
		cmds.warning("Error")