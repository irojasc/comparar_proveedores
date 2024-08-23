import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class ListWidget(QWidget):
    def __init__(self, data1):
        super().__init__()
        self.initUI(data1)

    def initUI(self,data1):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QListWidget Example')

        self.listWidget = QListWidget()

        # Add some more items to the list
        for index, value in enumerate(data1):
            item = QListWidgetItem(value["content"])
            self.listWidget.addItem(item)

        # Set the selection mode to single selection
        self.listWidget.setSelectionMode(QListWidget.SingleSelection)

        # Connect the itemClicked signal to a slot
        self.listWidget.itemClicked.connect(self.onItemClicked)

        layout = QVBoxLayout()
        layout.addWidget(self.listWidget)
        self.setLayout(layout)

    def onItemClicked(self, item):
        index = self.listWidget.row(item)
        item = self.listWidget.item(index)
        item.setBackground(QColor("red"))
        self.listWidget.addItem(item)
        print(f"Item clicked: {item.text()}")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())