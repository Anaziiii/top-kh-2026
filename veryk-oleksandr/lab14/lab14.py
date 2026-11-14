
from abc import ABC, abstractmethod


class MediaContent:
    def __init__(self, title, year, rating):
        self.title = title
        self.year = year
        self.rating = rating


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, items):
        pass


class SortByTitle(SortStrategy):
    def sort(self, items):
        return sorted(items, key=lambda item: item.title)


class SortByYear(SortStrategy):
    def sort(self, items):
        return sorted(items, key=lambda item: item.year)


class SortByRating(SortStrategy):
    def sort(self, items):
        return sorted(
            items,
            key=lambda item: item.rating,
            reverse=True
        )


class MediaCatalog:
    def __init__(self, strategy):
        self.items = []
        self.strategy = strategy

    def add_content(self, content):
        self.items.append(content)

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_content(self):
        return self.strategy.sort(self.items)


catalog = MediaCatalog(SortByTitle())

catalog.add_content(MediaContent("Interstellar", 2014, 8.7))
catalog.add_content(MediaContent("Inception", 2010, 8.8))
catalog.add_content(MediaContent("The Dark Knight", 2008, 9.0))

print("Сортування за назвою:")
for item in catalog.sort_content():
    print(item.title, item.year, item.rating)

catalog.set_strategy(SortByYear())

print("\nСортування за роком:")
for item in catalog.sort_content():
    print(item.title, item.year, item.rating)

catalog.set_strategy(SortByRating())

print("\nСортування за рейтингом:")
for item in catalog.sort_content():
    print(item.title, item.year, item.rating)
