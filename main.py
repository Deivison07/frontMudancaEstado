import sys
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import QThread, pyqtSignal

# Subclasse de QThread para executar uma função em segundo plano
class WorkerThread(QThread):
    # Sinal que será emitido quando a tarefa for concluída
    update_signal = pyqtSignal(str)

    def run(self):
        # Simular uma tarefa longa
        for i in range(5):
            time.sleep(1)  # Simula uma tarefa que demora 1 segundo
            self.update_signal.emit(f"Atualização {i+1}/5")  # Emite o sinal com a atualização

        self.update_signal.emit("Tarefa Concluída!")  # Emite sinal quando a tarefa termina

# Classe principal da interface gráfica
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração básica da janela
        self.setWindowTitle("Exemplo de Thread no PyQt6")
        self.setGeometry(300, 300, 300, 150)

        # Botão para iniciar a tarefa em uma nova thread
        self.button = QPushButton("Iniciar Tarefa Longa", self)
        self.button.setGeometry(50, 50, 200, 30)
        self.button.clicked.connect(self.start_thread)

        # Rótulo para mostrar o progresso
        self.label = QLabel("Aguardando tarefa...", self)
        self.label.setGeometry(50, 100, 200, 30)

        # Criação da thread de trabalho
        self.thread = WorkerThread()
        self.thread.update_signal.connect(self.update_label)

    # Inicia a thread quando o botão for clicado
    def start_thread(self):
        if not self.thread.isRunning():
            self.label.setText("Executando tarefa...")
            self.thread.start()

    # Atualiza o rótulo com informações da thread
    def update_label(self, message):
        self.label.setText(message)

# Código principal para rodar a aplicação
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
