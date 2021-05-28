# Encoding
Elektrik sinyallerinin (0 ve +5 volt) hangi sayıya, hangi sayının da hangi karaktere karşılık geleceğini belirleyebilirsiniz. Bunun tam tersi olan karakterden sayılara, sayılardan da elektrik sinyallerine dönüşümü de belirleyebilirsiniz. Bu dönüştürme işlemlerine **Karakter kodlama (character encoding)** denir. Her encoding sistem aynı olmayacağı için global encoding sistemlerinin kullanımı yaygındır.

## ASCII
**American Standard Code for Information Interchange (Türkçesi: Bilgi Alışverişi için Standart Amerikan Kodu)** kısaca **ASCII** **7 bit**'lik bir sistemdir. Amerika standartlarına göre yapıldığı için Türkçe karakter sıkıntısı yaşatan bir sistemdir. ASCII tablosuna [buradan](http://www.asciitable.com/) ulaşabilirsiniz veya kendiniz oluşturabilirsiniz:
```py
for i in  range(128):
	if i % 4 == 0:
		print("\n")
	print("{:<3}{:>8}\t".format(i, repr(chr(i))), sep="", end="")
```

### Genişletilmiş ASCII
*Normal ASCII*, 8. bit'i **hata kontrol sistemi** için kullandığı için 128 tane karakter kullanabiliyordu. *Genişletilmiş ASCII*'de 8. bit'in hata kontrol sistemi için kullanılmasında vazgeçildi ve kullanılabilen karakter sayısı 256'ya çıktı. Farklı ülkelere gönderilmek için geliştirilen birbirinden farklı bu sayfalara genel olarak **kod sayfası** adı verildi. Microsoft şirketinin Türkiye’ye gönderdiği bilgisayarlarda tanımlı **cp857** adlı kod sayfasında 128 ile 256 aralığında Türkçe karakterlere de yer verilmişti. 8. bit'in kullanılmaya başlanmasıyla dünyadaki bütün dillerin kod sayfası oluşturulabiliyor. Genişletilmiş ASCII karakterinin kapladığı yer: `1 karakter == 1 byte == 8 bit`

## UNICODE
ASCII'nin sıkıntısı, farklı kod sayfası kullanan bilgisayar arasında, birinden birine gönderilen mailde karakterlerin bozuk veya farklı çıkmasıydı. Bunu önlemek için her bir karakter için benzersiz bir kimlik çıkarmaktı. Bunun için **UNICODE** standartı yapıldı. UNICODE sistemi ASCII'yi tamamen görmezden gelmez. Yani ASCII ile kodlanmış karakterler UNICODE'da da vardır. Bu sebeple ASCII, UNICODE'un bir alt kümesidir denebilir. Bu sayede ASCII ile çalışan sistemlerin tamamı UNICODE ile de çalışır. UNICODE ilk ortaya çıktığında 16 bit'lik bir sistemdi ve `2**16 = 65536` karakterin kodlanmasına izin veriyordu. Bugün ise bunun bir sınırı yok çünkü 'X bitlik sistem' kavramı artık UNICODE için geçerli değil. Bu sayede ASCII'ye kıyasla UNICODE, bir milyondan fazla karakter kodlamasına izin verir. Bunu yapabilmesini sağlayan şey ise, ASCII sistemi gibi karakteri doğrudan doğruya kodlamak yerine o karakteri tanımlamaktır. Yani UNICODE'da her kararkter benzersiz bir **kod konumuna (code point)** karşılık gelir. UNICODE standartına ulaşmak için [tıklayınız](http://www.unicode.org/versions/Unicode6.2.0/UnicodeStandard-6.2.pdf). UNICODE tablosuna ulaşmak için [tıklayınız](https://unicode-table.com/tr/).

