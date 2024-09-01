import sys
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from program import MyDialog
from utils.login import Login

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 220, 155)
        self.setWindowTitle('Genesis')

        label_username = QLabel('Usuario', self)
        label_username.move(20, 10)

        self.line_username = QLineEdit(self)
        self.line_username.move(20, 30)
        self.line_username.setFixedWidth(175)
        self.line_username.returnPressed.connect(self.check_password)

        label_password = QLabel('Contraseña', self)
        label_password.move(20, 60)

        self.line_password = QLineEdit(self)
        self.line_password.setEchoMode(QLineEdit.Password)
        self.line_password.move(20, 80)
        self.line_password.setFixedWidth(175)
        self.line_password.returnPressed.connect(self.check_password)

        btn_login = QPushButton('Ingresar', self)
        btn_login.move(70, 115)
        btn_login.clicked.connect(self.check_password)
        self.center()
        self.show()

    def check_password(self):
        username = self.line_username.text()
        password = self.line_password.text()
        with Login(username, password) as data_auth:
            if bool(data_auth):
                dialog = MyDialog(data_auth)
                self.setVisible(False)
                if dialog.exec_() == QDialog.Accepted:
                    print(f"Hello, {dialog.getName()}!")
                else:
                    print("Dialog cancelled")
            else:
                QMessageBox.critical(self, 'Error', 'Invalid username or password')
    
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        #prevent escape exit qdialog?

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginForm()
    sys.exit(app.exec_())

    #install request package python?