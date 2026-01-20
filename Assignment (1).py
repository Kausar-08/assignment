import csv

# ----------------------------------------
# Dataset Management and Analysis Program
# ----------------------------------------

class DataManager:
    def __init__(self, numeric_file, category_file, threshold=50):
        # file paths
        self.numeric_file = numeric_file
        self.category_file = category_file
        self.threshold = threshold

        # data containers
        self.values = []          # holds numerical values
        self.unique_items = set() # holds unique categories

    # load numerical data from csv file
    def load_data(self):
        try:
            with open(self.numeric_file, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    for item in row:
                        item = item.strip()
                        if item != "":
                            self.values.append(float(item))
        except FileNotFoundError:
            print("Numerical data file not found.")
        except ValueError:
            print("File contains invalid (non-numeric) data.")

    # load categorical data from text file
    def load_categories(self):
        try:
            with open(self.category_file, 'r') as f:
                for line in f:
                    text = line.strip()
                    if text != "":
                        self.unique_items.add(text)
        except FileNotFoundError:
            print("Category file not found.")

    # calculate total
    def calculate_total(self):
        total = 0
        for number in self.values:
            total += number
        return total

    # calculate average
    def calculate_average(self):
        return self.calculate_total() / len(self.values)

    # find minimum value
    def find_min(self):
        smallest = self.values[0]
        for number in self.values:
            if number < smallest:
                smallest = number
        return smallest

    # find maximum value
    def find_max(self):
        largest = self.values[0]
        for number in self.values:
            if number > largest:
                largest = number
        return largest

    # display results on screen
    def display_results(self):
        if len(self.values) == 0:
            print("No numerical data to analyze.")
            return

        avg = self.calculate_average()

        print("Total:", self.calculate_total())
        print("Average:", avg)
        print("Minimum:", self.find_min())
        print("Maximum:", self.find_max())

        # performance check
        if avg > self.threshold:
            print("Performance: High Performance")
        else:
            print("Performance: Needs Improvement")

        print("Unique Categories:", self.unique_items)
        print("Number of Categories:", len(self.unique_items))

    # save analysis to report file
    def write_report(self, filename="analysis_report.txt"):
        if len(self.values) == 0:
            return

        with open(filename, "w") as f:
            f.write("DATA ANALYSIS REPORT\n")
            f.write("--------------------\n")
            f.write(f"Total: {self.calculate_total()}\n")
            f.write(f"Average: {self.calculate_average()}\n")
            f.write(f"Minimum: {self.find_min()}\n")
            f.write(f"Maximum: {self.find_max()}\n")
            f.write(f"Unique Categories Count: {len(self.unique_items)}\n")
            f.write("Categories: " + ", ".join(self.unique_items) + "\n")

            if self.calculate_average() > self.threshold:
                f.write("Performance: High Performance\n")
            else:
                f.write("Performance: Needs Improvement\n")

    # run entire program
    def run(self):
        self.load_data()
        self.load_categories()
        self.display_results()
        self.write_report()


# ----------------------------------------
# Program execution
# ----------------------------------------

manager = DataManager("data.csv", "categories.txt")
manager.run()
