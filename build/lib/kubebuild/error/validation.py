class InputValidator:
    @staticmethod
    def is_integer(input_value):
        try:
            int(input_value)
            return True
        except ValueError:
            return False
