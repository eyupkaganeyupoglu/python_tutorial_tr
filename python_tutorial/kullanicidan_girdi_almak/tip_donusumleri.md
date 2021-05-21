# Bazı Data Type'lar

## `int(x = 0, base = 10)`
Tam sayı anlamına gelen integer sayıları temsil eder. Diğer data type'ları **uygunsa** `int` data typr'ına dönüştürmekte kullanılabilir. Genelde `int` data type olarak bilinir. `int(x=0, base=10)` syntax'ına sahiptir.
- `x`, tam sayı değerini ifade eder. Default değeri `0`'dır.
- `base`, bit değerini ifade eder. Default değeri `10`'dur.

```py
# binary 0b or 0B
print("1010 sayısının int karşılığı:", int('1010', 2))
# Output: 1010 sayısının int karşılığı: 10
print("0b1010 sayısının int karşılığı:", int('0b1010', 2))
# Output: 0b1010 sayısının int karşılığı: 10

# octal 0o or 0O
print("12 sayısının int karşılığı:", int('12', 8))
# Output: 12 sayısının int karşılığı: 10
print("0o12 sayısının int karşılığı:", int('0o12', 8))
# Output: 0o12 sayısının int karşılığı: 10

# hexadecimal
print("A sayısının int karşılığı:", int('A', 16))
# Output: A sayısının int karşılığı: 10
print("0xA sayısının int karşılığı:", int('0xA', 16))
# Output: 0xA sayısının int karşılığı: 10
```
**Not:** floating point formattaki `str` data type bir value'yi direkt `int` type'a çeviremezsin. Önce `str`'den `float`'a, sonra `float`'dan `int`'e çevirmelisin. Örnek:
```py
a = "12.55"
a = float(a)
a = int(a)
print(a) # Output: 12
```

## `float([x])`
Kesirli/Ondalıklı sayıları ifade eder. *Kayan noktalı sayılar* anlamına gelmektedir. `int` data type'ı `float` data type'a çevirebilir. `str` data type'ı `float` data type'a çevirebilmesi için string değerin floating point number formatına uygun olması gerekiyor. Yani:
```py
str_number = str("12.50")
float_number = float(str_number)
print(float_number) # Output: 12.50
print(type(float_number)) # Output: <class 'float'>
```
`float(x = 0.0)` syntax'ına sahiptir.
- `x` floating point sayıyı ifade eder. Default değer olarak `0.0` alır.

## `complex([real[, imag]])`
Kompleks sayıları ifade etmek için kullanılır. `15 + 3j` gibi sayılar complex data type'ına sahip sayılardır.
- `real`, gerçek kısmı ifade eder.
- `imag`, sanal kısmı ifade eder.

**Not:** `complex` bir sayıyı sadece `str` data type'ına dönüştürebilirsin. `int` ya da `float` data type'a dönüştüremezsin, `TypeError` hatası alırsın.

## `str(object, encoding='utf-8', errors='strict')`
Karakter dizisilerini (*stringleri*) ifade eder. Birçok data type'ı string olarak ifade etmemizi sağlar. Örnek:
```py
int_type = 10
float_type = 10.15
complex_type = 15 + 2j

print(str(int_type), str(float_type), str(complex_type), sep="\n")
``` 
**Output:**
```
10
10.15
(15+2j)
```
 `str(object, encoding='utf-8', errors='strict')` syntax'ına sahiptir.
 - `object`,  karakter dizisini ifade eder.
 - `encoding`, encoding değerini ifade eder. Bilgisayar, karakterleri olduğu gibi anlamaz. Bilgisayar elektrik sinyallerini anlar. *ASCII* ya da *UNICODE* gibi kodlama sistemleri, harf, sayı, sembol gibi karakterlerin bilgisayarın anlayacağı karşılığa çevrilip depolandığı sistemlerdir. Bu çevirim bazen binary, bazen decimal, bazen de hexadecimal olabilir. Örneğin sizin `A` olarak bildiğiniz şeyin ASCII'deki decimal karşılığı `65`'dir. Bilgisayar bu decimal karşılığı değerlendirir. Kodlama sistemleri hakkında daha fazla bilgi için [**tıklayınız**](asd).
 - `errors`, kod çözme başarısız olduğunda verilen yanıttır. Default değeri `strict`'dir. Bu parametre 6 değer alabilir:
	 - `strict`, herhangi bir encoding hatasıyla karşılaşınca bir `UnicodeDecodeError` hata mesajı döndüren default değerdir.
	 - `ignore`, herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakteri yok sayar. Örnek: `şelam -> elam` 
	 - `replace`, herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakterin yerine bir `?` koyar.
	 - `xmlcharrefreplace`,  herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakterin yerine XML karakter referansını ekler.
		 - **XML**, interneti kullanarak veri alışverişi yapan sistemler ve platformlar arasındaki veri iletişimini standart hale getirmek için tasarlanan bir işaretleme dilidir.
	- `backslashreplace`, herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakterin yerine `\uNNNN` kaçış dizisi ekler.
	- `namereplace`, herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakterin yerine `\N{...}` kaçış dizisi ekler.

