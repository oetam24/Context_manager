class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # otwarcie i udostępnienie zasobów
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        # sprzątanie, zwalnianie zasobów
        self.file.close()


if __name__ == "__main__":
    with FileManager("Yo.txt", 'w') as f:
        f.write("Hi there mate!")