### UTF-8 Kod Çözücüsü
UNICODE karakterleri kendi kendine kodlamaz. Bu sistemde tanımlanan karakterleri kodlama işi kod çözücülerin görevidir. UNICODE sistemi içinde **UTF-1**, **UTF-7**, **UTF-8**, **UTF-16** ve **UTF-32** adlı kod çözücüler bulunur. **UTF-8**, UNICODE sistemi içindeki en yaygın, en bilinen ve en kullanışlı kod çözücüdür. UTF-8 adlı kod çözücünün kodlayabildiği karakterlerin listesine ulaşmak için [tıklayınız](http://www.fileformat.info/info/charset/UTF-8/list.htm). Gelmiş geçmiş bütün sistemleri kodlayabilmek için 4 byte'lık sistem (`2**(8*4) = 2**32 = 4,294,967,296`) yeterli olacaktır.

1 byte'lık sistem ile temsil edilebilecek bir karakterin 4 byte'lık sistemle tanımlamaya çalıştığımızda boşu boşuna 4 kat fazla yer kaplamış olursunuz. Bu sorunun çözümü elbette sabit boyutlu karakter kodlama biçimleri yerine değişken boyutlu karakter kodlama biçimleri kullanmaktır. UTF-8 adlı kod çözücü, karakterleri değişken sayıda baytlar halinde kodlayabilir. UTF-8, UNICODE sistemi içinde tanımlanmış karakterleri kodlayabilmek için 1 ile 4 bayt arası değerleri kullanır. Böylece de bu kod çözücü UNICODE sistemi içinde tanımlanmış bütün karakterleri temsil edebilir.
```py
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
for s in harfler:
	print("{:<5}{:<15}{:<15}".format(s, str(s.encode("utf-8")), len(s.encode("utf-8"))))
```
**Not:** Buradaki `s.encode("utf-8")` komutları, `s` stringini `encode()` methodu ile `utf-8`'e göre `bytes` data type'ına çeviriyor. `bytes` data type'ı, `string`'ler gibi `format()` methoduna sahip olmadığı için `s.encode("utf-8")` kodunu `str()` fonksiyonu ile string'e çevirip kullanmalıyız. Bunu yapmak istemeyenler için alternatif:
```py
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
for s in harfler:
	print("{:<5}{!s:<15}{:<15}".format(s, s.encode("utf-8"), len(s.encode("utf-8"))))
```
**Output:**
```
a    b'a'           1
b    b'b'           1
c    b'c'           1
ç    b'\xc3\xa7'    2
d    b'd'           1
e    b'e'           1
f    b'f'           1
g    b'g'           1
ğ    b'\xc4\x9f'    2
h    b'h'           1
ı    b'\xc4\xb1'    2
i    b'i'           1
j    b'j'           1
k    b'k'           1
l    b'l'           1
m    b'm'           1
n    b'n'           1
o    b'o'           1
ö    b'\xc3\xb6'    2
p    b'p'           1
r    b'r'           1
s    b's'           1
ş    b'\xc5\x9f'    2
t    b't'           1
u    b'u'           1
ü    b'\xc3\xbc'    2
v    b'v'           1
y    b'y'           1
z    b'z'           1
```
`a` harfinin ASCII'de karşılığı `97`'dir. UNICODE, ASCII ile uyumlu olduğu için ASCII karakterlerinin ASCII'deki decimal karşılıklarını kullanır. Kendisine girilen karakterlerin UNICODE'daki integer karşılıklarını veren `ord()` fonksiyonu kullanarak bunu görebilirsiniz.
```py
print(ord("a")) # Output: 97
```

# Encoding Hataları
Bir Python programı, kod sayfalarının farklı olmasın durumunda, eksik karakterin yerine başka bir karakter koyamayacağı için (mesela `ç` yerine `c` koymaz çünkü her karakter spesifiktir) hata verir. Bunu önlemek için `encode()` methodunun `errors` parametresinden yararlanılabilir. `errors` parametresinin aldığı değerlere ulaşmak için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/kullanicidan_girdi_almak/tip_donusumleri.md#strobject-encodingutf-8-errorsstrict).

# Dosyalar ve Karakter Kodlama
`open("dosya_adı", "dosya_açma_kipi", encoding="kod_çözücü_adı")` fonksiyonu 3 parametreye sahiptir. Bunlar:
- **encoding:** `encoding` parametresi, bir dosyanın hangi kod çözücü ile açılacağını belirtmemize olanak tanır. Python’da dosyalar default olarak, `locale` adlı bir modülün `getpreferredencoding()` adlı fonksiyonunu kullanarak öğrenebileceğiniz kod çözücü ile açılır. GNU/Linux, **UTF-8** ile çalışır ama Windows **cp1254** ile çalışır. Bu yüzden Windows cihazlarda encoding değerini UTF-8 olarak belirtmek önemlidir. Diğer bir önemli nokta da, cp1254 ile kodlanmış bir dosyayı UTF-8 ile açmaya çalışırsanız hata alırsınız çünkü sayılar aynı karakterlerle eşleştirilememektedir.
- **errors:** cp1254 ile kodlanmış bir dosyayı UTF-8 ile açmaya çalışırsanız program doğru çalışmaz ve hata verir. Bu gibi durumlarda programınızın verdiği reaksiyon türünü değiştirebilirsiniz. Bu reaksiyon türlerine [şuradan](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/kullanicidan_girdi_almak/tip_donusumleri.md#strobject-encodingutf-8-errorsstrict) ulaşabilirsiniz. Bu reaksiyon türlerinden olan `xmlcharrefreplace` türünün oluşturduğu değeri, open() fonksiyonunun kullanmasına izin verilmez. `replace` değeri ise kodlanamayan karakterlerin yerine `\ufffd` karakterini yerleştirecektir. Bu karakter işlev bakımından, `encode()` metodunu anlatırken gördüğümüz `?` işaretine benzer. Bu karaktere teknik olarak **UNICODE Değiştirme Karakteri (UNICODE Replacement Character)** adı verilir. Bazı yerlerde bu karakteri elmas şeklinde siyah bir küp içine yerleştirilmiş soru işareti şeklinde görebilirsiniz.

# Karakter Kodlama İle İlgili Fonksiyonlar

## `repr("string")` Fonksiyonu
Python programlama dilinde nesneler, **Python’ın göreceği** ve **kullanıcının göreceği** olmak üzere 2 farklı şekilde ifade edilir. Örneğin kaçış dizilerini **kullanıcının göreceği** formatta göremezken, **Python’ın göreceği** formatta görebilirsiniz.
```py
print("karakter dizisi \n")
print(repr("karakter dizisi \n"))
```
**Output:**
```
karakter dizisi
'karakter dizisi \n'
```

## `ascii("string")` Fonksiyonu
`repr()` fonskiyonuna benzerdir ama ASCII tablosunda yer almayan karakterlere karşı tutumları yönünden birbirlerinden ayrılır. `ascii()` fonksiyonu, ASCII tablosunda yer almayan karakterlerin **UNICODE kod konumlarını (code points)** döndürür.
```py
print(repr("İ")) # Output: 'i'
print(ascii("İ")) # Output: '\\u0130'
```
`ascii()` fonksiyonu ile string veri tipinin `encode()` methodu aynı sonuçları verir.
```py
print(ascii("€"))
print("€".encode("unicode_escape"))
```
**Output:**
```
'\u20ac'
b'\\u20ac'
```

## `ord("string")` Fonksiyonu
`"string"` parametresine girilen değerin UNICODE tablosundaki integer karşılığını verir.
```py
print(ord("€")) # Output: 8364
```

## `chr(int)` Fonksiyonu
`int` parametresine girilen integer değerin UNICODE tablosundaki karakter karşılığını verir.
```py
print(chr(8364)) # Output: €
```
