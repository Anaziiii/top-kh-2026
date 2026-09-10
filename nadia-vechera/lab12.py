from abc import ABC, abstractmethod

# 1. Абстрактний продукт
class Document(ABC):
    @abstractmethod
    def open(self) -> str:
        pass

# 2. Конкретні продукти
class PDFDocument(Document):
    def open(self) -> str:
        return "Відкрито PDF документ."

class WordDocument(Document):
    def open(self) -> str:
        return "Відкрито Word документ."

# 3. Абстрактна фабрика (Творець)
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        """Фабричний метод"""
        pass

    def open_document(self) -> str:
        # Виклик фабричного методу для створення об'єкта
        doc = self.create_document()
        return doc.open()

# 4. Конкретні фабрики
class PDFCreator(DocumentCreator):
    def create_document(self) -> Document:
        return PDFDocument()

class WordCreator(DocumentCreator):
    def create_document(self) -> Document:
        return WordDocument()

# Клієнтський код
if __name__ == "__main__":
    creator: DocumentCreator = PDFCreator()
    print(creator.open_document())  # Вивід: Відкрито PDF документ.

    creator = WordCreator()
    print(creator.open_document())  # Вивід: Відкрито Word документ.
    