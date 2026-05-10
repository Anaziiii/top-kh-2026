class FileStorage:
    def save(self):
        print("Saved to file")

class DatabaseStorage:
    def save(self):
        print("Saved in Database")

class SmartApp(FileStorage, DatabaseStorage):
    pass

class SecureApp(DatabaseStorage, FileStorage):
    pass

app1 = SmartApp()
app1.save() # Saved to file

app2 = SecureApp()
app2.save() # Saved in Database