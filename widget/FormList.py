from PyQt5.QtWidgets import QApplication, QMessageBox, QPushButton, QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit
from widget.ListWidget import ListWidget
from utils.linker import post_company_publisher

class FormList(QWidget):
    def __init__(self, data3, selected_color="light-red", limit_selected: int = 1, max_height: int = None):
        super().__init__()
        self.initUI(data3, selected_color, limit_selected, max_height)

    def initUI(self, data3, selected_color, limit_selected, max_height):
        self.setGeometry(0, 0, 300, 200)
        self.setMaximumHeight(200)
        label0 = QLabel('Buscar relación editorial - proveedor:')
        self.nameEdit0 = QLineEdit()
        self.qlist0 = ListWidget(data3, selected_color, limit_selected, max_height, isTopWidget=True)
        self.nameEdit0.textChanged.connect(lambda x: self.qlist0.update_list(x))
        self.qPushButton =  QPushButton('Desvincular')

        # qPushButton.clicked.connect(lambda x: print("Hola Mundo"))

        layout1 = QVBoxLayout()
        layout = QHBoxLayout()
        layout.addWidget(self.nameEdit0)
        layout.addWidget(self.qPushButton)
        layout1.addWidget(label0)
        layout1.addLayout(layout)
        layout1.addWidget(self.qlist0)
        self.setLayout(layout1)

    def addItem2Data1(self, leftList: list = [], rightList: list = [], data_auth: str = ''):
        if (bool(len(leftList)) and bool(len(rightList))):
            myList = []
            #post on db
            for item in rightList:
                myList.append({'publisher': leftList[0]['content'].split('-')[1], 'docNum': item['content'].split('-')[1]})
            status_code = post_company_publisher(myList, data_auth)
            if status_code == 201:
                index, docList = leftList[0]['content'].split('-')[1], list(map(lambda x: x['docNum'],myList))
                tmpItem = {'index': index,
                        'secondary': docList,
                        'content': f'-{index} * [' + '-'.join(docList)+  ']', 
                        'isSelected': False}
                self.qlist0.addItem2Data1(tmpItem)
                return True
            else:
                QMessageBox.critical(self, 'Error', 'Operacion no ejecutada')
                return False
        else:
            # Create a message box
            QMessageBox.information(None, "Advertencia", "Debe seleccionar filas")
            return False


