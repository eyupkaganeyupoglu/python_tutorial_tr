# İçindekiler
- [Sayı Kümeleri](#1)
    - [Tam Sayılar (Integers)](#1.1)
    - [Ondalıklı Sayılar (Float)](#1.2)
    - [Komplex Sayılar (Complex)](#1.3)
- [Sayı Sistemleri](#2)
    - [İkili (Binary) sayma sistemi](#2.1)
    - [Sekizli (Octal) sayma sistemi](#2.2)
    - [Onlu (Desimal) sayma sistemi](#2.3)
    - [On altılı (Heksadesimal) sayma sistemi](#2.4)
- [Numeric Data Types](#3)
    - [`int(x, base=10)` Fonksiyonu](#3.1)
        - [`bit_length()` Methodu](#3.1.1)
    - [`float(x)` Fonksiyonu](#3.2)
        - [`as_integer_ratio()` Methodu](#3.2.1)
        - [`is_integer()` Methodu](#3.2.2)
    - [`complex(real, imag)` Fonksiyonu](#3.3)
        - [`real` Methodu](#3.3.1)
        - [`imag` Methodu](#3.3.2)
- [Numeric Fonksiyonlar](#4)
    - [`bin(x)` Fonksiyonu](#4.1)
    - [`oct(x)` Fonksiyonu](#4.2)
    - [`hex(x)` Fonksiyonu](#4.3)
    - [`pow(base, exp, mod)` Fonksiyonu](#4.4)
    - [`abs(x)` Fonksiyonu](#4.5)
    - [`round(number, ndigits)` Fonksiyonu](#4.6)
    - [`divmod(a, b)` Fonksiyonu](#4.7)
    - [`max(item, *items, key, default)` Fonksiyonu](#4.8)
    - [`min(item, *items, key, default)` Fonksiyonu](#4.9)
    - [`sum(iterable, start=0)` Fonksiyonu](#4.10)

<h1 id="1">Sayı Kümeleri</h1>

<h2 id="1.1">Tam Sayılar (Integers)</h2>

Türkçe'deki **"Tam Sayılar"** kavramının İngilizce karşılığı **Integer**'dır. Negatif ve pozitif tam sayıların tamamını temsil eder. Matematikte **Z** harfi integer'ları temsil eder.

<h2 id="1.2">Ondalıklı Sayılar (Float)</h2>

Türkçe'deki **"Kesirli Sayılar"**, **"Kayan Noktalı Sayılar"**, **"Ondalıklı Sayılar"** kavramlarının İngilizce karşılığı **Floating Point Numbers**, kısaca **Float**'dır. Negatif ve pozitif kesirli sayıların tamamını temsil eder. Matematikte **Q** harfi, floating point sayıları temsil eder.

<h2 id="1.3">Komplex Sayılar (Complex)</h2>

Türkçe'deki **Komplex Sayılar**, **"Karmaşık Sayılar"** kavramlarının İngilizce karşılığı **Complex Numbers**, kısaca **Complex**'dır. Komplex sayıların tamamını temsil eder. Matematikte **C** harfi, komplex sayıları temsil eder.

<h1 id="2">Sayı Sistemleri</h1>

<h2 id="2.1">İkili (Binary) sayma sistemi</h2>

`0, 1` olmak üzere toplam iki sayısal simgeden oluşur.

<h2 id="2.2">Sekizli (Octal) sayma sistemi</h2>

`0, 1, 2, 3, 4, 5, 6, 7` olmak üzere toplam sekiz sayısal simgeden oluşur.  

<h2 id="2.3">Onlu (Desimal) sayma sistemi</h2>

`0, 1, 2, 3, 4, 5, 6, 7, 8, 9` olmak üzere toplam on sayısal simgeden (rakamlar) oluşur.

<h2 id="2.4">On altılı (Heksadesimal) sayma sistemi</h2>

`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f` olmak üzere toplam on altı sayısal ve harfsel simgeden oluşur. `a, b, c, d, e, f` yerine `A, B, C, D, E, F` de kullanılabilir.

<h1 id="3">Numeric Data Types</h1>

<h2 id="3.1"><code>int(x, base=10)</code> Fonksiyonu</h2>

`int()` build-in fonksiyonu, `x` parametresine girilen argümanı **uygunsa** `int` class'ında belirtilen integer data type'a dönüştürmekte kullanılır. `base` parametresine, bu çevirme işleminin hangi sayı sistemine göre yapılacağını belirleyebilirsiniz. `base` parametresinin default değeri `10`'dur.
```py
print(int(0b1010)) # Output: 10
print(int("1010")) # Output: 1010
print(int("1010", base=2)) # Output: 10
print(int("1010", base=8)) # Output: 520
print(int("1010", base=10)) # Output: 1010
print(int("1010", base=16)) # Output: 4112
```
**Not:** Float formatta yazılmış string data type bir value'yu direkt integer type'a çeviremezsiniz. Önce string'den float'a, sonra float'dan integer'e çevirmelisiniz. Örnek:
```py
a = "12.55"
a = float(int(a))
print(a) # Output: 12
```
**Not:** `int()` fonksiyonunun `x` parametresine herhangi bir argüman girmezseniz, `int()` fonksiyonu `0` değerini döndürür.
```py
print(int()) # Output: 0
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#int "https://docs.python.org/3/library/functions.html#int").

<h3 id="3.1.1"><code>bit_length()</code> Methodu</h3>

`bit_length()` methodu, uygulandığı integer'ın bit uzunluğunu döndürür. `bin()` fonksiyonu, kendisine argüman olarak verilen integer'ın bit karşılığını döndürür (Örnek: `print(bin(10))`: `0b1010`). `len(bin()[2:])` kodu ile `bit_length()` methodunun yaptığı iş aynıdır. Örnek:
```py
print((10).bit_length()) # Output: 4 (`1010` 4 birim uzunluğundadır)
print(len(bin(10)[2:])) # Output: 4 (`1010` 4 birim uzunluğundadır)
```

<h2 id="3.2"><code>float(x)</code> Fonksiyonu</h2>

`float()` build-in fonksiyonu, `x` parametresine girilen argümanı **uygunsa** `float` class'ında belirtilen float data type'a dönüştürmekte kullanılır.
```py
float_number = float(str("12.50"))
print(float_number) # Output: 12.50
print(type(float_number)) # Output: <class 'float'>
```

**Not:** `float()` fonksiyonunun `x` parametresine herhangi bir argüman girmezseniz, `float()` fonksiyonu `0.0` değerini döndürür.
```py
print(float()) # Output: 0.0
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#float "https://docs.python.org/3/library/functions.html#float").

<h3 id="3.2.1"><code>as_integer_ratio()</code> Methodu</h3>

Birbirine bölündüğünde uygulandığı `float` sayıyı veren en küçük iki integer'ı döndürür. Bu iki sayı `tuple` içinde döndürülür. Örnek:
```py
print((4.5).as_integer_ratio()) # Output: (9, 2)
print((4.1).as_integer_ratio()) # Output: (2308094809027379, 562949953421312)
print((5).as_integer_ratio()) # Output: (5, 1)
print((9.3).as_integer_ratio()) # Output: (2617717283409101, 281474976710656)
print((6.125).as_integer_ratio()) # Output: (49, 8)
print((9.337).as_integer_ratio()) # Output: (2628131857547395, 281474976710656)
```

<h3 id="3.2.2"><code>is_integer()</code> Methodu</h3>

Bir `float`'ın tam olmayan kısmında (noktanın sağındaki, ondalık olmayan) sıfır harici bir sayı olup olmadığını kontrol eder. Yani bu methodla, bir sayının integer'mı floating'mı olduğunu sorgulayabilirsiniz. Bu method, uygulandığı `float` integer ise `True`, değilse (yani integer ise) `False` döndürür. Örnek:
```py
print((10.00).is_integer()) # Output: True
print((10.01).is_integer()) # Output: False
```

<h2 id="3.3"><code>complex(real, imag)</code> Fonksiyonu</h2>

`complex()` build-in fonksiyonu, kendisine girilen argümanı **uygunsa** `complex` class'ında belirtilen complex data type'a dönüştürmekte kullanılır. Bir complex sayı real ve imag olmak üzere 2 parçadan oluşur:
- `real`, gerçek kısmı ifade eder.
- `imag`, sanal kısmı ifade eder.

**Not:** `complex` bir sayıyı sadece `str` data type'ına dönüştürebilirsin (tam tersi de geçerli). `int` ya da `float` data type'a dönüştüremezsin, `TypeError` hatası alırsın.

**Not:** `complex()` fonksiyonunun `x` parametresine herhangi bir argüman girmezseniz, `complex()` fonksiyonu `0j` değerini döndürür.
```py
print(complex()) # Output: 0j
```

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#complex "https://docs.python.org/3/library/functions.html#complex").

<h3 id="3.3.1"><code>real</code> Methodu</h3>

Bir complex sayının real kısmını döndüren property objesidir.
```py
print((12+5j).imag) # Output: 12.0
```

<h3 id="3.3.2"><code>imag</code> Methodu</h3>

Bir complex sayının imag kısmını döndüren property objesidir.
```py
print((12+5j).imag) # Output: 5.0
```

<h1 id="4">Numeric Fonksiyonlar</h1>

<h2 id="4.1"><code>bin(x)</code> Fonksiyonu</h2>

`x` parametresine girilen integer'ın binary karşılığını döndürür. Döndürdüğü değer string formattadır. Binary sayılar `0b`/`0B` ile temsil edilir (örnek `0b1010`). Bu yüzden `bin(10)[2:]` şeklinde bir kullanımla `0b`/`0B` kısımlarından sonraki kısmı alabilirsiniz. `x` parametresinde bir integer belirtilmemişse `TypeError` hatası yükseltir. Daha Fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#bin "https://docs.python.org/3/library/functions.html#bin"). Örnek:
```py
print(bin(10)) # Output: 0b1010
print(bin(10)[2:]) # Output: 1010
print(type(bin(10))) # Output: <class 'str'>
```

<h2 id="4.2"><code>oct(x)</code> Fonksiyonu</h2>

`x` parametresine girilen integer'ın octal karşılığını döndürür. Döndürdüğü değer string formattadır. Octal sayılar `0o`/`0O` ile temsil edilir (örnek `0o1010`). Bu yüzden `oct(10)[2:]` şeklinde bir kullanımla `0o`/`0O` kısımlarından sonraki kısmı alabilirsiniz. `x` parametresinde bir integer belirtilmemişse `TypeError` hatası yükseltir. Daha Fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#oct "https://docs.python.org/3/library/functions.html#oct"). Örnek:
```py
print(oct(10)) # Output: 0o12
print(oct(10)[2:]) # Output: 12
print(type(oct(10))) # Output: <class 'str'>
```

<h2 id="4.3"><code>hex(x)</code> Fonksiyonu</h2>

`x` parametresine girilen integer'ın hexadecimal karşılığını döndürür. Döndürdüğü değer string formattadır. Hexadecimal sayılar `0x`/`0X` ile temsil edilir (örnek `0o1010`). Bu yüzden `hex(10)[2:]` şeklinde bir kullanımla `0x`/`0X` kısımlarından sonraki kısmı alabilirsiniz. `x` parametresinde bir integer belirtilmemişse `TypeError` hatası yükseltir. Daha Fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#hex "https://docs.python.org/3/library/functions.html#hex"). Örnek:
```py
print(hex(10)) # Output: 0xa
print(hex(10)[2:]) # Output: a
print(type(hex(10))) # Output: <class 'str'>
```

<h2 id="4.4"><code>pow(base, exp, mod)</code> Fonksiyonu</h2>

`mod` parametresine argüman girilmemişse `(base**exp)` işlemini, girilmişse `(base**exp) % mod` işlemini yapar. `pow(base, exp, mod)` yerine `pow(base, exp) % mod` şeklindeki kullanım daha verimlidir. `base`, `exp` ve `mod` parametrelerine girilen argümanlar numeric type olmak zorundadır. Aksi halde `TypeError` hatası yükseltilir. Örnek:
```py
print(pow(2,3,2)) # ((2 ** 3) % 2) == 0
```
- Integer type olan `base` ve `exp` için `mod` mevcutsa, `mod` integer ve nonzero (sıfır olmayan) olmalıdır.
- `mod` mevcut ve `exp` negatif bir integer ise, `base`, `mod` için nispeten asal (relatively prime) olmalıdır.

Daha Fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#pow "https://docs.python.org/3/library/functions.html#pow").

<h2 id="4.5"><code>abs(x)</code> Fonksiyonu</h2>

"abs",*mutlak anlamına gelen absolute kelimesinden gelmektedir. Bu fonksiyon, `x` parametresine girilen değerin mutlak değerini döndürür. `x` parametresine girilen argümanlar integer, floating point ya da `__abs__()` uygulanabilen bir class objesi (instance) olabilir. Bu argüman bir complex sayı olursa, magnitude (büyüklüğü) döndürülür. Daha Fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#abs "https://docs.python.org/3/library/functions.html#abs").
```py
print(abs(-15)) ; print(abs(15)) # Output: 15
print(abs(-15.18)) ; print(abs(15.18)) # Output: 15.18
print(abs(-15+3j)) ; print(abs(15+3j)) # Output: 15.297058540778355
```

<h2 id="4.6"><code>round(number, ndigits)</code> Fonksiyonu</h2>

`number` parametresine girilen integer'ın `10**(ndigits)`'inci basamağını, `10**(ndigits - 1)`'inci basamağını referans alarak yuvarlar:
```py
print(round(2.6, 0)) # Output: 3.0 (10^(0-1) = 10^(-1))
print(round(2.66, 1)) # Output: 2.7 (10^(-1-1) = 10^(-2))
print(round(2.666, 2)) # Output: 2.67 (10^(-2-1) = 10^(-3))
```
`ndigits` parametresine `0`, `None` değerleri girilirse ya da hiçbir değer girilmezse aşağıdaki gibi davranır:
```py
print(round(2.6, 0)) # Output: 3.0
print(round(2.6, None)) # Output: 3
print(round(2.6)) # Output: 3
```
Tam ortada kalan değerler (`2.5`, `9.5` vs.), en yakın çift sayıya yuvarlanır:
```py
print(round(2.5)) # Output: 2
print(round(1.5)) # Output: 2

print(round(-1.5)) # Output: -2
print(round(-2.5)) # Output: -2
```
`0,5` ile `-0.5` sayıları istisnadır. İki sayı da `0`'a yuvarlanır:
```py
print(round(0.5)) # Output: 0
print(round(-0.5)) # Output: 0
```
**Dikkat:** `round()` fonksiyonu, bazı sayılarda istenilen sonucu döndürmez. Örneğin `round(2.675,  2)` fonksiyonunun output'u `2.68` olması beklenirken `2.67` output'unu alırsınız. Bunun nedeni [Float Sapması](https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues)'dır.  Bu kusur, float sapması için spesifik önlemler almamış bütün programlama dillerinde vardır. Örneğin Normal şartlar altında `0.1 + 0.2` işleminin sonucu `0.3`'dür ama Python'da `0.30000000000000004` sonucunu alırsınız.
```py
print(0.1 + 0.2) # Output: 0.30000000000000004
```
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#round "https://docs.python.org/3/library/functions.html#round").

<h2 id="4.7"><code>divmod(a, b)</code> Fonksiyonu</h2>

`complex` olmayan iki sayıyı alır ve matematikteki `a/b` işlemindeki bölüm ve kalanı döndürür. Yani aşağıdaki bölme işleminde C ve D kısımlarını döndürür.
```
 A | B 
   |----
---| C
 D
```
Integer'lar için output `((a // b), (a % b))` işlemiyle aynıdır. Bu output `tuple` formatındadır.
```py
print(divmod(10, 2)) # Output: (5, 0)
```

<h2 id="4.8"><code>max(item, *items, key, default)</code> Fonksiyonu</h2>

`item` parametresine girilen `list`, `tuple` ya da `set` objesinin içerdiği en büyük öğeyi ya da bir `dict` objesinin içerdiği en büyük `key`'i döndürür. Ayrıca `*items` yıldızlı parametresi sayesinde, birden fazla `item` girmemize izin verir. `*items` parametresine girilen itemlerin data type'ları farklı olursa sorun çıkabilir. Örnek:
```py
# 1. Kod
print(max([1,2],"sel",(1,2,3,4))) # TypeError: '>' not supported between instances of 'str' and 'list'
```
Ama aynı kodu şöyle yazarsak sorun çıkmaz:
```py
# 2. Kod
print(max([1,2],"sel",(1,2,3,4), key=len)) # Output: (1, 2, 3, 4)
```
`key` parametresine argüman olarak girilen ölçüte göre `item` ya da `*items` parametresine girilen argümanlar sıralanır. Bu parametreye argüman girilmediğinde Python, bütün item'ları `>` operator'ını kullanarak sıralamaya çalıştığı ve farklı data type'lar arasında bu operator kullanılamadığı için hata yükseltir. Ama `key` parametresine argüman olarak hangi sıralama ölçütü ile sıralama işlemi yapılacağı belirtilirse ve bu ölçüt bütün `item`'larda uygulanabilirse (örneğin `len`, yukarıdaki bütün `item`'lara uygulanabilir) sorun çıkmaz. Örnek:
```py
print(min([1,2],"sel", 12, key=len))
# Output: TypeError: object of type 'int' has no len()
```
Gördüğünüz gibi integer bir değere `len` uygulanamadığı için hata yükseltildi.

<h2 id="4.9"><code>min(item, *items, key, default)</code> Fonksiyonu</h2>

`item` parametresine girilen `list`, `tuple` ya da `set` objesinin içerdiği en küçük öğeyi ya da bir `dict` objesinin içerdiği en küçük `key`'i döndürür. Ayrıca `*items` yıldızlı parametresi sayesinde, birden fazla `item` girmemize izin verir. `*items` parametresine girilen itemlerin data type'ları farklı olursa sorun çıkabilir. Örnek:
```py
# 1. Kod
print(min([1,2],"sel",(1,2,3,4))) # TypeError: '>' not supported between instances of 'str' and 'list'
```
Ama aynı kodu şöyle yazarsak sorun çıkmaz:
```py
# 2. Kod
print(min([1,2],"sel",(1,2,3,4), key=len)) # Output: [1,2]
```
`key` parametresine argüman olarak girilen ölçüte göre `item` ya da `*items` parametresine girilen argümanlar sıralanır. Bu parametreye argüman girilmediğinde Python, bütün item'ları `>` operator'ını kullanarak sıralamaya çalıştığı ve farklı data type'lar arasında bu operator kullanılamadığı için hata yükseltir. Ama `key` parametresine argüman olarak hangi sıralama ölçütü ile sıralama işlemi yapılacağı belirtilirse ve bu ölçüt bütün `item`'larda uygulanabilirse (örneğin `len`, yukarıdaki bütün `item`'lara uygulanabilir) sorun çıkmaz. Örnek:
```py
print(min([1,2],"sel", 12, key=len))
# Output: TypeError: object of type 'int' has no len()
```
Gördüğünüz gibi integer bir değere `len` uygulanamadığı için hata yükseltildi.

<h2 id="4.10"><code>sum(iterable, start=0)</code> Fonksiyonu</h2>

`iterable` parametresine girilen `list`, `tuple` ya da `set` objesinin içerdiği öğelerin ya da bir `dict` objesinin içerdiği `key`'lerin toplamını döndürür.  Bu toplama işlemi matematiksel düzeydedir. Yani sadece numeric type'ları kabul eder. Örnek:
```py
print(sum([1, 2.6, 3+4j])) # Output: (6.6+4j)
```
`sum()` fonksiyonunun `start` parametresine argüman olarak bir numeric type girilirse, bu fonksiyon, `iterable` parametresine girilen argümanlar üzerinde işlem yaptıktan sonra sonucu `start` parametresiyle toplar ve döndürür. Örnek:
```py
print(sum([1, 2.6, 3+4j], 5)) # Output: (11.6+4j)
```