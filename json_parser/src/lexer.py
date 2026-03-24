from .utils import SmartIterator

def tokenize(text):
    tokens = []
    chars = SmartIterator(text)

    while True:
        char = chars.peek()
        if char is None: break

        if char.isspace():
            next(chars)
            continue

        if char in '{}[],:':
            tokens.append(next(chars))

        elif char == '"':
            next(chars) # başlangictaki " karakteri tüketir 
            res = ""
            while chars.peek() != '"' and chars.peek() is not None:
                res += next(chars)
            next(chars) # kapanıştaki " karakterini tğketir
            tokens.append(res)

        elif char.isdigit() or char == '-': # for negatives
            res = ""
            while chars.peek() is not None and (chars.peek().isdigit() or chars.peek() == '.'):
                res += next(chars)
            tokens.append(float(res) if '.' in res else int(res))
        
        elif char.isalpha():
            res = ""
            while chars.peek() is not None and chars.peek().isalpha():
                res += next(chars)

            mapping = {"true": True, "false": False, "null": None}
            tokens.append(mapping.get(res, res))
        
        else: 
            from .utils import JSONDecodeError
            raise JSONDecodeError(f"Beklenmedik karakter: {char}", chars.line, chars.column)
    
    return tokens