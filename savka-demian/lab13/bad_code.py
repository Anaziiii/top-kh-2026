class OldPrinter:
    def print_old(self, text: str):
        return f"[Старий принтер]: {text}"


class ModernPrinter:
    def print_document(self, text: str):
        return f"[Новий принтер]: {text}"


class DocumentManager:
    def print_file(self, printer, text: str):
        if isinstance(printer, ModernPrinter):
            print(printer.print_document(text))
        elif isinstance(printer, OldPrinter):
            print(printer.print_old(text))


if __name__ == "__main__":
    manager = DocumentManager()
    manager.print_file(OldPrinter(), "Звіт №13")