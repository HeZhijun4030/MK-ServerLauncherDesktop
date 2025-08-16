# tcp_server_pkg/server.py
import json
import socket
import threading
import logging


class JSONTCPServer:
    def __init__(self, host='0.0.0.0', port=8080):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False
        self._thread = None
        self._callback = None
        self.logger = logging.getLogger('TCP_Server')
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def set_callback(self, callback):
        # 设置回调函数 也就是说如果有数据到来，则会调用这个函数进行处理
        self._callback = callback

    def start(self):
        if self._running:
            self.logger.warning("服务器已经在运行")
            return False

        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.bind((self.host, self.port))
            self._socket.listen(5)
            self._running = True

            self._thread = threading.Thread(target=self._run_server, daemon=True)
            self._thread.start()

            self.logger.info(f"服务器启动成功，监听 {self.host}:{self.port}")
            return True
        except Exception as e:
            self.logger.error(f"服务器启动失败: {str(e)}")
            return False

    def _run_server(self):
        #主循环
        while self._running:
            try:
                client_socket, addr = self._socket.accept()
                self.logger.debug(f"新客户端连接: {addr}")

                client_thread = threading.Thread(
                    target=self._handle_client,
                    args=(client_socket, addr),
                    daemon=True
                )
                client_thread.start()

            except socket.timeout:
                continue
            except Exception as e:
                if self._running:
                    self.logger.error(f"接受连接错误: {str(e)}")

    def _handle_client(self, client_socket, addr):
        # 处理客户端请求
        try:
            data = client_socket.recv(4096)
            if not data:
                self.logger.debug(f"客户端 {addr} 断开连接")
                return

            try:
                json_data = json.loads(data.decode('utf-8'))
                self.logger.info(f"收到来自 {addr} 的数据: {json_data}")

                # 如果有设置回调函数则调用
                if self._callback:
                    self._callback(json_data)

                # 发送响应
                response = {"status": "success", "message": "数据接收成功"}
                client_socket.sendall(json.dumps(response).encode('utf-8'))

            except json.JSONDecodeError:
                error_msg = "无效的JSON格式"
                self.logger.error(error_msg)
                response = {"status": "error", "message": error_msg}
                client_socket.sendall(json.dumps(response).encode('utf-8'))

        except Exception as e:
            self.logger.error(f"处理客户端 {addr} 时出错: {str(e)}")
        finally:
            client_socket.close()

    def stop(self):
        """停止服务器"""
        if self._running:
            self._running = False
            if self._socket:
                self._socket.close()
            self.logger.info("服务器已停止")