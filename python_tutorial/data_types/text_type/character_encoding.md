# İçindekiler

- [Encoding](#1)
    - [ASCII](#1.1)
        - [Genişletilmiş ASCII](#1.1.1)
    - [UNICODE](#1.2)
        - [UTF-8 Kod Çözücüsü](#1.2.1)
- [Encoding Hataları](#2)
- [Dosyalar ve Karakter Kodlama](#3)
- [Karakter Kodlama İle İlgili Fonksiyonlar](#4)
    - [`repr(object)` Fonksiyonu](#4.1)
    - [`ascii(object)` Fonksiyonu](#4.2)
    - [`ord(c)` Fonksiyonu](#4.3)
    - [`chr(i)` Fonksiyonu](#4.4)

<h1 id="1">Encoding</h1>

Bilgisayar, insanlar gibi kelimelerden anlamaz. Bilgisayar, elektrik sinyallerinden anlar. Elektrik sinyallerinin (0 ve +5 volt) hangi sayıya, hangi sayının da hangi karaktere karşılık geleceğini belirleyebilirsiniz. Bunun tam tersi olan karakterden sayılara, sayılardan da elektrik sinyallerine dönüşümü de belirleyebilirsiniz. Bu dönüştürme işlemlerine **Karakter kodlama (character encoding)** denir. Her encoding sistem aynı olmayacağı için global encoding sistemlerinin kullanımı yaygındır.

<h2 id="1.1">ASCII</h2>

**American Standard Code for Information Interchange (Türkçesi: Bilgi Alışverişi için Standart Amerikan Kodu)** kısaca **ASCII** **7 bit**'lik bir sistemdir. Amerika standartlarına göre yapıldığı için Türkçe karakter sıkıntısı yaşatan bir sistemdir. ASCII tablosuna [buradan](http://www.asciitable.com/) ulaşabilirsiniz veya kendiniz oluşturabilirsiniz:
```py
for i in  range(128):
	if i % 4 == 0:
		print("\n")
	print("{:<3}{:>8}\t".format(i, repr(chr(i))), sep="", end="")
```
Bu kod ASCII tablosu gibi dizayn edilmiş bir output verir.

<h3 id="1.1.1">Genişletilmiş ASCII</h3>

Normal ASCII, 8. bit'i **hata kontrol sistemi** için kullandığı için 128 tane karakter kodlayabiliyordu. Genişletilmiş ASCII'de 8. bit'in hata kontrol sistemi için kullanılmasında vazgeçildi ve kodlanabilen karakter sayısı 256'ya çıktı. Farklı ülkelere gönderilmek için geliştirilen birbirinden farklı bu sayfalara genel olarak **kod sayfası** adı verildi. Microsoft şirketinin Türkiye'ye gönderdiği bilgisayarlarda tanımlı **cp857** adlı kod sayfasında 128 ile 256 aralığında Türkçe karakterlere de yer verilmişti. 8. bit'in kullanılmaya başlanmasıyla dünyadaki bütün dillerin kod sayfası oluşturulabiliyor. Genişletilmiş ASCII karakterinin kapladığı yer: `1 karakter == 1 byte == 8 bit`

<h2 id="1.2">UNICODE</h2>

ASCII'nin sıkıntısı, farklı kod sayfası kullanan bilgisayarlar arasında kurulan yazılı iletişimde karakterlerin bozuk veya farklı çıkmasıydı. Bunu önlemek için **UNICODE** standartı yapıldı. UNICODE sistemi ASCII'yi tamamen görmezden gelmez. Yani ASCII ile kodlanmış karakterler UNICODE'da da vardır. Bu sebeple ASCII, UNICODE'un bir alt kümesidir denebilir. Bu sayede ASCII ile çalışan sistemlerin tamamı UNICODE ile de çalışır. UNICODE ilk ortaya çıktığında 16 bit'lik bir sistemdi ve `2**16 = 65536` karakterin kodlanmasına izin veriyordu. Bugün ise bunun bir sınırı yok çünkü 'X bitlik sistem' kavramı artık UNICODE için geçerli değil. Bu sayede ASCII'ye kıyasla UNICODE, bir milyondan fazla karakter kodlamasına izin verir. Bunu yapabilmesini sağlayan şey ise, ASCII sistemi gibi karakteri doğrudan doğruya kodlamak yerine o karakteri tanımlamasıdır. Yani UNICODE'da her kararkter benzersiz bir **kod konumuna (code point)** karşılık gelir. UNICODE standartına ulaşmak için [tıklayınız](http://www.unicode.org/versions/Unicode6.2.0/UnicodeStandard-6.2.pdf). UNICODE tablosuna ulaşmak için [tıklayınız](https://unicode-table.com/tr/).

<h3 id="1.2.1">UTF-8 Kod Çözücüsü</h3>

UNICODE karakterleri kendi kendine kodlanmaz. Bu sistemde tanımlanan karakterleri kodlama işi kod çözücülerin görevidir. UNICODE sistemi içinde **UTF-1**, **UTF-7**, **UTF-8**, **UTF-16** ve **UTF-32** adlı kod çözücüler bulunur. **UTF-8**, UNICODE sistemi içindeki en yaygın, en bilinen ve en kullanışlı kod çözücüdür. UTF-8 adlı kod çözücünün kodlayabildiği karakterlerin listesine ulaşmak için [tıklayınız](http://www.fileformat.info/info/charset/UTF-8/list.htm). Gelmiş geçmiş bütün sistemleri kodlayabilmek için 4 byte'lık sistem (`2**(8*4) = 2**32 = 4,294,967,296`) yeterli olacaktır.

1 byte'lık sistem ile temsil edilebilecek bir karakterin 4 byte'lık sistemle tanımlamaya çalıştığımızda boşu boşuna 4 kat fazla yer kaplamış olursunuz. Bu sorunun çözümü elbette sabit boyutlu karakter kodlama biçimleri yerine değişken boyutlu karakter kodlama biçimleri kullanmaktır. UTF-8 adlı kod çözücü, karakterleri değişken sayıda byte'lar halinde kodlayabilir. UTF-8, UNICODE sistemi içinde tanımlanmış karakterleri kodlayabilmek için 1 ile 4 byte arası değerleri kullanır. Böylece de bu kod çözücü UNICODE sistemi içinde tanımlanmış bütün karakterleri temsil edebilir.
```py
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
for s in harfler:
	print("{:<5}{:<15}{:<15}".format(s, str(s.encode("utf-8")), len(s.encode("utf-8"))))
```
Burada `harfler` variable'ına atanmış string'in her bir karakterinin UNICODE'da kaç byte yer kapladığını döndüren bir kod var. Buradaki `s.encode("utf-8")` komutları, `s` string'ini `encode()` methodu ile `utf-8`'e göre `bytes` data type'ına dönüştürüyor. `bytes` data type'ı, `str`'ler gibi `format()` methoduna sahip olmadığı için `s.encode("utf-8")` kodunu `str()` fonksiyonu ile string'e dönüştürüp kullanmalıyız. Bunu yapmak istemeyenler için alternatif:
```py
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
for s in harfler:
	print("{:<5}{!s:<15}{:<15}".format(s, s.encode("utf-8"), len(s.encode("utf-8"))))
```
`ord()` build-in fonksiyonu kullanarak UNICODE tablosundaki karakterlerin decimal karşılıklarını elde edebilirsiniz. Örnek:
```py
print(ord("a")) # Output: 97
```

<h1 id="2">Encoding Hataları</h1>

Bir Python programı, kod sayfalarının farklı olmasın durumunda eksik karakterin yerine başka bir karakter koyamayacağı için (mesela `ç` yerine `c` koymaz çünkü her karakter spesifiktir) hata yükseltir.

<h1 id="3">Dosyalar ve Karakter Kodlama</h1>

`open()` build-in fonksiyonu dosya işlemlerinde ilgili dosyayı açmak için kullanılan bir fonksiyondur. Bu fonksiyonun konumuzla ilgili `encoding` ve `errors` adında iki parametresi vardır:
- **encoding:** `encoding` parametresi, bir dosyanın hangi kod çözücü ile açılacağını belirtmemize olanak tanır. Python'da dosyalar default olarak, `locale` adlı bir modülün `getpreferredencoding()` adlı fonksiyonunu kullanarak öğrenebileceğiniz kod çözücü ile açılır. GNU/Linux, **UTF-8** ile çalışır ama Windows **cp1254** ile çalışır. Bu yüzden Windows cihazlarda encoding değerini UTF-8 olarak belirtmek önemlidir. Diğer bir önemli nokta da, cp1254 ile kodlanmış bir dosyayı UTF-8 ile açmaya çalışırsanız hata yükseltilir çünkü sayılar aynı karakterlerle eşleştirilememektedir.
- **errors:** cp1254 ile kodlanmış bir dosyayı UTF-8 ile açmaya çalışırsanız program doğru çalışmaz. Bu gibi durumlarda Python'un nasıl davranacağını (daha önce `str()` fonksiyonunda da anlattığım) `errors` parametresine gireceğiniz argüman ile belirleyebilirsiniz. Bu argümanlardan biri olan `xmlcharrefreplace`'in `open()` fonksiyonunda kullanmasına Python tarafından izin verilmez. `replace` argümanı ise kodlanamayan karakterlerin yerine `\ufffd` karakterini yerleştirecektir. Bu karakter işlev bakımından `encode()` metodunu anlatırken anlattığım `?` işaretine benzer. Bu karaktere teknik olarak **UNICODE Değiştirme Karakteri (UNICODE Replacement Character)** adı verilir. Bazı yerlerde bu karakteri `�` şeklinde görebilirsiniz.

<h1 id="4">Karakter Kodlama İle İlgili Fonksiyonlar</h1>

<h2 id="4.1"><code>repr(object)</code> Fonksiyonu</h2>

Python programlama dilinde nesneler, **Python'ın gözünden** ve **kullanıcının gözünden** olmak üzere 2 farklı şekilde ifade edilir. Örneğin kaçış dizilerini kullanıcının gözünden göremezken, Python'ın gözünden görebilirsiniz. `repr` fonksiyonu, karakter dizilerini Python'ın gözünden görmemizi sağlar. Örnek:
```py
print("Karakter\nDizisi")
print(repr("Karakter\nDizisi"))
```
**Output:**
```
Karakter
Dizisi
'Karakter\nDizisi'
```
Gördüğünüz gibi `repr` fonksiyonu, string'leri tek tırnak içinde belirtir ve kaçış dizilerini görmemizi sağlar. Bu işlem yüzünden kaçış dizileri işlevlerini geçekleştiremez. Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#repr).

<h2 id="4.2"><code>ascii(object)</code> Fonksiyonu</h2>

`object` parametresinde girilen objenin yazdırılabilir karşılığını döndürür. ASCII karakterlerin direkt kendisini döndürürken, ASCII olmayan karakterlerin `\x`, `\u` ya da `\U` karşılıklarını, yani **UNICODE kod konumlarını (code points)** döndürür. Ürettiği değer `repr()` fonksiyonuna benzerdir. Örnek:
```py
print(repr("İ")) # Output: 'i'
print(ascii("İ")) # Output: '\\u0130'

print(ascii('şeker')) # Output: '\\u015feker'
print(repr('şeker')) # Output: 'şeker'
```
`ascii()` fonksiyonu ile string veri tipinin `encode()` methodu aynı sonuçları verir.
```py
print(ascii("€")) # Output: '\u20ac'
print("€".encode("unicode_escape")) # Output: b'\\u20ac'
```
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#ascii).

<h2 id="4.3"><code>ord(c)</code> Fonksiyonu</h2>

`c` parametresine girilen değerin UNICODE tablosundaki decimal karşılığını verir.
```py
print(ord("€")) # Output: 8364
```

<h2 id="4.4"><code>chr(i)</code> Fonksiyonu</h2>

`i` parametresine girilen decimal değerin UNICODE karşılığını döndürür. `ord()` fonksiyonunun tam tersi işleve sahiptir. `i` parametresine girilen argüman 0 ile 1,114,111 arasındaysa bu fonksiyon çalışır. `i` parametresine girilen argüman bu değerleri geçerse `ValueError` hatası yükseltilir.
```py
print(chr(8364)) # Output: €
```