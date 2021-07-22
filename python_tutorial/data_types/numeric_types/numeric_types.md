# Sayı Kümeleri

## Tamsayılar (Integer)
Türkçe'deki **tam sayının** İngilizce karşılığı **Integer**'dır. Negatif ve pozitif tam sayıların tamamını temsil eder. Matematikte **Z** harfi, Integer sayıları temsil eder.

## Ondalıklı Sayılar (Float)
Türkçe'deki **kesirli sayılar** İngilizce karşılığı **floating point**, kısaca **float**'dır. Negatif ve pozitif kesirli sayıların tamamını temsil eder. Matematikte **Q** harfi, floating point sayıları temsil eder.

## Komplex Sayılar (Complex)
Türkçe'deki **komplex sayının** İngilizce karşılığı **Complex**'dır. Komplex sayıların tamamını temsil eder. Matematikte **C** harfi, Komplex sayıları temsil eder.

# Sayı Sistemleri

## İkili (Binary) sayma sistemi
`0, 1` olmak üzere toplam iki simgeden oluşur.

## Sekizli (Octal) sayma sistemi
`0, 1, 2, 3, 4, 5, 6, 7` olmak üzere toplam sekiz simgeden oluşur.  

## Onlu (Desimal) sayma sistemi
`0, 1, 2, 3, 4, 5, 6, 7, 8, 9` olmak üzere toplam on rakamdan/simgeden oluşur.

## On altılı (Heksadesimal) sayma sistemi
`0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f` olmak üzere toplam on altı simgeden oluşur. `a, b, c, d, e, f` yerine `A, B, C, D, E, F` de kullanılabilir.

# Numeric Data Types

## `int(x, base=10)`
Tam sayı anlamına gelen integer sayıları temsil eder. `int()` build-in fonksiyonu, `x`parametresine girilen argümanı **uygunsa** `int` class'ında belirtilen integer data type'a dönüştürmekte kullanılabilir. `base` parametresine, bu çevirme işleminin hangı sayı sistemine göre yapılacağını belirleyebilirsiniz. `base` parametresinin default değeri `10`'dur. Örneğin 8'li sayı sistemindeki `1010` sayısı, 10'lu sayı sistemindeki `520` sayısına eşit olduğu için `int("1010", base=8)` işleminin sonucu `520`'dir.
```py
print(int(0b1010)) # Output: 10
print(int("10")) # Output: 10
print(int("1010", base=2)) # Output: 10
print(int("1010", base=8)) # Output: 520
print(int("1010", base=10)) # Output: 1010
print(int("1010", base=16))) # Output: 4112
```
**Not:** floating point formattaki `str` data type bir value'yi direkt `int` type'a çeviremezsin. Önce `str`'den `float`'a, sonra `float`'dan `int`'e çevirmelisin. Örnek:
```py
a = "12.55"
a = float(int(a))
print(a) # Output: 12
```
**Not:** `int()` tek başına `0` value'sine sahiptir.
```py
print(int()) # Output: 0
```
### Integer Class Methodları

#### `bit_length()`
Uygulandığı integer sayının kaç bit yer kapladığını söyler. `bin()` fonksiyonu, herhangi bir integer sayıyı binary'e dönüştürüp döndürür. Örneğin `10` integer sayısının binary karşılığı `0b1010`'dır. Bu binary sayının ilk iki index'inden sonrası, bu integer sayının bir uzunluğu (bit length) oluyor. `len(bin())` komutunu `len(bin()[2:])` şeklinde kullanırsak istediğimiz sonucu elde ederiz. `len(bin()[2:])` komutuyla `bit_length()` methodunun yaptığı iş aynıdır. Örnek:
```py
print((10).bit_length()) # Output: 4
print(len(bin(10)[2:])) # Output: 4
``` 

## `float(x)`
Kesirli/Ondalıklı sayıları ifade eder. *Kayan noktalı sayılar* anlamına gelmektedir. `int` data type'ı `float` data type'a çevirebilir. `str` data type'ı `float` data type'a çevirebilmesi için string değerin floating point number formatına uygun olması gerekiyor. Yani:
```py
float_number = float(str("12.50")
print(float_number) # Output: 12.50
print(type(float_number)) # Output: <class 'float'>
```
**Not:** `float()` tek başına `0.0` value'sine sahiptir.
```py
print(float()) # Output: 0.0
```
### Float Class Methodları

#### `as_integer_ratio()`
Birbirine bölündüğünde uygulandığı `float` sayıyı veren en küçük iki tane integer sayı döndürür. Döndürdüğü output'u `tuple` içindedir.
```py
print((4.5).as_integer_ratio()) # Output: (9, 2)
print((4.1).as_integer_ratio()) # Output: (2308094809027379, 562949953421312)
print((5).as_integer_ratio()) # Output: (5, 1)
print((9.3).as_integer_ratio()) # Output: (2617717283409101, 281474976710656)
print((6.125).as_integer_ratio()) # Output: (49, 8)
print((9.337).as_integer_ratio()) # Output: (2628131857547395, 281474976710656)
```

