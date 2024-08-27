from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from widget.ListWidget import ListWidget
from widget.FormList import FormList

class Body(QBoxLayout):
    def __init__(self, data1, data2, parent=None):
        super(Body, self).__init__(2,parent)
        self.parent = parent
        self.initUI(data1,data2)

    def initUI(self,data1, data2):
        #Create 3 rows
        #1st, row 1
        layout1 = QHBoxLayout()
        #2nd, row 2
        layout2 = QHBoxLayout()
        #3rd, row 3 for button guardar
        layout3 = QHBoxLayout()

        #1st row
        ########################
        column0 = QVBoxLayout()
        form1 =  FormList([], "light-red", limit_selected = 1, max_height=200)
        #
        column0.addWidget(form1)
        ########################
        layout1.addLayout(column0)
        ########################
        
        #2nd row
        ########################
        #column 1, row 2
        ########################
        column1 = QVBoxLayout()
        qlist1 = ListWidget(data1, "light-red", limit_selected = 1)
        label1 = QLabel('Buscar por editorial:')
        self.nameEdit1 = QLineEdit()
        #event
        self.nameEdit1.textChanged.connect(lambda x: qlist1.update_list(x))
        #
        #
        column1.addWidget(label1)
        column1.addWidget(self.nameEdit1)
        column1.addWidget(qlist1)
        ########################
        #column 2, row 2
        ########################
        column2 = QVBoxLayout()
        #widget3: qlist3
        qlist3 = ListWidget(data2, "light-green", limit_selected = 20, max_height=None)
        ########
        #widget2
        button2 = QPushButton('Vincular')
        button2.clicked.connect(lambda x: form1.addItem2Data1(qlist1.selectedItems, qlist3.selectedItems))
        #
        #show informative QMessagebox pqyt5?
        column2.addWidget(button2)
        ########################
        
        #column 3, row 2
        column3 = QVBoxLayout()
        #widget3
        label3 = QLabel('Buscar por proveedor:')
        self.nameEdit3 = QLineEdit()
        #event
        self.nameEdit3.textChanged.connect(lambda x: qlist3.update_list(x))
        #
        column3.addWidget(label3)
        column3.addWidget(self.nameEdit3)
        column3.addWidget(qlist3)
        ########################

        layout2.addLayout(column1)
        layout2.addLayout(column2)
        layout2.addLayout(column3)

        #3rd row
        ########################
        button21 = QPushButton('GUARDAR')
        layout3.addWidget(button21)
        ########################
        
        self.addLayout(layout1)
        self.addLayout(layout2)
        self.addLayout(layout3)
        button21.clicked.connect(self.parent.accept)

    def vincular(self):
        pass

    


