from PyQt6 import QtCore, QtGui, QtWidgets
from database.users_database import Database

class Window_autorization(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, x2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41,61,132,235), stop:1 rgba(155,79,165,255));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_Login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Button_Login.setGeometry(QtCore.QRect(270, 373, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button_Login.setFont(font)
        self.Button_Login.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
            "border: 1px solid rgba(255,255,255, 0.4);\n"
            "border-radius: 6px;\n"
            "color: white;")
        self.Button_Login.setObjectName("Button_Login")
        self.Button_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Button_exit.setGeometry(QtCore.QRect(394, 373, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Button_exit.setFont(font)
        self.Button_exit.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
            "border: 1px solid rgba(255,255,255, 0.4);\n"
            "border-radius: 6px;\n"
            "color: white;")
        self.Button_exit.setObjectName("Button_exit")
        self.Label_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.Label_password.setGeometry(QtCore.QRect(291, 280, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.Label_password.setFont(font)
        self.Label_password.setStyleSheet("background-color: rgba(39, 176, 87, 0.9);\n"
            "border: 1px solid rgba(255,255,255,40);\n"
            "border-radius: 7px;\n"
            "color: white;")
        self.Label_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_password.setObjectName("Label_password")
        self.Label_login = QtWidgets.QLabel(parent=self.centralwidget)
        self.Label_login.setGeometry(QtCore.QRect(289, 190, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.Label_login.setFont(font)
        self.Label_login.setStyleSheet("background-color: rgba(39, 176, 87, 0.9);\n"
            "border: 1px solid rgba(255,255,255,40);\n"
            "border-radius: 7px;\n"
            "color: white;")
        self.Label_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_login.setObjectName("Label_login")
        self.Lineedit_login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Lineedit_login.setGeometry(QtCore.QRect(270, 230, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Lineedit_login.setFont(font)
        self.Lineedit_login.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
            "border: 1px solid rgba(255,255,255, 0.4);\n"
            "border-radius: 6px;\n"
            "color: white;")
        self.Lineedit_login.setObjectName("Lineedit_login")
        self.Lineedit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Lineedit_password.setGeometry(QtCore.QRect(270, 320, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Lineedit_password.setFont(font)
        self.Lineedit_password.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
            "border: 1px solid rgba(255,255,255, 0.4);\n"
            "border-radius: 6px;\n"
            "color: white;")
        self.Lineedit_password.setObjectName("Lineedit_password")
        self.Label_present = QtWidgets.QLabel(parent=self.centralwidget)
        self.Label_present.setGeometry(QtCore.QRect(100, 110, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Label_present.setFont(font)
        self.Label_present.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
            "border: 1px solid rgba(255,255,255, 0.4);\n"
            "border-radius: 6px;\n"
            "color: white;")
        self.Label_present.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_present.setObjectName("Label_present")
        self.Label_icon_login = QtWidgets.QLabel(parent=self.centralwidget)
        self.Label_icon_login.setGeometry(QtCore.QRect(270, 190, 31, 31))
        self.Label_icon_login.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
            "border: 1px solid rgba(255,255,255,50);\n"
            "border-radius: 7px;")
        self.Label_icon_login.setText("")
        self.Label_icon_login.setPixmap(QtGui.QPixmap(":/icon/icons/login_white_24dp.svg"))
        self.Label_icon_login.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_icon_login.setObjectName("Label_icon_login")
        self.Label_icon_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.Label_icon_password.setGeometry(QtCore.QRect(270, 280, 31, 31))
        self.Label_icon_password.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.Label_icon_password.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
            "border: 1px solid rgba(255,255,255,40);\n"
            "border-radius: 7px;")
        self.Label_icon_password.setText("")
        self.Label_icon_password.setPixmap(QtGui.QPixmap(":/icon/icons/lock_white_24dp.svg"))
        self.Label_icon_password.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_icon_password.setObjectName("Label_icon_password")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NameProgramm- Авторизация"))
        self.Button_Login.setText(_translate("MainWindow", "Войти"))
        self.Button_Login.clicked.connect(self.btn_login)
        self.Button_exit.setText(_translate("MainWindow", "Выйти"))
        self.Label_password.setText(_translate("MainWindow", "Пароль:"))
        self.Label_login.setText(_translate("MainWindow", "Логин:"))
        self.Label_present.setText(_translate("MainWindow", "Здравствуйте, добро пожаловать в мою программу!"))

    def btn_login(self):
        #получаем логин и пароль, введенный пользователем
        login = self.Lineedit_login.text()
        password = self.Lineedit_password.text()

        #очищаем поля ввода логина и пароля
        self.Lineedit_login.clear()
        self.Lineedit_password.clear()

        db = Database()
        user_in_database, message = db.find_user(login, password)

        #если логин и пароль правильны
        if user_in_database:
            #открываем админ-панель
            if message == 'admin':
                MainWindow.close()
            #открываем программу с обычным уровнем доступа
            elif message == 'user':
                MainWindow.close()
        else:
            self.label_error = QtWidgets.QLabel(parent=self.centralwidget)
            self.label_error.setGeometry(QtCore.QRect(510, 190, 190, 30))
            self.label_error.setStyleSheet('background-color: rgba(39, 176, 87, 0.9); border: 1px solid rgba(255,255,255,40); border-radius: 7px; color: white;')
            self.label_error.setText(message)
            self.label_error.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window_autorization()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
