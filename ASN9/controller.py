from PySide6.QtWidgets import QMainWindow, QMessageBox
from model import CalculatorModel
from view import Ui_MainWindow


class CalculatorController(QMainWindow):

    def __init__(self):
        super().__init__()

        # View setup
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Model setup
        self.model = CalculatorModel()

        # Signal-slot connections
        self.ui.btnAdd.clicked.connect(self.add_numbers)
        self.ui.btnSubtract.clicked.connect(self.subtract_numbers)
        self.ui.btnClear.clicked.connect(self.clear_form)
        self.ui.btnExit.clicked.connect(self.close)

    def _get_input_text(self):
        first_text = self.ui.txtFirstNumber.text()
        second_text = self.ui.txtSecondNumber.text()
        return first_text, second_text

    def _show_result(self, result):
        self.ui.lblResult.setText(f"Result: {result:.3f}")

    def _show_error(self, message):
        QMessageBox.warning(self, "Invalid Input", message)
        self.ui.lblResult.setText("Result will appear here")
        self.ui.txtFirstNumber.setFocus()

    def add_numbers(self):
        first_text, second_text = self._get_input_text()

        try:
            result = self.model.add(first_text, second_text)
        except ValueError as error:
            self._show_error(str(error))
            return

        self._show_result(result)

    def subtract_numbers(self):
        first_text, second_text = self._get_input_text()

        try:
            result = self.model.subtract(first_text, second_text)
        except ValueError as error:
            self._show_error(str(error))
            return

        self._show_result(result)

    def clear_form(self):
        self.model.clear()
        self.ui.txtFirstNumber.clear()
        self.ui.txtSecondNumber.clear()
        self.ui.lblResult.setText("Result will appear here")
        self.ui.txtFirstNumber.setFocus()
