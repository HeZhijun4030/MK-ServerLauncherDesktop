import json
import socket
import logging

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
logger = logging.getLogger("UDP_service")
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s][%(name)s][%(levelname)s]%(message)s', '%H:%M:%S')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class udp_Sender:
    def __init__(self, ip="127.0.0.1", port=8080, timeout=2.0):
        self.ip = ip  #默认本地地址
        self.port = port  #默认端口
        self.timeout = timeout  #接收超时时间

    def send(self, msg: bytes, expect_reply=False):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(msg, (self.ip, self.port))
            logger.info(f"已发送消息到 {self.ip}:{self.port}")

            if not expect_reply:
                return None

            s.settimeout(self.timeout)
            try:
                data, addr = s.recvfrom(1024)
                logger.info(f"收到来自 {addr} 的回复: {data.decode()}")
                return data, addr
            except socket.timeout:
                logger.error("等待回复超时")
                return None
            except ConnectionResetError:
                logger.error("连接被远程主机重置")
                return None

    def send_json(self, msg, expect_reply=False):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(json.dumps(msg).encode(), (self.ip, self.port))
            if expect_reply:
                s.settimeout(self.timeout)
                try:
                    data, addr = s.recvfrom(1024)
                    logger.info(f"收到来自 {addr} 的回复: {data.decode()}")
                    return data, addr
                except socket.timeout:
                    logger.error("等待回复超时")
                except ConnectionResetError:
                    logger.error("连接被远程主机重置")

    def __del__(self):
        if hasattr(self, 'sock'):
            self.sock.close()


class udp_Server:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 8080

    def start_udp_server(self, reply_msg: bytes, reply=True):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.ip, self.port))
            logger.warning("UDP服务端已启动，等待消息...")
            while True:
                data, addr = s.recvfrom(1024)
                logger.info(f"收到来自 {addr} 的消息: {data.decode()}")
                if reply:
                    s.sendto(reply_msg, addr)
                    logger.info(f"已回复消息: {reply_msg}")
