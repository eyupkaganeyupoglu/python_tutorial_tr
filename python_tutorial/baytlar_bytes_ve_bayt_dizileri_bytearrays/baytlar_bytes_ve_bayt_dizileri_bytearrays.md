## Ön Bilgi
Herhangi bir değerin, bellekte ne kadar yer kapladığı işletim sisteminden işletim sistemine, kod çözücüden kod çözücüye değişebilir. Örneğin Python 2.x sürümlerinde bir karakterlik karakter dizisi, byte dizisi olarak temsil ediliyordu. Bu byte dizisi Windows sistemlerde `1`, GNU/Linux sistemlerde `2` byte ile temsil ediliyordu. Bu yüzden `len()` fonksiyonu ile kullanıldığında farklı sonuçlar döndürür. Bilgisayarınızda tanımlı kod çözücüyü öğrenmek için:
```py
import locale
print(locale.getpreferredencoding()) # Output: cp1254
```
`cp1254` kod çözücünün içeriğine ulaşmak için [tıklayınız](https://en.wikipedia.org/wiki/Windows-1254).

Python 3'den sonra bu Python 2'deki olay değişti. Artık `str` veri tipi UNICODE kod konumlarını döndürüyor. Dolayısıyla artık her karakter dizisi, sahip oldukları karakter sayısına göre sayılabiliyor. `string` veri tipinin Python 2'deki halini istiyorsanız, Python 3'deki `bytes()` adlı fonksiyonu kullanabilirsiniz.

# Byte Tanımlamak
Listeler `list`, stringler `str` ile gösterildiği gibi byte'lar da `bytes` ile gösterilir. Örnek:
```py
byte_exp = b""  # Boş bir byte tanımlandı
print(byte_exp) # Output: b''
```
## `bytes(source, encoding, errors)` Fonksiyonu
byte data type, temel olarak ASCII karakterlerini kabul eder. Yani ASCII tablosu dışında kalan karakterler doğrudan byte olarak temsil edilemez. Bu durumu düzeltmek için `bytes()` fonksiyonu kullanılır. `bytes()` ile karakterlerin hangi kod çözücü ile kodlanacağını `encoding` parametresinde belirleyebilirsiniz.. Kod çözücünün uyumlu olmadığı durumlarda Python'un nasıl davranacağını da `errors` parametresinde belirleyebilirsiniz. `errors` parametresinin alabileceği değerleri öğrenmek için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/kullanicidan_girdi_almak/tip_donusumleri.md#strobject-encodingutf-8-errorsstrict).
```py
print(bytes("şçİ", "utf-8"))
# Output: b'\xc5\x9f\xc3\xa7\xc4\xb0'

print(bytes("şçİ", "ascii", "replace"))
# Output: b'???'
```

## Byte Methodları

### `decode(encoding)` Methodu
Bir stringi belli bir kod çözücü kullanılarak byte formatına, string data type'ının methodu olan `encode()` methodunu kullanarak dönüştürebiliyorduk. Bunun tam tersini `decode()` ile yapıyoruz. Örnek:
```py
print("İ".encode("utf-8")) # Output: b'\xc4\xb0'
print(b"\xc4\xb0".decode("utf-8")) # Output: İ
```

### `fromhex("string")` Methodu
hexadecimal sayı sistemindeki bir sayıyı temsil eden string değerini byte'a çevirir.
```py
print(bytes.fromhex("c4b0"))
# Output: b'\xc4\xb0'
```

# Bayt Dizileri

## `bytearray()`
Byte gibi bu da farklı bir data type'dır. Byte'ların aksine bytearray'lar üzerinde değişiklik yapılabilen bir data type'dır.

### `bytearray()` Methodları
append, capitalize, center, clear, copy, count, decode, endswith, expandtabs, extend, find, fromhex, hex, index, insert, isalnum, isalpha, isascii, isdigit, islower, isspace, istitle, isupper, join, ljust, lower, lstrip, maketrans, partition, pop, remove, removeprefix, removesuffix, replace, reverse, rfind, rindex, rjust, rpartition, rsplit, rstrip, split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill

**Not:** Her data type'ın methodlarını teker teker açıklamaya kalkarsam sayfalarca yazı yazmam gerekir. Çoğu method birbiriyle aynı isimde methodlara sahiptir. Bunların neler olduğunu `dir()` fonksiyonu ile kolayca öğrenebilirsiniz.
