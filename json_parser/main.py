from src.lexer import tokenize
from src.parser import JSONParser

def main():
    json_data = """
    {
        "proje": "Otonom Yazılım Evi",
        "ogrenci": "Ibrahim",
        "aktif": true,
        "notlar": [100, 95, null],
        "detay": {
            "dil": "Python",
            "seviye": "iyi"
        }
    }
    """
    
    try:
        tokens = tokenize(json_data)
        parser = JSONParser(tokens)
        result = parser.parse()
        
        print("Ayrıştırma Başarılı!")
        #print(result)
        print(f"Öğrenci: {result['ogrenci']}")
        print(f"Dil: {result['detay']['dil']}")
        
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()