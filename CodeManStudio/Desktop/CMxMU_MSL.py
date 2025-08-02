from PySide2.QtWidgets import QApplication, QMainWindow
from client import Ui_Form

class Client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("MK-ServerLauncher 桌面版")
        self.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #2D2D2D;
            }
            QLabel {
                color: #FFFFFF;
            }
        """)

if __name__ == "__main__":
    app = QApplication([])
    window = Client()
    window.show()
    app.exec_()