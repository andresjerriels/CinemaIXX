# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addFilm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from db import database
import pathlib

class Ui_AddFilmPage(QtWidgets.QWidget):
    def setupUi(self, AddFilmPage):
        self.filename = ""
        AddFilmPage.setObjectName("AddFilmPage")
        AddFilmPage.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(AddFilmPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/bg/AdminPage.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(28, 670, 160, 48))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.logout.setFont(font)
        self.logout.setStyleSheet("background-color: #0984E3;\n"
"color: rgb(255,255,255);\n"
"")
        self.logout.setObjectName("logout")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(28, 600, 160, 48))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setStyleSheet("background-color: #0984E3;\n"
"color: rgb(255,255,255);\n"
"")
        self.backButton.setObjectName("backButton")
        self.labelPoster = QtWidgets.QLabel(self.centralwidget)
        self.labelPoster.setGeometry(QtCore.QRect(580, 400, 251, 331))
        self.labelPoster.setText("")
        self.labelPoster.setObjectName("labelPoster")
        self.labelPoster.setScaledContents(True)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(270, 110, 671, 481))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.titleInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.titleInput.setFont(font)
        self.titleInput.setObjectName("titleInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleInput)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.synopsisInput = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.synopsisInput.setMaximumSize(QtCore.QSize(16777215, 150))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        self.synopsisInput.setFont(font)
        self.synopsisInput.setObjectName("synopsisInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.synopsisInput)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.yearSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.yearSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.yearSpinBox.setMaximum(999999999)
        self.yearSpinBox.setObjectName("yearSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.yearSpinBox)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.priceSpinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.priceSpinBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.priceSpinBox.setMaximum(999999999)
        self.priceSpinBox.setObjectName("priceSpinBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.priceSpinBox)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.browseButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.browseButton.setMinimumSize(QtCore.QSize(0, 31))
        self.browseButton.setMaximumSize(QtCore.QSize(71, 16777215))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.browseButton.setFont(font)
        self.browseButton.setStyleSheet("background-color: #0984E3;\n"
"color: rgb(255,255,255);\n"
"")
        self.browseButton.setObjectName("browseButton")
        self.browseButton.clicked.connect(self.getImageFile)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.browseButton)
        self.submitFilmButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitFilmButton.setGeometry(QtCore.QRect(270, 610, 101, 40))
        self.submitFilmButton.setMinimumSize(QtCore.QSize(101, 0))
        self.submitFilmButton.setMaximumSize(QtCore.QSize(16777215, 71))
        self.submitFilmButton.clicked.connect(self.addNewFilm)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(True)
        font.setWeight(75)
        self.submitFilmButton.setFont(font)
        self.submitFilmButton.setStyleSheet("background-color: #0984E3;\n"
"color: rgb(255,255,255);\n"
"")
        self.submitFilmButton.setObjectName("submitFilmButton")
        AddFilmPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddFilmPage)
        QtCore.QMetaObject.connectSlotsByName(AddFilmPage)

    def getImageFile(self):
        self.filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Film Poster", str(pathlib.Path(__file__).parent.absolute()), "Image files (*.jpg *.jpeg *.png)")
        self.labelPoster.setPixmap(QtGui.QPixmap(self.filename))

    def convertToBinaryData(self, filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    
    def addNewFilm(self):
        if self.filename == "" or self.titleInput.text() == "" or self.synopsisInput.toPlainText() == "":
            self.showAlert('Please fill the form')
        else:
            filmData = (self.titleInput.text(), self.synopsisInput.toPlainText(), self.yearSpinBox.value(), self.convertToBinaryData(self.filename), self.priceSpinBox.value(), 0)
            connection = database.connect()
            database.addFilm(connection, filmData)
            self.backButton.click()
    
    def clearInputs(self):
        self.titleInput.setText("")
        self.synopsisInput.setText("")
        self.yearSpinBox.setValue(0)
        self.priceSpinBox.setValue(0)
        self.labelPoster.setPixmap(QtGui.QPixmap())

    def showAlert(self,err):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(err)
        msg.exec_()

    def retranslateUi(self, AddFilmPage):
        _translate = QtCore.QCoreApplication.translate
        AddFilmPage.setWindowTitle(_translate("AddFilmPage", "Cinema IXX"))
        self.logout.setText(_translate("AddFilmPage", "LOG OUT"))
        self.backButton.setText(_translate("AddFilmPage", "BACK"))
        self.label_2.setText(_translate("AddFilmPage", "Title                     :"))
        self.label_4.setText(_translate("AddFilmPage", "Synopsis            :"))
        self.label_3.setText(_translate("AddFilmPage", "Release Year     :"))
        self.label_5.setText(_translate("AddFilmPage", "Price                     :"))
        self.label_6.setText(_translate("AddFilmPage", "Poster                  :"))
        self.browseButton.setText(_translate("AddFilmPage", "Browse"))
        self.submitFilmButton.setText(_translate("AddFilmPage", "Add Film"))
import admin_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddFilmPage = QtWidgets.QMainWindow()
    ui = Ui_AddFilmPage()
    ui.setupUi(AddFilmPage)
    AddFilmPage.show()
    sys.exit(app.exec_())
