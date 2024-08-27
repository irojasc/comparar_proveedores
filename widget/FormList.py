from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit
from widget.ListWidget import ListWidget

class FormList(QWidget):
    def __init__(self, data1, selected_color="light-red", limit_selected: int = 1, max_height: int = None):
        super().__init__()
        self.initUI(data1, selected_color, limit_selected, max_height)

    def initUI(self, data1, selected_color, limit_selected, max_height):
        self.setGeometry(0, 0, 300, 200)
        self.setMaximumHeight(200)
        label0 = QLabel('Buscar relación editorial - proveedor:')
        self.nameEdit0 = QLineEdit()
        # self.nameEdit0.textChanged.connect(lambda x: qlist0.update_list(x))
        self.qlist0 = ListWidget(data1, selected_color, limit_selected, max_height)
        qPushButton =  QPushButton('Desvincular')
        qPushButton.clicked.connect(lambda x: print("Hola Mundo"))
        layout1 = QVBoxLayout()
        layout = QHBoxLayout()
        layout.addWidget(self.nameEdit0)
        layout.addWidget(qPushButton)
        layout1.addWidget(label0)
        layout1.addLayout(layout)
        layout1.addWidget(self.qlist0)
        self.setLayout(layout1)

    def addItem2Data1(self, leftList: list = [], rightList: list = []):
        if (bool(len(leftList)) and bool(len(rightList))):
            pass
            #aqui nos quedamos
            # dictObj = {"Index": None, "Content": "hola" ,"isSelected": False}
        else:
            # Create a message box
            QMessageBox.information(None, "Advertencia", "Debe seleccionar filas")
        # self.qlist0.addItem2Data1()
        #give me params of QMessageBox.information?




        #on click event pyqt5 button?

