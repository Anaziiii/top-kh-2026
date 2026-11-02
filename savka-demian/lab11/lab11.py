class BadReport:
    def __init__(self, text):
        self.text = text

    def print_report(self):
        print(f"Звіт: {self.text}")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.text)


class Report:
    def __init__(self, text):
        self.text = text

class ReportPrinter:
    @staticmethod
    def print_report(report):
        print(f"Звіт: {report.text}")

my_report = Report("Усі завдання виконано успішно!")
ReportPrinter.print_report(my_report)