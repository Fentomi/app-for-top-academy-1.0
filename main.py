from PyQt6 import QtCore, QtGui, QtWidgets
from database.database_controller import Database

class Ui_authorization(object):
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
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NameProgramm- Авторизация"))
        self.Button_Login.setText(_translate("MainWindow", "Войти"))
        self.Button_exit.setText(_translate("MainWindow", "Выйти"))
        self.Label_password.setText(_translate("MainWindow", "Пароль:"))
        self.Label_login.setText(_translate("MainWindow", "Логин:"))
        self.Label_present.setText(_translate("MainWindow", "Здравствуйте, добро пожаловать в мою программу!"))

        self.Button_exit.clicked.connect(self.exit)
        self.Button_Login.clicked.connect(self.btn_login)

    def btn_login(self):
        # получаем логин и пароль, введенный пользователем
        login = self.Lineedit_login.text()
        password = self.Lineedit_password.text()
        self.Lineedit_login.clear()
        self.Lineedit_password.clear()
        # создаем экземпляр класса Database
        db = Database()
        user_in_database, message = db.find_user(login, password)
        # если логин и пароль правильны
        if user_in_database:
            # открываем админ-панель
            if message == 'admin':
                MainWindow.resize(888, 600)
                MainWindow.setCentralWidget(MainWindow1)
            # открываем программу с обычным уровнем доступа
            elif message == 'user':
                MainWindow.close()
        else:
            self.label_error = QtWidgets.QLabel(parent=self.centralwidget)
            self.label_error.setGeometry(QtCore.QRect(510, 190, 190, 30))
            self.label_error.setStyleSheet(
                'background-color: rgba(39, 176, 87, 0.9); border: 1px solid rgba(255,255,255,40); border-radius: 7px; color: white;')
            self.label_error.setText(message)
            self.label_error.show()
    def exit(self):
        MainWindow.close()