#### `is_integer()`
Bir `float` sayının, tam olmayan kısmında (noktanın sağındaki, ondalık olmayan) sıfır harici bir sayı olup olmadığını kontrol eder. Yani bu methodla, bir sayının integer'mı floating point'mi olduğunu sorgulayabilirsiniz.

## `complex(real, imag)`
Kompleks sayıları ifade etmek için kullanılır. `15 + 3j` gibi sayılar complex data type'ına sahip sayılardır.
- `real`, gerçek kısmı ifade eder.
- `imag`, sanal kısmı ifade eder.

**Not:** `complex` bir sayıyı sadece `str` data type'ına dönüştürebilirsin. `int` ya da `float` data type'a dönüştüremezsin, `TypeError` hatası alırsın.

**Not:** `complex()` tek başına `0j` value'sine sahiptir.
```py
print(complex()) # Output: 0j
```
### Complex Class Methodları
#### `imag`
Bir complex number'ın **imag** kısmını döndürür.
```py
print((12+5j).imag) # Output: 5.0
```

#### `real`
Bir complex number'ın **real** kısmını döndürür.
```py
print((12+5j).real) # Output: 12.0
```
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#complex).

# Numeric Fonksiyonlar

## `bin(x)`
`x` parametresine girilen integer sayının binary karşılığını döndürür. Output'u **string** type'dır ve her output `0b` ile başlar çünkü binary sayılar Python'da `0b` ya da `0B` ile temsil edilir. `x` parametresinde bir integer belirtilmemişse `TypeError` hatası yükseltir. Daha Fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#bin).
```py
print(bin(10)) # Output: 0b1010
print(bin(10[2:])) # Output: 1010
```

## `oct(x)`
`x` parametresine girilen integer sayının octal karşılığını döndürür. Output'u **string** type'dır ve her output `0o` ile başlar çünkü binary sayılar Python'da `0o` ile temsil edilir. Bu sayede index işlemleri yapabiliriz. `x` parametresinde bir integer belirtilmemişse `TypeError` hatası yükseltir. Daha Fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#oct).
```py
print(oct(10)) # Output: 0o12
print(oct(10[2:])) # Output: 12
```

## `hex(x)`
`x` parametresine girilen integer sayının hexadecimal karşılığını döndürür. Output'u **string** type'dır ve her output `0x` ile başlar çünkü binary sayılar Python'da `0x` ile temsil edilir. Bu sayede index işlemleri yapabiliriz. `x` parametresinde bir integer belirtilmemişse `TypeError` hatası yükseltir. Daha Fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#hex).
```py
print(hex(10)) # Output: 0xa
print(hex(10[2:])) # Output: a
```

## `pow(base, exp, mod)`
`mod` girilmemişse `(base**exp)`, `mod` girilmişse `(base**exp) % mod)` işlemini yapar. `pow(base, exp, mod)` yerine `pow(base, exp) % mod` şeklindi kullanım daha verimlidir. `base`, `exp` ve `mod` parametrelerine girilen argümanlar numeric type olmak zorundadır. `int` type `base` ve `exp` için `mod` mevcutsa, `mod` integer ve nonzero olmalıdır. Eğer `mod` mevcut ve `exp` negatifse, `base`, `mod` için nispet asal (relatively prime) olmalıdır. Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#pow).
```py
print(pow(2,3,2)) # (2 ** 3) % 2
# Output: 0
```

## `abs(x)`
abs, **mutlak** anlamına gelen **absolute** kelimesinden gelmektedir. Bu fonksiyon, `x` parametresine girilen değerin mutlak değerini döndürür. `x` parametresine girilen argümanlar integer, floating point ya da `__abs__()` uygulanabilen bir obje olabilir. Bu argüman bir complex sayı olursa, magnitude (büyüklüğü) döndürülür. Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#abs).
```py
print(abs(-15)) ; print(abs(15)) # Output: 15
print(abs(-15.18)) ; print(abs(15.18)) # Output: 15.18
print(abs(-15+3j)) ; print(abs(15+3j)) # Output: 15.297058540778355
```

## `round(number, ndigits)`
`number` parametresine girilen değeri, `10^(ndigits - 1)`'inci basamağını referans alarak `10^(ndigits)`'inci basamağı yuvarlar:
```py
print(round(2.6, 0)) # Output: 3.0 (10^(0-1) = 10^(-1))
print(round(2.66, 1)) # Output: 2.7 (10^(0-2) = 10^(-2))
print(round(2.666, 2)) # Output: 2.67 (10^(0-2) = 10^(-3))
```
`ndigits` parametresine `0`, `None` değerleri girilirse ya da hiçbir değer girilmezse aşağıdaki gibi davranır. `round()` fonksiyonuna `None` değeri girildiğinde ya da hiçbir değer girilmediğinde, aynı davranışı sergiler:
```py
print(round(2.6, 0)) # Output: 3.0
print(round(2.6, None)) # Output: 3
print(round(2.6)) # Output: 3
```
`round()` fonksiyonuna tam ortada kalan değerler (`2.5`, `9.5`) girerseniz, en yakın çift sayıya yuvarlar. Yani:
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
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#round).

