import sys
from PyQt5.QtWidgets import QDialog, QApplication, QBoxLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox, QMessageBox
from widget.NewClient_layout import  NewClient_Body

class NewClientDialog(QDialog):
    def __init__(self, data_auth):
        super().__init__()
        self.data_auth = data_auth
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Crear nuevo cliente')
        self.setFixedWidth(300)
        self.newClient_layout = NewClient_Body('xxx', self)
        self.setLayout(self.newClient_layout)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        print("Session terminada")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = NewClientDialog('xxx')
    if dialog.exec_() == QDialog.Accepted:
        print(f"{dialog.newClient_layout.returnedData}")
    else:
        print("Dialog cancelled")
