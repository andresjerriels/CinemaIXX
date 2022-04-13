from PyQt5 import QtCore, QtGui, QtWidgets
from db import database
from listfilm import UI_ListFilm
from account import Ui_cinemaIXX
from mymovies import Ui_MyMovies

class CustomerMainWindow(QtWidgets.QMainWindow):
    def __init__(self, id=-1, parent=None):
        super(CustomerMainWindow, self).__init__(parent)

        # Init list film page
        self.Window_ListFilm = QtWidgets.QWidget()
        self.uiListFilm = UI_ListFilm()
        self.uiListFilm.setupUi(self.Window_ListFilm, id)
        self.uiListFilm.myMoviesButton.clicked.connect(self.startUIMyMovies)
        self.uiListFilm.accountButton.clicked.connect(self.startUIAccount)
        
        # Init mymovies page
        self.Window_MyMovies = QtWidgets.QMainWindow()
        self.uiMyMovies = Ui_MyMovies()
        self.uiMyMovies.setupUi(self.Window_MyMovies, id)
        self.uiMyMovies.home.clicked.connect(self.startUIListFilm)
        self.uiMyMovies.account.clicked.connect(self.startUIAccount)

        # Init account page
        self.Window_Account = QtWidgets.QMainWindow()
        self.uiAccount = Ui_cinemaIXX()
        self.uiAccount.setupUi(self.Window_Account, id)
        self.uiAccount.home.clicked.connect(self.startUIListFilm)
        self.uiAccount.mymovies.clicked.connect(self.startUIMyMovies)

        self.startUIListFilm()        

    def startUIListFilm(self):
        self.Window_MyMovies.hide()
        self.Window_Account.hide()
        self.uiListFilm.displayFilms()
        self.Window_ListFilm.show()

    def startUIMyMovies(self):
        self.Window_ListFilm.hide()
        self.Window_Account.hide()
        self.uiMyMovies.displayFilms()
        self.Window_MyMovies.show()

    def startUIAccount(self):
        self.Window_ListFilm.hide()
        self.Window_MyMovies.hide()
        self.Window_Account.show()

if __name__ == "__main__":
    import sys
    connection = database.connect()
    database.create_tables(connection)

    app = QtWidgets.QApplication(sys.argv)
    CustomerPage = CustomerMainWindow()
    sys.exit(app.exec_())
