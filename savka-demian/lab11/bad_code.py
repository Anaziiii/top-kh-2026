class BadReport:
    def __init__(self, text: str):
        self.text = text

    def print_report(self):
        print(f"Звіт: {self.text}")

    def save_to_file(self, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.text)


if __name__ == "__main__":
    report = BadReport("Усі завдання виконано успішно!")
    report.print_report()
    report.save_to_file("report.txt")