import sys
from PySide6.QtWidgets import QApplication

from controller import CalculatorController


def main():
    app = QApplication(sys.argv)
    window = CalculatorController()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
