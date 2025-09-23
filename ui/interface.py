from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
from core.reader import process_code
import sys

def start_app():
    app = QApplication(sys.argv)
    window = ReaderUI()
    window.show()
    sys.exit(app.exec_())

class ReaderUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contabilizador para leitor Danfe QR Code/Código de Barras")
        self.layout = QVBoxLayout()

        self.label = QLabel("Escaneie o código:")
        self.input = QLineEdit()
        self.result = QLabel("")

        self.input.returnPressed.connect(self.read_code)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.result)
        self.setLayout(self.layout)

    def read_code(self):
        code = self.input.text().strip()
        total = process_code(code)
        self.result.setText(f"Código: {code}\nTotal: {total}")
        self.input.clear()