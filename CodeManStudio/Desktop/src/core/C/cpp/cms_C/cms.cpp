#include "cms.h"


class TCPSender {
private:
    SOCKET sock = INVALID_SOCKET;
    std::string ip;
    int port;
    bool wsaInitialized = false;

    void initializeWSA() {
        WSADATA wsaData;
        if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
            throw std::runtime_error("WSAStartup failed: " + std::to_string(WSAGetLastError()));
        }
        wsaInitialized = true;
    }

    void createSocket() {
        sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
        if (sock == INVALID_SOCKET) {
            throw std::runtime_error("Socket creation failed: " + std::to_string(WSAGetLastError()));
        }
    }

    void connectSocket() {
        sockaddr_in servAddr{};
        servAddr.sin_family = AF_INET;
        servAddr.sin_port = htons(port);

        // 使用 inet_pton 替代已弃用的 inet_addr
        if (inet_pton(AF_INET, ip.c_str(), &servAddr.sin_addr) <= 0) {
            throw std::runtime_error("Invalid IP address format");
        }

        if (connect(sock, (SOCKADDR*)&servAddr, sizeof(servAddr)) == SOCKET_ERROR) {
            throw std::runtime_error("Connection failed: " + std::to_string(WSAGetLastError()));
        }
    }

public:
    TCPSender(const std::string& ip, int port) : ip(ip), port(port) {
        try {
            initializeWSA();
            createSocket();
            connectSocket();
        }
        catch (...) {
            cleanup();
            throw;
        }
    }

    void send(const std::string& data) {
        if (sock == INVALID_SOCKET) {
            throw std::runtime_error("Socket not initialized");
        }

        int result = ::send(sock, data.c_str(), static_cast<int>(data.size()), 0);
        if (result == SOCKET_ERROR) {
            throw std::runtime_error("Send failed: " + std::to_string(WSAGetLastError()));
        }
    }

    void cleanup() {
        if (sock != INVALID_SOCKET) {
            closesocket(sock);
            sock = INVALID_SOCKET;
        }
        if (wsaInitialized) {
            WSACleanup();
            wsaInitialized = false;
        }
    }

    ~TCPSender() {
        cleanup();
    }

    TCPSender(const TCPSender&) = delete;
    TCPSender& operator=(const TCPSender&) = delete;
};

PYBIND11_MODULE(cms_C, m) {
    py::class_<TCPSender>(m, "cms_C")
        .def(py::init<const std::string&, int>(),
            py::arg("ip"), py::arg("port"),
            "Initialize TCP sender with IP and port")
        .def("send", &TCPSender::send,
            py::arg("data"),
            "Send data through TCP connection")
        .def("__enter__", [](TCPSender& self) -> TCPSender& { return self; })
        .def("__exit__", [](TCPSender& self, py::args) { self.cleanup(); });
}
