
class MediaContent:
    def __init__(self, title, year):
        self.title = title
        self.year = year


class MediaCatalog:
    def __init__(self):
        self.items = []

    def add_content(self, content):
        self.items.append(content)

    def remove_content(self, title):
        self.items = [
            item for item in self.items
            if item.title != title
        ]


class CatalogStorage:
    def save(self, items, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for item in items:
                file.write(f"{item.title} ({item.year})\n")


class CatalogReport:
    def create(self, items):
        return f"Кількість записів у каталозі: {len(items)}"


catalog = MediaCatalog()

catalog.add_content(MediaContent("Inception", 2010))
catalog.add_content(MediaContent("Interstellar", 2014))
catalog.add_content(MediaContent("Breaking Bad", 2008))

storage = CatalogStorage()
storage.save(catalog.items, "catalog.txt")

report = CatalogReport()
print(report.create(catalog.items))
