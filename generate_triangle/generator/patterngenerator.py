import sys

class PatternPrinter:
    def __init__(self,int_val:str) -> None:
        try:
            self.number_of_rows = PatternPrinter.positive_int_check(int_val)
            self.final_pattern_list = []
        except ValueError as e:
            print(f"The entered input is invalid, re-run with valid input - {e}")
            sys.exit()

    @staticmethod
    def positive_int_check(int_val:str) -> int:
        input_val = int(int_val)
        if input_val<0:
            raise ValueError("Enter a value > 0")
        else:
            return input_val

    