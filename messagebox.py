from PyQt6.QtWidgets import QMessageBox

class MessageBox(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thông báo")
        self.setIcon(QMessageBox.Icon.Warning)
        self.setStyleSheet("background-coler: #F8F2EC; coler: #356a9c")
        