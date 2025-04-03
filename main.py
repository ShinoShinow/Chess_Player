import page
from PyQt6.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    window = page.ChessWindow()
    window.show()
    sys.exit(app.exec())

  
if __name__ == "__main__":
  main()