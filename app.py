import sys
import time
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets
from PyQt6.QtCore import QThread, pyqtSignal
from FrontMudancadestatus import Ui_MainWindow
#from modelFrontMudancadestatus import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.thread : WorkerThread = WorkerThread()
        self.thread.update_signal.connect(self.update_label)
        self.pushButton.clicked.connect(self.start_thread)
    
    def start_thread(self):
        if not self.thread.isRunning():
            self.thread.start()
            self.pushButton.setText("Encerrar")
        else:
            self.update_label(0)
            self.pushButton.setText("Iniciar")
            self.thread.terminate()

    # Atualiza o rótulo com informações da thread
    def update_label(self, value):
        self.progressBar.setValue(value)

class WorkerThread(QThread):
    # Sinal que será emitido quando a tarefa for concluída
    update_signal = pyqtSignal(int)

    def run(self):
        # Simular uma tarefa longa
        while self.isRunning:
            for i in range(100):
                time.sleep(1)  # Simula uma tarefa que demora 1 segundo
                self.update_signal.emit(i)  # Emite o sinal com a atualização
            self.update_signal.emit(100)  # Emite sinal quando a tarefa termina

# Código principal para rodar a aplicação
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