## `divmod(a, b)`
`complex` olmayan iki sayıyı alır ve matematikteki `a/b` işlemindeki bölüm ve kalanı verir. Integer sayılar için output `((a // b), (a % b))` işlemiyle aynıdır. Bu output `tuple` şeklindedir.
```py
divmod(10, 2)
# Output: (5, 0)
# Bölüm: 5
# Kalan: 0
```

## `max(item, *items, key, default)`
`item` parametresine girilen `list`, `tuple` ya da `set` objesinin içerdiği en büyük öğeyi ya da bir `dict` objesinin içerdiği en büyük `key`'i döndürür. Ayrıca `*items` yıldızlı parametresi sayesinde, birden fazla `item` girmemize izin verir. `*items` parametresine girilen itemlerin data type'ları farklı olursa sorun çıkabilir. Örnek:
```py
# 1. Kod
print(max([1,2],"sel",(1,2,3,4)))
# Output: TypeError: '>' not supported between instances of 'str' and 'list'
```
Ama aynı kodu şöyle yazarsak sorun çıkmaz:
```py
# 2. Kod
print(max([1,2],"sel",(1,2,3,4), key=len))
# Output: (1, 2, 3, 4)
```
`key` parametresi, kendisine verilen ölçüte göre `item` ya da `*items` parametresine girilen itemleri sıralar. Yukarıdaki kodlarda, `1. kod`'da sıkıntı çıkmasının sebebi: `1. kod`'da sıralama ölçütü belirtilmediği için `>` operatörüyle itemleri birbiriyle karşılaştırması ve farklı data type'lar arasında bu operatörle karşılaştırma işlemi yapılamamasıdır.  `2. kod`'da çıkmamasının sebebi: Sıralama ölçütünü `key` parametresinde belirttikten sonra bütün itemlerin `key`'de belirtilen sıralama ölçütünü desteklemesidir. Örnek:
```py
print(max([1,2],"sel", 12, key=len))
# Output: TypeError: object of type 'int' has no len()
```
Gördüğünüz gibi bu kodda `key` parametresinde `len` belirtilen sıralama ölçütünü `int` data type'ı desteklemediği için kod hata verdi.

## `min(item, *items, key, default)`
`item` parametresine girilen `list`, `tuple` ya da `set` objesinin içerdiği en küçük öğeyi ya da bir `dict` objesinin içerdiği en küçük `key`'i döndürür. Ayrıca `*items` yıldızlı parametresi sayesinde, birden fazla `item` girmemize izin verir. `*items` parametresine girilen itemlerin data type'ları farklı olursa sorun çıkabilir. Örnek:
```py
# 1. Kod
print(min([1,2],"sel",(1,2,3,4)))
# Output: TypeError: '>' not supported between instances of 'str' and 'list'
```
Ama aynı kodu şöyle yazarsak sorun çıkmaz:
```py
# 2. Kod
print(max([1,2],"sel",(1,2,3,4), key=len))
# Output: [1,2]
```
`key` parametresi, kendisine verilen ölçüte göre `item` ya da `*items` parametresine girilen itemleri sıralar. Yukarıdaki kodlarda, `1. kod`'da sıkıntı çıkmasının sebebi: `1. kod`'da sıralama ölçütü belirtilmediği için `<` operatörüyle itemleri birbiriyle karşılaştırması ve farklı data type'lar arasında bu operatörle karşılaştırma işlemi yapılamamasıdır.  `2. kod`'da çıkmamasının sebebi: Sıralama ölçütünü `key` parametresinde belirttikten sonra bütün itemlerin `key`'de belirtilen sıralama ölçütünü desteklemesidir. Örnek:
```py
print(min([1,2],"sel", 12, key=len))
# Output: TypeError: object of type 'int' has no len()
```
Gördüğünüz gibi bu kodda `key` parametresinde `len` belirtilen sıralama ölçütünü `int` data type'ı desteklemediği için kod hata verdi.

## `sum(iterable, start=0)`
`iterable` parametresine girilen `list`, `tuple` ya da `set` objesinin içerdiği öğelerin ya da bir `dict` objesinin içerdiği `key`'lerin toplamını döndürür.  Bu toplama işlemi matematiksel düzeydedir. Yani sadece numeric type'ları kabul eder. Örnek:
```py
print(sum([1, 2.6, 3+4j]))
# Output: (6.6+4j)
```
`sum()` fonksiyonunun `start` parametresine bir numeric type girilirse, bu fonksiyon, `iterable` parametresinin sonucu, `start` parametresiyle toplar ve sonucu döndürür. Örnek:
```py
print(sum([1, 2.6, 3+4j], 5))
# Output: (11.6+4j)
```