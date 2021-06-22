# `bytearray(source, encoding, errors)`
Bytes data type, temel olarak ASCII karakterlerini kabul eder. Yani ASCII tablosu dışında kalan karakterler doğrudan bytes olarak temsil edilemez. Bytes data type, string data type gibi değiştirilemez (immutable) bir data type'dır. `bytearray()` bu durumu kaldıran bir fonksiyondur çünkü `bytearray()` mutable bir obje döndürür. `bytearray()`, kendisine girilen argümanı bytes'a, sonra bytearray'a çevirip üzerinde değişiklik yapmamıza izin veren bir bytearray nesnesi döndürür. 3 parametresi vardır:
- `source`, bytes'lardan oluşan bir dizi (sequence) içerir. Bu dizi (sequence) bir string, integer ya da iterable bir obje olabilir.
    - `source` bir string ise mutlaka `encoding` parametresi belirtilmelidir ki herhangi bir uyuşmazlıkta program sapıtmasın.
    - `source` bir integer ise girilen sayı kadar `b'\x00'` oluşturulur. Örneğin `print(bytearray(12))` kodunun output'u: `bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')`
    - `source` bir iterable obje ise iterable nesnenin count degeri (eleman sayısı) kadar bir array oluşur. Bu array içerisinde integer değerler olmalıdır. String bir iterable yaparsanız `TypeError` hatası alırsınız. Bu yüzden iterable obje elemanları integer'lardan oluşmalı ve mutlaka `0 <= x < 256` olmalıdır. Eğer `0 <= x < 256` integer kuralına uyulmazsa `ValueError` hatası alırsınız.
- `encoding`, kod çözücünün ne olacağını argüman olarak girdiğimiz parametredir. `source` parametresine girdiğimiz string value'nin hangi kod çözücü ile çözüleceğini bu parametreye argüman olarak giriyoruz.
- `errors`, Kod çözücünün uyumlu olmadığı durumlarda Python'un nasıl davranacağını belirlediğimiz parametredir. `errors` parametresinin alabileceği değerleri öğrenmek için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/kullanicidan_girdi_almak/tip_donusumleri.md#strobject-encodingutf-8-errorsstrict).
```py
print(bytearray("şçİ", "utf-8"))
# Output: bytearray(b'\xc5\x9f\xc3\xa7\xc4\xb0')

print(bytearray("şçİ", "ascii", "replace"))
# Output: bytearray(b'???')
```
Daha fazla bilgi için:
- [Bytearray function](https://docs.python.org/3/library/functions.html#func-bytearray)
- [Bytearray function](https://docs.python.org/3/library/stdtypes.html#bytearray)
- [Programiz bytearray function](https://www.programiz.com/python-programming/methods/built-in/bytearray)

### `bytearray()` Methodları
`bytearray()`, [Mutable Sequence Types](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable)'da açıklanan değişirilebilir dizi (mutable sequence) methodlarının çoğuna ve `bytes` type'ın sahip olduğu methodlara sahiptir. Bu methodlara [Bytes and Bytearray Operations](https://docs.python.org/3/library/stdtypes.html#bytes-methods)'dan ulaşabilirsiniz.
```py
print(dir(bytearray()))
```
**Output:**
```
['append', 'capitalize', 'center', 'clear',
 'copy', 'count', 'decode', 'endswith',
 'expandtabs', 'extend', 'find', 'fromhex', 'hex',
 'index', 'insert', 'isalnum', 'isalpha',
 'isascii', 'isdigit', 'islower', 'isspace',
 'istitle', 'isupper', 'join', 'ljust', 'lower',
 'lstrip', 'maketrans', 'partition', 'pop',
 'remove', 'removeprefix', 'removesuffix',
 'replace', 'reverse', 'rfind', 'rindex', 'rjust',
 'rpartition', 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 'strip', 'swapcase',
 'title', 'translate', 'upper', 'zfill']
```

**Not:** Her data type'ın methodlarını teker teker açıklamaya kalkarsam sayfalarca yazı yazmam gerekir. Çoğu method birbiriyle aynı isimde methodlara sahiptir. Bunların neler olduğunu `dir()` fonksiyonu ile kolayca öğrenebilirsiniz.