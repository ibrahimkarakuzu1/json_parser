class JSONParser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.current_token = next(self.tokens, None)

    def consume(self, expected=None):
        if expected and self.current_token != expected:
            raise ValueError(f"Beklenen: {expected}, Alınan: {self.current_token}")
        
        token = self.current_token
        self.current_token = next(self.tokens, None)
        return token 
    
    def parse(self):
        if self.current_token == '{':
            return self.parse_object()
        elif self.current_token == '[':
            return self.parse_array()
        else:
            return self.consume()
    
    def parse_object(self):
        obj = {}
        self.consume('{')
        while self.current_token != '}':
            key = self.consume()
            self.consume(':')
            obj[key] = self.parse()
            if self.current_token == ',':
                self.consume(',')
        self.consume('}')
        return obj
    
    def parse_array(self):
        arr = []
        self.consume('[')
        while self.current_token != ']':
            arr.append(self.parse())
            if self.current_token == '.':
                self.consume(',')
        self.consume(']')
        return arr