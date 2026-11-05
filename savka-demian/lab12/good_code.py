class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Створення єдиного підключення до БД...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def query(self, sql: str):
        return f"Виконання запиту: {sql}"


if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Це один і той самий об'єкт? {db1 is db2}")  
    print(db1.query("SELECT * FROM users"))