class LogAnalyzer:
    def __init__(self, input_file):
        # store file name and counters
        self.input_file = input_file
        self.info = 0
        self.warning = 0
        self.error = 0

    def analyze(self):
        try:
            with open(self.input_file, "r") as f:
                for line in f:
                    self.info += line.count("INFO")
                    self.warning += line.count("WARNING")
                    self.error += line.count("ERROR")
        except FileNotFoundError:
            print("file not found")
            exit()

    def print_result(self):
        print("INFO:", self.info)
        print("WARNING:", self.warning)
        print("ERROR:", self.error)

    def write_result(self):
        with open("output.txt", "w") as f:
            f.write(f"INFO: {self.info}\n")
            f.write(f"WARNING: {self.warning}\n")
            f.write(f"ERROR: {self.error}\n")


# -------- main --------
analyzer = LogAnalyzer("input.txt")
analyzer.analyze()
analyzer.print_result()
analyzer.write_result()
