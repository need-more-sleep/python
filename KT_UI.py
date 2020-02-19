# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dyd52\Desktop\pyqt_study\KT_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(628, 498)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 551, 121))
        self.label.setStyleSheet("font: 87 38pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(36, 230, 181, 51))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(223, 230, 181, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 230, 181, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 182, 171, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 150, 591, 141))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(240, 0, 101, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 360, 131, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 360, 131, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(20, 320, 591, 141))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(240, 0, 101, 20))
        self.label_3.setObjectName("label_3")
        self.frame_2.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "KT 데이터 변환 EXE"))
        self.pushButton_1.setText(_translate("Dialog", "OUTPUT : KT_trans1_1.txt"))
        self.pushButton_2.setText(_translate("Dialog", "OUTPUT : kt_trans1_2(A,B)"))
        self.pushButton_3.setText(_translate("Dialog", "OUTPUT : kt_trans2(A,B)"))
        self.pushButton_4.setText(_translate("Dialog", "INPUT : data"))
        self.label_2.setText(_translate("Dialog", "Raw Data 변환"))
        self.pushButton_5.setText(_translate("Dialog", "INPUT : data"))
        self.pushButton_6.setText(_translate("Dialog", "OUTPUT : 시나리오"))
        self.label_3.setText(_translate("Dialog", "시나리오 변환"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

