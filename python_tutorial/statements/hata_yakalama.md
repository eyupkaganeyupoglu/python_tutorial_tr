# Hata Yakalama Nedir?
Python, herhangi bir hata ile karşılaşınca default hata mesajları gösterir. **Hata yakalama işlemleri**, bu hata mesajları üzerinde işlemler yapmamızı veya hata ile karşılaşınca Python'un nasıl davranacağını belirlememizi sağlar.

## Programcı Hataları (Error)
Yazılan kod, dilin söz dizilimine (syntax'ına) uymaması durumunda karşılaştığımız `SyntaxError` buna örnek verilebilir. Bir programın, programlama dilinin syntax'ına uymaması durumunda oluşan hatalara **Syntax Error** ya da **Parsing Error** denir.

## Program Kusurları (Bug)
Eksik yazılan programlar, istenilenin dışında çalışır ve istenilen outputları vermez. Bu eksiklikle sonucu oluşan hatalara **bug** denir. Bug'lar bazen güvenlik açıkları oluşturabilir (örneğin `eval()` fonksiyonu). Bu oluşan güvenlik açıklarına **security bug** veya **security flaw** denir.

## İstisnalar (Exception)
Syntax hatası olmayan bir programda, runtime (çalıştığı süre) sırasında oluşabilecek hatalara **exceptions** ya da **logical errors** denir. Build-in (gömülü) exception'lar aşağıda gösterilmiştir:
| Exception | Hatanın Nedeni |
|-----------|----------------|
| `AssertionError` | Bir `assert` statement başarısız olduğunda yükseltilen hata mesajıdır. |
| `AttributeError` | Attribute assignment ya da reference fails'de yükseltilen hata mesajıdır. |
| `EOFError` | `input()` fonksiyonu, end-of-file şartına ulaştığında yükseltilen hata mesajıdır. |
| `FloatingPointError` | Bir floating point işlemi başarısız olduğunda yükseltilen hata mesajıdır. |
| `GeneratorExit` | Bir generator'ın `close()` methodu çağırıldığında yükseltilen hata mesajıdır. generator'un ne olduğunu öğrenmek için [tıklayınız](asd). |
| `ImportError` | Imported module bulunamadığında (not found) yükseltilen hata mesajıdır. |
| `IndexError` | Bir sequence'ın index'i out of range olduğunda yükseltilen hata mesajıdır. |
| `KeyError` | Bir dictionary'de `key` bulunamadığında (not found) yükseltilen hata mesajıdır. |
| `KeyboardInterrupt` | Kullanıcı interrupt key'e (`Ctrl+C` ya da `Delete`) bastığında yükseltilen hata mesajıdır. |
| `MemoryError` | Bir işlem sırasında out of memory olduğunda yükseltilen hata mesajıdır. Out of memory, diyelim ki öyle bir program yazdınız ki, o program bütün RAM'inizi kullanıyor ve RAM'inizde yer kalmadı. RAM'inizde yer kalmamasına rağmen RAM kullanmaya çalışırsanız bu hata yükseltilen. |
| `NameError` | Bir variable, global veya local scope'da bulunamazsa (not found) yükseltilen hata mesajıdır. |
| `NotImplementedError` | [Abstract method](asd) tarafından yükseltilen hata mesajıdır. |
| `OSError` | Sistem işlemleri, sistemle ilgili hataya neden olduğunda yükseltilen hata mesajıdır. |
| `OverflowError` | Bir aritmetik işlemin sonucu temsil edilemeyecek kadar büyük olduğunda yükseltilen hata mesajıdır. |
| `ReferenceError` | Bir [garbage collection](https://www.tutorialspoint.com/How-does-garbage-collection-work-in-Python#:~:text=The%20process%20by%20which%20Python,object%27s%20reference%20count%20reaches%20zero.) referansına erişmek için zayıf bir proxy referansı kullanıldığında yükseltilen hata mesajıdır. |
| `RuntimeError` | Bir error, herhangi bir kategoriye girmediğinde yükseltilen hata mesajıdır. |
| `StopIteration` | `next()` fonksiyonu tarafından döndürülecek başka bir öğe kalmadığında yükseltilen hata mesajıdır. |
| `SyntaxError` | Python'un syntax'ına uymayan bir kodla karşılaşıldığında yükseltilen hata mesajıdır. |
| `IndentationError` | Indentation'ların hatalı kullanılması sonucu yükseltilen hata mesajıdır. |
| `TabError` | Indentation'lar birbiriyle tutarsız olduğunda (örneğin bazıları 2 spaces, bazıları 4 spaces uzunluğunda olduğunda) yükseltilen hata mesajıdır. |
| `SystemError` | [Internal error](https://www.google.com/search?q=what%20is%20internal%20error&client=opera-gx&hs=O1t&sxsrf=ALeKk003LeQ3bOnBhmUKaD-7ImUm4u-0FA:1621149477103&ei=JcegYKPkBcPgkgWt_IOoDw&oq=what%20is%20internal%20error&gs_lcp=Cgdnd3Mtd2l6EAMyBggjECcQEzIECCMQJzIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIECAAQHjIECAAQHjoHCCMQsAMQJzoHCAAQRxCwAzoHCCMQsAIQJzoECAAQEzoICAAQDRAeEBNQvl9Yh2FgvmJoAnACeACAAbcBiAGfA5IBAzAuM5gBAKABAaoBB2d3cy13aXrIAQnAAQE&sclient=gws-wiz&ved=0ahUKEwjjite11M3wAhVDsKQKHS3-APUQ4dUDCAw&uact=5) tespit edildiğinde yükseltilen hata mesajıdır. |
| `SystemExit` | `sys.exit()` fonksiyonunun yükselttiği hata mesajıdır. |
| `TypeError` | Bir fonksiyon veya işlem, uygunsuz type'da bir objeye uygulandığında yükseltilen hata mesajıdır. |
| `UnboundLocalError` | Global variable üzerinde local scope'da işlem yapmaya çalıştığınızda yükseltilen hata mesajıdır. Ayrıntılı bilgi için [tıklayınız](asd). |
| `UnicodeError` | UNICODE'da `\U` ya da `\u` kullanımında, kod çözücü kodu çözemediğinde oluşan encoding ya da decoding hatasından dolayı yükseltilen hata mesajıdır. |
| `UnicodeEncodeError` | Stringlerdeki `encode()` methodu, kodu çözemediğinde yükseltilen hata mesajıdır. |
| `UnicodeDecodeError` | Stringlerdeki `decode()` methodu, kodu çözemediğinde yükseltilen hata mesajıdır. |
| `UnicodeTranslateError` | `UnicodeError` ile ilgili bir hata mesajıdır. `UnicodeError`'ün subclass'ıdır. |
| `ValueError` | Bir fonksiyon, doğru type'da ancak uygun olmayan value'de bir arguman aldığında yükseltilen hata mesajıdır. |
| `ZeroDivisionError` | Bir division ya da modulo işleminde, ikinci operand'ın sıfır olmasından dolayı yükseltilen hata mesajıdır. |
**Not:** Daha Fazla bilgi için [tıklayınız](https://docs.python.org/3/library/exceptions.html).

# Hata Yakalama Kodları
Hata yakalama kodlar, bir kod parçasında oluşabilecek hataları yakalayıp, Python'un nasıl davranacağını belirlememizi sağlar.

## `try` - `except <ErrorCode>` Yapısı
`try` ile `except` arasındaki kodda oluşacak hataları yakalayıp, `except` bloğunda Python'un davranışını belirlediğimiz yapıdır. Syntax:
```py
try:
	# Kodlar.
except <ErrorCode>:
	# <ErrorCode>'da belirtilen hata ortaya çıkarsa
	# yapılmasını işlediğimiz işlemler.
```
**Not:** `<ErrorCode>` kısmını boş bırakırsanız, `try` - `except` arasındaki kodlarda oluşabilecek herhangi bir hatada `except` çalışır.

**`try` - `except` ile ilgili örnek program:**
```py
ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
	sayı1 = int(ilk_sayı)
	sayı2 = int(ikinci_sayı)
	print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
	
except ValueError:
	print("Lütfen sadece sayı girin!")
	
except ZeroDivisionError:
	print("Bir sayıyı 0'a bölemezsiniz!")
```
**Outputs:**
```
ilk sayı: a
ikinci sayı: 1
Lütfen sadece sayı girin!
```
```
ilk sayı: 1
ikinci sayı: 0
Bir sayıyı 0'a bölemezsiniz!
```
**Not:** `try`'dan sonra birden fazla `except` ekleyebilirsiniz. Bu özellik, birden fazla spesifik durumu ele alıp, her durum için farklı bir işlem yapılmasını istediğinizde çok yararlı olan bir özelliktir. Birden fazla spesifik durum için aynı işlemi yapmak istediğinizde, bu hata mesajlarını gruplayarak tek bir `except`'e ekleyebilirsiniz. Örnek:
```py
ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
	sayı1 = int(ilk_sayı)
	sayı2 = int(ikinci_sayı)
	print(sayı1, "/", sayı2, "=", sayı1 / sayı2)

except (ValueError, ZeroDivisionError):
	print("Bir hata oluştu!")
```
**Outputs:**
```
ilk sayı: a
ikinci sayı: 1
Bir hata oluştu!
```
```
ilk sayı: 1
ikinci sayı: 0
Bir hata oluştu!
```

## `try` - `except <ErrorCode>` - `as <identifier>` Yapısı
`as` deyimi, hata mesajına ulaşmamızı sağlar. Hata mesajını `<identifier>`'e atar. Örnek:
```py
ilk_sayı = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
	sayı1 = int(ilk_sayı)
	sayı2 = int(ikinci_sayı)
	print(sayı1, "/", sayı2, "=", sayı1 / sayı2)

except (ValueError, ZeroDivisionError) as hata:
	print("Bir hata oluştu!")
	print("orijinal hata mesajı: ", hata)
```
**Outputs:**
```
ilk sayı: a
ikinci sayı: 1
Bir hata oluştu!
orijinal hata mesajı:  invalid literal for int() with base 10: 'a'
```
```
ilk sayı: 1
ikinci sayı: 0
Bir hata oluştu!
orijinal hata mesajı:  division by zero
```

## `try` - `except <ErrorCode>` - `else` Yapısı
`except` çalışmazsa `else` çalışır. Bu yapının, programda bug'lar yaratma olasılığı olduğu için tercih edilmez.
```py
try:
	bölünen = int(input("bölünecek sayı: "))
	bölen = int(input("bölen sayı: "))
except  ValueError:
	print("Lütfen sadece sayı girin!")
else:
	try:
		print(bölünen/bölen)
	except  ZeroDivisionError:
		print("Bir sayıyı 0'a bölemezsiniz!")
```
**Outputs:**
```
bölünecek sayı: a
Lütfen sadece sayı girin!
```
```
bölünecek sayı: 1
bölen sayı: a
Lütfen sadece sayı girin!
```
```
bölünecek sayı: 1
bölen sayı: 0
Bir sayıyı 0'a bölemezsiniz!
```

## `try` - `except <ErrorCode>` - `finally` Yapısı
`finally`, kullanıldığı `try` - `except` yapısı çalışsa da çalışmasa da çalışan bir statement'dir. Syntax:
```
try:
	# Kodlar.
except <ErrorCode>:
	# Hata alınınca yapılacak işlemler.
finally:
	# Hata olsa da olmasa da yapılacak işlemler.
```
`finally` statement, dosya işlemlerinde kullanışlı bir deyimdir. Çünkü dosya işlemlerinde, `open()` fonksiyonu ile açılan bir bir dosyayı sonra kapatmadığınızda **fatal error** dediğimiz durum oluşur. Bu ciddi hatadan kaçınmak için dosya işlemlerini `try` - `except` yapısı içerisinde yaptıktan sonra en sona eklediğimiz `finally` statement'e eklediğimiz `close()` methodu sayesinde, `open()` ile açılan dosya hata verse de vermese de son işlem olarak kapatılır. Örnek kod yapısı:
```py
try:
	dosya = open("dosyaadı", "r")
		# Dosya işlemleri.
except <ErrorCode>:
	# Hata alınınca yapılacak işlemler.
finally:
	dosya.close()
```

## `raise` Keyword'ü
`raise` deyimi *yükseltmek* anlamına gelir. Python'da herhangi bir hataya sebep olacak bir işlemde, hata mesajları *yükseltilir*. Yani bu keyword, düzenleyebildiğimiz hata mesajları *yükseltmemizi* sağlar. Hata mesajı Python'da kayıtlıysa bu deyimi kullanabilirsiniz. Yani bu keyword, `FalanFilanError` tarzı Python'da olmayan hata mesajları üzerinde kullanılamaz. Örnek:
```py
tr_karakter = "şçğüöıİ"
parola = input("Parolanız: ")

for i in parola:
	if i in tr_karakter:
		raise TypeError("Parolada Türkçe karakter kullanılamaz!")
	else:
		pass
```
**Output:**
```
Parolanız: asdç
Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 7, in <module>
    raise TypeError("Parolada Türkçe karakter kullanılamaz!")
TypeError: Parolada Türkçe karakter kullanılamaz!
```
`raise` keyword'ünü `if` statement ile kullanmak zorunda değilsiniz. `raise` keyword'ü, çalışmak için herhangi bir koşula bağlı değildir. Çalışması için Python'un `raise` keyword'ünü okuması yeterlidir. Örnek:
```py
print("selam")
raise  TypeError("helllooo")
print("selam")
```
**Output:**
```
selam
Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 2, in <module>
    raise TypeError("helllooo")
TypeError: helllooo
```
`raise` deyimini aşağıdaki şekilde de kullanabilirsiniz:
```py
try:
	bölünen = int(input("bölünecek sayı: "))
	bölen = int(input("bölen sayı: "))
	print(bölünen/bölen)
except ZeroDivisionError:
	print("bir sayıyı 0'a bölemezsiniz")
	raise
```
**Output:**
```
bölünecek sayı: 1
bölen sayı: 0
bir sayıyı 0'a bölemezsiniz
Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 4, in <module>
    print(bölünen/bölen)
ZeroDivisionError: division by zero
```
Yukarıdaki kodda hem `print("bir sayıyı 0'a bölemezsiniz")` kodu çalıştı, hem de default `ZeroDivisionError` hata mesajı yazdırıldı. `try` - `except <ErrorCode>` - `as <identifier>` yapısı buna benzer olsa da aynı şey değildir. Örnek:
```py
try:
	bölünen = int(input("bölünecek sayı: "))
	bölen = int(input("bölen sayı: "))
	print(bölünen/bölen)
except ZeroDivisionError as hata:
	print("bir sayıyı 0'a bölemezsiniz", hata, sep="\n")
```
**Output:**
```
bölünecek sayı: 1
bölen sayı: 0 
bir sayıyı 0'a bölemezsiniz
division by zero
```
gördüğünüz gibi `try` - `except <ErrorCode>` - `as <identifier>` yapısında sadece `ZeroDivisionError` hatasının hata mesajı yazdırıldı. Hatanın hangi line'da olduğu, hangi kodda oluştuğu vs. gibi bilgiler eksik.

`raise` keyword'ünü `from` keyword'ü ile birlikte kullanınca, Python'un verdiği tepki değişir. Örnek:
```py
try:
    print(i)
except NameError as NE:
    raise ValueError("From için")
```
**Output:**
```
Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 2, in <module>
    print(i)
NameError: name 'i' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 4, in <module>
    raise ValueError("From için")
ValueError: From için
```
Yukarıdaki output'da `During handling of the above exception, another exception occurred:`, yani `Yukarıdaki exception'ın işlenmesi sırasında başka bir exception oluştu:` yazmaktadır. Bunun anlamı: "`NameError` oluştuğu sırada, başka bir exception olan (another exception) `ValueError` oluştu." şeklindedir.
```py
try:
    print(i)
except NameError as NE:
    raise ValueError("From için") from NE
```
**Output:**
```
Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 2, in <module>
    print(i)
NameError: name 'i' is not defined

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 4, in <module>
    raise ValueError("From için") from NE
ValueError: From için
```
Yukarıdaki output'da `The above exception was the direct cause of the following exception:`, yani `Yukarıdaki exception, aşağıdaki exception'ın doğrudan nedeniydi:` yazmaktadır. Bunun anlamı: "`ValueError` oluşma nedeni `NameError`'dür." şeklindedir.

## `assert <condition>, <error message>` Statement
`assert` deyimi `raise` deyiminin aksine, özelleştirilebilir Hata kodları yaratmamıza olanak tanır. `assert <condition>,<error message>` syntax'ına sahiptir. Buradaki `<condition>`, logic bir ifadedir ve `False` sonucuna eşit olursa `assert` çalışır. `assert` çalıştığında `AssertionError` hata koduyla birlikte `<error message>`'da belirtilen hata mesajını yükseltir. Örneğin, aşağıdaki iki kod aynı işleve sahiptir:
```py
giriş = input("Merhaba! Adın ne? ")
if  len(giriş) == 0:
	raise AssertionError("İsim bölümü boş.")
print("Hoşgeldiniz.")
```
**Output:**
```
Merhaba! Adın ne? 
Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 3, in <module>
    raise AssertionError("İsim bölümü boş.")
AssertionError: İsim bölümü boş.
```
```py
giriş = input("Merhaba! Adın ne? ")
assert (not (len(giriş) == 0)), ("İsim bölümü boş.")
print("Hoşgeldiniz.")
```
**Output:**
```
Merhaba! Adın ne? 
Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 2, in <module>
    assert not (len(giriş) == 0), ("İsim bölümü boş.")
AssertionError: İsim bölümü boş.
```
**Not:** Bir Python kodunu terminalden çalıştırırken `python -O dosya_adı` komutuyla çalıştırırsanız, Python dosyası içindeki bütün `assert` statement'lerini görmezden gelir. Bunu sağlayan şey optimize anlamına gelen `-O` parametresidir. Eğer `-O` olmadan `python dosya_adı` koduyla çalıştırırsanız, Python dosyası içindeki `assert` statement'lerini görmezden gelmez. Kanıtı:
<img src="https://i.ibb.co/pZqwRNF/Ekran-Al-nt-s.png" alt="Ekran-Al-nt-s" border="0">

