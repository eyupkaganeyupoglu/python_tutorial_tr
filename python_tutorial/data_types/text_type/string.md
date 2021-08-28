# İçindekiler
- [Karakter dizileri (Strings)](#1)
    - [String Tanımlamak](#1.1)
    - [String'lerde İşlemler](#1.2)
    - [`str()` Fonksiyonu](#1.3)
    - [`reversed(seq)` Fonksiyonu](#1.4)
    - [`sorted(iterable, key=None, reverse=False)` Fonksiyonu](#1.5)
    - [`enumerate(iterable, start=0)` Fonksiyonu](#1.6)
- [Karakter Dizisi Biçimlendirme](#2)
    - [Eski Yöntem (`%`)](#2.1)
        - [Biçimlendirme Karakterleri](##2.1.1)
            - [`s` Harfi](#2.1.1.1)
            - [`d` Harfi](#2.1.1.2)
            - [`i` Harfi](#2.1.1.3)
            - [`o` Harfi](#2.1.1.4)
            - [`x`/`X` Harfi](#2.1.1.5)
            - [`f` Harfi](#2.1.1.6)
            - [`c` Harfi](#2.1.1.7)
    - [Yeni Yöntem (`format()` methodu)](#2.2)
        - [Biçimlendirme Karakterleri](#2.2.1)
            - [`s` Harfi](#2.2.1.1)
            - [`c` Harfi](#2.2.1.2)
            - [`d` Harfi](#2.2.1.3)
            - [`o` Harfi](#2.2.1.4)
            - [`x`/`X` Harfi](#2.2.1.5)
            - [`b` Harfi](#2.2.1.6)
            - [`f` Harfi](#2.2.1.7)
            - [Basamak Ayracı (`,`)](#2.2.1.8)
    - [f-string](#2.3)
- [String Methodları](#3)
    - [`replace(old, new, count)` Methodu](#3.1)
    - [`split(sep=" ", maxsplit)` Methodu](#3.2)
    - [`rsplit(sep=" ", maxsplit)` Methodu](#3.3)
    - [`splitlines(keepends)` Methodu](#3.4)
    - [`lower()` Methodu](#3.5)
    - [`upper()` Methodu](#3.6)
    - [`islower()` Methodu](#3.7)
    - [`isupper()` Methodu](#3.8)
    - [`endswith(suffix, start, end)` Methodu](#3.9)
    - [`startswith(prefix, start, end)` Methodu](#3.10)
    - [`capitalize()` Methodu](#3.11)
    - [`swapcase()` Methodu](#3.12)
    - [`casefold()` Methodu](#3.13)
    - [`strip(chars)` Methodu](#3.14)
    - [`lstrip("string")` Methodu](#3.15)
    - [`rstrip("string")` Methodu](#3.16)
    - [`join(iterable)` Methodu](#3.17)
    - [`count(x, start, end)` Methodu](#3.18)
    - [`index(sub, start, end)` Methodu](#3.19)
    - [`rindex(sub, start, end)` Methodu](#3.20)
    - [`find(sub, start, end)` Methodu](#3.21)
    - [`rfind(sub, start, end)` Methodu](#3.22)
    - [`center(width, fillchar)` Methodu](#3.23)
    - [`rjust(width, fillchar)` Methodu](#3.24)
    - [`ljust(width, fillchar)` Methodu](#3.25)
    - [`zfill(width)` Methodu](#3.26)
    - [`partition(sep)` Methodu](#3.27)
    - [`partition(sep)` Methodu](#3.28)
    - [`encode(encoding='UTF-8',errors='strict')` Methodu](#3.29)
    - [`expandtabs(tabsize)` Methodu](#3.30)
    - [`maketrans(x, y, z)` Methodu](#3.31)
    - [`translate(table)` Methodu](#3.32)
    - [`isalpha()` Methodu](#3.33)
    - [`isnumeric()` Methodu](#3.34)
    - [`isalnum()` Methodu](#3.35)
    - [`isdigit()` Methodu](#3.36)
    - [`isdecimal()` Methodu](#3.37)
    - [`isidentifier()` Methodu](#3.38)
    - [`isspace()` Methodu](#3.39)
    - [`isprintable()` Methodu](#3.40)

<h1 id="1">Karakter dizileri (Strings)</h1>

Karakter dizileri adı üstünde karakterlerden oluşan dizilerdir. Örneğin `"ALİ"` karakter dizisi `"A"`, `"L"` ve `"İ"` karakterlerinden oluşmaktadır. "Karakter dizisi" kelimesinin ingilizce karşılığı **"string"** kelimesidir. String'ler değiştirilemez (immutable) data type'lardır. Bir string'i değiştirmenin tek yolu onu yeniden tanımlamaktır (redefinition) (replace methodu ile bile olmaz).  Örnek:
```py
a = "String 1"
print(a, id(a)) # Output: String 1 2667507778672
a = "String 2"
print(a, id(a)) # Output: String 2 2667507778736
a = a.replace("S", "s", 1)
print(a, id(a)) # Output: string 2 2667508084400
```

<h2 id="1.1">String Tanımlamak</h2>

```py
a = 'Tek tırnak ile tanımlamak.' # Tek Tırnak
print(a)
a = "Tek tırnak ile tanımlamak." # Çift Tırnak
print(a)
a = """
Tek
tırnak
ile
tanımlamak
""" # Üçlü Çift Tırnak
print(a)
```
**Output:**
```
Tek tırnak ile tanımlamak.
Tek tırnak ile tanımlamak.

Tek
tırnak
ile
tanımlamak

```
Bu çeşitlilik, kesme işareti ya da alıntı ifadeleri gibi yerlerde Python'a sıkıntı çıkarmamak için vardır. Örnek:
```py
a = """İstanbul'un içinden bir dayı "Selam!" dedi."""
print(a) # Output: İstanbul'un içinden bir dayı "Selam!" dedi.
```

<h2 id="1.2">String'lerde İşlemler</h2>

Stringleri oluşturan karakterlerin her birinin string içindeki konumuna **index** denir. Index, soldan 0, 1, 2, 3; sağdan -1, -2, -3, -4 şeklinde sıralanmaktadır.
```py
a = "Merhaba"
print(a[3], a[-4], sep=", ")

#Output: h, h
```
Bir string'i dilimlerken `str_exp[Başlama index'i : bitiş index'i : atlama değeri]` syntax'ı kullanılır. Örnekler:
```py
a = "Python Programlama Dili"

# 4. index'ten başlar, (10. index'i dahil etmeden) 10. index'e kadar string'i yazdırır.
print(a[4:10]) # Output: on Pro

# Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (10. index'i dahil etmeden) 10. index'e kadar string'i yazdırır.
print(a[:10]) # Output: Python Pro

# Bitiş index'i belirtilmediği için 4. indexten başlar, en son index'e kadar string'i yazdırır.
print(a[4:]) # Output: on Programlama Dili

# Başlangıç ve bitiş intex'i belirtilmediği için tüm string'i yazdırır.
print(a[:]) # Output: Python Programlama Dili

# Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (-1. index'i dahil etmeden) -1. index'e kadar (sonran bir önceki index) string'i yazdırır.
print(a[:-1])# Output: Python Programlama Dil

# Baştan sona index atlamadan string'i yazdırır.
print(a[::1]) # Output: Pto rgalm ii

# Baştan sona 1 index atlaya atlaya string'i yazdırır.
print(a[::2]) # Output: Pto rgalm ii

# 4. index'ten başlar, (12. index'i dahil etmeden) 12. index'e kadar 2 index atlaya atlaya string'i yazdırır.
print(a[4:12:3]) # Output: oPg

# Sondan başa index atlamadan string'i yazdırır. (String'i ters çevirme)
print(a[::-1]) # Output: iliD amalmargorP nohtyP
```

String'lerde matematiksel işlem örnekleri:
```py
c1 = "Python "
c2 = "Programlama "
c3 = "Dili"

print(c1 + c2 + c3) # Output: Python Programlama Dili
print(c1 * 3)	    # Output: Python Python Python
```

String'leri birleştirme işlemi örnekleri:
```py
print("Merhaba" + " Nasılsınız") # Output: Merhaba Nasılsınız
print("Merhaba" " Nasılsınız") # Output: Merhaba Nasılsınız
```

Bir string'in uzunluğunu `len()` build-in fonksiyonunu kullanarak elde edebilirsiniz.
```py
a = "Python"
print(len(a)) # Output: 6
```
**Not:** Bir `len(a)-1` işlemi string'in sonuncu index'ini verir. Örnek:
```py
a = "Python"
print(a[len(a)-1]) # Output: n
```

<h2 id="1.3"><code>str()</code> Fonksiyonu</h2>

`str(object=b'', encoding='utf-8', errors='strict')` syntax'ına sahiptir:
- **`object`**: Bu parametreye argüman olarak girilen value'ların string'e dönüştürüp döndürür. Default değeri boş string'dir (`b''`, boş byte).
- **`encoding`**: Bilgisayar karakterleri olduğu gibi anlamaz. Bilgisayar elektrik sinyallerini, yani binary formatta ifade edilen şeyleri anlar. *ASCII*, *UNICODE* gibi kodlama sistemleri harf, sayı, sembol gibi karakterlerin bilgisayarın anlayacağı dilde ifade edildiği tablolardır. Bu karakterler bu tablolarda bazen binary, bazen decimal, bazen de hexadecimal formatta ifade edilir. Örneğin sizin `A` olarak bildiğiniz karakterin ASCII'deki decimal karşılığı `65`'dir. Kodlama sistemleri hakkında daha fazla bilgi için [**tıklayınız**](karakter_kodlama_character_encoding.md). `encoding` parametresine argüman olarak `object` parametresinde belirtilen string'in hangi kod çözücü (kodlama sistemi tablosunun program hali olarak düşünebilirsiniz) ile çözüleceğini belirleyebildiğiniz kısımdır.
- **`errors`**: `encoding` parametresindeki kod çözücü başarısız olursa Python'un davranışını belirleyebileceğimiz parametredir. Default değeri `strict`'dir. Bu parametreye 6 çeşit argüman girilebilir:
    - **`strict`**: Herhangi bir encoding hatasıyla karşılaşınca bir `UnicodeDecodeError` hatası yükselten default değerdir.
    - **`ignore`**: Herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakterleri yok sayarak string'in yazdırılmasını sağlayan değerdir. Örneğin ASCII'ye göre: `şelam -> elam` 
    - **`replace`**: Herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakterin yerine `?` sembolünü koyar.
    - **`xmlcharrefreplace`**: Herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakterin yerine o karakterin XML karakter referansını ekler. XML, interneti kullanarak veri alışverişi yapan sistemler ve platformlar arasındaki veri iletişimini standart hale getirmek için tasarlanan bir işaretleme dilidir.
    - **`backslashreplace`**: Herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakterin yerine `\uNNNN` kaçış dizisi ekler.
    - **`namereplace`**: Herhangi bir encoding hatasıyla karşılaşınca kodlanamayan karakterin yerine `\N{...}` kaçış dizisi ekler.

    ```py
    print("bu Türkçe bir cümledir.".encode("ascii", errors="strict")) # Output: UnicodeEncodeError
    print("bu Türkçe bir cümledir.".encode("ascii", errors="ignore")) # Output: b'bu Trke bir cmledir.'
    print("bu Türkçe bir cümledir.".encode("ascii", errors="replace")) # Output: b'bu T?rk?e bir c?mledir.'
    print("bu Türkçe bir cümledir.".encode("ascii", errors="xmlcharrefreplace")) # Output: b'bu T&#252;rk&#231;e bir c&#252;mledir.'
    print("bu Türkçe bir cümledir.".encode("ascii", errors="backslashreplace")) # Output: b'bu T\\xfcrk\\xe7e bir c\\xfcmledir.'
    print("bu Türkçe bir cümledir.".encode("ascii", errors="namereplace")) # Output: b'bu T\\N{LATIN SMALL LETTER U WITH DIAERESIS}rk\\N{LATIN SMALL LETTER C WITH CEDILLA}e bir c\\N{LATIN SMALL LETTER U WITH DIAERESIS}mledir.'
    ```

<h2 id="1.4"><code>reversed(seq)</code> Fonksiyonu</h2>

**Sequance** dediğimiz şey basitçe, bir sonuca ulaşmak için kurulan algoritma olarak düşünebilirsiniz. Bu süreçte sonuca ulaşmak için başlıngıçta verilen durumu parçalara ayırmalı ve her parçayı ayrı ele almalısınız. Örneğin ekmek ve krem peynir durumlarından krem peynir sürülmüş ekmek sonucuna ulaşmak için ekmek ve krem peyniri teker teker ele almalısınız. Python'da da bu mantık geçerlidir. Herhangi bir `tuple`, `string`, `list` ve `range` etc. objesinden, bu objelerin reversed (ters) halini elde etmek için her parçayı ayrı değerlendirmelisiniz. `reversed()` fonksiyonu, [sequence protokolünü](https://www.google.com/search?client=opera-gx&q=what%20is%20sequence%20protocol%20in%20python&sourceid=opera&ie=UTF-8&oe=UTF-8 "https://www.google.com/search?client=opera-gx&q=what%20is%20sequence%20protocol%20in%20python&sourceid=opera&ie=UTF-8&oe=UTF-8") destekleyen `tuple`, `string`, `list` ve `range` etc. type'ındaki objeleri ters çevirmekte kullanabileceğiniz bir fonksiyondur. Ters çevirmek istediğiniz iterable objeyi `seq` parametresine argüman olarak girmeniz yeterlidir. Örnek:
```py
a = "1234"
print(*a) # Output: 1 2 3 4
a = reversed(a)
print(*a) # Output: 4 3 2 1
```

| `reversed()` | `var1` | `var2` | `var3` | `var4` |
| :-: | :-: | :-: | :-: | :-: |
| Before Value | 1 2 3 4 | 1 2 3 4 | 1 2 3 4 | 1 2 3 4 |
| Before `type()` | <class 'tuple'> | <class 'str'> | <class 'list'> | <class 'range'> |
| After Value | 4 3 2 1 | 4 3 2 1 | 4 3 2 1 | 4 3 2 1 |
| After `type()` | <class 'reversed'> | <class 'reversed'> | <class 'list_reverseiterator'> | <class 'range_iterator'> |

<h2 id="1.5"><code>sorted(iterable, key=None, reverse=False)</code> Fonksiyonu</h2>

`iterable` parametresine argüman olarak girilen iterable objeyi `key` parametresinde belirtilen ölçüte göre sıralar. `reverse` parametresine bağlı olarak da bu sıralamanın normal mi yoksa ters mi olacağına karar verebilirsiniz. Bu fonksiyon, output'u `list` type'dır. Örnekler:

**String'leri Türkçeye uygun sıralamak:**
```py
print(sorted("çiçek")) # Output: ['e', 'i', 'k', 'ç', 'ç']
```
Türkçeye uygun hale getirmek için:
```py
import locale
locale.setlocale(locale.LC_ALL, "tr_TR")
# locale.setlocale(locale.LC_ALL, "tr_TR") # GNU/Linux için
print(sorted("çiçek", key=locale.strxfrm)) # Output: ['ç', 'ç', 'e', 'i', 'k']
```
`İ`, `ı` karakter sorununu çözmek için:
```py
import locale
locale.setlocale(locale.LC_ALL, "tr_TR")
# locale.setlocale(locale.LC_ALL, "tr_TR") # GNU/Linux için

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}

print(sorted("ıi", key=locale.strxfrm)) #Output: ['i', 'ı']
print(sorted("ıi", key=çevrim.get)) #Output: ['ı', 'i']
```

**Nested (iç içe) listelerde her bir index'i ilk index'ine göre sıralamak:**
```py
elemanlar = [['ahmet',       33,    'karataş'],
             ['mehmet',      45,    'arpaçbahşiş'],
             ['sevda',       24,    'arsuz'],
             ['arzu',        40,    'siverek'],
             ['abdullah',    30,    'payas'],
             ['ilknur',      40,    'kilis'],
             ['abdurrezzak', 40,    'bolvadin']]

print(*sorted(elemanlar), sep='\n')
```
**Output:**
```
['abdullah', 30, 'payas']
['abdurrezzak', 40, 'bolvadin']
['ahmet', 33, 'karataş']
['arzu', 40, 'siverek']
['ilknur', 40, 'kilis']
['mehmet', 45, 'arpaçbahşiş']
['sevda', 24, 'arsuz']
```
Her bir index'i ikinci index'ine göre sıralamak:
```py
elemanlar = [['ahmet',       33,    'karataş'],
             ['mehmet',      45,    'arpaçbahşiş'],
             ['sevda',       24,    'arsuz'],
             ['arzu',        40,    'siverek'],
             ['abdullah',    30,    'payas'],
             ['ilknur',      40,    'kilis'],
             ['abdurrezzak', 40,    'bolvadin']]

print(*sorted(elemanlar, key=lambda x: x[1]), sep='\n')
```
**Output:**
```
['sevda', 24, 'arsuz']
['abdullah', 30, 'payas']
['ahmet', 33, 'karataş']
['arzu', 40, 'siverek']
['ilknur', 40, 'kilis']
['abdurrezzak', 40, 'bolvadin']
['mehmet', 45, 'arpaçbahşiş']
```
İkinci index'deki değerleri aynı olan index'leri üçüncü index'lerine göre sıralamak:
```py
elemanlar = [['ahmet',       33,    'karataş'],
             ['mehmet',      45,    'arpaçbahşiş'],
             ['sevda',       24,    'arsuz'],
             ['arzu',        40,    'siverek'],
             ['abdullah',    30,    'payas'],
             ['ilknur',      40,    'kilis'],
             ['abdurrezzak', 40,    'bolvadin']]

print(*sorted(elemanlar, key=lambda x: (x[1],x[2])), sep='\n')
```
**Output:**
```
['sevda', 24, 'arsuz']
['abdullah', 30, 'payas']
['ahmet', 33, 'karataş']
['abdurrezzak', 40, 'bolvadin']
['ilknur', 40, 'kilis']
['arzu', 40, 'siverek']
['mehmet', 45, 'arpaçbahşiş'] 
```

<h2 id="1.6"><code>enumerate(iterable, start=0)</code> Fonksiyonu</h2>

`iterable` parametresine argüman olarak girilen iterable objeyinin her bir index'ini numaralandırmaya yarayan bir fonksiyondur. Bu fonksiyon bir `enumerate` objesi döndürür. Bu iterator'ün (`enumerate` objesinin) `__next__()` methodu, `start` parametresinde belirtilen (default değeri `0` olan) sayıdan başlayan bir sayım ve `iterable` parametresine argüman olarak girilen objenin elemanını içeren bir `tuple` döndürür. Örnek:
```py
print(*enumerate("abcd")) # Output: (0, 'a') (1, 'b') (2, 'c') (3, 'd')
print(*enumerate("abcd", start=1)) # Output: (1, 'a') (2, 'b') (3, 'c') (4, 'd')
```

<h1 id="2">Karakter Dizisi Biçimlendirme</h1>

Python, karakter dizilerini biçimlendirme konusunda bazı yöntemlere sahiptir. Bir karakter dizisini bir kere yazdıktan sonra o karakter dizisi üzerinde bazı değişiklikler yapmak istediğinizde bunu elle yapmanız gerekiyor olarak düşünebilirsiniz ama Python, karakter dizilerini isteğe bağlı değiştirebileceğiniz **Karakter Dizisi Biçimlendirme** yöntemlerine sahiptir. Örnekler:
```py
while True:
    a = input("First: ")
    b = input("Second: ")

    if a == "çıkış" or b == "çıkış":
        print("Program sonlandırılıyor...")
        break

    print("%s ve %s iyi bir ikilidir!" %(a,b))
```
**Output:**
```
First: ben  
Second: sen
ben ve sen iyi bir ikilidir!
First: falan      
Second: filan
falan ve filan iyi bir ikilidir!
First: çıkış
Second: çıkış
Program sonlandırılıyor...
```
Başka bir örnek:
```py
while True:
    a = input("First: ")
    b = input("Second: ")

    if a == "çıkış" or b == "çıkış":
        print("Program sonlandırılıyor...")
        break

    print("{} ve {} iyi bir ikilidir!".format(a,b))
```
**Output:**
```
First: ben  
Second: sen
ben ve sen iyi bir ikilidir!
First: falan      
Second: filan
falan ve filan iyi bir ikilidir!
First: çıkış
Second: çıkış
Program sonlandırılıyor...
```

<h2 id="2.1">Eski Yöntem (<code>%</code>)</h2>

Python'un 2.x sürümlerinde, karakter biçimlendirmek kullanılan yöntemdir. Python'un 3.x sürümlerinde de hala kullanılabilir olsa bile `format` methodu daha kaliteli bir tercih olduğu için pek tercih edilmez. Ama eski kodları okurken karşımıza çıkacak. Bu yüzden öğrenmekte fayda var. Örnek:
```py
print("%s ve %s iyi bir ikilidir!" %("Python", "Django")) # Output: Python ve Django iyi bir ikilidir!
```
String içinde her bir `%` işareti ile belirtilen bölüme, string'in dışında `%` işaretinden sonra açılan parantezin içine tanımlanan değerler sırasıyla yerleştirilir. Bu yüzden string'in içindeki `%` ile belirtilen kısımların her birine gelecek ifade string'in dışındaki `%`'nin parantezinin içinde tanımlı olmalıdır. Aksi halde `TypeError` hatası yükseltilir. Örnek:
```py
print("%(isim)s'in arabası\n%(isim)s'in parası\n%(isim)s'in çocuğu" %{"isim": "Ahmet"})
```
**Output:**
```
Ahmet'in arabası
Ahmet'in parası
Ahmet'in çocuğu
```
Böylelikle String içinde her bir `%` işareti ile belirtilen bölüme girilecek değerleri string'in dışında `%` işaretinden sonra açılan parantezin içine teker teker tanımlamak yerine bu değeri bir key'e atayıp o key'i string içinde her bir `%` işareti ile belirtilen bölüme girebiliriz.

**Not:** Bir string içinde `%` işaretini `"%100 başarıyla çalıştı!"` örneğindeki gibi kullanmanız gerektiğinde `%%%` syntax'ını kullanmalısınız. Örnek:
```py
print("Yükleniyor... %%%s" %(99)) # Output: Yükleniyor... %99
```
`%%%` yerine `%%` kullanırsanız `TypeError: not all arguments converted during string formatting` hatası alırsınız.

String'leri sağa yaslamak için:
```py
l1 = ["123", "123456789", "1234567891011"]
for i in l1:
	print("'%15s'" %(i))
```
**Output:**
```
'           1234'
'      123456789'
'  1234567891011'
```
`"'%15s'"` işlemi şu şekilde yorumlanıyor:  Önce 15 karakterlik alan belirleniyor ve belirtilen karakter dizisi bu alanın en sağına yerleştiriliyor. Örneğin `"1234"` karakter dizisine bu işlemi uyguladıktan sonra elimizde sağa yaslanmış 4 karakter uzunluğunda bir `"1234"` karakter dizisi ve 11 karakter uzunluğunda boşluk karakteri dizisi oluyor. Burada dikkat edilmesi gereken şey, sınırlandırılan uzunluktan daha uzun bir karakter dizisi varsa, o karakter dizisi manipüle edilemez. Örnek:
```py
l1 = ["1234", "1234567", "1234567891011"]
for i in l1:
	print("'%7s'" %(i))
```
**Output:**
```
'   1234'
'1234567'
'1234567891011'
```
Gördüğünüz gibi 7 karakterden daha uzun karakter dizileri manipüle edilemezken, 7 karakterden daha kısa ve 7 karakter olan karakter dizilerini manipüle edilebilir. Aynı şey sola yaslamada da geçerkidir. Sola yaslamak için pozisif sayılar yerine negatif sayıları kullanırız. Örnek:
```py
l1 = ["1234", "1234567", "1234567891011"]
for i in l1:
	print("'%-7s'" %(i))
```
**Output:**
```
'1234   '
'1234567'
'1234567891011'
```
Gördüğünüz gibi 7 karakterden daha uzun karakter dizileri manipüle edilemezken, 7 karakterden daha kısa ve 7 karakter olan karakter dizilerini manipüle edilebilir.

<h3 id="2.1.1">Biçimlendirme Karakterleri</h3>

Biçimlendirme karakterleri, String içinde her bir `%` işareti ile belirtilen bölüme girilecek değerin type'ını belirtmemizde olanak tanır. Bu, belirli bir bölüme istenmeyen type'a sahip bir objenin girilmesine engel olur çünkü eğer bu durum yaşanırsa `TypeError` hata mesajı yükseltilir. Örnek:
```py
print("%d" %("selam")) # TypeError: %d format: a number is required, not str
```
Gördüğünüz gibi integer type'ı temsil eden biçimlendirme karakterine string type bir değer girmeye çalıştığımızda `"%d biçimi: bir sayı gereklidir, str değil"` anlamına gelen bir hata mesajı döndürülür.

<h4 id="2.1.1.1"><code>s</code> Harfi</h4>

String type'ı (`str`) temsil eder. Örnek:
```py
print("%s" %("Bu bir String")) # Output: Bu bir String
```

<h4 id="2.1.1.2"><code>d</code> Harfi</h4>

Integer (`int`) type'ı temsil eder. Float type değer girilirse, bu değeri integer type'a çevirip kullanır. Örnek:
```py
print("%d" %(1)) # Output: 1
```
Sağa sola yaslama işleminde oluşan boşlukların istediğiniz kadarını `0` ile doldurabilirsiniz. Örnek:
```py
print("'%05.d'" %(1))  # Output: '00001'
print("'%5.2d'" %(1))  # Output: '   01'
print("'%-5.2d'" %(1)) # Output: '01   '
```
Gördüğünüz gibi bütün boşlukları `0` ile doldurmak için `%0x.d` ya da `%0xd` formatını kullanıyoruz (ikisi de bende çalıştı). Bu formattaki `x` yerine girdiğiniz sayıdan önce bir adet `0` koyarsanız, bütün boşluklar sıfır ile doldurulur (başka bir örnek: `print("'%010.d'" %(1))  # Output: '0000000001'`). Eğer belli bir sayıda boşluğu sıfır ile doldurmak istiyorsanız `%x.yd` formatını kullanıyoruz. Bu formattaki `y` yerine `0` ile doldurmak istediğiniz karakter sayısını giriyorsunuz. Buradaki `y` yerinde belirtilen alana, string'in dışında `%` işaretinden sonra açılan parantezin içinde belirtilen değerin karakter uzunluğunun da dahil edildiğini unutmayın. Örneğin `%5.2d` kısmında 2 karakterin sıfır ile doldurulması istendiğinde, bu 2 karaktere bir karakter uzunluğundaki `1` de dahil edildiği için output'da 1 tane sıfır görüyorsunuz. `%5.2d` yerine `%5.3d` olsaydı ve `11` sayısı değer olarak girilseydi, output `'  011'` şeklinde olacaktı.

<h4 id="2.1.1.3"><code>i</code> Harfi</h4>

Kullanım ve işlev olarak `d` Harfinden hiçbir farklı yoktur. Örnek:
```py
print("'%05i'" %(1))   # Output: '00001'
print("'%5.2i'" %(1))  # Output: '   01'
print("'%-5.2i'" %(1)) # Output: '01   '
```

<h4 id="2.1.1.4"><code>o</code> Harfi</h4>

Octal sayıları temsil eder. Decimal sayıları octal sayıya çevirir. Örnek:
```py
print("%i decimal == %o octal" %(10, 10)) # Output: 10 decimal == 12 octal
```

<h4 id="2.1.1.5"><code>x</code>/<code>X</code> Harfi</h4>

Hexadecimal sayıları temsil eder. `x` ve `X` kullanmak arasındaki tek fark, hexadecimal sayı sisteminde kullanılan harfların küçük ya da büyük olmasıdır. Örnek:
```py
print("%i decimal == %x octal" %(10, 10)) # Output: 10 decimal == a octal
print("%i decimal == %X octal" %(10, 10)) # Output: 10 decimal == A octal
```

<h4 id="2.1.1.6"><code>f</code> Harfi</h4>

Float (`float`) type'ı temsil eder. Virgülden sonra 6 karakterlik sıfır koyar. Eğer virgülden sonra sayılar varsa, kalan boşluklara sıfır ile tamamlanır. Örnek:
```py
print("'%f', '%f'" %(10, 10.354)) # Output: '10.000000', '10.354000'
```

<h4 id="2.1.1.7"><code>c</code> Harfi</h4>

`C` dil ailesindeki `char` data type gibidir. Tek karakterleri (single characters) temsil eder. Single character'leri ve integer'ları kabul eder, `"Falan filan"` gibi string'leri kabul etmez. Aksi halde `TypeError: %c requires int or char` hatası yükseltir. Decimal bir sayı girildiğinde, o sayıya karşılık gelen ASCII karakterini yazdırır. ASCII kodlama sistemini kullandığı için 255'den sonra aptal karakterler basmaya başlar. Örnek:
```py
print("%c" %("A")) # Output: A
print("%c" %(65))  # Output: A
print("%c" %(666)) # Output: ʚ
print("%c" %("String")) # TypeError: %c requires int or char
```

<h2 id="2.2">Yeni Yöntem (<code>format()</code> methodu)</h2>

`format()` methodu, Python'un 2.6 sürümünden sonra eklendi ve aktif olarak kullanılmaya başlandı. String'in içinde belirtilen süslü parantezleri (`"{}"`) kullanarak karakter dizisi biçimlendirmeye yarar. Eski yöntemden farklı olarak, String'de data type belirtmenize gerek yoktur. Örnek:
```py
print("{} ve {} iyi bir ikilidir!".format("Django", "Python")) # Output: Django ve Python iyi bir ikilidir!
```
Gördüğünüz gibi `format()` methodu, kendisine girilen değerleri soldan sağa doğru (aynı eski yöntemdeki gibi) süslü parantezlerin olduğu yere yerleştirerek karakter dizisini biçimlendirdi. Başka bir özellik:
```py
print("{1} ve {0} iyi bir ikilidir!".format("Django", "Python")) # Output: Python ve Django iyi bir ikilidir!
```
Gördüğünüz gibi `format()` methoduna girilen değerleri index mantığıyla süslü parantezlerin içine istediğiniz gibi yerleştirebilirsiniz. Ayrıca bu yöntemi kullanarak bir değeri birden fazla süslü paranteze yerleştirebilirsiniz. Örnek:
```py
print("{0}, {1}, {0}, {1}...".format("Bir", "İki")) # Output: Bir, İki, Bir, İki...
```

Yeni string formatlama yönteminde sağa sola yaslama ve ortalama işlemleri yapabilirsiniz.

**Sağa yaslama:**
```py
print("'{:>15}'" .format("0123456789")) # Output: '     0123456789'
```
Yukarıda 10 karakterlik karakter dizisi ve 5 karakterli boşluk vardır. Eski formattaki durumlar burada da geçerlidir. Örnek:
```py
print("'{:>7}'\n'{:>7}'\n'{:>7}'\n" .format("1234", "1234567", "1234567891011"))
```
**Output:**
```
'   1234'
'1234567'
'1234567891011'
```
Gördüğünüz gibi belirtilen uzunluğu aşan karakter dizileri formatlanamıyor.

**Sola yaslama:**
```py
print("'{:<15}'" .format("0123456789")) # Output: '0123456789     '
```
Yukarıda 10 karakterlik karakter dizisi ve 5 karakterli boşluk vardır. Eski formattaki durumlar burada da geçerlidir. Örnek:
```py
print("'{:<7}'\n'{:<7}'\n'{:<7}'\n" .format("1234", "1234567", "1234567891011"))
```
**Output:**
```
'1234   '
'1234567'
'1234567891011'
```
Gördüğünüz gibi belirtilen uzunluğu aşan karakter dizileri formatlanamıyor.

**Ortalama:**
Ortalama işleminin doğru yapılabilmesi için süslü parantez içinde belirtilen uzunluğun ve `format()` methoduna argüman olarak girilen string'in uzunluğunun ikisinin de ya çift ya tek sayı olması gerekmektedir. Aksi halde karakter dizisinin sağ ve solundaki boşuk karakteri sayısı aynı olmaz (genelde sağda 1 boşluk karakteri fazla olur). Örnek:
```py
print("'{:^10}'".format("1234"))  # Output: '   1234   '  sağ 3, sol 3
print("'{:^11}'".format("12345")) # Output: '   12345   ' sağ 3, sol 3
print("'{:^10}'".format("12345")) # Output: '  12345   '  sağ 2, sol 3
print("'{:^11}'".format("1234"))  # Output: '   1234    ' sağ 3, sol 4
```
Bu biçimlendirme yönteminde de süslü parantez içinde belirtilen uzunluk ile `format()` methoduna argüman olarak girilen string'in uzunluğundan az olursa formatlama işlemi gerçekleşmez. Örnek:
```py
print("'{:^8}'\n'{:^8}'\n'{:^8}'\n" .format("1234", "123456", "1234567891011"))
```
**Output:**
```
'  1234  '
' 123456 '
'1234567891011'
```

<h3 id="2.2.1">Biçimlendirme Karakterleri</h3>

Eski formatlama yönteminde harflerin belirttiği type dışında bir data type verilirse tip dönüşümü yapmaya çalışır. Örneğin `d` harfine float type bir değer verirseniz, onu integer type'a dönüştürür. `format()` methodunda böyle bir durum yoktur. Süslü parantez içinde belirtilen type dışında bir data type verilirse, `format()` methodu `ValueError` hatası yükseltir. Örnek:
```py
print("%d" %(1.123)) # Output: 1
print("{:d}".format(1.123)) # ValueError: Unknown format code 'd' for object of type 'float'
```
Gördüğünüz gibi integer type'ı temsil eden biçimlendirme karakterine string type bir değer girmeye çalıştığımızda `'str' türündeki nesne için bilinmeyen biçim kodu 'd'"` anlamına gelen bir hata mesajı döndürülür.

<h4 id="2.2.1.1"><code>s</code> Harfi</h4>

String type'ı (`str`) temsil eder. Örnek:
```py
print("{:s}".format("Bu bir string'dir.")) # Output: Bu bir string'dir.
```

<h4 id="2.2.1.2"><code>c</code> Harfi</h4>

`C` dil ailesindeki `char` data type gibidir. Tek karakterleri (single characters) temsil eder. Integer'ları kabul eder, `"Falan filan"` gibi string'leri ve `"A"` gibi single character'leri kabul etmez. Aksi halde `ValueError: Unknown format code 'c' for object of type 'str'` hatası yükseltir. Decimal bir sayı girildiğinde, o sayıya karşılık gelen ASCII karakterini yazdırır. ASCII kodlama sistemini kullandığı için 255'den sonra aptal karakterler basmaya başlar. Örnek:
```py
print("{:c}".format(65))  # Output: A
print("{:c}".format(666)) # Output: ʚ
```

<h4 id="2.2.1.3"><code>d</code> Harfi</h4>

Integer (`int`) type'ı temsil eder. Örnek:
```py
print("{:d}".format(1)) # Output: 1
```
Sağa sola yaslama işleminde oluşan boşlukları `0` ile doldurabilir ya da string'in belli bir kısmını alabilir ya da ikisini de aynı anda yapabilirsiniz. Örnek:
```py
print("'{:<15}'" .format("123456789"))    # Output: '123456789      '
print("'{:<015}'" .format("123456789"))   # Output: '123456789000000'
print("'{:<15.5}'" .format("123456789"))  # Output: '12345          '
print("'{:<015.5}'" .format("123456789")) # Output: '123450000000000'

print("'{:>15}'" .format("123456789"))    # Output: '      123456789'
print("'{:>015}'" .format("123456789"))   # Output: '000000123456789'
print("'{:>15.5}'" .format("123456789"))  # Output: '          12345'
print("'{:>015.5}'" .format("123456789")) # Output: '000000000012345'

print("'{:^15}'" .format("123456789"))    # Output: '   123456789   '
print("'{:^015}'" .format("123456789"))   # Output: '000123456789000'
print("'{:^15.5}'" .format("123456789"))  # Output: '     12345     '
print("'{:^015.5}'" .format("123456789")) # Output: '000001234500000'
```
Gördüğünüz gibi bütün boşlukları `0` ile doldurmak için `{:0xd}` formatını kullanıyoruz. Bu formattaki `x` yerine girdiğiniz sayıdan önce bir adet `0` koyarsanız, bütün boşluklar sıfır ile doldurulur. Ayrıca `{:x.yd}` formatını kullanarak string'in baştan (soldan)`y` uzunluğundaki kısmını alabilirsiniz.

<h4 id="2.2.1.3"><code>o</code> Harfi</h4>

Octal sayıları temsil eder. Decimal sayıları octal sayılara dönüştürür. Örnek:
```py
print("{:d} decimal == {:o} octal".format(10, 10)) # Output: 10 decimal == 12 octal
```

<h4 id="2.2.1.4"><code>x</code>/<code>X</code> Harfi</h4>

Hexadecimal sayıları temsil eder. `x` ve `X` kullanmak arasındaki tek fark, hexadecimal sayı sisteminde kullanılan harfların küçük ya da büyük olmasıdır. Örnek:
```py
print("{:d} decimal == {:x} octal".format(10, 10)) # Output: 10 decimal == a octal
print("{:d} decimal == {:X} octal".format(10, 10)) # Output: 10 decimal == A octal
```

<h4 id="2.2.1.5"><code>b</code> Harfi</h4>

Binary sayıları temsil eder. Decimal sayıları binary sayılara dönüştürür. Örnek:
```py
print("{:d} decimal == {:b} binary".format(10, 10)) # Output: 10 decimal == 1010 binary
```

<h4 id="2.2.1.6"><code>f</code> Harfi</h4>

Float (`float`) type'ı temsil. Virgülden sonra kaç basamağını istediğimizi belirleyebilmemize olanak tanır. Örnek:
```py
print("{}".format(50.25463)) # Output: 50.25463
print("{:.2f}".format(50)) # Output: 50.00
print("{:.2f}".format(50.25463)) # Output: 50.25
```

<h4 id="2.2.1.7">Basamak Ayracı (<code>,</code>)</h4>

Decimal sayıların basamaklarını ayırmak için kullanılabilir. Örnek:
```py
print("{:,}".format(1234567890)) # Output: 1,234,567,890
print("{:,}".format(1234567890.123456789)) # Output: 1,234,567,890.1234567
```

<h2 id="2.3">f-string</h2>

**f-string** yapısı Python'un 3.6 sürümünde eklenmiştir. String oluşturmak için kullanılan tırnak işaretinin başına `f` ya da `F` koyarak f-string formatını kullanabilirsiniz. `format()` methoduna benzer çalışır.
```py
yaş = 27
isim = "Python"
print(f"Selam ben {isim}, {yaş} yaşındayım.") # Output: Selam ben Python, 27 yaşındayım.
```

<h1 id="3">String Methodları</h1>

<h2 id="3.1"><code>replace(old, new, count)</code> Methodu</h2>

`old` parametresinde argüman olarak girilen string'i `new` parametresine argüman olarak girilen string ile değiştirir. `count` parametresine argüman girilmezse, o string'deki uyuşan bütün değerleri değiştirir. `count` parametresine argüman olarak integer bir değer girilirse, Python soldan sağa doğru `count` kadar ilgili değeri değiştirir. Örnek:
```py
var1 = "a a a a b b b b"
print(var1) # Output: a a a a b b b b

var1 = var1.replace("a", "A")
print(var1) # Output: A A A A b b b b

var1 = var1.replace("b", "B", 2)
print(var1) # Output: A A A A B B b b
```
Gördüğünüz gibi `replace` methodu ile ilgili string'de yaptığımız değişikliklerin kalıcı olmasını istiyorsanız, ilgili variable'ı yukarıdaki gibi yeniden tanımlamadın (redefinition) gerekmektedir.

<h2 id="3.2"><code>split(sep=" ", maxsplit)</code> Methodu</h2>

String'leri parçalarına ayırıp bir liste içinde döndürür. `sep` parametresine argüman olarak girilen string'i referans alarak soldan sağa doğru parçalama işlemini gerçekleştirir. `sep` parametresine argüman girilmezse default değeri olan boşluk karakterini (`" "`) referans alarak parçalama işlemi yapar. `maxsplit` parametresine argüman girilmezse, `sep` parametresine argüman olarak girilen string'i referans alarak bütün string'i parçalar. `maxsplit` parametresine argüman olarak integer bir değer girilirse, o değerde belirtilen kadar parçalama işlemi yapar. Örnek:
```py
metin = "abc abc abc abc"

print(metin.split()) # Output: ['abc', 'abc', 'abc', 'abc']
print(metin.split(maxsplit=2)) # Output: ['abc', 'abc', 'abc abc']
print(metin.split("b")) # Output: ['a', 'c a', 'c a', 'c a', 'c']
print(metin.split("b", 2)) # Output: ['a', 'c a', 'c abc abc']
```
`maxsplit` parametresinde belirtilen integer, `split` methodunun döndürdüğü listede bulunan virgül sayısına eşit, eleman sayısından bir eksiktir. Yani: `maxsplit = virgül sayısı = len(split methodunun döndürdüğü liste)-1`. `sep` parametresine girilen referans ilgili string'de yoksa, hiçbir işlem yapılmaz. Örnek:
```py
metin = "abc abc abc abc"

print(metin.split("d")) # Output: ['abc abc abc abc']
```

<h2 id="3.3"><code>rsplit(sep=" ", maxsplit)</code> Methodu</h2>

`split()` methodunun yaptığı işi sağdan sola doğru yapar. Örnek:
```py
metin = "abc abc abc abc"

print(metin.rsplit()) # Output: ['abc', 'abc', 'abc', 'abc']
print(metin.rsplit(maxsplit=2)) # Output: ['abc abc', 'abc', 'abc']
print(metin.rsplit("b")) # Output: ['a', 'c a', 'c a', 'c a', 'c']
print(metin.rsplit("b", 2)) # Output: ['abc abc a', 'c a', 'c']
print(metin.rsplit("d")) # Output: ['abc abc abc abc']
```

<h2 id="3.4"><code>splitlines(keepends)</code> Methodu</h2>

Karakter dizilerini satır satır (line) olarak parçalar. `keepends` parametresi boolean type değerleri kabul eder. `keepends` parametresine girilen argüman `True` boolean değerine sahipse `splitlines` methodu `\n` kaçış dizilerini de dahil eder, `False` ise etmez. Örnek:
```py
a = """Line1
Line2
Line3
Line4"""

print(a.splitlines(False)) # Output:['Line1', 'Line2', 'Line3', 'Line4'] 
print(a.splitlines(True)) # Output: ['Line1\n', 'Line2\n', 'Line3\n', 'Line4']

b = "Line1\nLine2\nLine3\nLine4"

print(b.splitlines(False)) # Output: ['Line1', 'Line2', 'Line3', 'Line4']
print(b.splitlines(True)) # Output: ['Line1\n', 'Line2\n', 'Line3\n', 'Line4']
```

<h2 id="3.5"><code>lower()</code> Methodu</h2>

String'in bütün karakterlerini küçük harf yapar. Örnek:
```py
exp = "SeLaMlArRrR"
print(exp.lower()) # Output: selamlarrrr
```
Türkçe karakterleri küçültürken hatalarla karşılaşabilirsiniz. Basit çözüm:
```py
iller = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"
print(iller.replace("I", "ı").replace("İ", "i").lower()) # Output: ısparta, adıyaman, diyarbakır, aydın, balıkesir, ağrı
```

<h2 id="3.6"><code>upper()</code> Methodu</h2>

String'in bütün karakterlerini büyük harf yapar. Örnek:
```py
exp = "SeLaMlArRrR"
print(exp.upper()) # Output: SELAMLARRRR
```
Türkçe karakterleri büyütürken hatalarla karşılaşabilirsiniz. Basit çözüm:
```py
iller = "ısparta, adıyaman, diyarbakır, aydın, balıkesir, ağrı"
print(iller.replace("i", "İ").upper()) # Output: ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI
```

<h2 id="3.7"><code>islower()</code> Methodu</h2>

Karakter dizisi tamamen küçük harflerden oluşuyorsa `True`, diğer durumlarda `False` döndürür.
```py
metin1="selamlar"
metin2="Selamlar"
print(metin1.islower()) # Output: True
print(metin2.islower()) # Output: False
```
<h2 id="3.8"><code>isupper()</code> Methodu</h2>

Karakter dizisi tamamen büyük harflerden oluşuyorsa `True`, diğer durumlarda `False` döndürür.
```py
metin1="SELAMLAR"
metin2="SELAMLAr"
print(metin1.isupper()) # Output: True
print(metin2.isupper()) # Output: False
```

<h2 id="3.9"><code>endswith(suffix, start, end)</code> Methodu</h2>

Uygulandığı string'in en son index'inden en baş index'ine doğru tarayarak, `suffix` parametresine argüman olarak girilen string'i ya da tuple içinde belirtilen stringleri arar ve bulursa `True`, bulamazsa `False` boolean değerini döndürür. `start` ve `end` parametreleri tanımlanırsa, bu parametrelere tanımlanan index'ler arasında tarama işlemi yapar. `start` parametresinde belirtilen index dahil edilirken, `end` parametresinde belirtilen index dahil edilmez. Örnek:
```py
metin1 = "abc i abc abc abc x"
metin2 = "abc j abc abc abc y"
metin3 = "abc k abc abc abc z"
print(metin1.endswith("x")) # Output: True
print(metin1.endswith("i", 0, 5), end="\n\n") # Output: True

for i in [metin1, metin2, metin3]:
    print(i.endswith(("x", "y", "z", "p")))
```
**Output:**
```
True
True

True
True
True
```
Gördüğünüz gibi `suffix` parametresine argüman olarak girilen tuple içinde belirtilen string'lerden herhangi birisi `endswith` methodunun uygulandığı string'in sonunda varsa `True` output'u verilir.

<h2 id="3.10"><code>startswith(prefix, start, end)</code> Methodu</h2>

`endswith` methodunun yaptığı işin aynısının, uygulandığı string'in başını kontrol eden versiyonudur. Örnek:
```py
metin1 = "x abc abc i abc abc"
metin2 = "y abc abc j abc abc"
metin3 = "z abc abc k abc abc"
print(metin1.startswith("x")) # Output: True
print(metin1.startswith("i", 10), end="\n\n") # Output: True

for i in [metin1, metin2, metin3]:
    print(i.startswith(("x", "y", "z", "p")))
```
**Output:**
```
True
True

True
True
True
```

<h2 id="3.11"><code>capitalize()</code> Methodu</h2>

Bir karakter dizisinin 0. index'indeki harf karakterini büyük harf karakterine çevirir. 0. index'indeki harf karakterinin üstünde `upper()` methodu uygulanmış gibi düşünebilirsiniz. Türkçe karakterlerde sıkıntı çıkarabilir. Örnekler:
```py
metin = "istisnalar kaideyi bozmaz."
print(metin.capitalize()) # Output: Istisnalar kaideyi bozmaz.
print(metin.replace("i", "İ").capitalize()) # Output: İsti̇snalar kai̇deyi̇ bozmaz.

metin = " istisnalar kaideyi bozmaz."
print(metin.capitalize()) # Output:  istisnalar kaideyi bozmaz.
```
```py
metin = "selam ben python."
print(metin.title()) # Output: Selam Ben Python.
```
Türkçe karakter sorununu çözmek için alternatif kod:
```py
metin = "on iki ada"

for kelime in metin.split():
	if kelime.startswith("i"):
		kelime = "İ" + kelime[1:]
	kelime = kelime.title()
	print(kelime, end=" ")
```
**Output:**
```
On İki Ada 
```

<h2 id="3.12"><code>swapcase()</code> Methodu</h2>

Karakter dizisi içindeki büyük harfleri küçük harfe, küçük harfleri de büyük harfe çevirir. Türkçe karakterlerde sıkıntı çıkabilir.
```py
metin = "SelaMLar"
print(metin.swapcase()) # Output: sELAmlAR

# Output: sELAmlAR
```
Türkçe sorununa alternatif çözüm:
```py
metin = "İllimünati"

temp_list = []
for i in metin:
    temp_list.append(i)

metin = ""
index_cal = 0
for i in temp_list:
    if i == "İ":
        temp_list[index_cal] = "i"
    elif i == "i":
        temp_list[index_cal] = "İ"
    else:
        temp_list[index_cal] = i.swapcase()
    metin = metin + temp_list[index_cal]
    index_cal += 1

print(metin) # Output: iLLİMÜNATİ
```

<h2 id="3.13"><code>casefold()</code> Methodu</h2>

`lower()` methodu ile aynı işi yapar. Tek farkı, başka dillerdeki harflerde farklı sonuçlar vermesidir. Örneğin Almanca'da ki `ß` harfi için `ss` sonucunu verir. Türkçe karakter sorunu vardır.

<h2 id="3.14"><code>strip(chars)</code> Methodu</h2>

Bir string'deki her line'ın başındaki ve sonundaki `chars` parametresine argğman olarak girilen string'i kırpmaya yarar. Default değer olarak boşluk karakteri `" "` alır. Bu method'un nasıl davranacağını kestirmek zordur. Bu yüzden kullanıldığında nasıl bir output vereceğini test etmek önem arz ediyor.
```py
metin = "   salamlar salamlar salamlar    " 
print(metin.strip(" "), end="\n\n")

metin = ".. salamlar .."
print(metin.strip(".. "), end="\n\n")
print(metin.strip(" .."), end="\n\n")

metin = ".. salamlar ..\n.. salamlar ..\n.. salamlar .."
print(metin.strip(".. "), end="\n\n")
print(metin.strip(" .."), end="\n\n")
```
**Output:**
```
salamlar salamlar salamlar

salamlar

salamlar

salamlar ..
.. salamlar ..
.. salamlar

salamlar ..
.. salamlar ..
.. salamlar
```

<h2 id="3.15"><code>lstrip("string")</code> Methodu</h2>

`strip("string")`'den tek farkı, sadece soldaki kısmı kırpar.

<h2 id="3.16"><code>rstrip("string")</code> Methodu</h2>

`strip("string")`'den tek farkı, sadece sağdaki kısmı kırpar

<h2 id="3.17"><code>join(iterable)</code> Methodu</h2>

Uygulandığı string'i, `iterable` parametresine girilen iterable objelerin (`list`, `tuple`, `set` ...) elemanları arasına ekleyerek bir string oluşturur ve döndürür. Örnek:
```py
m1 = ["1","2","3"]
m2 = ("1","2","3")
m3 = {"1","2","3"}
print("--".join(m1)) # Output: 1--2--3
print("--".join(m2)) # Output: 1--2--3
print("--".join(m3)) # Output: 1--3--2 (rastgele olmasının sebebi set'in bir özelliği)
```

<h2 id="3.18"><code>count(x, start, end)</code> Methodu</h2>

`x` parametresine argüman olarak girilen string'in, uygulandığı string'in içinde kaç defa geçtiğini söyler. `start` ve `end` parametrelerine başlama ve bitiş index'lerini girerek string içerisinde belli bir bölümü kontrol edebilirsiniz. Örnek:
```py
metin="Kahramanmaraş"
print(metin.count("a")) # Output: 5
```

<h2 id="3.19"><code>index(sub, start, end)</code> Methodu</h2>

`sub` parametresine argüman olarak girilen string'in, uygulandığı string'in içinde soldan sağa doğru arar ve ilk kaçıncı index'de olduğunu söyler. `sub` parametresine argüman olarak birden fazla karakterden oluşan string girilirse, soldan sağa doğru arar ve o string'in ilk karakterinin geçtiği index'i söyler. `start` ve `end` parametrelerine başlama ve bitiş index'lerini girerek string içerisinde belli bir bölümü kontrol edebilirsiniz. Örnek:
```py
metin = "abc abc abcd abc abc abcd abc abc"
print(metin.index("d")) # Output: 11
print(metin.index("abcd")) # Output: 8 (a karakteri ilk 8. index'te bulunmuş)
```
İstenilen string bulunamazsa `ValueError` hatası yükseltilir. Örnek:
```py
metin = "abc abc abcd abc abc abcd abc abc"
print(metin.index("x")) # ValueError: substring not found
```

<h2 id="3.20"><code>rindex(sub, start, end)</code> Methodu</h2>

`index()` methodunun yaptığı işi sağdan sola yapar. Örnek:
```py
metin = "abc abc abcd abc abc abcd abc abc"
print(metin.rindex("d")) # Output: 24
print(metin.rindex("abcd")) # Output: 21 (a karakteri ilk 21. index'te bulunmuş)
print(metin.rindex("x")) # ValueError: substring not found
```

<h2 id="3.21"><code>find(sub, start, end)</code> Methodu</h2>

`index()` methodunun yaptığı işi yapar. Tek farkı, istenilen string bulunamazsa `ValueError` hatası yükseltmek yerine yerine `-1` output'unu döndürür. Örnek:
```py
metin = "abc abc abcd abc abc abcd abc abc"
print(metin.find("d")) # Output: 11
print(metin.find("abcd")) # Output: 8 (a karakteri ilk 8. index'te bulunmuş)
print(metin.find("x")) # Output: -1
```

<h2 id="3.22"><code>rfind(sub, start, end)</code> Methodu</h2>

`find()` methodunun sağdan sola versiyonudur. Örnek:
```py
metin = "abc abc abcd abc abc abcd abc abc"
print(metin.rfind("d")) # Output: 24
print(metin.rfind("abcd")) # Output: 21 (a karakteri ilk 21. index'te bulunmuş)
print(metin.rfind("x")) # Output: -1
```

<h2 id="3.23"><code>center(width, fillchar)</code> Methodu</h2>

Uygulandığı string'i, `width` parametresine girilen argüman kadar ortalar. Ortalama işleminde oluşan boşlukları `fillchar` parametresine argüman olarak girilen string'ler ile doldurur. `fillchar` parametresinin default değeri boşluk karakteridir (`" "`). Örnek:
```py
print("1234".center(4,"-")) # Output: 1234
print("1234".center(5,"-")) # Output: -1234
print("1234".center(6,"-")) # Output: -1234-

print("12345".center(5,"-")) # Output: 12345
print("12345".center(6,"-")) # Output: 12345-
print("12345".center(7,"-")) # Output: -12345-
```
Ortalama işleminde `fillchar` parametresine argüman olarak girilen string'in düzgünce kullanılabilmesi için `width` parametresinde belirtilen sayının, `center` methodunun uygulandığı string'in uzunluğundan en az 2 fazla olması gerekmektedir. Örnek:
```py
for i in range(1,11,2):
	print("1".center(i,"-"), f"({i})")

print()

for i in range(0,11,2):
	print("12".center(i,"-"), f"({i})")

print()

for i in range(1,11,2):
	print("12345".center(i,"-"), f"({i})")

print()

for i in range(0,11,2):
	print("123456".center(i,"-"), f"({i})")
```
**Output:**
```
1 (1)
-1- (3)
--1-- (5)
---1--- (7)
----1---- (9)

12 (0)
12 (2)
-12- (4)
--12-- (6)
---12--- (8)
----12---- (10)

12345 (1)
12345 (3)
12345 (5)
-12345- (7)
--12345-- (9)

123456 (0)
123456 (2)
123456 (4)
123456 (6)
-123456- (8)
--123456-- (10)
```

<h2 id="3.24"><code>rjust(width, fillchar)</code> Methodu</h2>

`center()` methoduna benzer çalışır. Tek farkı uygulandığı string'i ortalamaz, sağa yaslar. `fillchar` parametresinin default değeri boşluk karakteridir (`" "`). Örnek:
```py
for i in range(1,11,2):
	print("1".rjust(i,"-"), f"({i})")

print()

for i in range(0,11,2):
	print("123456".rjust(i,"-"), f"({i})")
```
**Output:**
```
1 (1)
--1 (3)
----1 (5)
------1 (7)
--------1 (9)

123456 (0)
123456 (2)
123456 (4)
123456 (6)
--123456 (8)
----123456 (10)
```

<h2 id="3.25"><code>ljust(width, fillchar)</code> Methodu</h2>

`center()` methoduna benzer çalışır. Tek farkı uygulandığı string'i ortalamaz, sola yaslar. `fillchar` parametresinin default değeri boşluk karakteridir (`" "`). Örnek:
```py
for i in range(1,11,2):
	print("1".ljust(i,"-"), f"({i})")

print()

for i in range(0,11,2):
	print("123456".ljust(i,"-"), f"({i})")
```
**Output:**
```
1 (1)
1-- (3)
1---- (5)
1------ (7)
1-------- (9)

123456 (0)
123456 (2)
123456 (4)
123456 (6)
123456-- (8)
123456---- (10)
```

<h2 id="3.26"><code>zfill(width)</code> Methodu</h2>

Uygulandığı string'in soluna `width` parametresine argüman olarak girilen integer kadar sıfır (`0`) ekler. Sıfırların gözükebilmesi için `width` parametresine argüman olarak girilen integer, `zfill` methodunun uygulandığı string'in uzunluğundan en az 2 fazla olması gerekmektedir. Örnek:
```py
print("1".zfill(3))   # Output: 001
print("123".zfill(3)) # Output: 123
print("123".zfill(5)) # Output: 00123
```
Uygulandığı string'in en solunda `+` ya da `-` karakterleri varsa, `zfill` methodu bunu algılar ve sıfırları `+`/`-` karakterlerinden sonra koyar. Örnek:
```py
print("-290".zfill(8)) # Output: -0000290
print("+290".zfill(8)) # Output: +0000290
print("--random+text".zfill(20)) # Output: -0000000-random+text
```

<h2 id="3.27"><code>partition(sep)</code> Methodu</h2>

`sep` parametresine argüman olarak girilen string'i referans alarak, uygulandığı string'i soldan sağa doğru okur ve referansa uyan ilk yerden üçe böler. Sonucu list type olarak döndürür. Örnek:
```py
print("İstanbul".partition("an")) # Output: ('ist', 'an', 'bul')
```
`sep` parametresine argüman olarak girilen string, uygulandığı string'de yoksa aşağıdaki gibi bir output verir:
```py
print("İstanbul".partition("fil")) # Output: ('İstanbul', '', '')
```

<h2 id="3.28"><code>partition(sep)</code> Methodu</h2>

`partition()` methodunun yaptığı işi sağdan sola yapar. Örnek:
```py
print("İstanbul".partition("an")) # Output: ('ist', 'an', 'bul')
print("İstanbul".partition("fil")) # Output: ('İstanbul', '', '')
```

<h2 id="3.29"><code>encode(encoding='UTF-8',errors='strict')</code> Methodu</h2>

Uygulandığı string'i istenilen kodlama sistemine göre kodlamamıza imkan tanır. `encoding` parametresine argüman olarak istediğiniz kodlama sistemini girersiniz. `errors` parametresine gireceğiniz argümanla, `encoding` parametresine argüman olarak girdiğiniz kod çözücünün `encode` methodunun uygulandığı string'i çözemediği durumda Python'un nasıl davranması gerektiğini belirleyebilirsiniz. `errors` parametresine girebileceğiniz argümanlara [buradan](bu md dosyasında "`str()` Fonksiyonu" başlığında) ulaşabilirsiniz. `encode` methodu output'larını `bytes` formatında verir. Örnek:
```py
print("çilek".encode("ascii", "replace")) # Output: b'?ilek'
print("çilek".encode("utf-8")) # Output: b'\xc3\xa7ilek'
```

<h2 id="3.30"><code>expandtabs(tabsize)</code> Methodu</h2>

Uygulandığı string'in içeriğindeki TAB (`\t`) kaçış dizisinin kaç space (boşluk) genişliğinde olacağını `tabsize` parametresine girilen integer argümanla belirleyebiliriz.
```py
print("elma\tbir\tmeyvedir.".expandtabs(10)) # Output: elma      bir       meyvedir.
```

<h2 id="3.31"><code>maketrans(x, y, z)</code> Methodu</h2>

Dictionary oluşturmak için kullanılır. Sadece `x` parametresini kullanacaksanız, bu parametreye bir dictionary tanımlamak zorundasınız. Bu dictionary'nin key'leri 1 uzunluğunda olmak zorudadır. Aksi halde `ValueError: string keys in translate table must be of length 1` hatası yükseltilir. Value'larında böyle bir kısıtlama yoktur. Örnek:
```py
dict_exp = {"a": 1, "b": 2, "c": 3}
print(str.maketrans(dict_exp)) # Output: {97: 1, 98: 2, 99: 3}

dict_exp = {"1": 1, "2": 2, "3": 3}
print(str.maketrans(dict_exp)) # Output: {49: 1, 50: 2, 51: 3}

dict_exp = {"a": "a harfi", "b": "b harfi", "c": "c harfi"}
print(str.maketrans(dict_exp)) # Output: {97: 'a harfi', 98: 'b harfi', 99: 'c harfi'}
```

`x` ve `y` parametrelerini kullanacaksanız, bu parametrelere argüman olarak string girmelisiniz. `maketrans` methodu, `x` ve `y` parametrelerine argüman olarak girilen string'leri indexleyip birbiri ile eşleştirdiği bir dictionary döndürür. Örnek:
```py
print(str.maketrans("abc", "123")) # Output: {97: 49, 98: 50, 99: 51}
```
`maketrans` methodu, yukarıda da gördüğünüz gibi harf ve sayı gibi karakterlerin UNICODE tablosundaki decimal karşılıklarını kullanır. Kanıtı:
```py
d1 = str.maketrans("abc", "123")

for i in d1:
    print(f"{chr(i)}: {chr(d1[i])}", end=", ")
```
**Output:**
```
a: 1, b: 2, c: 3, 
```
Burada kullanılan `chr()` build-in fonksiyonu, kendisine argüman olarak verilen UNICODE karakterlerin decimal karşılıklarını alır ve karakter karşılıklarını döndürür.

`x`, `y` ve `z` parametrelerini kullanacaksanız, bu parametrelere argüman olarak string girmelisiniz. `maketrans` methodu, `x`, `y` ve `z` parametrelerine argüman olarak girilen string'leri indexler, `x` ve `y`'yi birbiri ile eşleştirdikten sonra `z`'nin index'lerinin key, value'larının `None` oladuğu bir dictionary döndürür. Örnek:
```py
print(str.maketrans("abc", "123", "dfe")) # Output: {97: 49, 98: 50, 99: 51, 100: None, 102: None, 101: None}
```

<h2 id="3.32"><code>translate(table)</code> Methodu</h2>

Uygulandığı string'i, `table` parametresinde belirtilen dictionary'e göre düzenler. `table` parametresinde argüman olarak girilen dictionary, `maketrans()` methodu ile oluşturulan dictionary'lerin formatında olmalıdır. Yani UNICODE karakterlerin decimal karşılıklarından oluşmalıdır. Örnek:
```py
büyük_harfler = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
küçük_harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
bk= str.maketrans(büyük_harfler,küçük_harfler)
kb= str.maketrans(küçük_harfler,büyük_harfler)

print("SeLamLar BeN PytHoN".translate(bk)) # Output: selamlar ben python
print("SeLamLar BeN PytHoN".translate(kb)) # Output: SELAMLAR BEN PYTHON
```

`table` parametresinde argüman olarak girilen dictionary'de, `translate` methodunun uygulandığı string'in içeriğinde bulunan bir karakter tanımlı değilse, `translate` methodu o karaktere müdahele etmez.
```py
büyük_harfler = "ABC"
küçük_harfler = "abc"
bk= str.maketrans(büyük_harfler,küçük_harfler)
kb= str.maketrans(küçük_harfler,büyük_harfler)

print("aBCd".translate(bk)) # Output: abcd
print("aBCD".translate(kb)) # Output: ABCD
```

<h2 id="3.33"><code>isalpha()</code> Methodu</h2>

Bir string yalnızca alfabe harflerinden oluşuyorsa (a, b, c, ...), o string için **alfabetik** denir. `isalpha` methodu, uygulandığı string'in alfabetik olup olmadığını kontrol eder. Alfabetik ise `True`, aksi durumlarda `False` döndürür. Örnek:
```py
print("abcd".isalpha()) # Output: True
print("abcd1".isalpha()) # Output: False
print("abcd?".isalpha()) # Output: False
```

<h2 id="3.34"><code>isnumeric()</code> Methodu</h2>

**Numeric**, sayısal demektir. Bir string, alfabe harfleri ve `<!+$` gibi özel karakterler dışında rakamlar (digits), fraction (`/` kesir. Örnek: `½`), roma rakamları ve currency numerators (`$`, `€`, `₺` gibi para birimi işaretleri), superscript'ler (alt sayı) ve subscript'lerden (üst sayı) oluşuyorsa, o string için numeric denir. `isnumeric` methodu, uygulandığı string'in numeric olup olmadığını sorgular. Numeric ise `True`, aksi durumlarda `False` döndürür. Örnek:
```py
print("abcd".isnumeric()) # Output: False
print("1234!".isnumeric()) # Output: False
print("1234".isnumeric()) # Output: True 
print("½".isnumeric()) # Output: True 
print("½".isnumeric()) # Output: True 
print("½".isnumeric()) # Output: True 
print("2²".isnumeric()) # Output: True 
```

<h2 id="3.35"><code>isalnum()</code> Methodu</h2>

integer, float ve complex type sayılara **Numeric** denir. Hem numeric hem alfabetik karakterleri içeren karakter dizilerine **alfanumeric** denir. `isalnum` methodu, uygulandığı string'in numeric ya da alfabetik ya da alfanumeric olup olmadığını sorgular. `<!+$` gibi özel karakterler numeric ya da alfabetik olmadığı için alfanumeric kategorisine girmez. Örnek:
```py
print("12345".isalnum()) # Output: True
print("12345a".isalnum()) # Output: True
print("12345½".isalnum()) # Output: True
print("12345$".isalnum()) # Output: False
```

<h2 id="3.36"><code>isdigit()</code> Methodu</h2>

**Digit**, rakam demektir. Bir string, rakamlardan (1, 2, 3, 4, 5, 6, 7, 8, 9, 0), superscript'lerden veya subscript'lerden oluşuyorsa, o string için digits denir. `isdigit` methodu, uygulandığı string'in digits olup olmadığını sorgular. Digits ise `True`, aksi durumlarda `False` döndürür. UNICODE'daki fraction (`/` kesir. Örnek: `½`), roma rakamları ve currency numerators (`$`, `€`, `₺` gibi para birimi işaretleri) digits olarak kabul edilmez.
```py
print("12345".isdigit()) # Output: True
print("2²".isdigit()) # Output: True
print("12345a".isdigit()) # Output: False
print("12345½".isdigit()) # Output: False
print("12345$".isdigit()) # Output: False
```

<h2 id="3.37"><code>isdecimal()</code> Methodu</h2>

**Decimal**, ondalıklı sayı demektir. Bir string, alfabe harfleri, `<!+$` gibi özel karakterler, fraction (`/` kesir. Örnek: `½`), roma rakamları ve currency numerators (`$`, `€`, `₺` gibi para birimi işaretleri), superscript'ler (alt sayı) ve subscript'ler (üst sayı) dışında rakamlardan oluşuyorsa, o string için numeric denir. Örnek:
```py
print("12345".isdecimal()) # Output: True
print("2²".isdecimal()) # Output: False
print("12345a".isdecimal()) # Output: False
print("12345½".isdecimal()) # Output: False
print("12345$".isdecimal()) # Output: False
```

<h2 id="3.38"><code>isidentifier()</code> Methodu</h2>

Bir string'in identifier kurallarına uygunluğunu denetler. Uygunsa `True`, aksi durumlarda `False` döndürür. Örnek:
```py
print("1vrb".isidentifier())   # Output: False
print("vr b".isidentifier())   # Output: False
print("vr:b".isidentifier())   # Output: False
print("vrb".isidentifier())    # Output: True
```
Keyword'ler identifier olarak kullanılamaz ama `isidentifier()` methodu bunu denetleyemez.
```py
print("global".isidentifier()) # Output: True
```

<h2 id="3.39"><code>isspace()</code> Methodu</h2>

Uygulandığı string'in tamamen space (`" "`) karakterinden oluşup oluşmadığını denetler. String'in tamamen space (`" "`) karakterinden oluşuyorsa `True`, diğer durumlarda `False` döndürür. Örnek:
```py
print("     ".isspace()) # Output: True
print("  a  ".isspace()) # Output: False
```

<h2 id="3.40"><code>isprintable()</code> Methodu</h2>

Python'da `\n`, `\t`, `\r` gibi karakterlere **non-printing characters** (basılmayan karakter) denir. Bu fonksiyon, karakter dizisi içinde non-printing character olup olmadığını denetler. Non-printing characters varsa `False`, yoksa `True` döndürür.
```py
print("\n".isprintable()) # Output: False
print("  ".isprintable()) # Output: True
```