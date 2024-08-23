import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QLineEdit
from widget.ListWidget import ListWidget
from tools.readexcel import read_excel_file

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.leftList = read_excel_file('./proveedores.xls','Editoriales')
        self.initUI(self.leftList)
    
    # data1:proveedores
    def initUI(self, data1):
        self.setWindowTitle('Actualizador de Proveedores')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        qlist = ListWidget(data1)
        label = QLabel('Ingrese editorial:')
        self.nameEdit = QLineEdit()
        button = QPushButton('OK')

        layout.addWidget(label)
        layout.addWidget(self.nameEdit)
        layout.addWidget(button)
        layout.addWidget(qlist)

        self.setLayout(layout)

        button.clicked.connect(self.accept)

    def getName(self):
        return self.nameEdit.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    dialog = MyDialog()
    if dialog.exec_() == QDialog.Accepted:
        print(f"Hello, {dialog.getName()}!")
    else:
        print("Dialog cancelled")

    # sys.exit(app.exec_())




   