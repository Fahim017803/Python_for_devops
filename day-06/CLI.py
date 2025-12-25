import argparse
# Import argparse module
# Used to read command-line arguments like --file and --out


class LogAnalyzer:
    # LogAnalyzer class (this is your Day-05 logic)

    def __init__(self, x):
        # Constructor
        # x = input log file path
        self.input_file = x
        self.info = 0
        self.warning = 0
        self.error = 0

    def analyze(self):
        # Reads the log file and counts log levels
        try:
            with open(self.input_file, "r") as f:
                for line in f:
                    self.info += line.count("INFO")
                    self.warning += line.count("WARNING")
                    self.error += line.count("ERROR")
        except FileNotFoundError:
            # If the file does not exist, show error and exit
            print("File not found")
            exit(1)

    def print_result(self):
        # Prints the result to the terminal
        print("INFO:", self.info)
        print("WARNING:", self.warning)
        print("ERROR:", self.error)

    def write_result(self, y):
        # Writes the result to an output file
        # y = output file path
        with open(y, "w") as f:
            f.write(f"INFO: {self.info}\n")
            f.write(f"WARNING: {self.warning}\n")
            f.write(f"ERROR: {self.error}\n")


def z():
    # This function is the main entry point of the program
    # It handles CLI arguments and runs the Day-05 logic

    x = argparse.ArgumentParser(description="CLI Log Analyzer")
    # Create ArgumentParser object
    # This object knows how to read CLI arguments

    x.add_argument("--file", required=True)
    # Define --file argument
    # required=True means the user MUST provide this
    # Example: --file input.txt

    x.add_argument("--out", default="output.txt")
    # Define --out argument
    # If user does not provide it, output.txt will be used
    # Example: --out summary.txt

    y = x.parse_args()
    # Parse arguments from the terminal
    # y.file -> input file path
    # y.out  -> output file path

    analyzer = LogAnalyzer(y.file)
    # Create LogAnalyzer object
    # Input file now comes from CLI, not hard-coded

    analyzer.analyze()
    # Analyze the log file (Day-05 logic)

    analyzer.print_result()
    # Print result to terminal

    analyzer.write_result(y.out)
    # Write result to output file (path from CLI)


if __name__ == "__main__":
    # This block ensures the code runs only when the file
    # is executed directly (not when imported)

    z()
    # Call the main function
