import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QTabBar, QTabWidget, QComboBox
from widget.ListWidget import ListWidget
from widget.FormList import FormList
from utils.linker import delete_company_publisher
from tools.readexcel import read_excel_ubigeo

class NewClient_Body(QBoxLayout):
    def __init__(self, data_auth, parent=None):
        super(NewClient_Body, self).__init__(2,parent)
        original, unique_departamentos = read_excel_ubigeo('./ubigeos.xls', 'Sheet1')
        self.data_auth = data_auth
        self.initUI(original, unique_departamentos, parent)
        self.returnedData = None

    def initUI(self, original, unique_departamentos, parent):
        layout = QVBoxLayout()
        layout_h = QHBoxLayout()
         # First name field
        self.firstNameLabel = QLabel('RUC o DNI:')
        self.DocNum = QLineEdit()
        layout.addWidget(self.firstNameLabel)
        layout.addWidget(self.DocNum)
        layout_h.addLayout(layout)

        # Last name field
        self.lastNameLabel = QLabel('Razon social o nombre:')
        self.DocName = QLineEdit()
        layout.addWidget(self.lastNameLabel)
        layout.addWidget(self.DocName)

        # Email field
        self.emailLabel = QLabel('Dirección:')
        self.DocAddress = QLineEdit()
        layout.addWidget(self.emailLabel)
        layout.addWidget(self.DocAddress)

        # Location field
        layout_ubigeo_main = QVBoxLayout()
        layout_ubigeo = QHBoxLayout()
        self.locationLabel = QLabel('Ubicación:')
        self.departamento = QComboBox()
        self.provincia = QComboBox()
        self.distrito = QComboBox()
        self.provincia.setFixedWidth(85)
        self.departamento.currentTextChanged.connect(lambda x: self.cargarProvincias(x, original))
        self.provincia.currentTextChanged.connect(lambda x: self.cargarDistritos(departamento = self.departamento.currentText(), provincia =  x, original= original))
        self.departamento.blockSignals(True)
        self.departamento.addItems(unique_departamentos)
        self.departamento.blockSignals(False)
        self.cargarProvincias(self.departamento.currentText(), original)
        layout_ubigeo.addWidget(self.departamento)    
        layout_ubigeo.addWidget(self.provincia)    
        layout_ubigeo.addWidget(self.distrito)
        layout_ubigeo_main.addWidget(self.locationLabel)
        layout_ubigeo_main.addLayout(layout_ubigeo)
        layout.addLayout(layout_ubigeo_main)    

        # Email field
        self.emailLabel = QLabel('Email:')
        self.DocEmail = QLineEdit()
        layout.addWidget(self.emailLabel)
        layout.addWidget(self.DocEmail)

        # Email field
        self.emailLabel = QLabel('Telefono:')
        self.DocPhone = QLineEdit()
        layout.addWidget(self.emailLabel)
        layout.addWidget(self.DocPhone)

        # Email field
        self.companyTypeLabel = QLabel('Tipo de empresa:')
        self.cmbTipoEmpresa = QComboBox()
        self.cmbTipoEmpresa.addItem("Propio")
        self.cmbTipoEmpresa.addItem("Proveedor")
        self.cmbTipoEmpresa.addItem("Cliente")
        self.cmbTipoEmpresa.setCurrentIndex(-1)
        layout.addWidget(self.companyTypeLabel)
        layout.addWidget(self.cmbTipoEmpresa)
        
        # Submit button
        self.submitButton = QPushButton('Guardar')
        self.submitButton.clicked.connect(lambda x: self.filtroantesdeguardar(original, parent))
        layout.addWidget(self.submitButton)
        self.addLayout(layout_h)
    
    def filtroantesdeguardar(self, original, parent):
        # print("DocNum", bool(self.DocNum.text()))
        # print("DocName", bool(self.DocName.text()))
        # print("DocAddress", bool(self.DocAddress.text()))
        # print("DocEmail", bool(self.DocEmail.text()))
        # print("DocPhone", bool(self.DocPhone.text()))
        # print("cmbTipoEmpresa", self.cmbTipoEmpresa.currentIndex() != -1)
        docnum = bool(self.DocNum.text())
        docname = bool(self.DocName.text())
        docaddress = bool(self.DocAddress.text())
        docemail = bool(self.DocEmail.text())
        docphone = bool(self.DocPhone.text())
        tipoempresa = self.cmbTipoEmpresa.currentIndex() != -1
        if(docnum and docname and docaddress and docemail and docphone and tipoempresa):
            prev_data = {
                "DocNum": self.DocNum.text(),
                "DocName": self.DocName.text(),
                "DocAddress": self.DocAddress.text(),
                "DocDepartamento": {"name": self.departamento.currentText(), "id": None},
                "DocProvincia": {"name": self.provincia.currentText(), "id": None},
                "DocDistrito": {"name": self.distrito.currentText(), "id": None},
                "DocEmail": self.DocEmail.text(),
                "DocPhone": self.DocPhone.text(),
                "TipoEmpresa": 'S' if self.cmbTipoEmpresa.currentText() == 'Proveedor' else 'C' if self.cmbTipoEmpresa.currentText() == 'Cliente' else 'O',
                }
            self.returnedData = self.setidlocation(prev_data, original)
            parent.accept()
        else:
            QMessageBox.warning(None, "Advertencia", "Debe completar todos los campos")
        
    def setidlocation(self, data, original):
        prev_item = None
        for item in original:
            if (f'{data["DocDepartamento"]["name"]}_dp' in item) and  (f'{data["DocProvincia"]["name"]}_pr' in item) and (f'{data["DocDistrito"]["name"]}_dt' in item):
                prev_item = item
        data["DocDepartamento"]["id"] = int(prev_item[f'{data["DocDepartamento"]["name"]}_dp'])
        data["DocProvincia"]["id"] = int(prev_item[f'{data["DocProvincia"]["name"]}_pr'])
        data["DocDistrito"]["id"] = int(prev_item[f'{data["DocDistrito"]["name"]}_dt'])
        return data

    def cargarProvincias(self, x, original):
        dptList = []
        prvList = []
        for item in original:
            if f'{x}_dp' in item:
                dptList.append(list(item.keys()))
        for item in dptList:
            prvList.append(list(filter(lambda x: '_pr' in x, item))[0])
        pvList = [string.replace('_pr', '') for string in list(dict.fromkeys(prvList)) if True]
        self.provincia.blockSignals(True)
        self.provincia.clear()
        self.provincia.addItems(pvList)
        self.provincia.blockSignals(False)
        self.cargarDistritos(x, self.provincia.currentText(), original)

    def cargarDistritos(self, departamento, provincia, original):
        dptList = []
        prvList = []
        for item in original:
            if (f'{departamento}_dp' in item) and (f'{provincia}_pr' in item):
                dptList.append(list(item.keys()))
        for item in dptList:
            prvList.append(list(filter(lambda x: '_dt' in x, item))[0])
        pvList = [string.replace('_dt', '') for string in list(dict.fromkeys(prvList)) if True]
        self.distrito.blockSignals(True)
        self.distrito.clear()
        self.distrito.addItems(pvList)
        self.distrito.blockSignals(False)