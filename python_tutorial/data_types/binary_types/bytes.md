# İçindekiler

- [Binary Sistem](#1)
    - [8 bit'lik Sistem](#1.1)
    - [Hata Kontrolü](#1.2)
    - [Karakterlerin Temsili](#1.3)
- [Bytes](#2)
    - [Bytes Tanımlamak](#2.1)
    - [Bytes Methodları](#2.2)
        - [`fromhex(s)` Methodu](#2.2.1)
        - [`hex(sep, bytes_per_sep)` Methodu](#2.2.2)
        - [`decode(encoding="utf-8", errors="strict")` Methodu](#2.2.3)
        - [`replace(old, new, count)` Methodu](#2.2.4)
        - [`split(sep = None, maxsplit)` Methodu](#2.2.5)
        - [`rsplit(sep = None, maxsplit = -1)` Methodu](#2.2.6)
        - [`splitlines()` Methodu](#2.2.7)
        - [`lower()` Methodu](#2.2.8)
        - [`islower()` Methodu](#2.2.9)
        - [`upper()` Methodu](#2.2.10)
        - [`isupper()` Methodu](#2.2.11)
        - [`endswith(suffix, start, end)` Methodu](#2.2.12)
        - [`startswith(prefix, start, end)` Methodu](#2.2.13)
        - [`capitalize()` Methodu](#2.2.14)
        - [`swapcase()` Methodu](#2.2.15)
        - [`strip(chars)` Methodu](#2.2.16)
        - [`rstrip(chars)` Methodu](#2.2.17)
        - [`lstrip(chars)` Methodu](#2.2.18)
        - [`join(iterable)` Methodu](#2.2.19)
        - [`center(width, fillbyte)` Methodu](#2.2.20)
        - [`rjust(width, fillbyte)` Methodu](#2.2.21)
        - [`ljust(width, fillbyte)` Methodu](#2.2.22)
        - [`count(x, start, end)` Methodu](#2.2.23)
        - [`index(sub, start, end)` Methodu](#2.2.24)
        - [`rindex(sub, start, end)` Methodu](#2.2.25)
        - [`find(sub, start, end)` Methodu](#2.2.26)
        - [`rfind(sub, start, end)` Methodu](#2.2.27)
        - [`zfill(width)` Methodu](#2.2.28)
        - [`partition(sep)` Methodu](#2.2.29)
        - [`rpartition(sep)` Methodu](#2.2.30)
        - [`expandtabs(tabsize)` Methodu](#2.2.31)
        - [`maketrans(from, to)` Methodu](#2.2.32)
        - [`translate(table)` Methodu](#2.2.33)
        - [`title()` Methodu](#2.2.34)
        - [`istitle()` Methodu](#2.2.35)
        - [`isalpha()` Methodu](#2.2.36)
        - [`isalnum()` Methodu](#2.2.37)
        - [`isdigit()` Methodu](#2.2.38)
        - [`isspace()` Methodu](#2.2.39)
        - [`isascii()` Methodu](#2.2.40)
        - [`removeprefix(prefix)` Methodu](#2.2.41)
        - [`removesuffix(suffix)` Methodu](#2.2.42)

<h1 id="1">Binary Sistem</h1>

Binary, ikili demektir. ikili anlam birçok şeyle ifade edilebilir. Var/yok, sıcak/soğuk, aydınlık/karanlık... Bunlar gibi ikili anlam taşıyan ifadeler kullanan sistemler arasındaki iletişimi sağlamak için ikili anlam taşıyan ifadeleri birbirine dönüştürmeye **kodlama (encoding)** debir. Bilgisayar dilinde ikili sistem olarak `0` ve `1` kullanılır. Bu sisteme **Binary sistem** denir ve her bir `0` ya da `1`'e **bit** olarak ifade edilir.

<h2 id="1.1">8 bit'lik Sistem</h2>

8 bit'in (8 tane `0` ya da `1`'in) bir araya gelerek oluşturduğu sisteme denir. Bu sistem, binary sayıları (`0` ve `1`'leri) kullanarak 0'dan 256'ya (0 dahil, 256 dahil değil) kadar olan sayılar üretebilir. Dolayısıyla 256 tane farklı sinyal oluşturabilir. Bu sinyaller topluluğunun ifade ettiği verinin büyüklüklerine verilen isimler ve birbirlerine dönüşümleri aşağıda listelenmiştir:
- 8 **bit**'in bir araya gelmesi ile **byte** oluşur.
- 1024 byte'ın bir araya gelmesi ile **kilobyte** oluşur.
- 1024 kilobyte'ın bir araya gelmesi ile **megabyte** oluşur.
- 1024 megabyte'ın bir araya gelmesi ile **gigabyte** oluşur.
- 1024 gigabyte'ın bir araya gelmesi ile **terabyte** oluşur.
- 1024 terabyte'ın bir araya gelmesi ile **petabyte** oluşur.

<h2 id="1.2">Hata Kontrolü</h2>

Alıcı ile verici arasında paylaşılan byte'lar, herhangi bir nedenden dolayı bozulabilir. Bunun yaratabileceği sorunlardan kurtulmak için hatalı byte'ları tespit eden hata kontrol sistemleri geliştirilmiştir. 8 bit'lik (1 byte) hata kontrol mekanizmalarında ilk 7 bit'i ifade etmek için kullanılırken, 8. bit hata kontrol mekanizması için kullanılır. Hata kontrol makenizması için kullanılan 8. bit'in çalışma mantığı, ilk 7 bit'in çift/tek olduğunu kontrol etmeye dayanır. İlk 7 bit'i ifade etmek için kullanılan `1`'lerin toplamı tek sayı ise byte tektir, çiftse byte çiftir. Örneğin `0110111` byte'ında beş tane `1` olduğu için bu byte tektir. Kullanıcının göndermek istediği byte tekse, gönderilen byte de tek; çiftse, çift olmalıdır. Hata kontrol mekanizması bunu denetler.

**Örnek Protokol:** Bir sistemde, bütün byte'ların tek olarak iletilmesini istiyorsak kullanılacak protokolü şöyle düzenleyebiliriz:
- Eğer karşı tarafa iletilen bir byte zaten tekse, o byte'ın başına `0` ekleyeceğiz. Böylece byte'ın teklik-çiftlik durumu değişmemiş olacak. Ama eğer iletilecek byte çiftse, o byte'ın başına `1` ekleyeceğiz. Böylece çift byte'ı, sistemimizin gerektirdiği şekilde, tek byte'a dönüştürmüş olacağız. Bu kontrol türüne **eşlik denetimi (parity check)** denir. Bu yapmamızı sağlayan bit'e de **eşlik bit'i (parity bit)** denir. `Tek eşlik denetimi (odd parity check)` ve **Çift eşlik denetimi (even parity check)** adlı iki tür eşlik denetimi bulunur. Merak ediyorsanız araştırabilirsiniz.

<h2 id="1.3">Karakterlerin Temsili</h2>

Binary sistem kullanarak alfabedeki farklı karakterleri temsil edebilirsiniz. Örnek:

![](https://i.ibb.co/JzmHvzc/Ekran-Al-nt-s.png)

<h1 id="2">Bytes</h1>

**Ön Bilgi:** Herhangi bir verinin bellekte ne kadar yer kapladığı işletim sisteminden işletim sistemine, kod çözücüden kod çözücüye değişebilir. Örneğin Python 2.x sürümlerinde bir karakterlik string, byte dizisi olarak temsil ediliyordu. Bu byte dizisi, Windows sistemlerde `1`, GNU/Linux sistemlerde `2` byte ile temsil ediliyordu. Bu yüzden `len()` fonksiyonu ile kullanıldığında farklı sonuçlar döndürüyordu. Bilgisayarınızda tanımlı kod çözücüyü öğrenmek için:
```py
import locale
print(locale.getpreferredencoding()) # Output: cp1254
```
`cp1254` kod çözücünün içeriğine ulaşmak için [tıklayınız](https://en.wikipedia.org/wiki/Windows-1254 "https://en.wikipedia.org/wiki/Windows-1254"). Python 3'den sonra bu Python 2'deki olay değişti. Artık bir karakterlik string'ler UNICODE kod konumlarını döndürüyor. Dolayısıyla artık her string sahip olduğu karakter sayısına göre sayılabiliyor. String type'ın data'ların Python 2'deki halini istiyorsanız, Python 3'deki `bytes()` adlı fonksiyonu kullanabilirsiniz.

`bytes` data type temel olarak ASCII karakterlerini kabul eder. Yani ASCII tablosu dışında kalan karakterler doğrudan `bytes` olarak temsil edilemez. `bytes` data type değiştirilemez (immutable) bir data type'dır. 

<h2 id="2.1">Bytes Tanımlamak</h2>

`bytes` type objeler `b''` syntax'ına sahiptir. Örnek:
```py
bytes_exp1 = b'\xc5\x9f'
bytes_exp2 = b'\xc3\xa7'
bytes_exp3 = b'\xc4\xb0'
bytes_exp4 = b'' # Boş byte

print(type(bytes_exp1),type(bytes_exp2),type(bytes_exp3),type(bytes_exp4)) # Output: <class 'bytes'> <class 'bytes'> <class 'bytes'> <class 'bytes'>
```
Burada aklınıza "Byte'lar `0` ve `1`'ler ile ifade ediliyorsa neden buradaki ifadeler binary değil hexadecimal formatta?" sorusu gelmiş olabilir. En az kaynak harcayarak en büyük miktarda veriyi hexadecimal formatla ifade edebiliriz. Örneğin 15 decimal sayısı hexadecimal formatta `f` ile ifade edilebilirken binary formatta `1111` ile ifade edilir.

Bytes data type, temel olarak ASCII karakterlerini kabul eder. Yani ASCII tablosu dışında kalan karakterler doğrudan bytes olarak temsil edilemez. Bu durumu düzeltmek için `bytes(source, encoding, errors)` fonksiyonu kullanılır:
- `source` parametresine argüman olarak bytes'lardan oluşan bir dizi (sequence) girilebilir ya da hiçbir şey girilmeyebilir. Bu dizi (sequence) bir string, integer ya da iterable bir obje olabilir.

    ![](https://i.ibb.co/Vt49VrC/image.png)

    - `source` parametresine argüman olarak string girilirse, mutlaka `encoding` parametresine bu string'in hangi kod çözücü ile çözülmesi gerektiğini belirlemelisiniz. Aksi halde `TypeError: string argument without an encoding` hatası yükseltilir. Yanlış kod çözücü kullanırsanız yine hata yükseltilir. Örnek:
        ```py
        print(bytes("aş")) # TypeError: string argument without an encoding
        print(bytes("aş", "utf-8")) # Output: b'a\xc5\x9f'
        print(bytes("aş", "ascii")) # UnicodeEncodeError: 'ascii' codec can't encode character '\u015f' in position 1: ordinal not in range(128)
        ```
        Yanlış kod çözücü tanımlama sonucu Python'un nasıl davranacağını `errors` parametresine gireceğiniz agümanla belirleyebilirsiniz. Örnek:
        ```py
        print(bytes("aş", "ascii", "replace")) # Output: b'a?'
        ```
    - `source` parametresine argüman olarak integer girilirse, tamamı null (`b'\x00'`) olarak başlatılmış integer kadar bir dizi oluşturulur. Örnek:
        ```py
        print(bytes(5)) # Output: b'\x00\x00\x00\x00\x00'
        ```
    - `source` parametresine argüman olarak iterable bir obje girilirse, iterable objenin eleman sayısı kadar bir array oluşturulur. Örnek:
        ```py
        print(bytes([1,2,3])) # Output: b'\x01\x02\x03'
        print(bytes({1,2,3})) # Output: b'\x01\x02\x03'
        print(bytes((1,2,3))) # Output: b'\x01\x02\x03'
        ```
        Bu iterable objenin elemanları `0 <= x < 256` değer aralığındaki integer sayılar olabilir. Bu değer aralığında olmazsa `ValueError: bytes must be in range(0, 256)` hatası yükseltilir.
        ```py
        print(bytes([254,255,256])) # ValueError: bytes must be in range(0, 256)
        ```
        Integer haricinde bir type girilirse `TypeError` hatası yükseltilir. Örnek:
        ```py
        print(bytes(["a"])) # TypeError: 'str' object cannot be interpreted as an integer
        print(bytes([[254,255],256])) # TypeError: 'list' object cannot be interpreted as an integer
        ```
- `encoding` parametresine argüman olarak girilen değerle, `source` parametresine argüman olarak girilen string'in hangi kod çözücü ile çözüleceğini belirleyebilirsiniz. Örnek:
    ```py
    print(bytes("Selam", "ascii")) # Output: b'Selam'
    print(bytes("Selam", "utf-8")) # Output: b'Selam'
    ```
- `errors` parametresine argüman olarak girilen değerle, `encoding` parametresine argüman olarak girilen kod çözücünün `source` parametresine argüman olarak girilen string'i çözememsi durumunda Python'un nasıl davranacağını belirleyebilirsiniz. Örnek:
    ```py
    print(bytes("aş", "ascii", "replace")) # Output: b'a?'
    ```
    Bu argümanlara ulaşmak için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/data_types/text_type/string.md#1.3 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/data_types/text_type/string.md#1.3").

<h2 id="2.2">Bytes Methodları</h2>

**Not:** Aşağıdaki methodlardan bazıları uygulandığı `bytes` objesini değiştirirken, bazıları işlevini gerçekleştikten sonra o `bytes` objesinin kopyasını döndürür. Bu yüzden kimi zaman ilgili methodu uyguladığınız `bytes` objesi değişikliğe uğramaz. Bu gibi durumları aşağıdaki methodları anlatırken belirtmeyi unutmuş olabilirim. Bu yüzden methodu kullanmadan önce o method uygulandığı `bytes` objesini mi değiştiriyor yoksa kopyasını mı döndürüyor, kontrol etmeyi ihmal etmeyin.

<h3 id="2.2.1"><code>fromhex(s)</code> Methodu</h3>

Bu method bir class method olduğu için direkt `bytes` class'ına veya bu class'dan türetilen objelere uygulanabilir. `s` parametresine argüman olarak girilen, hexadecimal digit'ler belirten bir string'i `bytes` type'a dönüştürür. Bu dönüşümün ancak her bytes için en az 2 hexadecimal digit tanımlandığında yapılabilir. Aksi halde `ValueError: non-hexadecimal number found in fromhex() arg at position n` hatası yükseltilir. Bu dönüşüm hexadecimal digit'lerin kapsamında (`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f`) gerçekleşebilir. Aksi halde yine `ValueError` hatası yükseltilir. Boşluk (space) karakterlerini görmezden gelir. Python 3.7'den sonra ASCII whitespaces karakterini de (`20`) görmezden gelir. Örnek:
```py
print(bytes.fromhex("f9 c8")) # Output: b'\xf9\xc8'
print(bytes.fromhex("f920c8")) # Output: b'\xf9 \xc8'
print(bytes.fromhex("c")) # ValueError: non-hexadecimal number found in fromhex() arg at position 1
print(bytes.fromhex("ÇŞ")) # ValueError: non-hexadecimal number found in fromhex() arg at position 0
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.fromhex "https://docs.python.org/3/library/stdtypes.html#bytes.fromhex").

<h3 id="2.2.2"><code>hex(sep, bytes_per_sep)</code> Methodu</h3>

Uygulandığı `bytes` objesinin içerdiği string objesi olarak döndürür. Bir nevi `fromhex()` methodunun yaptığı işin tersini yapar diyebiliriz. `fromhex()` methodunun space karakterlerini görmezden gelmesi gibi `hex()` methodu da hexadecimal anlamına gelen `\x` kaçış dizisini (escape character) görmezden gelir. `sep` parametresine girilen string'i, her ikili hexadecimal digit'in arasına uygular ve bu sayede kullanıcı tarafından output'un okunması kolaylaşır. Örnek:
```py
print((bytes.fromhex("f9 c8")).hex("-")) # Output: f9-c8
print((bytes.fromhex("f920c8")).hex("-")) # Output: f9-20-c8
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.hex "https://docs.python.org/3/library/stdtypes.html#bytes.hex").

<h3 id="2.2.3"><code>decode(encoding="utf-8", errors="strict")</code> Methodu</h3>

Uygulandığı `bytes` objesini, default değeri `utf-8` olan `encoding` parametresine girilen argümanın belirttiği kod çözücüye göre çözer ve döndürür. Örnek:
```py
print("İ".encode("utf-8")) # Output: b'\xc4\xb0'
print(b"\xc4\xb0".decode("utf-8")) # Output: İ
```
`encoding` parametresine girilen argümanın belirttiği kod çözücünün kodu çözemediği zamanlarda Python'un nasıl davranacağını `errors` parametresine girilen argüman ile belirleyebilirsiniz. Bu parametreye `strict` (default değer), `ignore` ve `replace` argümanlarını girebilirsiniz. Bu argümanların ne gibi sonuçlara sebep olduklarına ulaşmak için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/data_types/text_type/string.md#str-fonksiyonu "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/data_types/text_type/string.md#str-fonksiyonu"). Örnek:
```py
print(b'abcd\xe7'.decode("ascii", "ignore")) # Output: abcd
print(b'abcd\xe7'.decode("ascii", "replace")) # Output: abcd�
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.decode "https://docs.python.org/3/library/stdtypes.html#bytes.decode").

<h3 id="2.2.4"><code>replace(old, new, count)</code> Methodu</h3>

`old` parametresinde argüman olarak girilen `bytes`'ı `new` parametresine argüman olarak girilen `bytes` ile değiştirir ve döndürür. `count` parametresine argüman girilmezse, o `bytes`'daki uyuşan bütün değerleri değiştirir. `count` parametresine argüman olarak integer bir değer girilirse, Python soldan sağa doğru `count` kadar ilgili değeri değiştirir. Örnek:
```py
a = b"\xf0\xf1\xf2\xf1\xf3"
a1 = a.replace(b"\xf1",b"\xf5")
a2 = a.replace(b"\xf1",b"\xf5", 1)

print(a1) #Output: b'\xf0\xf5\xf2\xf5\xf3'
print(a2) #Output: b'\xf0\xf5\xf2\xf1\xf3'
```
`replace` methodunu kullanarak `bytes`'da yaptığımız değişikliklerin kalıcı olmasını istiyorsanız, ilgili variable'ı yukarıdaki gibi yeniden tanımlamanız (redefinition) gerekmektedir.

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.replace "https://docs.python.org/3/library/stdtypes.html#bytes.replace").

<h3 id="2.2.5"><code>split(sep = None, maxsplit)</code> Methodu</h3>

Bytes'ları parçalarına ayırıp bir liste içinde döndürür. `sep` parametresine argüman olarak girilen `bytes`'ı referans alarak soldan sağa doğru parçalama işlemini gerçekleştirir. `sep` parametresine argüman girilmezse boşluk karakterini (`b" "`) veya ASCII boşluk (whitespaces) karakterini referans alarak parçalama işlemi yapar. Bu boşluk karakteri ve ASCII boşluk (whitespaces) karakteri birbiri ardına geliyorsa, bunlar tek bir space karakteri olarak kabul edilir. Örnek:
```py
bytes_exp = b"            abc             abc   abc          abc       "
print(bytes_exp.split()) # Output: [b'abc', b'abc', b'abc', b'abc']
```
`maxsplit` parametresine argüman girilmezse, default değeri olan `-1` geçerli olur ve `sep` parametresine argüman olarak girilen `bytes`'ı referans alarak uygulandığı bütün `bytes`'ı parçalar. Bu durum argüman olarak girilen diğer negatif sayılar için de geçerlidir. `maxsplit` parametresine argüman olarak `0` girilirse, parçalama işlemi yapmaz. `maxsplit` parametresine argüman olarak integer bir değer girilirse, o değerde belirtilen kadar parçalama işlemi yapar. Örnek:
```py
bytes_exp = b"abc abc abc abc"

print(bytes_exp.split()) # Output: [b'abc', b'abc', b'abc', b'abc']
print(bytes_exp.split(maxsplit=0)) # Output: [b'abc abc abc abc']
print(bytes_exp.split(maxsplit=2)) # Output: [b'abc', b'abc', b'abc abc']
print(bytes_exp.split(b"b")) # Output: [b'a', b'c a', b'c a', b'c a', b'c']
print(bytes_exp.split(b"b", 2)) # Output: [b'a', b'c a', b'c abc abc']
```
`maxsplit` parametresinde belirtilen integer, `split` methodunun döndürdüğü listede bulunan virgül sayısına eşit, eleman sayısından bir eksiktir. Yani: `maxsplit = virgül sayısı = len(split methodunun döndürdüğü liste)-1`. `sep` parametresine girilen referans ilgili `bytes`'da yoksa, hiçbir işlem yapılmaz. Örnek:
```py
bytes_exp = b"abc abc abc abc"

print(bytes_exp.split(b"d")) # Output: [b'abc abc abc abc']
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.split "https://docs.python.org/3/library/stdtypes.html#bytes.split").

<h3 id="2.2.6"><code>rsplit(sep = None, maxsplit = -1)</code> Methodu</h3>

`split()` methodunun yaptığı işi sağdan sola doğru yapar. Örnek:
```py
bytes_exp = b"abc abc abc abc"

print(bytes_exp.rsplit()) # Output: [b'abc', b'abc', b'abc', b'abc']
print(bytes_exp.rsplit(maxsplit=0)) # Output: [b'abc abc abc abc']
print(bytes_exp.rsplit(maxsplit=2)) # Output: [b'abc abc', b'abc', b'abc']
print(bytes_exp.rsplit(b"b")) # Output: [b'a', b'c a', b'c a', b'c a', b'c']
print(bytes_exp.rsplit(b"b", 2)) # Output: [b'abc abc a', b'c a', b'c']
print(bytes_exp.rsplit(b"d")) # Output: [b'abc abc abc abc']
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.rsplit "https://docs.python.org/3/library/stdtypes.html#bytes.rsplit").

<h3 id="2.2.7"><code>splitlines()</code> Methodu</h3>

Bytes'ları satır satır (line) olarak parçalar. `keepends` parametresi boolean type değerleri kabul eder. `keepends` parametresine girilen argüman `True` boolean değerine sahipse `splitlines` methodu `\n` kaçış dizilerini de dahil eder, `False` ise etmez. `keepends` parametresinin default değeri `False`'dır. Örnek:
```py
a = b'abc\nabc\nabc\nabc\nabc'
print(a.splitlines(False)) # Output: [b'abc', b'abc', b'abc', b'abc', b'abc']
print(a.splitlines(True))  # Output: [b'abc\n', b'abc\n', b'abc\n', b'abc\n', b'abc']
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.splitlines "https://docs.python.org/3/library/stdtypes.html#bytes.splitlines").

<h3 id="2.2.8"><code>lower()</code> Methodu</h3>

Uygulandığı `bytes` objesinin içerdiği bütün ASCII karakterlerini küçük harfe dönüştürür. Örnek:
```py
exp = b"SeLaMlArRrR"
print(exp.lower()) # Output: b'selamlarrrr'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.lower "https://docs.python.org/3/library/stdtypes.html#bytes.lower").

<h3 id="2.2.9"><code>islower()</code> Methodu</h3>

Uygulandığı `bytes` objesinin içerdiği bütün ASCII karakterlerini küçük harf olup olmadığını sorgular. Hepsi küçük harf ise `True`, diğer durumlarda `False` döndürür. Örnek:
```py
bytes1 = b"selamlar"
bytes2 = b"Selamlar"
print(bytes1.islower()) # Output: True
print(bytes2.islower()) # Output: False
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.islower "https://docs.python.org/3/library/stdtypes.html#bytes.islower").

<h3 id="2.2.10"><code>upper()</code> Methodu</h3>

Uygulandığı `bytes` objesinin içerdiği bütün ASCII karakterlerini büyük harfe dönüştürür. Örnek:
```py
exp = b"SeLaMlArRrR"
print(exp.upper()) # Output: b'SELAMLARRRR'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.upper "https://docs.python.org/3/library/stdtypes.html#bytes.upper").

<h3 id="2.2.11"><code>isupper()</code> Methodu</h3>

Uygulandığı `bytes` objesinin içerdiği bütün ASCII karakterlerini büyük harf olup olmadığını sorgular. Hepsi büyük harf ise `True`, diğer durumlarda `False` döndürür. Örnek:
```py
bytes1 = b"SELAMLAR"
bytes2 = b"SELAMLAr"
print(bytes1.isupper()) # Output: True
print(bytes2.isupper()) # Output: False
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.isupper "https://docs.python.org/3/library/stdtypes.html#bytes.isupper").

<h3 id="2.2.12"><code>endswith(suffix, start, end)</code> Methodu</h3>

Uygulandığı `bytes`'ın en son index'inden en baş index'ine doğru tarayarak, `suffix` parametresine argüman olarak girilen `bytes`'ı ya da tuple içinde belirtilen `bytes`'ları arar ve bulursa `True`, bulamazsa `False` boolean değerini döndürür. `start` ve `end` parametreleri tanımlanırsa, bu parametrelere tanımlanan index'ler arasında tarama işlemi yapar. `start` parametresinde belirtilen index dahil edilirken, `end` parametresinde belirtilen index dahil edilmez. Örnek:
```py
bytes1 = b"abc i abc abc abc x"
bytes2 = b"abc j abc abc abc y"
bytes3 = b"abc k abc abc abc z"
print(bytes1.endswith(b"x")) # Output: True
print(bytes1.endswith(b"i", 0, 5), end="\n\n") # Output: True

for i in [bytes1, bytes2, bytes3]:
    print(i.endswith((b"x", b"y", b"z", b"p")))
```
**Output:**
```
True
True

True
True
True
```
Gördüğünüz gibi `suffix` parametresine argüman olarak girilen tuple içinde belirtilen `bytes`'lardan herhangi birisi `endswith` methodunun uygulandığı `bytes`'ın sonunda varsa `True` output'u verilir.

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.endswith "https://docs.python.org/3/library/stdtypes.html#bytes.endswith").

<h3 id="2.2.13"><code>startswith(prefix, start, end)</code> Methodu</h3>

`endswith` methodunun yaptığı işin aynısının, uygulandığı `bytes`'ın başını kontrol eden versiyonudur. Örnek:
```py
bytes1 = b"x abc abc i abc abc"
bytes2 = b"y abc abc j abc abc"
bytes3 = b"z abc abc k abc abc"
print(bytes1.startswith(b"x")) # Output: True
print(bytes1.startswith(b"i", 10), end="\n\n") # Output: True

for i in [bytes1, bytes2, bytes3]:
    print(i.startswith((b"x", b"y", b"z", b"p")))
```
**Output:**
```
True
True

True
True
True
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.startswith "https://docs.python.org/3/library/stdtypes.html#bytes.startswith").

<h3 id="2.2.14"><code>capitalize()</code> Methodu</h3>

Bir `bytes`'ın 0. index'indeki ASCII karakteri büyük harf karakterine dönüştürür. 0. index'indeki harf karakterinin üstünde `upper()` methodu uygulanmış gibi düşünebilirsiniz. Non-ASCII (ASCII olmayan) karakterlere bir şey yapmaz. Örnek:
```py
bytes1 = b"istisnalar kaideyi bozmaz."
print(bytes1.capitalize()) # Output: b'Istisnalar kaideyi bozmaz.'

bytes2 = b" istisnalar kaideyi bozmaz."
print(bytes2.capitalize()) # Output: b' istisnalar kaideyi bozmaz.'

bytes3 = b'\xc3\xa7al\xc4\xb1\xc5\x9fkan \xc3\xa7ocuk'
print(bytes3.capitalize()) # Output: b'\xc3\xa7al\xc4\xb1\xc5\x9fkan \xc3\xa7ocuk'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.capitalize "https://docs.python.org/3/library/stdtypes.html#bytes.capitalize").

<h3 id="2.2.15"><code>swapcase()</code> Methodu</h3>

`bytes`'ın içindeki büyük ASCII harflerini küçük ASCII harferine, küçük ASCII harferini de büyük ASCII harferine dönüştürür. Yani `b'abcdefghijklmnopqrstuvwxyz'` ve `b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'` verilerini kullanarak dönüşüm işlemi yapar. Örnek:
```py
bytes1 = b"SelaMLar"
print(bytes1.swapcase()) # Output: b'sELAmlAR'

bytes2 = b"iRiTe"
print(bytes2.swapcase()) # Output: b'IrItE'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.swapcase "https://docs.python.org/3/library/stdtypes.html#bytes.swapcase").

<h3 id="2.2.16"><code>strip(chars)</code> Methodu</h3>

Bir `bytes`'daki her line'ın başındaki ve sonundaki `chars` parametresine argüman olarak girilen string'i kırpmaya yarar. Default değer olarak boşluk karakteri `" "` alır. Bu method'un nasıl davranacağını kestirmek zordur. Bu yüzden kullanıldığında nasıl bir output vereceğini test etmek önem arz ediyor.
```py
bytes1 = b"   salamlar salamlar salamlar    " 
print(bytes1.strip(b" "), end="\n\n") # Output: b'salamlar salamlar salamlar'

bytes1 = b".. salamlar .."
print(bytes1.strip(b".. "), end="\n\n") # Output: b'salamlar'
print(bytes1.strip(b" .."), end="\n\n") # Output: b'salamlar'

bytes1 = b".. salamlar ..\n.. salamlar ..\n.. salamlar .."
print(bytes1.strip(b".. "), end="\n\n") # Output: b'salamlar ..\n.. salamlar ..\n.. salamlar'
print(bytes1.strip(b" .."), end="\n\n") # Output: b'salamlar ..\n.. salamlar ..\n.. salamlar'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.strip "https://docs.python.org/3/library/stdtypes.html#bytes.strip").

<h3 id="2.2.17"><code>rstrip(chars)</code> Methodu</h3>

`strip(chars)`'den tek farkı, sadece sağdaki kısmı kırpar. Örnek:
```py
pytes1 = b"   salamlar salamlar salamlar    " 
print(pytes1.rstrip(b" "), end="\n\n") # Output: b'   salamlar salamlar salamlar'

pytes2 = b".. salamlar .."
print(pytes2.rstrip(b".. "), end="\n\n") # Output: b'.. salamlar'
print(pytes2.rstrip(b" .."), end="\n\n") # Output: b'.. salamlar'

pytes3 = b".. salamlar ..\n.. salamlar ..\n.. salamlar .."
print(pytes3.rstrip(b".. "), end="\n\n") # Output: b'.. salamlar ..\n.. salamlar ..\n.. salamlar'
print(pytes3.rstrip(b" .."), end="\n\n") # Output: b'.. salamlar ..\n.. salamlar ..\n.. salamlar'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.rstrip "https://docs.python.org/3/library/stdtypes.html#bytes.rstrip").

<h3 id="2.2.18"><code>lstrip(chars)</code> Methodu</h3>

`strip(chars)`'den tek farkı, sadece soldaki kısmı kırpar. Örnek:
```py
pytes1 = b"   salamlar salamlar salamlar    " 
print(pytes1.lstrip(b" "), end="\n\n") # Output: b'salamlar salamlar salamlar    '

pytes2 = b".. salamlar .."
print(pytes2.lstrip(b".. "), end="\n\n") # Output: b'salamlar ..'
print(pytes2.lstrip(b" .."), end="\n\n") # Output: b'salamlar ..'

pytes3 = b".. salamlar ..\n.. salamlar ..\n.. salamlar .."
print(pytes3.lstrip(b".. "), end="\n\n") # Output: b'salamlar ..\n.. salamlar ..\n.. salamlar ..'
print(pytes3.lstrip(b" .."), end="\n\n") # Output: b'salamlar ..\n.. salamlar ..\n.. salamlar ..'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.lstrip "https://docs.python.org/3/library/stdtypes.html#bytes.lstrip").

<h3 id="2.2.19"><code>join(iterable)</code> Methodu</h3>

Uygulandığı `bytes`'ı, `iterable` parametresine girilen iterable objelerin (`list`, `tuple`, `set` ...) elemanları arasına ekleyerek bir string oluşturur ve döndürür. Örnek:
```py
m1 = [b"1",b"2",b"3"]
m2 = (b"1",b"2",b"3")
m3 = {b"1",b"2",b"3"}
print(b"--".join(m1)) # Output: b'1--2--3'
print(b"--".join(m2)) # Output: b'1--2--3'
print(b"--".join(m3)) # Output: b'1--3--2' (rastgele olmasının sebebi set'in bir özelliği)
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.join "https://docs.python.org/3/library/stdtypes.html#bytes.join").

<h3 id="2.2.20"><code>center(width, fillbyte)</code> Methodu</h3>

Uygulandığı `bytes`'ı, `width` parametresine girilen argüman kadar ortalar. Ortalama işleminde oluşan boşlukları `fillbyte` parametresine argüman olarak girilen `bytes`'lar ile doldurur. `fillbyte` parametresinin default değeri boşluk karakteridir (`b" "`). Örnek:
```py
print(b"1234".center(4,b"-")) # Output: b'1234'
print(b"1234".center(5,b"-")) # Output: b'-1234'
print(b"1234".center(6,b"-")) # Output: b'-1234-'

print(b"12345".center(5,b"-")) # Output: b'12345'
print(b"12345".center(6,b"-")) # Output: b'12345-'
print(b"12345".center(7,b"-")) # Output: b'-12345-'
```
Ortalama işleminde `fillbyte` parametresine argüman olarak girilen `bytes`'ın düzgünce kullanılabilmesi için `width` parametresinde belirtilen sayının, `center` methodunun uygulandığı `bytes`'ın uzunluğundan en az 2 fazla olması gerekmektedir. Örnek:
```py
for i in range(1,11,2):
	print(b"1".center(i,b"-"), f"({i})")

print()

for i in range(0,11,2):
	print(b"12".center(i,b"-"), f"({i})")

print()

for i in range(1,11,2):
	print(b"12345".center(i,b"-"), f"({i})")

print()

for i in range(0,11,2):
	print(b"123456".center(i,b"-"), f"({i})")
```
**Output:**
```
b'1' (1)
b'-1-' (3)
b'--1--' (5)
b'---1---' (7)
b'----1----' (9)

b'12' (0)
b'12' (2)
b'-12-' (4)
b'--12--' (6)
b'---12---' (8)
b'----12----' (10)

b'12345' (1)
b'12345' (3)
b'12345' (5)
b'-12345-' (7)
b'--12345--' (9)

b'123456' (0)
b'123456' (2)
b'123456' (4)
b'123456' (6)
b'-123456-' (8)
b'--123456--' (10)
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.center "https://docs.python.org/3/library/stdtypes.html#bytes.center").

<h3 id="2.2.21"><code>rjust(width, fillbyte)</code> Methodu</h3>

`center()` methoduna benzer çalışır. Tek farkı uygulandığı `bytes`'ı ortalamaz, sağa yaslar. `fillchar` parametresinin default değeri boşluk karakteridir (`b" "`). Örnek:
```py
for i in range(1,11,2):
	print(b"1".rjust(i,b"-"), f"({i})")

print()

for i in range(0,11,2):
	print(b"123456".rjust(i,b"-"), f"({i})")
```
**Output:**
```
b'1' (1)
b'--1' (3)
b'----1' (5)
b'------1' (7)
b'--------1' (9)

b'123456' (0)
b'123456' (2)
b'123456' (4)
b'123456' (6)
b'--123456' (8)
b'----123456' (10)
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.rjust "https://docs.python.org/3/library/stdtypes.html#bytes.rjust").

<h3 id="2.2.22"><code>ljust(width, fillbyte)</code> Methodu</h3>

`center()` methoduna benzer çalışır. Tek farkı uygulandığı `bytes`'ı ortalamaz, sola yaslar. `fillchar` parametresinin default değeri boşluk karakteridir (`b" "`). Örnek:
```py
for i in range(1,11,2):
	print(b"1".ljust(i,b"-"), f"({i})")

print()

for i in range(0,11,2):
	print(b"123456".ljust(i,b"-"), f"({i})")
```
**Output:**
```
b'1' (1)
b'1--' (3)
b'1----' (5)
b'1------' (7)
b'1--------' (9)

b'123456' (0)
b'123456' (2)
b'123456' (4)
b'123456' (6)
b'123456--' (8)
b'123456----' (10)
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.ljust "https://docs.python.org/3/library/stdtypes.html#bytes.ljust").

<h3 id="2.2.23"><code>count(x, start, end)</code> Methodu</h3>

`x` parametresine argüman olarak girilen `bytes`'ın, uygulandığı `bytes`'ın içinde kaç defa geçtiğini söyler. `start` ve `end` parametrelerine başlama ve bitiş index'lerini girerek `bytes` içerisinde belli bir bölümü kontrol edebilirsiniz. Örnek:
```py
bytes1 = b"Kahramanmaras"
print(bytes1.count(b"a")) # Output: 5
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.count "https://docs.python.org/3/library/stdtypes.html#bytes.count").

<h3 id="2.2.24"><code>index(sub, start, end)</code> Methodu</h3>

`sub` parametresine argüman olarak girilen `bytes`'ı, uygulandığı `bytes`'ın içinde soldan sağa doğru arar ve ilk kaçıncı index'de olduğunu söyler. `sub` parametresine argüman olarak birden fazla ASCII karakterden oluşan `bytes` girilirse, soldan sağa doğru arar ve o ASCII karakterlerden oluşan `bytes`'ın ilk ASCII karakterinin geçtiği index'i söyler. `start` ve `end` parametrelerine başlama ve bitiş index'lerini girerek `bytes` içerisinde belli bir bölümü kontrol edebilirsiniz. Örnek:
```py
bytes1 = b"abc abc abcd abc abc abcd abc abc"
print(bytes1.index(b"d")) # Output: 11
print(bytes1.index(b"abcd")) # Output: 8 (a ASCII karakteri ilk 8. index'te bulunmuş)
```
İstenilen `bytes`'ı bulunamazsa `ValueError` hatası yükseltilir. Örnek:
```py
bytes2 = b"abc abc abcd abc abc abcd abc abc"
print(bytes2.index(b"x")) # ValueError: substring not found
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.index "https://docs.python.org/3/library/stdtypes.html#bytes.index").

<h3 id="2.2.25"><code>rindex(sub, start, end)</code> Methodu</h3>

`index()` methodunun yaptığı işi sağdan sola yapar. Örnek:
```py
bytes1 = b"abc abc abcd abc abc abcd abc abc"
print(bytes1.rindex(b"d")) # Output: 24
print(bytes1.rindex(b"abcd")) # Output: 21 (a ASCII karakteri ilk 21. index'te bulunmuş)
print(bytes1.rindex(b"x")) # ValueError: substring not found
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.rindex "https://docs.python.org/3/library/stdtypes.html#bytes.rindex").

<h3 id="2.2.26"><code>find(sub, start, end)</code> Methodu</h3>

`index()` methodunun yaptığı işi yapar. Tek farkı, istenilen `bytes`'ı bulunamazsa `ValueError` hatası yükseltmek yerine yerine `-1` değerini döndürür. Örnek:
```py
bytes1 = b"abc abc abcd abc abc abcd abc abc"
print(bytes1.find(b"d")) # Output: 11
print(bytes1.find(b"abcd")) # Output: 8 (a ASCII karakteri ilk 8. index'te bulunmuş)
print(bytes1.find(b"x")) # Output: -1
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.find "https://docs.python.org/3/library/stdtypes.html#bytes.find").

<h3 id="2.2.27"><code>rfind(sub, start, end)</code> Methodu</h3>

`find()` methodunun sağdan sola versiyonudur. Örnek:
```py
bytes1 = b"abc abc abcd abc abc abcd abc abc"
print(bytes1.rfind(b"d")) # Output: 24
print(bytes1.rfind(b"abcd")) # Output: 21 (a ASCII karakteri ilk 21. index'te bulunmuş)
print(bytes1.rfind(b"x")) # Output: -1
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.rfind "https://docs.python.org/3/library/stdtypes.html#bytes.rfind").

<h3 id="2.2.28"><code>zfill(width)</code> Methodu</h3>

Uygulandığı `bytes`'ın soluna `width` parametresine argüman olarak girilen integer kadar sıfır (`0`) ekler. Sıfırların gözükebilmesi için `width` parametresine argüman olarak girilen integer, `zfill` methodunun uygulandığı `bytes`'ın uzunluğundan en az 2 fazla olması gerekmektedir. Örnek:
```py
print(b"1".zfill(1))   # Output: b'1'
print(b"1".zfill(2))   # Output: b'01'
print(b"123".zfill(7)) # Output: b'0000123'
```
Uygulandığı string'in en solunda `+` ya da `-` karakterleri varsa, `zfill` methodu bunu algılar ve sıfırları `+`/`-` karakterlerinden sonra koyar. Örnek:
```py
print(b"-290".zfill(8)) # Output: b'-0000290'
print(b"+290".zfill(8)) # Output: b'+0000290'
print(b"--random+text".zfill(20)) # Output: b'-0000000-random+text'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.zfill "https://docs.python.org/3/library/stdtypes.html#bytes.zfill").

<h3 id="2.2.29"><code>partition(sep)</code> Methodu</h3>

`sep` parametresine argüman olarak girilen `bytes`'ı referans alarak, uygulandığı `bytes`'ı soldan sağa doğru okur ve referansa uyan ilk yerden üçe böler. Sonucu list type olarak döndürür. Örnek:
```py
print(b"Istanbul".partition(b"an")) # Output: (b'Ist', b'an', b'bul')
```
`sep` parametresine argüman olarak girilen `bytes`, uygulandığı `bytes`'da yoksa aşağıdaki gibi bir output verir:
```py
print(b"Istanbul".partition(b"fil")) # Output: (b'Istanbul', b'', b'')
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.partition "https://docs.python.org/3/library/stdtypes.html#bytes.partition").

<h3 id="2.2.30"><code>rpartition(sep)</code> Methodu</h3>

`partition()` methodunun yaptığı işi sağdan sola yapar. Örnek:
```py
print(b"Istanbul".rpartition(b"an")) # Output: (b'Ist', b'an', b'bul')
print(b"Istanbul".rpartition(b"fil")) # Output: (b'', b'', b'Istanbul')
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.rpartition "https://docs.python.org/3/library/stdtypes.html#bytes.rpartition").

<h3 id="2.2.31"><code>expandtabs(tabsize)</code> Methodu</h3>

Uygulandığı `bytes`'ın içeriğindeki TAB (`\t`) kaçış dizisinin kaç space (boşluk) genişliğinde olacağını `tabsize` parametresine girilen integer argümanla belirleyebiliriz.
```py
print(b"elma\tbir\tmeyvedir.".expandtabs(10)) # Output: b'elma      bir       meyvedir.'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.expandtabs "https://docs.python.org/3/library/stdtypes.html#bytes.expandtabs").

<h3 id="2.2.32"><code>maketrans(from, to)</code> Methodu</h3>

`maketrans` methodu bir static method olduğu için direkt `bytes` class'ına veya `bytes` objesine uygulanabilir. `from` parametrelerine tanımalanan `bytes`'ları `to` parametresine tanımlanan `bytes`'larla eşlediği (mapping) bir `bytes` objesi döndürür. Bu mapping `bytes` objesini `translate()` methodunun `table` parametresinde kullanabiliriz. Örnek:
```py
a = b"abc"
b = b"123"
c = bytes.maketrans(a,b)
print(c) # Output: b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`123defghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.maketrans "https://docs.python.org/3/library/stdtypes.html#bytes.maketrans").

<h3 id="2.2.33"><code>translate(table)</code> Methodu</h3>

Uygulandığı `bytes`'ı, `table` parametresinde belirtilen mapping `bytes` objesine göre düzenler ve döndürür. `table` parametresine argüman olarak girilen mapping `bytes` objesi, `maketrans()` methodu ile oluşturulan mapping `bytes` objelerin formatında olmalıdır. Örnek:
```py
büyük_harfler = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
küçük_harfler = b'abcdefghijklmnopqrstuvwxyz'
bk= bytes.maketrans(büyük_harfler,küçük_harfler)
kb= bytes.maketrans(küçük_harfler,büyük_harfler)

print(b"SeLamLar BeN PytHoN".translate(bk)) # Output: b'selamlar ben python'
print(b"SeLamLar BeN PytHoN".translate(kb)) # Output: b'SELAMLAR BEN PYTHON'
```

`table` parametresinde argüman olarak girilen mapping `bytes` objesinde, `translate` methodunun uygulandığı `bytes`'ın içeriğinde bulunan bir ASCII karakter tanımlı değilse, `translate` methodu o ASCII karaktere müdahele etmez.
```py
büyük_harfler = b"ABC"
küçük_harfler = b"abc"
bk= bytes.maketrans(büyük_harfler,küçük_harfler)
kb= bytes.maketrans(küçük_harfler,büyük_harfler)

print(b"aBCD".translate(bk)) # Output: b'abcD'
print(b"aBCd".translate(kb)) # Output: b'ABCd'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.translate "https://docs.python.org/3/library/stdtypes.html#bytes.translate").

<h3 id="2.2.34"><code>title()</code> Methodu</h3>

Uygulandığı `bytes`'daki ASCII harflerinden oluşmuş her kelimenin (her kelime space karakteri ile birbirinden ayrılıyor) büyük harfle başlayıp küçük harflerle devam ettiği başlıklı (titlecased) versiyonunu döndürür. Örnek:
```py
print(b" falan filan".title()) # Output: b' Falan Filan'
print(b"falan filan".title())  # Output: b'Falan Filan'
```
Bu algoritma, kelime grupları için dilden bağımsız (language-independent) basit bir tanımlama kullanır. Bu algoritma çoğu zaman işe yarasa bile, kısaltmalarda ve kesme işaretlerinin kullanıldığı yerlerde istenmeyen sonuçlara neden olabilir. Örnek:
```py
print(b"they're bill's friends from the USA.".title()) # Output: b"They'Re Bill'S Friends From The Usa."
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.title "https://docs.python.org/3/library/stdtypes.html#bytes.title").

<h3 id="2.2.35"><code>istitle()</code> Methodu</h3>

Uygulandığı `bytes`, `title()` methodunun algoritmasına uygunsa `True`, diğer durumlarda `False` döndürür. Örnek:
```py
print((b"they're bill's friends from the USA.".title()).istitle()) # Output: True
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.istitle "https://docs.python.org/3/library/stdtypes.html#bytes.istitle").

<h3 id="2.2.36"><code>isalpha()</code> Methodu</h3>

Bir `bytes` yalnızca `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'` bunlardan oluşuyorsa, `isalpha` methodu `True`, aksi durumlarda `False` döndürür. Örnek:
```py
print(b"abcd".isalpha()) # Output: True
print(b"abcd1".isalpha()) # Output: False
print(b"abcd?".isalpha()) # Output: False
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.isalpha "https://docs.python.org/3/library/stdtypes.html#bytes.isalpha").

<h3 id="2.2.37"><code>isalnum()</code> Methodu</h3>

Bir `bytes` yalnızca `b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'` veya `b'0123456789'` bunlardan oluşuyorsa, `isalnum` methodu `True`, aksi durumlarda `False` döndürür. Örnek:
```py
print(b"abcd".isalnum()) # Output: True
print(b"1234".isalnum()) # Output: True
print(b"1234abcd".isalnum()) # Output: True
print(b"1234!".isalnum()) # Output: False
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.isalnum "https://docs.python.org/3/library/stdtypes.html#bytes.isalnum").

<h3 id="2.2.38"><code>isdigit()</code> Methodu</h3>

Bir `bytes` yalnızca `b'0123456789'` bunlardan oluşuyorsa, `isdigit` methodu `True`, aksi durumlarda `False` döndürür. Örnek:
```py
print(b"1234".isdigit()) # Output: True
print(b"abcd".isdigit()) # Output: False
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.isdigit "https://docs.python.org/3/library/stdtypes.html#bytes.isdigit").

<h3 id="2.2.39"><code>isspace()</code> Methodu</h3>

Bir `bytes`, `b" "`, `b"\t"`, `b"\n"`, `b"\r"`, `b"\x0b"`, `b"\f"` bunlardan oluşuyorsa, `isspace` methodu `True`, aksi durumlarda `False` döndürür. Örnek:
```py
print(b" ".isspace()) # Output: True
print(b"\t".isspace()) # Output: True
print(b"\n".isspace()) # Output: True
print(b"\r".isspace()) # Output: True
print(b"\x0b".isspace()) # Output: True
print(b"\f".isspace()) # Output: True
print(b"a".isspace()) # Output: False
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.isspace "https://docs.python.org/3/library/stdtypes.html#bytes.isspace").

<h3 id="2.2.40"><code>isascii()</code> Methodu</h3>

Bir `bytes` boşsa veya tamamı ASCII karakterlerden oluşuyorsa `isascii` methodu `True`, diğer durumlarda `False` döndürür. Örnek:
```py
print(b"".isascii()) # Output: True
print(b"abcs".isascii()) # Output: True
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.isascii "https://docs.python.org/3/library/stdtypes.html#bytes.isascii").

<h3 id="2.2.41"><code>removeprefix(prefix)</code> Methodu</h3>

Eğer uygulandığı `bytes`, `prefix` parametresinde argüman olarak belirtilen `bytes` ile başlıyorsa, `bytes[len(prefix):]` işleminin sonucunu döndürür. `removeprefix` methodunun uygulandığı `bytes` `prefix` parametresinde belirtilen `bytes` ile başlamıyorsa, `removeprefix` methodunun uygulandığı `bytes` aynen döndürülür. Örnek:
```py
print(b"TestHook".removeprefix(b"Test")) # Output: b'Hook'
print(b"ATestHook".removeprefix(b"Test")) # Output: b'ATestHook'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.removeprefix "https://docs.python.org/3/library/stdtypes.html#bytes.removeprefix").

<h3 id="2.2.42"><code>removesuffix(suffix)</code> Methodu</h3>

Eğer uygulandığı `bytes`, `suffix` parametresinde argüman olarak belirtilen `bytes` ile bitiyorsa, `bytes[:-len(suffix)]` işleminin sonucunu döndürür. `removesuffix` methodunun uygulandığı `bytes` `suffix` parametresinde belirtilen `bytes` ile bitmiyorsa, `removesuffix` methodunun uygulandığı `bytes` aynen döndürülür. Örnek:
```py
print(b"TestHook".removesuffix(b"Hook")) # Output: b'Test'
print(b"TestHookA".removesuffix(b"Hook")) # Output: b'TestHookA'
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#bytes.removesuffix "https://docs.python.org/3/library/stdtypes.html#bytes.removesuffix").