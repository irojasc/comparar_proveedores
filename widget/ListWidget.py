import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget, QLabel
from functools import reduce
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

colors = {
    "light-green": QColor(173, 255, 173),
    "light-yellow": QColor(255, 255, 224),
    "light-red": QColor(255, 204, 204),
    "light-white": QColor(255,255,255),
}

class ListWidget(QWidget):
    def __init__(self, data1, selected_color="light-red", limit_selected: int = 1, max_height: int = None):
        super().__init__()
        self.data1 = data1
        self.selected_limit = limit_selected
        self.selectedColor = colors[selected_color]
        self.max_height = max_height
        self.selectedItems = []
        self.pattern = ''
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        bool(self.max_height) and self.setMaximumHeight(self.max_height)
        #crea listwidget
        self.listWidget = QListWidget()

        # obtiene parametros r, g, b
        # color = self.listWidget.item(1).background().color()
        # print(color.red(), color.green(), color.blue())
        # saved_color = item.background().color()
        # Set the selection mode to single selection
        self.listWidget.setSelectionMode(QListWidget.SingleSelection)
        # Connect the itemClicked signal to a slot
        self.listWidget.itemClicked.connect(self.onItemClicked)

        # QLabel
        self.selectedLabel =  QLabel(f'0 seleccionados, total: {str(len(self.data1))}')
        layout = QVBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addWidget(self.selectedLabel)
        self.setLayout(layout)
        # Add some more items to the list
        self.update_list()


    def onItemClicked(self, item):
        #obtiene index
        index = self.listWidget.row(item)
        item = self.listWidget.item(index)
        findedItem = self.findItemByItemWidget(item)
        # Parte logica principal
        if(self.isSelectedItem(findedItem)):
            self.unselectEvent(item, findedItem) 
        else:
            self.selectEvent(item, findedItem)
        
    def findItemByItemWidget(self,item):
        #buscar en bd
        return next((item_data1 for item_data1 in self.data1 if int(item_data1['content'].split('-')[0]) == int(item.text().split('-')[0])), False)
    
    def updateSelectedLabel(self):
        self.selectedLabel.setText(f'{str(self.getSelectedQty())} seleccionados, total: {str(len(self.data1))}')
    
    def unselectEvent(self, item, findedItem):
        self.data1[findedItem['index']]['isSelected'] = False
        item.setBackground(colors['light-white'])
        self.listWidget.addItem(item)
        self.getSelectedItems()

    def selectEvent(self, item, findedItem):
        #verifica que los seleccionados superan el limite
        if (self.selected_limit != 1):
            if (self.getSelectedQty() < self.selected_limit) and (bool(findedItem)):
                self.data1[findedItem['index']]['isSelected'] = True
                self.getSelectedItems()
                self.update_list()
        elif(self.selected_limit == 1):
            self.unselectallItems()
            indexes = [i for i, d in enumerate(self.data1) if d['index'] == findedItem['index']]
            self.data1[indexes[0]]['isSelected'] = True
            self.getSelectedItems()
            self.update_list()
        
        # print(f"Item clicked: {item.text()}")
        #find index of dictiories list?

    def isSelectedItem(self, findedItem):
        return findedItem['isSelected']

    def getSelectedIndexesItems(self):
        indexes = [i for i, d in enumerate(self.data1) if d['isSelected'] == True]
        return indexes
    
    def getSelectedItems(self):
        self.selectedItems = list(filter(lambda x: x['isSelected'] == True, self.data1)).copy()
        return self.selectedItems
    
    def getSelectedQty(self):
        return reduce(lambda x, y: x + int(y['isSelected']),  self.data1, 0)
    
    def update_list(self, pattern: str = None):
        if (isinstance(pattern, str)):
            self.pattern = pattern
        self.listWidget.clear()
        # Add some more items to the list
        for index, value in enumerate(list(filter(lambda x: self.pattern.lower() in x["content"].lower(), self.data1))):
            item = QListWidgetItem(value["content"])
            bool(value["isSelected"]) and (item.setBackground(self.selectedColor))
            self.listWidget.addItem(item)
        self.updateSelectedLabel()

    def addItem2Data1(self, data: dict = None):
        self.data1.append(data)
        self.update_list()

    def unselectallItems(self, doUpdate: bool = False):
        tmp_data = [{'index': x['index'], 'content': x['content'], 'isSelected': False} for x in self.data1 if True]
        self.data1.clear()
        self.data1 = tmp_data.copy()
        doUpdate and self.update_list()

    def removeSelectedItems(self):
        indexes = self.getSelectedIndexesItems()
        if(bool(len(indexes))):
            self.data1.pop(indexes[0])
            self.update_list()
    

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())