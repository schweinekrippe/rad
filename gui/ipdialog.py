# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogIP.ui'
#
# Created: Tue Jul 04 10:32:28 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(170, 100)
        Dialog.setMinimumSize(QtCore.QSize(170, 100))
        Dialog.setMaximumSize(QtCore.QSize(170, 100))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-180, 70, 341, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 171, 71))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 121, 22))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit_3 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setMaxLength(3)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setMaxLength(3)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_5.setMaxLength(3)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.horizontalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_2 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(39, 1, 121, 21))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setMaxLength(5)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 31, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "IP config", None))
        self.lineEdit_3.setText(_translate("Dialog", "168", None))
        self.lineEdit_4.setText(_translate("Dialog", "192", None))
        self.lineEdit_5.setText(_translate("Dialog", "1", None))
        self.lineEdit_2.setText(_translate("Dialog", "1", None))
        self.label.setText(_translate("Dialog", "IP", None))
        self.lineEdit.setText(_translate("Dialog", "9999", None))
        self.label_2.setText(_translate("Dialog", "Port", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

