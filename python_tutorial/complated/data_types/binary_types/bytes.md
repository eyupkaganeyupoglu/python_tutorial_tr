﻿# Binary Sistem
İkili anlam taşıyan sistemler arasında iletişimi sağlamak için yapılan dönüşümlere **kodlama (encoding)** denir. Bu ikili anlam taşıyan değerler binary sistemde **0** ve **1** olarak ifade edilir.

## 8 bit'lik Sistem
8 bit'in bir araya gelerek oluşturduğu sisteme denir. Bu sistem, binary sayıları kullanarak 0'dan 255'e (0 ve 255 dahil) kadar olan sayılar üretebilir. Dolayısıyla 256 tane farklı sinyal oluşturabilir. Bir ve byte kavramlarını şöyle listeleyebilirim:
- 8 bit'in bir araya gelmesi ile oluşan yapıya: byte
- 1024 byte'ın bir araya gelmesi ile oluşan yapıya: kilobyte
- 1024 kilobyte'ın bir araya gelmesi ile oluşan yapıya: megabyte
- 1024 megabyte'ın bir araya gelmesi ile oluşan yapıya: gigabyte
- 1024 gigabyte'ın bir araya gelmesi ile oluşan yapıya: terabyte
- 1024 terabyte'ın bir araya gelmesi ile oluşan yapıya: petabyte

## Hata Kontrolü
Alıcı ile verici arasında paylaşılan veriler herhangi bir nedenden dolayı bozulabilir. Bunun yaratabileceği sorunlardan kurtulmak için hata kontrol sistemleri geliştirilmiştir. 8 bit'lik hata kontrol mekanizmalarında 7 bit'i kullanıp 8. bit'i hata kontrol mekanizması için ayırırız. Hata kontrol makenizması için kullanılan 8. bit'in çalışma mantığı, sayının çift mi tek mi olduğunu kontrol etmeye dayanır. Sayıdaki birlerin sayısı tekse, sayı tektir; çiftse, sayı çiftir. Örneğin `0110111` sayısında beş tane bir olduğu için bu sayı tektir. Kullanıcının göndermek istediği sayı tekse, gönderilen sayı da tek olmalıdır. Hata kontrol mekanizması bunu denetler.

### Örnek Protokol
Bir sistemde, bütün sayıların tek sayı olarak iletilmesini istiyorsak kullanılacak protokolü şöyle düzenleyebiliriz:
- Eğer karşı tarafa iletilen bir sayı zaten tekse, o sayının başına `0` ekleyeceğiz. Böylece sayının teklik-çiftlik durumu değişmemiş olacak. Ama eğer iletilecek sayı çiftse, o sayının başına `1` ekleyeceğiz. Böylece çift sayıyı, sistemimizin gerektirdiği şekilde, tek sayıya çevirmiş olacağız. Bu kontrol türüne **eşlik denetimi (parity check)** denir. Bu yapmamızı sağlayan bit'e de **eşlik bit'i (parity bit)** denir. `Tek eşlik denetimi (odd parity check)` ve **Çift eşlik denetimi (even parity check)** adlı iki tür eşlik denetimi bulunur.

## Karakterlerin Temsili
`1` ve `0` sinyallerini bir ara getirerek farklı karakterleri temsil etmesini sağlayabiliriz. Örneğin:
<img src="https://i.ibb.co/6XhWqFb/binary-chart.png" alt="binary-chart" border="0">

# Byte

## Ön Bilgi
Herhangi bir değerin, bellekte ne kadar yer kapladığı işletim sisteminden işletim sistemine, kod çözücüden kod çözücüye değişebilir. Örneğin Python 2.x sürümlerinde bir karakterlik karakter dizisi, byte dizisi olarak temsil ediliyordu. Bu byte dizisi Windows sistemlerde `1`, GNU/Linux sistemlerde `2` byte ile temsil ediliyordu. Bu yüzden `len()` fonksiyonu ile kullanıldığında farklı sonuçlar döndürür. Bilgisayarınızda tanımlı kod çözücüyü öğrenmek için:
```py
import locale
print(locale.getpreferredencoding()) # Output: cp1254
```
`cp1254` kod çözücünün içeriğine ulaşmak için [tıklayınız](https://en.wikipedia.org/wiki/Windows-1254).

Python 3'den sonra bu Python 2'deki olay değişti. Artık `str` veri tipi UNICODE kod konumlarını döndürüyor. Dolayısıyla artık her karakter dizisi, sahip oldukları karakter sayısına göre sayılabiliyor. `string` veri tipinin Python 2'deki halini istiyorsanız, Python 3'deki `bytes()` adlı fonksiyonu kullanabilirsiniz.

## Byte Tanımlamak
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