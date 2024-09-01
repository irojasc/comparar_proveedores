import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog
from tools.readexcel import read_excel_file
from widget.Body import Body
from utils.company import get_all_suppliers

class MyDialog(QDialog):
    def __init__(self, data_auth):
        super().__init__()
        self.leftList = read_excel_file('./proveedores.xls','Editoriales', column=0)    
        self.rightList = get_all_suppliers(data_auth=data_auth)
        # self.rightList = read_excel_file('./proveedores.xls','Proveedores', column=1)
        self.initUI(self.leftList, self.rightList)
    
    # data1:proveedores
    def initUI(self, data1, data2):
        self.setWindowTitle('Actualizador de Proveedores')
        self.setGeometry(300, 300, 1100, 600)
        self.setMinimumHeight(400)
        mainLayout = Body(data1, data2, self)
        self.setLayout(mainLayout)
        # Center the dialog
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getName(self):
        return "Hola Mundo"
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            event.ignore()
        else:
            super().keyPressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    if dialog.exec_() == QDialog.Accepted:
        print(f"Hello, {dialog.getName()}!")
    else:
        print("Dialog cancelled")

    # sys.exit(app.exec_())




   