import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMenuBar,QHBoxLayout,QVBoxLayout, QMessageBox
from tools.readexcel import read_excel_file
from widget.Body import Body
from utils.company import get_all_suppliers, create_new_company
from utils.product import get_all_publishers
from utils.linker import get_all_company_publisher
from dialog.client import NewClientDialog
class MyDialog(QDialog):
    def __init__(self, data_auth):
        super().__init__()
        self.topList = get_all_company_publisher(data_auth=data_auth)
        self.rightList = get_all_suppliers(data_auth=data_auth)
        self.leftList = get_all_publishers(data_auth=data_auth)
        self.initUI(self.leftList, self.rightList, self.topList, data_auth)
    
    # data1:proveedores
    def initUI(self, data1, data2, data3, data_auth):
        self.setWindowTitle('Actualizador de Proveedores - Editoriales')
        self.setGeometry(300, 300, 1100, 650)
        self.setMinimumHeight(400)
        ##Menu Bar
        myMenuBar = QMenuBar(self)
        myMenuBar.setNativeMenuBar(True)
        myMenuBar.setStyleSheet("QMenuBar { height: 20px;}")
        company_menu = myMenuBar.addMenu("Empresa")
        publisher_menu = myMenuBar.addMenu("Editorial")
        new_company = company_menu.addAction("Crear")
        delete_company = company_menu.addAction("Eliminar")
        new_company.triggered.connect(lambda x: self.openNewClientForm(data_auth))
        delete_company.triggered.connect(lambda x: print("Adios Mundo"))

        #Layouts
        layout0 = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        self.mainLayout = Body(data1, data2, data3, data_auth, self)
        layout1.addWidget(myMenuBar)
        layout2.addLayout(self.mainLayout)
        layout0.addLayout(layout1)
        layout0.addLayout(layout2)
        self.setLayout(layout0)
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
    
    def openNewClientForm(self, data_auth):
        with NewClientDialog(data_auth) as newClientDialog:
            if newClientDialog.exec_() == QDialog.Accepted:
                if(create_new_company(newClientDialog.newClient_layout.returnedData, data_auth) == 201):
                    QMessageBox.information(None, 'Mensaje', 'Cliente creado exitosamente')
                    self.mainLayout.updateRightList(newList=get_all_suppliers(data_auth=data_auth))
                else:
                    QMessageBox.warning(None, "Mensaje", "Error durante la creación del cliente")
            else:
                print("Dialog cancelled")

#messageBox example pyqt5?

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     dialog = MyDialog()
#     if dialog.exec_() == QDialog.Accepted:
#         print(f"Hello, {dialog.getName()}!")
#     else:
#         print("Dialog cancelled")

    # sys.exit(app.exec_())