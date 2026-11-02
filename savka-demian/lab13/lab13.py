class OldPrinter:
    def print_old(self, text: str):
        return f"[Старий принтер]: {text}"


class ModernPrinterInterface:
    def print_document(self, text: str):
        pass


class PrinterAdapter(ModernPrinterInterface):
    def __init__(self, old_printer: OldPrinter):
        self.old_printer = old_printer

    def print_document(self, text: str):
        return self.old_printer.print_old(text)


old_device = OldPrinter()
adapter = PrinterAdapter(old_device)
print(adapter.print_document("Лабораторна робота №13"))