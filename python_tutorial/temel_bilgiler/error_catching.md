# İçindekiler

- [Hata Yakalama Nedir?](#1)
    - [Programcı Hataları (Error)](#1.1)
    - [Program Kusurları (Bug)](#1.2)
    - [İstisnalar (Exception)](#1.3)
- [Hata Yakalama Kodları](#2)
    - [`try` - `except (ErrorCode)` Yapısı](#2.1)
    - [`try` - `except (ErrorCode)` - `as (identifier)` Yapısı](#2.2)
    - [`try` - `except (ErrorCode)` - `else` Yapısı](#2.3)
    - [`try` - `except (ErrorCode)` - `finally` Yapısı](#2.4)
    - [`raise (error message)` Statement](#2.5)
    - [`assert (condition), (error message)` Statement](#2.6)

<h1 id="1">Hata Yakalama Nedir?</h1>

Python, herhangi bir hata ile karşılaşınca default hata mesajları gösterir. **Hata yakalama işlemleri**, bu hata mesajları üzerinde işlemler yapmamızı veya hata ile karşılaşınca Python'un nasıl davranacağını belirlememizi sağlar. Hatalar, Errors, Bugs ve Exceptions olarak üçe ayrılır.

<h2 id="1.1">Programcı Hataları (Error)</h2>

Yazılan kod, dilin söz dizilimine (syntax'ına) uymaması durumunda karşılaştığımız `SyntaxError` buna örnek verilebilir. Bir programın, programlama dilinin syntax'ına uymaması durumunda oluşan hatalara **Syntax Error** ya da **Parsing Error** denir.

<h2 id="1.2">Program Kusurları (Bug)</h2>

Eksik yazılan programlar istenilenin dışında çalışır ve istenilen outputları vermez. Bu eksiklikle sonucu oluşan hatalara **bug** denir. Bug'lar bazen güvenlik açıkları oluşturabilir (örneğin `eval()` fonksiyonu). Bu oluşan güvenlik açıklarına **security bug** veya **security flaw** denir.

<h2 id="1.3">İstisnalar (Exception)</h2>

Syntax hatası olmayan bir programda, runtime (çalıştığı süre) sırasında oluşabilecek hatalara **exceptions** ya da **logical errors** denir. Bu hatalar `Exception` class'ının subclass'ıdır. Bazı hatalar bu subclass'ların da subclass'ı olabilir. Örnek:
- **`StandardError`:** `StopIteration` ve `SystemExit` dışındaki tüm built-in exception'lar için base class'dır ama exception's inheritance chain'de gereksiz bir bağlantı oluşturduğunu kanıtladığı için Python 3'de kaldırıldı.
- **`ArithmeticError`:** Çeşitli aritmetik (sayısal) exception'lar için oluşturulan built-in exception'lar için base class'dır: `OverflowError`, `ZeroDivisionError`, `FloatingPointError`.
- **`EnvironmentError`:** Python'un dışından (işletim sistemi, dosya sistemi vb.) gelen exception'lar için base class'dır: `IOError`, `OSError`
- **`LookupError`:** Bir mapping üzerinden kullanılan key veya bir sequence üzerinden kullanılan index geçersiz (invalid) olduğunda yükseltilen exception'lar için base class'dır: `IndexError`, `KeyError`. Bu, doğrudan `codecs.lookup()` tarafından yükseltilebilir.

Build-in (gömülü) exception'ların çoğu aşağıda gösterilmiştir:

| Exception | Description |
| :-----------: |----------------|
| `AssertionError` | Bir `assert` statement başarısız olduğunda yükseltilen hata mesajıdır. |
| `AttributeError` | Attribute assignment fails'de ya da reference fails'de (x=10 ; x.append(1) gibi) yükseltilen hata mesajıdır. |
| `EOFError` | Dosya sonuna (end-of-file) ulaştığında ya da `raw_input()` veya `input()` fonksiyonlarında input olmadığında yükseltilen hata mesajıdır. |
| `FloatingPointError` | Bir floating point işlemi başarısız olduğunda yükseltilen hata mesajıdır. |
| `GeneratorExit` | Bir generator'ın `close()` methodu çağırıldığında yükseltilen hata mesajıdır. |
| `ImportError` | Import edilmiş module bulunamadığında (not found) (daha genel bir tabirle, import işlemi başarısız olduğunda) yükseltilen hata mesajıdır. |
| `IndexError` | Bir sequence'ın index'i out of range olduğunda (yani sequence'ın index'i bulunamadığında) yükseltilen hata mesajıdır. |
| `IOError` | Var olmayan bir dosyayı açmaya çalışırken, yazdırma sırasında veya `open()` fonksiyonu gibi bir IO işlemi başarısız olduğunda yükseltilen hata mesajıdır. Bu hata, bir anlamda işletim sistemi ile ilgili sorunlar olarak düşünülebilir. |
| `KeyError` | Bir dictionary'de `key` bulunamadığında (not found) yükseltilen hata mesajıdır. |
| `KeyboardInterrupt` | Kullanıcı interrupt key'e (`Ctrl + C` ya da `Delete`) bastığında program yürütülmeyi (execute) sonlandırır ve Python bu hatayı yükseltir. |
| `MemoryError` | Bir işlem sırasında out of memory olduğunda yükseltilen hata mesajıdır. Out of memory; diyelim ki öyle bir program yazdınız ki, o program bütün RAM'inizi kullanıyor ve RAM'inizde yer kalmadı. RAM'inizde yer kalmamasına rağmen RAM kullanmaya çalışırsanız bu hata yükseltilen. |
| `NameError` | Bir identifier, global veya local scope'da bulunamazsa (not found) yükseltilen hata mesajıdır. |
| `NotImplementedError` | Bu hata mesajını anlamak için gerekli kaynaklar: [Kaynak 1](https://www.tutorialspoint.com/How-to-catch-NotImplementedError-Exception-in-Python "https://www.tutorialspoint.com/How-to-catch-NotImplementedError-Exception-in-Python"), [Kaynak 2](https://docs.python.org/3/library/exceptions.html#NotImplementedError "https://docs.python.org/3/library/exceptions.html#NotImplementedError"), [Kaynak 3](https://qastack.info.tr/programming/372042/difference-between-abstract-class-and-interface-in-python "https://qastack.info.tr/programming/372042/difference-between-abstract-class-and-interface-in-python"). |
| `OSError` | İşletim sistemi (OS) işlemleri, işletim sistemi ile ilgili hataya neden olduğunda yükseltilen hata mesajıdır. |
| `OverflowError` | Bir aritmetik (sayısal) işlemin sonucu temsil edilemeyecek kadar büyük olduğunda yükseltilen hata mesajıdır. |
| `ReferenceError` | Bir [garbage collection](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/basic_concepts.md#12 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/temel_bilgiler/basic_concepts.md#12") referansına erişmek için zayıf bir proxy referansı kullanıldığında yükseltilen hata mesajıdır. |
| `RuntimeError` | Bir hata mesajı herhangi bir kategoriye girmediğinde yükseltilen hata mesajıdır. |
| `StopIteration` | Bir iterator'ın `next()` methodu tarafından döndürülecek başka bir öğe kalmadığında yükseltilen hata mesajıdır. |
| `SyntaxError` | Python'un syntax'ına uymayan bir kodla karşılaşıldığında yükseltilen hata mesajıdır. |
| `IndentationError` | Indentation'ların (girinti) kusurlu olması sonucu yükseltilen hata mesajıdır. |
| `TabError` | Indentation'lar birbiriyle tutarsız olduğunda (örneğin bazıları 2 spaces, bazıları 4 spaces uzunluğunda olduğunda) yükseltilen hata mesajıdır. |
| `SystemError` | Python interpreter, bir iç sorun ([Internal error](https://www.google.com/search?q=what%20is%20internal%20error&client=opera-gx&hs=O1t&sxsrf=ALeKk003LeQ3bOnBhmUKaD-7ImUm4u-0FA:1621149477103&ei=JcegYKPkBcPgkgWt_IOoDw&oq=what%20is%20internal%20error&gs_lcp=Cgdnd3Mtd2l6EAMyBggjECcQEzIECCMQJzIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIECAAQHjIECAAQHjoHCCMQsAMQJzoHCAAQRxCwAzoHCCMQsAIQJzoECAAQEzoICAAQDRAeEBNQvl9Yh2FgvmJoAnACeACAAbcBiAGfA5IBAzAuM5gBAKABAaoBB2d3cy13aXrIAQnAAQE&sclient=gws-wiz&ved=0ahUKEwjjite11M3wAhVDsKQKHS3-APUQ4dUDCAw&uact=5)) tespit ettiğinde yükseltilen hata mesajıdır. Python interpreter, bu hatayla karşılaşsa bile kodları yorumlamaya devam eder. |
| `SystemExit` | `sys.exit()` fonksiyonunun yükselttiği hata mesajıdır. |
| `TypeError` | Bir fonksiyon veya işleme uygunsuz type'da bir objeye uygulandığında yükseltilen hata mesajıdır. |
| `UnboundLocalError` | Local namespace'de bulunan bir obje üzerinde işlem yapmaya çalışırken yükseltilebilecek hata mesajıdır. Ayrıntılı bilgi için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/functions.md#1.6 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/functions.md#1.6"). |
| `UnicodeError` | UNICODE'da `\U` ya da `\u` kullanımında kod çözücü kodu çözemediğinde oluşan, encoding ya da decoding hatasından dolayı yükseltilen hata mesajıdır. |
| `UnicodeEncodeError` | Stringlerdeki `encode()` methodu, kodu çözemediğinde yükseltilen hata mesajıdır. |
| `UnicodeDecodeError` | Stringlerdeki `decode()` methodu, kodu çözemediğinde yükseltilen hata mesajıdır. |
| `UnicodeTranslateError` | `UnicodeError` ile ilgili bir hata mesajıdır. `UnicodeError`'ün subclass'ıdır. |
| `ValueError` | Bir fonksiyon ya da işlem (operation), doğru type'a sahip ancak uygun olmayan bir value'ya sahip bir argüman aldığında ve durum `IndexError` gibi daha kesin bir exception tarafından tanımlanmadığında (yani `IndexError` yükseltilmediğinde) yükseltilen hata mesajıdır. |
| `ZeroDivisionError` | Bir division ya da modulo işleminde, ikinci operand'ın sıfır olmasından dolayı yükseltilen hata mesajıdır. |

**Not:** Bütün exception'lar hakkında daha ayrıntılı bilgi için [tıklayınız](https://docs.python.org/3/library/exceptions.html).

<h1 id="2">Hata Yakalama Kodları</h1>

Hata yakalama kodlar, bir kod parçasında oluşabilecek hataları yakalayıp Python'un nasıl davranacağını belirlememizi sağlayan statement'lardır.

<h2 id="2.1"><code>try</code> - <code>except (ErrorCode)</code> Yapısı</h2>

`try` - `except (ErrorCode)` yapısı, `try` - `except` statement'larının arasına yazılan kodlarda oluşacak hataları yakalayıp, `except` statement'ın `(ErrorCode)` kısmında belirtilen error'un yükseltilmesi halinde Python'un davranışını `except` statement'ın kod bloğunda belirlediğimiz yapıdır. Syntax:
```py
try:
	# Expression
except (ErrorCode):
	# Expression
```
**Not:** `(ErrorCode)` kısmını boş bırakırsanız, `try` - `except` statement'ları arasındaki kodlarda oluşabilecek herhangi bir hatada `except` statement çalışır.

**Örnek Program:** `try`'dan sonra birden fazla `except` ekleyebilirsiniz. Bu özellik, birden fazla spesifik durumu ele alıp her durum için farklı bir işlem yapılmasını istediğinizde çok yararlı olan bir özelliktir.
```py
while True:
    a1 = input("ilk sayı: ")
    a2 = input("ikinci sayı: ")

    if a1 == "q" or a2 == "q":
        print("Program Sonlandırılıyor...")
        break

    try:
        a1 = int(a1)
        a2 = int(a2)
        print(a1, "/", a2, "=", a1 / a2)
        
    except ValueError:
        print("Lütfen sadece sayı girin!")
        
    except ZeroDivisionError:
        print("Bir sayıyı 0'a bölemezsiniz!")
```
**Output:**
```
ilk sayı: 5
ikinci sayı: 2
5 / 2 = 2.5
ilk sayı: 8
ikinci sayı: 4
8 / 4 = 2.0
ilk sayı: 2
ikinci sayı: 0
Bir sayıyı 0'a bölemezsiniz!
ilk sayı: 5
ikinci sayı: t
Lütfen sadece sayı girin!
ilk sayı: q
ikinci sayı: q
Program Sonlandırılıyor...
```
Birden fazla spesifik durum için aynı işlemi yapmak istediğinizde, bu hata mesajlarını gruplayarak tek bir `except`'e ekleyebilirsiniz. Örnek:
```py
while True:
    a1 = input("ilk sayı: ")
    a2 = input("ikinci sayı: ")

    if a1 == "q" or a2 == "q":
        print("Program Sonlandırılıyor...")
        break

    try:
        a1 = int(a1)
        a2 = int(a2)
        print(a1, "/", a2, "=", a1 / a2)
        
    except (ValueError, ZeroDivisionError):
        print("Hatalı bir işlem yaptınız!")
```
**Output:**
```
ilk sayı: 1
ikinci sayı: 0
Hatalı bir işlem yaptınız!
ilk sayı: 1
ikinci sayı: r
Hatalı bir işlem yaptınız!
ilk sayı: q
ikinci sayı: q
Program Sonlandırılıyor...
```
Burada hata kodlarını parantez içine alarak gruplamanız önemlidir. Aksi `SyntaxError: invalid syntax` hatası alırsınız.

<h2 id="2.2"><code>try</code> - <code>except (ErrorCode)</code> - <code>as (identifier)</code> Yapısı</h2>

`as` statement sayesinde hata mesajını bir variable'a atayabiliriz. Örnek:
```py
while True:
    a1 = input("ilk sayı: ")
    a2 = input("ikinci sayı: ")

    if a1 == "q" or a2 == "q":
        print("Program Sonlandırılıyor...")
        break

    try:
        a1 = int(a1)
        a2 = int(a2)
        print(a1, "/", a2, "=", a1 / a2)
        
    except (ValueError, ZeroDivisionError) as hata:
        print("Bir hata oluştu!")
        print("orijinal hata mesajı:", hata)
```
**Output:**
```
ilk sayı: 1
ikinci sayı: 0
Bir hata oluştu!
orijinal hata mesajı: division by zero
ilk sayı: 1
ikinci sayı: j
Bir hata oluştu!
orijinal hata mesajı: invalid literal for int() with base 10: 'j'
ilk sayı: q
ikinci sayı: q
Program Sonlandırılıyor...
```

<h2 id="2.3"><code>try</code> - <code>except (ErrorCode)</code> - <code>else</code> Yapısı</h2>

Bu yapıda, `except` statement çalışmazsa `else` statement çalışır. Bu yapının programda bug'lar yaratma olasılığı olduğu için tercih edilmez. Örnek:
```py
while True:
    a1 = input("ilk sayı: ")
    a2 = input("ikinci sayı: ")

    if a1 == "q" or a2 == "q":
        print("Program Sonlandırılıyor...")
        break

    try:
        a1 = int(a1)
        a2 = int(a2)
        print(a1, "/", a2, "=", a1 / a2)
        
    except (ValueError, ZeroDivisionError) as hata:
        print("Bir hata oluştu!")
        print("orijinal hata mesajı:", hata)

    else:
        print("Program çalıştı!")
```
**Output:**
```
ilk sayı: 1
ikinci sayı: 2
1 / 2 = 0.5
Program çalıştı!
ilk sayı: q
ikinci sayı: q
Program Sonlandırılıyor...
```

<h2 id="2.4"><code>try</code> - <code>except (ErrorCode)</code> - <code>finally</code> Yapısı</h2>

Bu yapıda, `except` statement çalışsa da çalışmasa da `finally` statement çalışır. Örnek:
```py
while True:
    a1 = input("ilk sayı: ")
    a2 = input("ikinci sayı: ")

    if a1 == "q" or a2 == "q":
        print("Program Sonlandırılıyor...")
        break

    try:
        a1 = int(a1)
        a2 = int(a2)
        print(a1, "/", a2, "=", a1 / a2)
        
    except (ValueError, ZeroDivisionError) as hata:
        print("Bir hata oluştu!")
        print("orijinal hata mesajı:", hata)

    finally:
        print("Program çalıştı!")
```
**Output:**
```
ilk sayı: 2
ikinci sayı: 1
2 / 1 = 2.0
Program çalıştı!
ilk sayı: 1
ikinci sayı: 0
Bir hata oluştu!
orijinal hata mesajı: division by zero
Program çalıştı!
ilk sayı: 1
ikinci sayı: l
Bir hata oluştu!
orijinal hata mesajı: invalid literal for int() with base 10: 'l'
Program çalıştı!
ilk sayı: q
ikinci sayı: q
Program Sonlandırılıyor...
```

<h2 id="2.5"><code>raise (error message)</code> Statement</h2>

`raise` statement, hata mesajını düzenleyebildiğimiz hata kodları yükseltebilmemizi sağlar. Bu hata kodları, Python'da tanımlı hata kodları olmak zorundadır. Aksi halde `NameError` hatası yükseltilir. Örnek:
```py
raise FalanFilanError("Bak yükseltim") # Output: NameError: name 'FalanFilanError' is not defined
```
`raise` statement çalışınca Python, programı sonlandırır. Doğru kullanıma örnek:
```py
tr_karakter = "şçğüöıİ"
parola = input("Parolanız: ")

for i in parola:
	if i in tr_karakter:
		raise TypeError("Parolada Türkçe karakter kullanılamaz!")
	else:
		a = 1
if a == 1:
    print("Parolanız kabul edilmiştir!")
```
**Output 1:**
```
Parolanız: asdqwe
Parolanız kabul edilmiştir!
```
**Output 2:**
```
Parolanız: asdqweş
Traceback (most recent call last):
  File "deneme.py", line 6, in <module>
    raise TypeError("Parolada Türkçe karakter kullanılamaz!")
TypeError: Parolada Türkçe karakter kullanılamaz!
```

**Not:** `reise` statement'ı `assert` statement gibi herhangi bir namespace içinde kullanabilirsiniz. `reise` statement çalışınca program sonlandırılır.

**Not:** `raise` statement'ı aşağıdaki örnekteki gibi de kullanabilirsiniz:
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
`raise` statement'a bir hata kodu girerseniz de şöyle davranır:
```py
while True:
    a1 = input("ilk sayı: ")
    a2 = input("ikinci sayı: ")

    if a1 == "q" or a2 == "q":
        print("Program Sonlandırılıyor...")
        break

    try:
        a1 = int(a1)
        a2 = int(a2)
        print(a1, "/", a2, "=", a1 / a2)
        
    except (ValueError, ZeroDivisionError):
        print("Bir hata oluştu!")
        raise TypeError("Öylesine bir error.")
```
**Output:**
```
ilk sayı: 1
ikinci sayı: w
Bir hata oluştu!
Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 11, in <module>
    a2 = int(a2)
ValueError: invalid literal for int() with base 10: 'w'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "d:\hata_yakalama.py", line 16, in <module>
    raise TypeError("Öylesine bir error.")
TypeError: Öylesine bir error.
```
Buradaki "During handling of the above exception, another exception occurred" mesajı "Yukarıdaki exception'ın işlenmesi sırasında başka bir exception oluştu" anlamına gelmektedir. Yani bu "`ValueError` oluştuğu sırada, başka bir exception olan (another exception) `TypeError` oluştu." anlamına gelmektedir. `raise` statement'ını `from` keyword'ü ile birlikte kullanınca bu anlam değişmektedir:
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
Buradaki "The above exception was the direct cause of the following exception" mesajı "Yukarıdaki exception, aşağıdaki exception'ın doğrudan nedeniydi" anlamına gelmektedir. Yani bu "`TypeError` oluşma nedeni `ValueError`'dür." anlamına gelmektedir. Bu iki farklı durumun hangi durumlarda spesifik olarak işinize yarayacağı hakkında en ufak fikrim yok.

<h2 id="2.6"><code>assert (condition), (error message)</code> Statement</h2>

`assert` statement'ı `raise` statement'ının aksine özelleştirilebilir hata mesajları yaratmamıza olanak tanır. `(condition)` logic bir ifadedir ve `False` olursa `assert` statement çalışır. `assert` çalıştığında `AssertionError` hata kodunu `(error message)` hata mesajı ile yükseltir. Aşağıdaki iki kod aynı işleve sahiptir:

**`raise` Statement Örneği:**
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
**`assert` Statement Örneği:**
```py
giriş = input("Merhaba! Adın ne? ")
assert ((len(giriş) != 0)), ("İsim bölümü boş.")
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

**Not:** `assert` statement'ı `reise` statement gibi herhangi bir namespace içinde kullanabilirsiniz. `assert` statement çalışınca program sonlandırılır.

**Not:** `assert` statement'ı, Python kodlarını debugging (hata ayıklama işlemi) yapmak için kullanılır. Bir Python dosyasını terminalden çalıştırırken `python -O dosya_adı` komutuyla çalıştırırsanız, Python dosyası içindeki bütün `assert` statement'lerini görmezden gelir. Bunu sağlayan şey optimize anlamına gelen `-O` parametresidir. Eğer `-O` olmadan `python dosya_adı` koduyla çalıştırırsanız, Python dosyası içindeki `assert` statement'lerini görmezden gelmez. Bunu debugging yapmak için kullanabiliriz:

![](https://i.ibb.co/pZqwRNF/Ekran-Al-nt-s.png)
