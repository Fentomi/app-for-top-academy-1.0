from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_adminpanel(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 600)
        font = QtGui.QFont()
        font.setPointSize(17)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, x2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41,61,132,235), stop:1 rgba(155,79,165,255));")
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
        self.tableView_users = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView_users.setGeometry(QtCore.QRect(60, 440, 231, 141))
        self.tableView_users.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.tableView_users.setObjectName("tableView_users")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 90, 231, 201))
        self.label_4.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.label_4.setText("")
        self.label_4.setWordWrap(False)
        self.label_4.setIndent(-1)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 90, 211, 31))
        self.label_5.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 300, 231, 171))
        self.label_3.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.label_3.setText("")
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 310, 211, 31))
        self.label_7.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.btn_add_learntype = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_add_learntype.setGeometry(QtCore.QRect(320, 390, 211, 31))
        self.btn_add_learntype.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.btn_add_learntype.setObjectName("btn_add_learntype")
        self.btn_delete_learntype = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_delete_learntype.setGeometry(QtCore.QRect(320, 430, 211, 31))
        self.btn_delete_learntype.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.btn_delete_learntype.setObjectName("btn_delete_learntype")
        self.lineEdit_learntype = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_learntype.setGeometry(QtCore.QRect(320, 350, 211, 31))
        self.lineEdit_learntype.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.lineEdit_learntype.setText("")
        self.lineEdit_learntype.setObjectName("lineEdit_learntype")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 90, 231, 201))
        self.label_6.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.label_6.setText("")
        self.label_6.setWordWrap(False)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(570, 90, 211, 31))
        self.label_8.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(560, 300, 231, 171))
        self.label_10.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.label_10.setText("")
        self.label_10.setWordWrap(False)
        self.label_10.setIndent(-1)
        self.label_10.setObjectName("label_10")
        self.lineEdit_learntime = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_learntime.setGeometry(QtCore.QRect(570, 350, 211, 31))
        self.lineEdit_learntime.setStyleSheet("background-color: rgba(39, 176, 87, 0.7);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.lineEdit_learntime.setText("")
        self.lineEdit_learntime.setObjectName("lineEdit_learntime")
        self.btn_add_learntime = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_add_learntime.setGeometry(QtCore.QRect(570, 390, 211, 31))
        self.btn_add_learntime.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.btn_add_learntime.setObjectName("btn_add_learntime")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(570, 310, 211, 31))
        self.label_11.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.btn_delete_learntime = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_delete_learntime.setGeometry(QtCore.QRect(570, 430, 211, 31))
        self.btn_delete_learntime.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.btn_delete_learntime.setObjectName("btn_delete_learntime")
        self.tableView_learntype = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView_learntype.setGeometry(QtCore.QRect(320, 120, 211, 161))
        self.tableView_learntype.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.tableView_learntype.setObjectName("tableView_learntype")
        self.tableView_learntime = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView_learntime.setGeometry(QtCore.QRect(570, 120, 211, 161))
        self.tableView_learntime.setStyleSheet("background-color: rgba(39, 176, 87, 0.4);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.tableView_learntime.setObjectName("tableView_learntime")
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
        self.btn_exit.setGeometry(QtCore.QRect(646, 540, 171, 41))
        self.btn_exit.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_logout = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(440, 540, 181, 41))
        self.btn_logout.setStyleSheet("background-color: rgba(39, 176, 87, 1);\n"
"border: 1px solid rgba(255,255,255, 0.4);\n"
"border-radius: 6px;\n"
"color: white;")
        self.btn_logout.setObjectName("btn_logout")
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

        self.btn_exit.clicked.connect(self.exit)
        self.btn_add_user.clicked.connect(self.add_user_in_database)

    def exit(self):
        MainWindow.close()
    def add_user_in_database(self):
        login = self.lineEdit_login.text()
        password = self.lineEdit_password.text()
        access = self.comboBox_access.currentText()

        self.lineEdit_login.clear()
        self.lineEdit_password.clear()

        db = Database()
        db.create_user(login, password, access)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_adminpanel()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
