class Report:
    def __init__(self, text: str):
        self.text = text


class ReportPrinter:
    @staticmethod
    def print_report(report: Report):
        print(f"Звіт: {report.text}")


class ReportSaver:
    @staticmethod
    def save_to_file(report: Report, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report.text)


if __name__ == "__main__":
    my_report = Report("Усі завдання виконано успішно!")
    ReportPrinter.print_report(my_report)
    ReportSaver.save_to_file(my_report, "report.txt")