class BadDatabaseConnection:
    def __init__(self):
        print("Відкриття нового важкого підключення до БД...")

    def query(self, sql: str):
        return f"Виконання запиту: {sql}"


if __name__ == "__main__":
    db1 = BadDatabaseConnection()
    db2 = BadDatabaseConnection()
    print(f"Це один і той самий об'єкт? {db1 is db2}")  