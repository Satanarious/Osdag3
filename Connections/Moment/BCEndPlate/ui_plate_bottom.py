# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_plate_bottom.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Plate_Bottom(object):
    def setupUi(self, Plate_Bottom):
        Plate_Bottom.setObjectName("Plate_Bottom")
        Plate_Bottom.resize(287, 227)
        self.gridLayout = QtWidgets.QGridLayout(Plate_Bottom)
        self.gridLayout.setObjectName("gridLayout")
        self.plateHeight = QtWidgets.QLabel(Plate_Bottom)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.plateHeight.setFont(font)
        self.plateHeight.setObjectName("plateHeight")
        self.gridLayout.addWidget(self.plateHeight, 1, 0, 1, 1)
        self.txt_plateThickness = QtWidgets.QLineEdit(Plate_Bottom)
        self.txt_plateThickness.setObjectName("txt_plateThickness")
        self.gridLayout.addWidget(self.txt_plateThickness, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(Plate_Bottom)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txt_plateWidth = QtWidgets.QLineEdit(Plate_Bottom)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_plateWidth.setFont(font)
        self.txt_plateWidth.setReadOnly(True)
        self.txt_plateWidth.setObjectName("txt_plateWidth")
        self.gridLayout.addWidget(self.txt_plateWidth, 2, 1, 1, 1)
        self.txt_plateLength = QtWidgets.QLineEdit(Plate_Bottom)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.txt_plateLength.setFont(font)
        self.txt_plateLength.setReadOnly(True)
        self.txt_plateLength.setObjectName("txt_plateLength")
        self.gridLayout.addWidget(self.txt_plateLength, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Plate_Bottom)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Plate_Bottom)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.txt_plateno = QtWidgets.QLineEdit(Plate_Bottom)
        self.txt_plateno.setObjectName("txt_plateno")
        self.gridLayout.addWidget(self.txt_plateno, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Plate_Bottom)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.txt_WeldSize = QtWidgets.QLineEdit(Plate_Bottom)
        self.txt_WeldSize.setObjectName("txt_WeldSize")
        self.gridLayout.addWidget(self.txt_WeldSize, 6, 1, 1, 1)
        self.txt_NotchSize = QtWidgets.QLineEdit(Plate_Bottom)
        self.txt_NotchSize.setObjectName("txt_NotchSize")
        self.gridLayout.addWidget(self.txt_NotchSize, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Plate_Bottom)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.retranslateUi(Plate_Bottom)
        QtCore.QMetaObject.connectSlotsByName(Plate_Bottom)

    def retranslateUi(self, Plate_Bottom):
        _translate = QtCore.QCoreApplication.translate
        Plate_Bottom.setWindowTitle(_translate("Plate_Bottom", "Bottom Continuity Plate"))
        self.plateHeight.setText(_translate("Plate_Bottom", "Length (mm)"))
        self.label.setText(_translate("Plate_Bottom", "Number"))
        self.label_2.setText(_translate("Plate_Bottom", "Width (mm)"))
        self.label_4.setText(_translate("Plate_Bottom", "Thickness(mm)"))
        self.label_5.setText(_translate("Plate_Bottom", "Weld Size(mm)"))
        self.label_6.setText(_translate("Plate_Bottom", "Notch Size(mm)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Plate_Bottom = QtWidgets.QDialog()
    ui = Ui_Plate_Bottom()
    ui.setupUi(Plate_Bottom)
    Plate_Bottom.show()
    sys.exit(app.exec_())

