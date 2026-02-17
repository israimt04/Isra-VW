import time
from abc import ABC, abstractmethod


def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper


def validate_before_save(func):
    def wrapper(self, *args, **kwargs):
        if not self.data_generated:
            raise Exception("No data generated. Cannot save report.")
        print("[VALIDATION] Data validated before saving.")
        return func(self, *args, **kwargs)
    return wrapper


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("[RESOURCE] Opening file...")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("[RESOURCE] Closing file...")
        if self.file:
            self.file.close()


class Report(ABC):

    def __init__(self, filename):
        self.filename = filename
        self.data_generated = False

    @abstractmethod
    def generate_data(self):
        pass

    @validate_before_save
    @log_action
    @measure_time
    def save(self):
        with FileManager(self.filename, "w") as f:
            for line in self.generate_data():
                f.write(line + "\n")
        print("Report saved successfully.")


class TextReport(Report):

    def generate_data(self):
        self.data_generated = True
        for i in range(1, 6):
            yield f"Text Report Line {i}"


class StructuredReport(Report):

    def generate_data(self):
        self.data_generated = True
        for i in range(1, 6):
            yield f"{{'record': {i}, 'value': {i*100}}}"


class ReportFactory:

    @staticmethod
    def create_report(report_type, filename):
        if report_type.lower() == "text":
            return TextReport(filename)
        elif report_type.lower() == "structured":
            return StructuredReport(filename)
        else:
            raise ValueError("Unsupported report type")


if __name__ == "__main__":

    print("Choose report type: text / structured")
    choice = input("Enter report type: ")

    try:
        report = ReportFactory.create_report(choice, "output_report.txt")
        report.save()
    except Exception as e:
        print("Error:", e)