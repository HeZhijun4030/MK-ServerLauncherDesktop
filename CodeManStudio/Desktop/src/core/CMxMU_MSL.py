import logging
import os

from PySide2.QtCore import QTextCodec, QProcess, Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from client_UI import Ui_Form
import Api.TCP_Func

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
logger = logging.getLogger('Application')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s]%(name)s:%(message)s')

if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
class Client(QMainWindow):
    def __init__(self):

        # UI
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 属性
        self.server_process = QProcess()
        self.codec = QTextCodec.codecForName("UTF-8")

        self.setWindowTitle("MK-ServerLauncher 桌面版")

        # 后端服务器

        self.server = Api.TCP_Func.JSONTCPServer(('127.0.0.1', 8000))

        self.server.set_callback(self.handle_server_message) # 设置回调函数

        self.server.start()



    def handle_server_message(self, data):
        pass
        # 回调函数，处理服务器发来的消息，详细见Api.TCP_Func.JSONTCPServer中的set_callback
        # self.text_area.append(data)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(dark_stylesheet)


    window = Client()

    window.show()
    logger.info("Application init success")

    app.exec_()
