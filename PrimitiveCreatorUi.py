try:
	from PySide6 import QtCore,QtGui,QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore,QtGui,QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui

import os
import importlib
from . import PrimitiveCreatorUtil as primUtil
importlib.reload(primUtil)

ICON_PATH = os.path.join(os.path.dirname(__file__),'icons').replace("\\","/")

class PrimativeCreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)

		self.resize(300,300)
		self.setWindowTitle("Primative Creator")

		self.main_layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.prim_listWidget = QtWidgets.QListWidget()
		self.prim_listWidget.setIconSize(QtCore.QSize(50,50))
		self.prim_listWidget.setSpacing(8)
		self.prim_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.prim_listWidget.setMovement(QtWidgets.QListView.Static)
		self.prim_listWidget.setResizeMode(QtWidgets.QListView.Adjust)

		self.main_layout.addWidget(self.prim_listWidget)

		self.name_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.name_layout)

		self.name_label = QtWidgets.QLabel("Name :")
		self.name_lineEdit = QtWidgets.QLineEdit()
		self.name_lineEdit.setStyleSheet('background-color: white; color:blue; font-family:Caveat')
		self.name_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_lineEdit)

		self.button_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)

		self.create_button = QtWidgets.QPushButton(" Create👌 ")
		self.create_button.clicked.connect(self.onClickedCreateOBJ)
		self.cancel_button = QtWidgets.QPushButton(" Cancel💀 ")
		self.cancel_button.clicked.connect(self.close)

		self.button_layout.addStretch()
		self.button_layout.addWidget(self.create_button)
		self.create_button.setStyleSheet(
			'''
			QPushButton{
				background-color:red;
			}
			'''
		)

		self.button_layout.addWidget(self.cancel_button)


		self.initIconWidgets()



	def initIconWidgets(self):
		prims = ["cone","cube","sphere","torus"]
		for prim in prims:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH, "{0}.png".format(prim))))
			self.prim_listWidget.addItem(item)

	def onClickedCreateOBJ(self):
		result = self.prim_listWidget.currentItem().text()
		name = self.name_lineEdit.text()
		primUtil.doCreateObject(result, name)

def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)
	ui = PrimativeCreatorDialog(parent = ptr)
	ui.show()