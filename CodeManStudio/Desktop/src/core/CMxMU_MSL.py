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
        self.server_running = False
        self.server_jar = "server.jar"  # 服务器核心文件名
        self.codec = QTextCodec.codecForName("UTF-8")

        self.setWindowTitle("MK-ServerLauncher 桌面版")
        """

        self._initialize_connections()



        def _initialize_connections(self):
            #初始化信号
            # 按钮连接
            self.ui.start.clicked.connect(self.toggle_server)
            self.ui.send_button.clicked.connect(self.send_command)

            # 回车键
            self.ui.command_input.returnPressed.connect(self.send_command)

            # 进程
            self.server_process.readyReadStandardOutput.connect(self._handle_output)
            self.server_process.readyReadStandardError.connect(self._handle_error)
            self.server_process.finished.connect(self._server_stopped)

        def toggle_server(self):
            # 启动状态切换
            if self.server_running:
                self.stop_server()
            else:
                self.start_server()

        def start_server(self):
            #启动
            if not os.path.exists(self.server_jar):
                QMessageBox.critical(self, "错误", f"找不到服务器核心文件: {self.server_jar}")
                return

            #清空控制台
            self.ui.console.clear()

            #启动命令
            java_cmd = ["java", "-Xmx2G", "-Xms1G", "-jar", self.server_jar, "nogui"]

            self.server_process.start(java_cmd[0], java_cmd[1:])
            if not self.server_process.waitForStarted():
                QMessageBox.critical(self, "错误", "无法启动服务器进程")
                return

            self.server_running = True
            self._update_ui_state()
            self._append_output("===服务器启动中===")

        def stop_server(self):
            # 停止
            if self.server_running:
                self.server_process.write("stop\n".encode())
                self._append_output("=== 正在停止服务器... ===")

        def send_command(self):
            # 发送命令
            if not self.server_running:
                QMessageBox.warning(self, "警告", "服务器未运行")
                return

            command = self.ui.command_input.text().strip()
            if command:
                # 回显输入
                self._append_output(f"> {command}")

                # 发送命令
                self.server_process.write(f"{command}\n".encode())

                # 清空
                self.ui.command_input.clear()

        def _handle_output(self):
            # 标准输出
            data = self.server_process.readAllStandardOutput()
            text = self.codec.toUnicode(data)
            self._append_output(text)

        def _handle_error(self):
            #错误输出
            data = self.server_process.readAllStandardError()
            text = self.codec.toUnicode(data)
            self._append_output(text, error=True)

        def _server_stopped(self):
            #服务器停止
            self.server_running = False
            self._update_ui_state()
            self._append_output("=== 服务器已停止 ===")

        def _append_output(self, text, error=False):
            # 追加文本到控制台
            cursor = self.ui.console.textCursor()
            cursor.movePosition(cursor.End)

            # 设置文本颜色
            if error:
                self.ui.console.setTextColor(Qt.red)
            else:
                self.ui.console.setTextColor(Qt.white)

            cursor.insertText(text)
            self.ui.console.setTextCursor(cursor)
            self.ui.console.ensureCursorVisible()

            # 恢复默认颜色
            self.ui.console.setTextColor(Qt.white)

        def _update_ui_state(self):
            self.ui.start_button.setText("停止服务器" if self.server_running else "启动服务器")
            self.ui.command_input.setEnabled(self.server_running)
            self.ui.send_button.setEnabled(self.server_running)

        def closeEvent(self, event):

            if self.server_running:
                reply = QMessageBox.question(
                    self, "确认",
                    "服务器仍在运行，确定要退出吗？",
                    QMessageBox.Yes | QMessageBox.No
                )

                if reply == QMessageBox.Yes:
                    self.stop_server()
                    self.server_process.waitForFinished(3000)  # 等待3秒
                    event.accept()
                else:
                    event.ignore()
            else:
                event.accept()



"""

if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet(dark_stylesheet)

    window = Client()
    window.show()
    app.exec_()