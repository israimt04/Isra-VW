from abc import ABC, abstractmethod


class ReportTemplate(ABC):

    def generate_report(self):
        self.parse()
        self.validate()
        if self.requires_revalidation():
            self.revalidate()
        self.save()

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def revalidate(self):
        pass

    @abstractmethod
    def save(self):
        pass

    def requires_revalidation(self):
        return False


class StandardReport(ReportTemplate):

    def parse(self):
        print("Parsing standard report data...")

    def validate(self):
        print("Validating standard report...")

    def save(self):
        print("Saving standard report...")


class SpecialReport(ReportTemplate):

    def parse(self):
        print("Parsing special report data...")

    def validate(self):
        print("Validating special report...")

    def revalidate(self):
        print("Revalidating special report...")

    def save(self):
        print("Saving special report...")

    def requires_revalidation(self):
        return True


class PDFReport(StandardReport):
    def save(self):
        print("Saving report as PDF file...")


class DOCXReport(StandardReport):
    def save(self):
        print("Saving report as DOCX file...")


class TXTReport(StandardReport):
    def save(self):
        print("Saving report as TXT file...")


class CSVReport(SpecialReport):
    def save(self):
        print("Saving report as CSV file...")


class JSONReport(SpecialReport):
    def save(self):
        print("Saving report as JSON file...")


class ReportFactory:

    @staticmethod
    def create_report(report_type):
        reports = {
            "pdf": PDFReport,
            "docx": DOCXReport,
            "txt": TXTReport,
            "csv": CSVReport,
            "json": JSONReport
        }

        report_class = reports.get(report_type.lower())

        if not report_class:
            raise ValueError("Unsupported report type")

        return report_class()


if __name__ == "__main__":

    print("Choose Report Type: pdf, docx, txt, csv, json")
    choice = input("Enter report type: ")

    try:
        report = ReportFactory.create_report(choice)
        print("\nGenerating Report...\n")
        report.generate_report()
    except ValueError as e:
        print(e)