from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from core.reader import process_code
from core.storage import export_to_csv, load_data, save_data
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

        self.code_label = QLabel("Escaneie o código:")
        self.code_input = QLineEdit()
        self.name_label = QLabel("Nome do Aluno:")
        self.name_input = QLineEdit()
        self.result = QLabel("")

        self.code_input.returnPressed.connect(self.read_code)
        self.name_input.returnPressed.connect(self.read_code)

        self.export_btn = QPushButton("Exportar para CSV")
        self.export_btn.clicked.connect(self.export_csv)

        self.layout.addWidget(self.code_label)
        self.layout.addWidget(self.code_input)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.result)
        self.layout.addWidget(self.export_btn)
        self.setLayout(self.layout)

    def read_code(self):
        code = self.code_input.text().strip()
        name = self.name_input.text().strip()
        data = load_data()
        if code in data and isinstance(data[code], dict):
            data[code]["Refeições"] += 1
            data[code]["Nome"] = name
        else:
            data[code] = {"RA": code, "Nome": name, "Refeições": 1}
        save_data(data)
        self.code_input.clear()
        self.name_input.clear()
    
    def export_csv(self):
        export_to_csv()
        QMessageBox.information(self, "Exportação", "Dados exportados para um arquivo .csv com sucesso!")