class Ui_adminpanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 600)
        font = QtGui.QFont()
        font.setPointSize(17)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, x2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41,61,132,235), stop:1 rgba(155,79,165,255));")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.present_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.present_label.setGeometry(QtCore.QRect(120, 30, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.present_label.setFont(font)
        self.present_label.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                         "border: 1px solid rgba(255,255,255, 0.4);\n"
                                         "border-radius: 6px;\n"
                                         "color: white;")
        self.present_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.present_label.setObjectName("present_label")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 90, 231, 341))
        self.label.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                 "border: 1px solid rgba(255,255,255, 0.4);\n"
                                 "border-radius: 6px;\n"
                                 "color: white;")
        self.label.setText("")
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 211, 31))
        self.label_2.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                   "border: 1px solid rgba(255,255,255, 0.4);\n"
                                   "border-radius: 6px;\n"
                                   "color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_add_user = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_add_user.setGeometry(QtCore.QRect(70, 350, 211, 31))
        self.btn_add_user.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                        "border: 1px solid rgba(255,255,255, 0.4);\n"
                                        "border-radius: 6px;\n"
                                        "color: white;")
        self.btn_add_user.setObjectName("btn_add_user")
        self.btn_delete_user = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_delete_user.setGeometry(QtCore.QRect(70, 390, 211, 31))
        self.btn_delete_user.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                           "border: 1px solid rgba(255,255,255, 0.4);\n"
                                           "border-radius: 6px;\n"
                                           "color: white;")
        self.btn_delete_user.setObjectName("btn_delete_user")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 90, 231, 201))
        self.label_4.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                   "border: 1px solid rgba(255,255,255, 0.4);\n"
                                   "border-radius: 6px;\n"
                                   "color: white;")
        self.label_4.setText("")
        self.label_4.setWordWrap(False)
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 90, 211, 31))
        self.label_5.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                   "border: 1px solid rgba(255,255,255, 0.4);\n"
                                   "border-radius: 6px;\n"
                                   "color: white;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 300, 231, 171))
        self.label_3.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                   "border: 1px solid rgba(255,255,255, 0.4);\n"
                                   "border-radius: 6px;\n"
                                   "color: white;")
        self.label_3.setText("")
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 310, 211, 31))
        self.label_7.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                   "border: 1px solid rgba(255,255,255, 0.4);\n"
                                   "border-radius: 6px;\n"
                                   "color: white;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.btn_add_learntype = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_add_learntype.setGeometry(QtCore.QRect(380, 390, 211, 31))
        self.btn_add_learntype.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                             "border: 1px solid rgba(255,255,255, 0.4);\n"
                                             "border-radius: 6px;\n"
                                             "color: white;")
        self.btn_add_learntype.setObjectName("btn_add_learntype")
        self.btn_delete_learntype = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_delete_learntype.setGeometry(QtCore.QRect(380, 430, 211, 31))
        self.btn_delete_learntype.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                                "border: 1px solid rgba(255,255,255, 0.4);\n"
                                                "border-radius: 6px;\n"
                                                "color: white;")
        self.btn_delete_learntype.setObjectName("btn_delete_learntype")
        self.lineEdit_learntype = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_learntype.setGeometry(QtCore.QRect(380, 350, 211, 31))
        self.lineEdit_learntype.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
                                              "border: 1px solid rgba(255,255,255, 0.4);\n"
                                              "border-radius: 6px;\n"
                                              "color: white;")
        self.lineEdit_learntype.setText("")
        self.lineEdit_learntype.setObjectName("lineEdit_learntype")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(620, 90, 231, 201))
        self.label_6.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                   "border: 1px solid rgba(255,255,255, 0.4);\n"
                                   "border-radius: 6px;\n"
                                   "color: white;")
        self.label_6.setText("")
        self.label_6.setWordWrap(False)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(630, 90, 211, 31))
        self.label_8.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                   "border: 1px solid rgba(255,255,255, 0.4);\n"
                                   "border-radius: 6px;\n"
                                   "color: white;")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(620, 300, 231, 171))
        self.label_10.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                    "border: 1px solid rgba(255,255,255, 0.4);\n"
                                    "border-radius: 6px;\n"
                                    "color: white;")
        self.label_10.setText("")
        self.label_10.setWordWrap(False)
        self.label_10.setIndent(-1)
        self.label_10.setObjectName("label_10")
        self.lineEdit_learntime = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_learntime.setGeometry(QtCore.QRect(630, 350, 211, 31))
        self.lineEdit_learntime.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
                                              "border: 1px solid rgba(255,255,255, 0.4);\n"
                                              "border-radius: 6px;\n"
                                              "color: white;")
        self.lineEdit_learntime.setText("")
        self.lineEdit_learntime.setObjectName("lineEdit_learntime")
        self.btn_add_learntime = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_add_learntime.setGeometry(QtCore.QRect(630, 390, 211, 31))
        self.btn_add_learntime.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                             "border: 1px solid rgba(255,255,255, 0.4);\n"
                                             "border-radius: 6px;\n"
                                             "color: white;")
        self.btn_add_learntime.setObjectName("btn_add_learntime")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(630, 310, 211, 31))
        self.label_11.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                    "border: 1px solid rgba(255,255,255, 0.4);\n"
                                    "border-radius: 6px;\n"
                                    "color: white;")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.btn_delete_learntime = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_delete_learntime.setGeometry(QtCore.QRect(630, 430, 211, 31))
        self.btn_delete_learntime.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                                "border: 1px solid rgba(255,255,255, 0.4);\n"
                                                "border-radius: 6px;\n"
                                                "color: white;")
        self.btn_delete_learntime.setObjectName("btn_delete_learntime")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 130, 151, 31))
        self.label_9.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                   "border: 1px solid rgba(255,255,255, 0.4);\n"
                                   "border-radius: 6px;\n"
                                   "color: white;")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(70, 200, 151, 31))
        self.label_12.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                    "border: 1px solid rgba(255,255,255, 0.4);\n"
                                    "border-radius: 6px;\n"
                                    "color: white;")
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.lineEdit_login = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_login.setGeometry(QtCore.QRect(70, 160, 211, 31))
        self.lineEdit_login.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
                                          "border: 1px solid rgba(255,255,255, 0.4);\n"
                                          "border-radius: 6px;\n"
                                          "color: white;")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(70, 270, 161, 31))
        self.label_13.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                    "border: 1px solid rgba(255,255,255, 0.4);\n"
                                    "border-radius: 6px;\n"
                                    "color: white;")
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.comboBox_access = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_access.setGeometry(QtCore.QRect(70, 300, 211, 31))
        self.comboBox_access.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
                                           "border: 1px solid rgba(255,255,255, 0.4);\n"
                                           "color: white;")
        self.comboBox_access.setObjectName("comboBox_access")
        self.comboBox_access.addItem("")
        self.comboBox_access.addItem("")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_password.setGeometry(QtCore.QRect(70, 230, 211, 31))
        self.lineEdit_password.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
                                             "border: 1px solid rgba(255,255,255, 0.4);\n"
                                             "border-radius: 6px;\n"
                                             "color: white;")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.btn_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(706, 540, 171, 41))
        self.btn_exit.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                    "border: 1px solid rgba(255,255,255, 0.4);\n"
                                    "border-radius: 6px;\n"
                                    "color: white;")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_logout = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(500, 540, 181, 41))
        self.btn_logout.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                      "border: 1px solid rgba(255,255,255, 0.4);\n"
                                      "border-radius: 6px;\n"
                                      "color: white;")
        self.btn_logout.setObjectName("btn_logout")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 440, 311, 151))
        self.tableWidget.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
                                       "border: 1px solid rgba(255,255,255, 0.4);\n"
                                       "border-radius: 6px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.combobox_learntype = QtWidgets.QComboBox(parent=self.centralwidget)
        self.combobox_learntype.setGeometry(QtCore.QRect(380, 130, 211, 31))
        self.combobox_learntype.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
                                              "border: 1px solid rgba(255,255,255, 0.4);\n"
                                              "color: white;")
        self.combobox_learntype.setObjectName("combobox_learntype")
        self.label_learntime = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_learntime.setGeometry(QtCore.QRect(630, 130, 211, 31))
        self.label_learntime.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
                                           "border: 1px solid rgba(255,255,255, 0.4);\n"
                                           "border-radius: 6px;\n"
                                           "color: white;")
        self.label_learntime.setText("")
        self.label_learntime.setObjectName("label_learntime")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Админ-панель"))
        self.present_label.setText(_translate("MainWindow", "Здравствуйте, господин! Чего желаете?"))
        self.label_2.setText(_translate("MainWindow", "Действия с пользователями"))
        self.btn_add_user.setText(_translate("MainWindow", "Добавить пользователя"))
        self.btn_delete_user.setText(_translate("MainWindow", "Удалить пользователя"))
        self.label_5.setText(_translate("MainWindow", "Действия с формами обучения"))
        self.label_7.setText(_translate("MainWindow", "Изменить форму обучения"))
        self.btn_add_learntype.setText(_translate("MainWindow", "Добавить форму обучения"))
        self.btn_delete_learntype.setText(_translate("MainWindow", "Удалить форму обучения"))
        self.label_8.setText(_translate("MainWindow", "Действия со сроками обучения"))
        self.btn_add_learntime.setText(_translate("MainWindow", "Добавить срок обучения"))
        self.label_11.setText(_translate("MainWindow", "Изменить сроки обучения"))
        self.btn_delete_learntime.setText(_translate("MainWindow", "Удалить срок обучения"))
        self.label_9.setText(_translate("MainWindow", "Введите логин"))
        self.label_12.setText(_translate("MainWindow", "Введите пароль"))
        self.label_13.setText(_translate("MainWindow", "Выберите уровень доступа"))
        self.comboBox_access.setItemText(0, _translate("MainWindow", "admin"))
        self.comboBox_access.setItemText(1, _translate("MainWindow", "user"))
        self.btn_exit.setText(_translate("MainWindow", "Выйти из программы"))
        self.btn_logout.setText(_translate("MainWindow", "Разлогиниться"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "login"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "access"))

        self.btn_exit.clicked.connect(self.exit)
        self.btn_add_user.clicked.connect(self.add_user_in_database)
        self.btn_delete_user.clicked.connect(self.del_user_in_database)
        self.load_current_userdata()

        self.btn_add_learntype.clicked.connect(self.add_learntype)
        self.btn_delete_learntype.clicked.connect(self.del_learntype)
        self.load_current_learntypedata()

        self.change_item_in_learntype()
        self.combobox_learntype.currentTextChanged.connect(self.change_item_in_learntype)

        self.btn_add_learntime.clicked.connect(self.add_learntime)
        self.btn_delete_learntime.clicked.connect(self.del_learntime)

    def add_user_in_database(self):
        login = self.lineEdit_login.text()
        password = self.lineEdit_password.text()
        access = self.comboBox_access.currentText()

        self.lineEdit_login.clear()
        self.lineEdit_password.clear()

        db = Database()
        db.create_user(login, password, access)

        self.load_current_userdata()
    def del_user_in_database(self):
        login = self.lineEdit_login.text()
        password = self.lineEdit_password.text()
        self.lineEdit_login.clear()
        self.lineEdit_password.clear()

        db = Database()
        if db.find_user(login, password)[0]:
            db.delete_user(login)
            self.load_current_userdata()
    def exit(self):
        MainWindow.close()
    def load_current_userdata(self):
        db = Database()
        data = db.get_database()['users']
        self.tableWidget.setRowCount(len(data['login']))
        for row in range(len(data['login'])):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['login'][row]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data['password'][row]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data['access'][row]))
    def add_learntype(self):
        learntype = self.lineEdit_learntype.text()
        self.lineEdit_learntype.clear()

        db = Database()
        db.create_learntype(learntype)

        self.load_current_learntypedata()
    def del_learntype(self):
        learntype = self.lineEdit_learntype.text()
        self.lineEdit_learntype.clear()

        db = Database()
        db.delete_learntype(learntype)

        self.load_current_learntypedata()
        self.label_learntime.setText("")
    def load_current_learntypedata(self) -> None:
        self.combobox_learntype.clear()
        db = Database()
        data = db.get_current_learntypedata()
        for i in range(len(data)):
            self.combobox_learntype.addItem(data[i]['name'])
    def change_item_in_learntype(self):
        choice = self.combobox_learntype.currentText()
        #обновить строку
        db = Database()
        data = db.get_current_learntypedata()
        for item in data:
            if item['name'] == choice:
                self.label_learntime.setText(item['learntime'])
    def add_learntime(self):
        choice = self.combobox_learntype.currentText()
        learntime = self.lineEdit_learntime.text()
        self.lineEdit_learntime.clear()

        db = Database()
        db.create_learntime(choice, learntime)

        self.change_item_in_learntype()
    def del_learntime(self):
        choice = self.combobox_learntype.currentText()

        db = Database()
        db.delete_learntime(choice)

        self.change_item_in_learntype()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow1 = QtWidgets.QMainWindow()

    authorization = Ui_authorization()
    authorization.setupUi(MainWindow)

    adminpanel = Ui_adminpanel()
    adminpanel.setupUi(MainWindow1)

    MainWindow.show()

    sys.exit(app.exec())


