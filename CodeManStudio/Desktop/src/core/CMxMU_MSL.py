import os

from PySide2.QtCore import QTextCodec, QProcess, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from client_UI import Ui_Form
import Api

dark_stylesheet = """
QWidget {
    background-color: #2b2b2b;
    color: #ffffff;
    selection-background-color: #3d3d3d;
    selection-color: #ffffff;
}
QMenu::item:selected {
    background-color: #3d3d3d;
}
QPushButton {
    background-color: #3d3d3d;

}
QLineEdit {
    background-color: #3d3d3d;
    border: 1px solid #444;
}
"""
class Client(QMainWindow):
    def __init__(self):

        #UI
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #属性
        self.server_process = QProcess()
        self.codec = QTextCodec.codecForName("UTF-8")

        self.setWindowTitle("MK-ServerLauncher 桌面版")


if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(dark_stylesheet)

    window = Client()
    window.show()
    app.exec_()