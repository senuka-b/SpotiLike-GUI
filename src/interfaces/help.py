from PyQt5 import QtWidgets
from PyQt5 import uic

class Help(QtWidgets.QMainWindow):
    def __init__(self, widget):
        super(Help, self).__init__()
        uic.loadUi("./uis/help.ui", self)
        self.show()
        self.widget = widget
        
        self.home.clicked.connect(lambda: self.widget.setCurrentIndex(widget.currentIndex()-2))
        self.settings.clicked.connect(lambda: self.widget.setCurrentIndex(widget.currentIndex()-1))
        
        