from abc import ABC, abstractmethod

# 1. Абстрактний продукт
class Document(ABC):
    @abstractmethod
    def open(self) -> str:
        pass

# 2. Конкретні продукти
class PDFDocument(Document):
    def open(self) -> str:#8
        return "Відкрито PDF документ." #9

class WordDocument(Document):
    def open(self) -> str: #0.8
        return "Відкрито Word документ." #0.9

# 3. Абстрактна фабрика (Творець)
class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        """Фабричний метод"""
        pass

    def open_document(self) -> str: #3 0.3
        # Виклик фабричного методу для створення об'єкта 
        doc = self.create_document() #4 0.4
        return doc.open() #7 0.7

# 4. Конкретні фабрики
class PDFCreator(DocumentCreator): 
    def create_document(self) -> Document:#5
        return PDFDocument() #6

class WordCreator(DocumentCreator):
    def create_document(self) -> Document: #0.5
        return WordDocument() #0.6

# Клієнтський код 
if __name__ == "__main__": #1
    creator: DocumentCreator = PDFCreator() 
    print(creator.open_document())  # Вивід: Відкрито PDF документ. 2 10

    creator = WordCreator() #0.1
    print(creator.open_document())  # Вивід: Відкрито Word документ. 0.2 0.10
    