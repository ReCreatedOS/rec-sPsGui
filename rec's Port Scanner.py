import sys
import socket
from concurrent.futures import ThreadPoolExecutor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QPlainTextEdit
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt

class PortScanner(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("rec's Port Scanner")
        self.setGeometry(100, 100, 500, 500)
        self.setWindowIcon(QIcon('icon.png'))

        # pencere rengi
        palette = self.palette()
        palette.setColor(QPalette.Window, Qt.black)
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)

        self.lbl_ip = QLabel('IP:', self)
        self.txt_ip = QLineEdit(self)
        self.txt_ip.setStyleSheet("background-color: white")


        self.lbl_startport = QLabel('Start Port:', self)
        self.txt_startport = QLineEdit(self)
        self.txt_startport.setStyleSheet("background-color: white")

        self.lbl_endport = QLabel('End Port:', self)
        self.txt_endport = QLineEdit(self)
        self.txt_endport.setStyleSheet("background-color: ")

        self.btn_scan = QPushButton('Scan', self)
        self.btn_scan.setStyleSheet("background-color: grey; color: white;")
        self.btn_scan.clicked.connect(self.scan_ports)

        self.txt_result = QPlainTextEdit(self)
        self.txt_result.setReadOnly(True)
        self.txt_result.setStyleSheet("QPlainTextEdit { background-color: #212121; color: white; }")

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl_ip)
        vbox.addWidget(self.txt_ip)
        vbox.addWidget(self.lbl_startport)
        vbox.addWidget(self.txt_startport)
        vbox.addWidget(self.lbl_endport)
        vbox.addWidget(self.txt_endport)
        vbox.addWidget(self.btn_scan)
        vbox.addWidget(self.txt_result)

        self.setLayout(vbox)

    def scan_port(self, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            self.txt_result.appendPlainText(f'{port} port is open on {ip}')
        sock.close()

    def scan_ports(self):
        ip = self.txt_ip.text()
        start_port = int(self.txt_startport.text())
        end_port = int(self.txt_endport.text())
        self.txt_result.clear()

        with ThreadPoolExecutor(max_workers=100) as executor:
            for port in range(start_port, end_port + 1):
                executor.submit(self.scan_port, ip, port)

        self.txt_result.appendPlainText('Scan finished.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scanner = PortScanner()
    scanner.show()
    sys.exit(app.exec_())
