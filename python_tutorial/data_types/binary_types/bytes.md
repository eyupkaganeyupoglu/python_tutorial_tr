# Binary Sistem
İkili anlam taşıyan sistemler arasında iletişimi sağlamak için yapılan dönüşümlere **kodlama (encoding)** denir. Bu ikili anlam taşıyan değerler binary sistemde **0** ve **1** olarak ifade edilir.

## 8 bit'lik Sistem
8 bit'in bir araya gelerek oluşturduğu sisteme denir. Bu sistem, binary sayıları kullanarak 0'dan 255'e (0 ve 255 dahil) kadar olan sayılar üretebilir. Dolayısıyla 256 tane farklı sinyal oluşturabilir. Bir ve bytes kavramlarını şöyle listeleyebilirim:
- 8 bit'in bir araya gelmesi ile oluşan yapıya: bytes
- 1024 bytes'ın bir araya gelmesi ile oluşan yapıya: kilobyte
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

# Bytes
**Ön Bilgi:** Herhangi bir değerin, bellekte ne kadar yer kapladığı işletim sisteminden işletim sistemine, kod çözücüden kod çözücüye değişebilir. Örneğin Python 2.x sürümlerinde bir karakterlik karakter dizisi, bytes dizisi olarak temsil ediliyordu. Bu bytes dizisi Windows sistemlerde `1`, GNU/Linux sistemlerde `2` bytes ile temsil ediliyordu. Bu yüzden `len()` fonksiyonu ile kullanıldığında farklı sonuçlar döndürür. Bilgisayarınızda tanımlı kod çözücüyü öğrenmek için:
```py
import locale
print(locale.getpreferredencoding()) # Output: cp1254
```
`cp1254` kod çözücünün içeriğine ulaşmak için [tıklayınız](https://en.wikipedia.org/wiki/Windows-1254). Python 3'den sonra bu Python 2'deki olay değişti. Artık `str` veri tipi UNICODE kod konumlarını döndürüyor. Dolayısıyla artık her karakter dizisi, sahip oldukları karakter sayısına göre sayılabiliyor. `string` veri tipinin Python 2'deki halini istiyorsanız, Python 3'deki `bytes()` adlı fonksiyonu kullanabilirsiniz.

Bytes data type, temel olarak ASCII karakterlerini kabul eder. Yani ASCII tablosu dışında kalan karakterler doğrudan bytes olarak temsil edilemez. Bytes data type, string data typr gibi değiştirilemez (immutable) bir data type'dır. 

## Bytes Tanımlamak
Listeler `list`, stringler `str` ile gösterildiği gibi bytes'lar da `bytes` ile gösterilir. Örnek:
```py
byte_exp = b""  # Boş bir bytes tanımlandı
print(byte_exp) # Output: b''
```
## `bytes(source, encoding, errors)` Fonksiyonu
Bytes data type, temel olarak ASCII karakterlerini kabul eder. Yani ASCII tablosu dışında kalan karakterler doğrudan bytes olarak temsil edilemez. Bu durumu düzeltmek için `bytes()` fonksiyonu kullanılır. 3 parametresi vardır.
- `source`, bytes'lardan oluşan bir dizi (sequence) içerir. Bu dizi (sequence) bir string, integer ya da iterable bir obje olabilir.
    - `source` bir string ise mutlaka `encoding` parametresi belirtilmelidir ki herhangi bir uyuşmazlıkta program sapıtmasın.
    - `source` bir integer ise girilen sayı kadar `b'\x00'` oluşturulur. Örneğin `print(bytes(12))` kodunun output'u: `b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'`
    - `source` bir iterable obje ise iterable nesnenin count degeri (eleman sayısı) kadar bir array oluşur. Bu array içerisinde integer değerler olmalıdır. String bir iterable yaparsanız `TypeError` hatası alırsınız. Bu yüzden iterable obje elemanları integer'lardan oluşmalı ve mutlaka `0 <= x < 256` olmalıdır. Eğer `0 <= x < 256` integer kuralına uyulmazsa `ValueError` hatası alırsınız.
- `encoding`, kod çözücünün ne olacağını argüman olarak girdiğimiz parametredir. `source` parametresine girdiğimiz string value'nin hangi kod çözücü ile çözüleceğini bu parametreye argüman olarak giriyoruz.
- `errors`, Kod çözücünün uyumlu olmadığı durumlarda Python'un nasıl davranacağını belirlediğimiz parametredir. `errors` parametresinin alabileceği değerleri öğrenmek için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/kullanicidan_girdi_almak/tip_donusumleri.md#strobject-encodingutf-8-errorsstrict).

```py
print(bytes("şçİ", "utf-8"))
# Output: b'\xc5\x9f\xc3\xa7\xc4\xb0'

print(bytes("şçİ", "ascii", "replace"))
# Output: b'???'
```

## Bytes Methodları

### `decode(encoding)` Methodu
Bir stringi belli bir kod çözücü kullanılarak bytes formatına, string data type'ının methodu olan `encode()` methodunu kullanarak dönüştürebiliyorduk. Bunun tam tersini `decode()` ile yapıyoruz. Örnek:
```py
print("İ".encode("utf-8")) # Output: b'\xc4\xb0'
print(b"\xc4\xb0".decode("utf-8")) # Output: İ
```

### `fromhex("string")` Methodu
hexadecimal sayı sistemindeki bir sayıyı temsil eden string değerini bytes'a çevirir.
```py
print(bytes.fromhex("c4b0"))
# Output: b'\xc4\xb0'
```
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#func-bytes).