```py
print("bu Türkçe bir cümledir.".encode("ascii", errors="strict")) # Output: UnicodeEncodeError
print("bu Türkçe bir cümledir.".encode("ascii", errors="ignore"))
print("bu Türkçe bir cümledir.".encode("ascii", errors="replace"))
print("bu Türkçe bir cümledir.".encode("ascii", errors="xmlcharrefreplace"))
print("bu Türkçe bir cümledir.".encode("ascii", errors="backslashreplace"))
print("bu Türkçe bir cümledir.".encode("ascii", errors="namereplace"))
```
**Output:**
```
b'bu Trke bir cmledir.'
b'bu T?rk?e bir c?mledir.'
b'bu T&#252;rk&#231;e bir c&#252;mledir.'
b'bu T\\xfcrk\\xe7e bir c\\xfcmledir.'
b'bu T\\N{LATIN SMALL LETTER U WITH DIAERESIS}rk\\N{LATIN SMALL LETTER C WITH CEDILLA}e bir c\\N{LATIN SMALL LETTER U WITH DIAERESIS}mledir.'
```

# `eval` Fonksiyonu
`eval(expression, globals=None, locals=None)` syntax'ına sahiptir. Kendisine verilen karakter dizilerini yorumlar ve çalıştırır. Yani `eval("print('selam')")` şeklinde bir komut tanımlarsanız, `eval()` bunu önce yorumlar, sonra yorumundan çıkardığı `print('selam')` anlamsal kodu çalıştırır. `eval()` herhangi bir değişken tanımlama işlemi, yani `eval("a=5")` tarzı işlemleri yapamaz. `eval()`'in bu özelliğini kullanırken dikkat edilmelidir çünkü bu fonksiyon kötü amaçlarla da kullanılabilir. Örneğin sistem dosyalarını silecek bir kodu `eval()` fonksiyonuna yazabilirsiniz. Bunu önlemek için birçok kontrol mekanizması eklemekten çekinmeyin. `eval()` fonksiyonu yavaş çalışan bir fonksiyondur. Bu yüzden en son tercih edilir. Örnek `eval()` kodu:
```py
eval("print('selam')")
print("""
İşlemler:
+ toplama
- çıkarma
* çarpma
/ bölme
  
Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23*46 yazdıktan sonra
ENTER tuşuna basın.)
""")
hesap = eval(input("İşleminiz: "))
print(hesap)
```

# `exec` Fonksiyonu
`eval()` fonksiyonunun özellikleri ve riskleri `exec()` için de geçerlidir. `eval()`'den tek farkı, daha gelişmiş komutları da çalıştırabiliyor. Örneğin `eval("a=5")` gibi bir şey yapamazken, `exec("a=5")` yapabiliyoruz.

# `format` methodu
Karakter dizelerini manipüle etmemizi sağlar. Örnekler:

Süslü parantezlerin içine formatta tanımlanmış değerler gelir.
```py
print("{}  {}  {}" .format(1 , 2 , 3))
# Output: 1 2 3
```
Matematiksel işlemler yapılabilir.
```py
a = 3
b = 5
print("{} + {} işleminin cevabı {}'dir." .format(a , b , a + b))
# Output: 3 + 5 işleminin cevabı 8'dir.
```
Süslü parantezler içine hangi format değerinin geleceği belirlenebilir.
```py
print("{1}  {0}  {2}" .format("A" , "B" , "C"))
# Output: B A C
```
Floating point sayıların bir kısmını almana olanak tanır.
```py
print("{:.2f}  {:.3f}  {:.4f}" .format(3.14631648 , 5.324458365 , 7.324327784))
# Output: 3.15 5.325 7.3243
```
**Not:** `format` methodunun diğer özelliklerine ulaşmak için [**tıklayınız**](https://pyformat.info/).
