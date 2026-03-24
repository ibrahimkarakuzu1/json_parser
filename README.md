# Python JSON Parser 

Bu proje, Python'un yerleşik `json` kütüphanesini kullanmadan, bir string'i bir Python nesnesine dönüştüren düşük seviyeli bir parser uygulamasıdır. 

## Teknik Özellikler & Kazanımlar

- **Lexical Analysis:** Ham metni anlamlı atomlara ayıran özel bir Tokenizer.
- **Peekable Iterator:** İleriye bakma (lookahead) problemini çözmek için özelleştirilmiş iterator sınıfı
- **Recursive Descent Parsing:** İçi içe geçmiş veri yapılarını çözmek için özyinelemeli mimari.
- **Error Tracking:** Hata anında satır ve sütun bilgisi veren dinamik hata yönetimi
