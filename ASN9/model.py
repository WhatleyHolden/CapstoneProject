class CalculatorModel:

    def __init__(self):
        self.result = 0.0

    def _to_number(self, value):
        value = value.strip()

        if value == "":
            raise ValueError("Please enter numbers in both input boxes.")

        try:
            return float(value)
        except ValueError:
            raise ValueError("Value entered is not numeric.")

    def add(self, first_value, second_value):
        num1 = self._to_number(first_value)
        num2 = self._to_number(second_value)
        self.result = num1 + num2
        return self.result

    def subtract(self, first_value, second_value):
        num1 = self._to_number(first_value)
        num2 = self._to_number(second_value)
        self.result = num1 - num2
        return self.result

    def clear(self):
        self.result = 0.0
