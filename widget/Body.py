from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QTabBar, QTabWidget
from widget.ListWidget import ListWidget
from widget.FormList import FormList
from utils.linker import delete_company_publisher

class Body(QBoxLayout):
    def __init__(self, data1, data2, data3, data_auth, parent=None):
        super(Body, self).__init__(2,parent)
        self.parent = parent
        self.data_auth = data_auth
        self.initUI(data1,data2, data3)

    def initUI(self,data1, data2, data3):
        #Add tab
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
        self.form1 =  FormList(data3, "light-red", limit_selected = 1, max_height=200)
        self.form1.qPushButton.clicked.connect(self.desvincular)
        #
        column0.addWidget(self.form1)
        ########################
        layout1.addLayout(column0)
        ########################
        
        #2nd row
        ########################
        #column 1, row 2
        ########################
        column1 = QVBoxLayout()
        self.qlist1 = ListWidget(data1, "light-red", limit_selected = 1)
        label1 = QLabel('Buscar por editorial:')
        self.nameEdit1 = QLineEdit()
        #event
        self.nameEdit1.textChanged.connect(lambda x: self.qlist1.update_list(x))
        #
        #
        column1.addWidget(label1)
        column1.addWidget(self.nameEdit1)
        column1.addWidget(self.qlist1)
        ########################
        #column 2, row 2
        ########################
        column2 = QVBoxLayout()
        #widget3: self.qlist3
        self.qlist3 = ListWidget(data2, "light-green", limit_selected = 100, max_height=None)
        ########
        #widget2
        button2 = QPushButton('Vincular')
        button2.clicked.connect(self.vincular)
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
        self.nameEdit3.textChanged.connect(lambda x: self.qlist3.update_list(x))
        #
        column3.addWidget(label3)
        column3.addWidget(self.nameEdit3)
        column3.addWidget(self.qlist3)
        ########################

        layout2.addLayout(column1)
        layout2.addLayout(column2)
        layout2.addLayout(column3)

        #3rd row
        ########################
        # myMenuBar = self.menuBar()
        # fileCompany = myMenuBar.addMenu('Empresas')
        # layout3.addWidget(myMenuBar)
        # self.tab1 = QWidget()
        # self.tab2 = QWidget()
        # tabWidget.resize(300,200)
        # tabWidget.addTab(self.tab1, "Tab 1")
        # tabWidget.addTab(self.tab2, "Tab 2")
        ########################
        
        # self.addLayout(layout3)
        self.addLayout(layout1)
        self.addLayout(layout2)
        # button21.clicked.connect(self.parent.accept)

    def vincular(self):
        if(self.form1.addItem2Data1(self.qlist1.getSelectedItems(), self.qlist3.getSelectedItems(),self.data_auth)):
            self.qlist1.removeSelectedItems()
            self.qlist1.unselectallItems(doUpdate=True)
            self.qlist3.unselectallItems(doUpdate=True)
    
    def desvincular(self):
        #condicion que verifica si hay fila seleccionada en top list
        if(bool(self.form1.qlist0.getSelectedQty())):
            selected_item = self.form1.qlist0.getSelectedItems()[0]
            payload = [{'publisher': selected_item['index'], 'docNum': item} for item in selected_item['secondary'] if True]
            if delete_company_publisher(payload, self.data_auth) == 204:
                index = selected_item['index']
                key = self.qlist1.getLastIndex()
                self.qlist1.addItem2Data1({'index': (key+1),
                                            'content': f'{str(key+1)}-{index}',
                                            'isSelected': False,
                                            'content_root': 'xxx'})
                self.form1.qlist0.removeSelectedItems()
            else:
                QMessageBox.critical(self, 'Error', 'Operacion no ejecutada')
    
    def updateRightList(self, newList: list = []):
        self.qlist3.update_list(pattern=None, newList=newList)
