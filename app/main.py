import sys
from PyQt5.QtWidgets import QApplication
from app.ui.main_window import MainWindow

def main():
    """
    The main function to run the application.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec_()
