import sys
from PyQt5 import QtGui, uic, QtWidgets
from Caesar import rot13

class Ui(QtWidgets.QMainWindow):
    def __init__(self): 
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)
        self.show()

        # Elements 
        self.combo = self.findChild(QtWidgets.QComboBox, 'comboBox')
        self.translation = self.findChild(QtWidgets.QTextBrowser, 'textBrowser')
        self.textIn = self.findChild(QtWidgets.QTextEdit, 'textEdit')

        # Get message
        self.textIn.textChanged.connect(self.translate)

    # Functionality
    def translate(self):
        self.translation.clear()
        text = self.textIn.toPlainText()
        transText = rot13(text)
        self.translation.append(transText)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()