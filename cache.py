def btn_login(self):
    # получаем логин и пароль, введенный пользователем
    login = self.Lineedit_login.text()
    password = self.Lineedit_password.text()
    self.Lineedit_login.clear()
    self.Lineedit_password.clear()
    print(login)
    print(password)
    # создаем экземпляр класса Database
    db = Database()
    user_in_database, message = db.find_user(login, password)
    # если логин и пароль правильны
    if user_in_database:
        # открываем админ-панель
        if message == 'admin':
            print('я здесь!')
            adminpanel = Window_adminpanel()
            adminpanel.setupUi(MainWindow)
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


def btn_exit(self):
    MainWindow.close()