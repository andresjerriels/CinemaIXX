from PyQt5 import QtCore, QtGui, QtWidgets
from db import database
from addFilm import Ui_AddFilmPage
from admin import Ui_AdminPage

class AdminMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AdminMainWindow, self).__init__(parent)

        # Init admin page
        self.UI_AdminPage = QtWidgets.QMainWindow()
        self.uiAdmin = Ui_AdminPage()
        self.uiAdmin.setupUi(self.UI_AdminPage)
        self.uiAdmin.addFilmButton.clicked.connect(self.startUIAddFilm)

        # Init add film page
        self.UI_AddFilmPage = QtWidgets.QMainWindow()
        self.uiAddFilm = Ui_AddFilmPage()
        self.uiAddFilm.setupUi(self.UI_AddFilmPage)
        self.uiAddFilm.backButton.clicked.connect(self.startUIAdmin)

        self.startUIAdmin()        

    def startUIAdmin(self):
        self.uiAddFilm.clearInputs()
        self.UI_AddFilmPage.hide()
        self.uiAdmin.displayFilms()
        self.UI_AdminPage.show()

    def startUIAddFilm(self):
        self.UI_AdminPage.hide()
        self.UI_AddFilmPage.show()

if __name__ == "__main__":
    import sys
    connection = database.connect()
    database.create_tables(connection)

    app = QtWidgets.QApplication(sys.argv)
    AdminPage = AdminMainWindow()
    sys.exit(app.exec_())
