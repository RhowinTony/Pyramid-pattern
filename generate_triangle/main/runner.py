# With the input of row number, write a program to generate the following pattern:

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1

# Here the input is 6.


def main() -> None:
    input_val = input("Please enter the number of rows for the pyramid")
    pattern_generator = PatternPrinter(input_val)
    pattern_generator.generate_pattern()

if __name__ == "__main__":
    main()