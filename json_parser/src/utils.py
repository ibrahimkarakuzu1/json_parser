class SmartIterator:
    def __init__(self, text):
        self.iterator = iter(text)
        self.line = 1
        self.column = 1
        self._peek = None
        self._has_peek = False

    
    def __next__(self):
        char = self.peek()
        if char is None:  raise StopIteration

        if char =='\n':
            self.line += 1
            self.column = 1

        else: 
            self.column += 1

        self._has_peek = False
        self._peek = None
        return char
    
    def peek(self):
        if not self._has_peek:
            try:
                self._peek = next(self.iterator)
                self._has_peek = True
            except StopIteration:
                return None
        return self._peek
    
class JSONDecodeError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"{message} (Satır: {line}, Sütun: {column})")