# Karakter dizileri
String'e karakter dizisi denilmektedir. Karakter dizisi karakterlerden oluştuğu gibi stringler de karakterlerden oluşmaktadır. Yani `"Ali"` string'i `A`, `l` ve `i` karakterlerinden oluşmaktadır. Bu yüzden string ile karakter dizisi aynı kavramdır. diyebiliriz.

** Stringleri manipüle etmenin tek yolu, yeni bir string oluşturmaktır.** Yani, karakter dizileri **değiştirilemeyen** veri tipleridir. Dolayısıyla eğer bir karakter dizisi üzerinde değişiklik yapmak istiyorsanız, o karakter dizisini baştan tanımlamalısınız.
```py
metin1="elma"
print(metin1, "id:", id(metin1))
metin1[0] = "E"
print(metin1, "id:", id(metin1))
```
Gördüğünüz gibi `metin1`'in herhangi bir index'ini doğrudan değiştiremezsiniz çünkü karakter dizileri (*string'ler*) doğrudan değiştirilemez.
```py
metin1="elma"
print(metin1, "id:", id(metin1))

metin1 = metin1.replace("e","E", 1)
print(metin1, "id:", id(metin1))

# Output:
elma id: 2116091741296
Elma id: 2116092045104
```
Gördüğünüz gibi `metin1`'i `replace` method'u ile değiştirilip tekrar `metin1`'e atanınca, `metin1`'in id'si değişiyor çünkü bir karakter dizisini (*string'i*) değiştirebilmek için yeniden tanımlamaktan başka çare yoktur. Bunun kanıtı:
```py
metin1="elma"
print(metin1, "id:", id(metin1))

metin1.replace("e","E", 1)
print(metin1, "id:", id(metin1))

# Output:
elma id: 2741499233392
elma id: 2741499233392
```
Gördüğünüz gibi `metin1`'i `replace` method'u ile değiştiriyoruz ama tekrardan `metin1`'e atamadığımız için `metin1`'in değeri değişmiyor. Çünkü daha önce de dediğimiz gibi bir karakter dizisi üzerinde değişiklik yapmak istiyorsanız, o karakter dizisini baştan tanımlamalısınız. `metin1`'in değerini değiştirdikten sonra bu değeri tekrardan `metin1`'e atamamızın nedeni de bu *"baştan tanımlama"* olayıdır.

## Karakter Dizisi Tanımlamak
**Tek Tırnak:**
```py
kd = 'Tek tırnak ile tanımlamak.'
```
**Çift Tırnak:**
```py
kd = "Tek tırnak ile tanımlamak."
```
**Üçlü Çift Tırnak:**
```py
kd = """
Tek
tırnak
ile
tanımlamak
"""
```
`İstanbul'un` gibi kelimelerde tek tırnak kullanmak zorunda kalabilir yada bir karakter dizisi içinde çift tırnak kullanmak zorunda kalabilirsiniz. Bu gibi durumlarda tırnak işaretlerindeki çeşitliliği kullanın. Örnek:
```py
"""İstanbul'un içinden bir dayı "Selam!" dedi."""
```

## String'lerde Index
Stringleri oluşturan karakterlerin her birinin string içindeki konumuna **index** denir. Index, soldan 0, 1, 2, 3; sağdan -1, -2, -3, -4 şeklinde sıralanmaktadır.
```py
a = "Merhaba"
print(a[3], a[-4], sep=", ")

#Output: h, h
```

## String Dilimleme
Bir string'i dilimlerken `str_exp[Başlama indeksi : bitiş indeksi : atlama değeri]` syntax'ı kullanılır. Örnekler:

Dördüncü indeksten başlar 10. indeksi dahil etmeden 10. indekse kadar alır.
```py
c = "Python Programlama Dili"
print(c[4:10])

# Output: on Pro
```
Başlangıç değeri belirtilmemişse en baştan başlayarak alır.
```py
c = "Python Programlama Dili"
print(c[:10])

# Output: Python Pro
```
Bitiş değeri belirtilmemişse en sonuna kadar alır.
```py
c = "Python Programlama Dili"
print(c[4:])

# Output: on Programlama Dili
```
İki değer de belirtilmemişse tüm string'i alır.
```py
c = "Python Programlama Dili"
print(c[:])

# Output: Python Programlama Dili
```
Son karaktere kadar alır.
```py
c = "Python Programlama Dili"
print(c[:-1])

# Output: Python Programlama Dil
```
Baştan sona 2 değer atlaya atlaya string'i alır.
```py
c = "Python Programlama Dili"
print(c[::2])

# Output: Pto rgalm ii
```
Dördüncü indeksten 12'nci indekse 3'er atlayarak string'i alır.
```py
c = "Python Programlama Dili"
print(c[4:12:3])

# Output: oPg
```
Baştan sona -1 atlayarak stringi alır. (String'i ters çevirme)
```py
c = "Python Programlama Dili"
print(c[::-1])

# Output: iliD amalmargorP nohtyP
```
## String Özellikleri
Stringlerde matematiksel işlem yapabilirsin:
```py
c1 = "Python "
c2 = "Programlama "
c3 = "Dili"

print(c1 + c2 + c3) # Output: Python Programlama Dili
print(c1 * 3)	    # Output: Python Python Python
```
Stringleri birlşetirme işlemlerine örnekler:
```py
print("Merhaba" + " Nasılsınız") # Output: Merhaba Nasılsınız
print("Merhaba" " Nasılsınız") # Output: Merhaba Nasılsınız
```
Bir stringin uzunluğunu ölçmek için `len()` fonksiyonunu kullanabilirsiniz.
```py
a = "Python"
print(len(a)) # Output: 6
```

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

## `reversed()` fonksiyonu
`reversed()` fonksiyonu, *[sequence protokolünü](https://www.google.com/search?client=opera-gx&q=what%20is%20sequence%20protocol%20in%20python&sourceid=opera&ie=UTF-8&oe=UTF-8)* destekleyen `tuple`, `string`, `list` ve `range` etc. type'ındaki objeleri ters çeviren bir fonksiyondur. **Sequance** dediğimiz şey basitçe, bir sonuca ulaşmak için kurulan algoritma olarak düşünebilirsiniz. Bu süreçte sonuca ulaşmak için başlıngıçta verilen durumu parçalara ayırmalı ve her parçayı ayrı ele almalısınız. Örneğin ekmek ve krem peynir durumlarından krem peynir sürülmüş ekmek sonucuna ulaşmak için ekmek ve krem peyniri teker teker ele almalısınız. Python'da da bu mantık geçerlidir. Herhangi bir `tuple`, `string`, `list` ve `range` etc. objesinden, bu objelerin reversed (ters) halini elde etmek için her parçayı ayrı değerlendirmelisiniz. Örnek:
```py
print(*reversed((1,2,3,4,5))) # Output: 5 4 3 2 1
print(*reversed("12345"))     # Output: 5 4 3 2 1
print(*reversed([1,2,3,4,5])) # Output: 5 4 3 2 1
print(*reversed(range(1,6)))  # Output: 5 4 3 2 1
```
Yıldızlı parametreler hakkında bilgi için [tıklayın](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/print_fonksiyonu/print.md#y%C4%B1ld%C4%B1zl%C4%B1-parametreler).

## `sorted()` fonksiyonu
Bir string veri tipini ögelerine parçalar ve bunları alfabetik olarak sıralar.
```py
print(sorted("kitap")) # list data type output verir.
print(*sorted("kitap"), sep="")

# Output:
# ['a', 'i', 'k', 'p', 't']
# aikpt
```
Ama bu sıralamayı yaparken Türkçe karakterler sıkıntı çıkarabilir. Türkçe karakter sorunun çözmek için:
```py
import locale
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254") # Windows için
locale.setlocale(locale.LC_ALL, "tr_TR") # GNU/Linux için
```
methodlarını kullanarak programın kullandığı encoding değerini değiştirebilirsin.
```py
import locale
locale.setlocale(locale.LC_ALL, "Turkish_Turkey.1254")
sorted("çiçek", key=locale.strxfrm)

# Output: ['ç', 'ç', 'e', 'i', 'k']
```
Bunu yaptıkran sonra bile sorunlar devam edebilir. Çünkü bazı durumlarda `İ` ve `ı` harfleri karışıklığa sebep oluyor. Bunun için kendi encoding standartımızı yazabiliriz. Örnek:
```py
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}
print(çevrim)
```
**Output:**
```
{'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9, 'ı': 10, 'i': 11, 'j': 12, 'k': 13, 'l': 14, 'm': 15, 'n': 16, 'o': 17, 'ö': 18, 'p': 19, 'r': 20, 's': 21, 'ş': 22, 't': 23, 'u': 24, 'ü': 25, 'v': 26, 'y': 27, 'z': 28}
```
Bu encoding standartını `sorted()` fonksiyonunda kullanabilirsiniz. Örnek:
```py
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}

print(sorted("afgdhkıi", key=çevrim.get))

# Output: ['a', 'd', 'f', 'g', 'h', 'ı', 'i', 'k']
```
Nested (iç içe) listelerde ilk elemana göre sıralar:
```py
elemanlar = [('ahmet',       33,    'karataş'),
             ('mehmet',      45,    'arpaçbahşiş'),
             ('sevda',       24,    'arsuz'),
             ('arzu',        40,    'siverek'),
             ('abdullah',    30,    'payas'),
             ('ilknur',      40,    'kilis'),
             ('abdurrezzak', 40,    'bolvadin')]

print(*sorted(elemanlar), sep='\n')
```
**Output:**
```
('abdullah', 30, 'payas')      
('abdurrezzak', 40, 'bolvadin')
('ahmet', 33, 'karataş')       
('arzu', 40, 'siverek')        
('ilknur', 40, 'kilis')        
('mehmet', 45, 'arpaçbahşiş')  
('sevda', 24, 'arsuz')
```
Yaşa göre sıralanması istenilirse:
```py
elemanlar = [('ahmet',       33,    'karataş'),
             ('mehmet',      45,    'arpaçbahşiş'),
             ('sevda',       24,    'arsuz'),
             ('arzu',        40,    'siverek'),
             ('abdullah',    30,    'payas'),
             ('ilknur',      40,    'kilis'),
             ('abdurrezzak', 40,    'bolvadin')]

def sırala(liste):
    return liste[1]
    
print(*sorted(elemanlar, key=sırala), sep='\n')
```
**Output:**
```
('sevda', 24, 'arsuz')
('abdullah', 30, 'payas')      
('ahmet', 33, 'karataş')       
('arzu', 40, 'siverek')        
('ilknur', 40, 'kilis')        
('abdurrezzak', 40, 'bolvadin')
('mehmet', 45, 'arpaçbahşiş')  
```
Aynı yaştakileri soy isme göre sıralaması istenirse:
```py
elemanlar = [('ahmet',       33,    'karataş'),
             ('mehmet',      45,    'arpaçbahşiş'),
             ('sevda',       24,    'arsuz'),
             ('arzu',        40,    'siverek'),
             ('abdullah',    30,    'payas'),
             ('ilknur',      40,    'kilis'),
             ('abdurrezzak', 40,    'bolvadin')]

def sırala(liste):
    return (liste[1], liste[2])

print(*sorted(elemanlar, key=sırala), sep='\n')
```
**Output:**
```
('sevda', 24, 'arsuz')
('abdullah', 30, 'payas')      
('ahmet', 33, 'karataş')       
('abdurrezzak', 40, 'bolvadin')
('ilknur', 40, 'kilis')        
('arzu', 40, 'siverek')        
('mehmet', 45, 'arpaçbahşiş')  
```

## `enumerate()` fonksiyonu
Nesneleri numalandırmanızı sağlar. Örnekler:
```py
print(enumerate("ornek"))

print(list(enumerate("ornek")))

enumerate_ornek = [i for i in enumerate('ornek')]
print(enumerate_ornek)

print(*enumerate('ornek'))
```
**Output:**
```
<enumerate object at 0x0000021883EE8DC0>
[(0, 'o'), (1, 'r'), (2, 'n'), (3, 'e'), (4, 'k')]
[(0, 'o'), (1, 'r'), (2, 'n'), (3, 'e'), (4, 'k')]
(0, 'o') (1, 'r') (2, 'n') (3, 'e') (4, 'k') 
```
`enumerate()` kullanarak da encoding standartı oluşturabilirsiniz. Örnek:
```py
# Daha sonra eklenecek.
```

# Karakter Dizisi Biçimlendirme

## `%` İşareti (Eski Yöntem)
Python'un **2.x** sürümlerinde kullanılan bir yöntemdir. Python'un **3.x** sürümlerinde de hala kaldırılmamış olsa bile `format` methodu kullanıldığı için `%` tercih edilmiyor. Ama eski sürümlerde kullanıldığı için eski kodları okurken karşımıza çıkacak. Bu yüzden öğrenmekte fayda var. Örnek syntax:
```py
print("%s ve %s iyi bir ikilidir!" %("Python", "Django"))
```
**Not:** Karakter dizisi içindeki `%s` işareti ile karakter dizisi dışındaki `%("Python", "Django")` içinde belirtilen elementlerin sayısı birbiri ile uyuşmasaydı, `TypeError` hata mesajı alırdınız. Yani:
```py
print("%s ve %s ve %s iyi bir üçlüdür!" %("Python", "Django"))
# Output: TypeError: not enough arguments for format string

print("%s iyi bir dildir!" %("Python", "Django"))
# Output: TypeError: not all arguments converted during string formatting
```
`%1, %2, ...` gibi outputlara ihtiyacınız varsa `%` işaretini `%%%` şeklinde kullanabilirsiniz. Bu sayede istenilen `%1, %2, ...` gibi outputlar elde edebilirsiniz. Ama `%%` şeklinde bir kullanımda `TypeError: not all arguments converted during string formatting` hatası alırsınız. Örnek:
```py
print("Yüzde bir: %%s" %(1))
# Output: TypeError: not all arguments converted during string formatting

print("Yüzde bir: %%%s" %(1))
# Output: Yüzde bir: %1
```
### Biçimlendirme
Stringleri sağa ya da sola yaslamak için:
```py
# Sağa Yaslamak
l1 = ["Abdullah", "Can", "Ayşe", "Abdülrezzak", "Alican"]
for i in l1:
	print("'%15s'" %(i))
```
**Output:**
```
'       Abdullah'
'            Can'
'           Ayşe'
'    Abdülrezzak'
'         Alican'
```
Yukarıdaki kodda, outputları sağa yaslamak için kullanılan format gösterilmiştir. `"'%15s'"` işlemi şu şekilde yorumlanıyor: Önce 15 karakterlik alan belirleniyor ve belirtilen karakter dizisi bu alanın en sağına yerleştiriliyor. Örneğin `"Can"` karakter dizisine bu işlemi uyguladıktan sonra elimizde sağa yaslanmış 3 karakter uzunluğunda bir `"Can"` ve 13 karakter uzunluğunda boşluk oluyor. Burada dikkat edilmesi gereken şey, `%15` şeklinde belirtilen uzunluktan daha uzun bir karakter dizisi varsa, o karakter dizisi manipüle edilemez. yani:
```py
l1 = ["Abdullah", "Can", "Ayşe", "Abdülrezzak", "Alican"]
for i in l1:
	print("%5s" %(i))
```
**Output:**
```
'Abdullah'
'  Can'
' Ayşe'
'Abdülrezzak'
'Alican'
```
Burada görüldüğü gibi 5'den kısa olan stringler için yaslama işlemi düzgün bir şekilde uygulanırken, 5'den uzun olan stringler için uygulanamaz. Bu yüzden, 5'den kısa olan `'  Can'` doğru output'u verirken, 5'den uzun olan `'Abdülrezzak'` doğru output'u vermez.

Aynı mantıkla karakter dizilerini sola yaslamak da mümkündür. Örnek:
```py
# Sola Yaslamak
l1 = ["Abdullah", "Can", "Ayşe", "Abdülrezzak", "Alican"]
for i in l1:
	print("%-15s" %(i))
```
**Output:**
```
'Abdullah       '
'Can            '
'Ayşe           '
'Abdülrezzak    '
'Alican         '
```
Aynı format değerini, karakter dizisi içerisinde birden fazla yerde kullanmak istediğinizde aynı şeyi teker teker belirtmek istemiyorsanız yapmanız gereken şey:
```py
print("""
%(isim)s'in arabası
%(isim)s'in parası
%(isim)s'in çocuğu
""" %{"isim": "Ahmet"})
```
**Output:**
```

Ahmet'in arabası
Ahmet'in parası
Ahmet'in çocuğu

```
Burada da gördüğünüz gibi elimizde `%(key)` ve `%{key: value}` syntax'ına sahip iki kod var. Bunları yukarıdaki kodda gösterildiği gibi kullanarak istenilen sonuca ulaşabilirsiniz. Bu `{key: value}` yapısına dictionary denir.

### Biçimlendirme Karakterler

#### `s` Harfi
String'i (karakter dizisini) temsil eder. 

#### `d` Karakteri
Integer (`int`) data type'ını temsil eder. `float` data type'ını `int`'e çevirir. Bu karakterde, sağa sola yaslama işleminde oluşan boşlukların istenilen kadarını `0` ile tamamlar. Örnek:
```py
print("'%10.5d'" %(23))
print("'%-10.5d'" %(23))
```
**Output:**
```
'     00023'
'00023     '
```
Bütün boşlukları `0` ile doldurmak için:
```py
print("'%010.d'" %23)

# Output: '0000000023'
```

#### `i` Harfi
Kullanım ve işlev olarak `d` Harfinden hiçbir farklı yoktur.

#### `o` Harfi
Octal sayıları temsil eder.
```py
print("%i sayısının sekizli düzendeki karşılığı %o sayısıdır." %(10, 10))

# Output: 10 sayısının sekizli düzendeki karşılığı 12 sayısıdır.
```

#### `x` ve `X`Harfi
Hexadecimal sayıları temsil eder.
```py
print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." %(20, 20))
print("%i sayısının onaltılı düzendeki karşılığı %X sayısıdır." %(20, 20))

# Output: 20 sayısının onaltılı düzendeki karşılığı 14 sayısıdır.
# Output: 20 sayısının onaltılı düzendeki karşılığı 14 sayısıdır.
```

#### `f` Harfi
`float`'ın kısaltmasıdır. virgülden sonra 6 karakterlik sıfır koyar (virgülden sonra sayılar varsa, kalan boşluklara sıfır ekler). Output'tan bu kısmı kaldırmak için şöyle yapabilirsin:
```py
print("'%f', '%f'" %(10, 10.354))

# Output: '10.000000', '10.354000'
```

#### `c` Harfi
`'a'` gibi tek bir karakteri kabul eder. `"deneme"` gibi karakter dizilerini kabul etmez. Decimal bir sayı girildiğinde, o sayıya karşılık gelen ASCII karakterini ekrana basar. 255'den sonra aptal karakterler basmaya başlar. Deneyin görün.

## `format()` methodu (Yeni Yöntem)
`format()` methodu, string data type'ın bir methodudur. Stringleri biçimlendirmek için kullanılır. Süslü parantez `{}` içine `format()` methoduna girilen değerler **soldan sağa sırasıyla** atanır. Örnek:
```py
print("{} ve {} iyi bir ikilidir!".format("Django", "Python"))

# Output: Django ve Python iyi bir ikilidir!
```
String veri tipine ait herhangi bir yapıda kullanılabilir Yani kafanızda `"Falan filan {}".format("Falan")` şeklinde kalmasın. String bir value'ya döndüren ya da string bir velue'ya barındıran herhangi bir objede kullanılabilir. Örneğin aşağıda, kendisine string bir data type atanmış bir variable üzerinde `format()` methodu kullanabiliyoruz. Python'un mantığı böyle işler.
```py
metin = "Selam {}."
print(metin.format("Ahmet")
```

### Değerleri planlı atama yönetmi
`format()` methodundaki elementleri, string içinde belirtilen index numaralarına göre atanır. Ayrıca indexleri birden fazla yere tanımlayabiliriz. Örnek:
```py
print("{0} {1}".format("Fırat", "Özgül"))
# Output: Fırat Özgül

print("{1} {0}".format("Fırat", "Özgül"))
# Output: Özgül Fırat

print("{0} {1} ({1} {0})".format("Fırat", "Özgül"))
# Output: Fırat Özgül (Özgül Fırat)
```

### Biçimlendirme yöntemleri
Eski string formatlama methodundaki biçimlendirme yöntemiyle aynı mantığa sahiptir. Aşağıdaki kodları tekrardan kısaca anlatmak gerekirse, `15` karakterlik alan belirler ve girilen string değeri bu alanın üstüne yazar. Duruma göre sağa sola yaslama veya ortalama işlemleri yapabilir.

Aşağıdaki kodda sağa yaslama işlemi aşağıda gösterilmiştir. `15` karakterlik alan yaratır ve bu alana 10 karakter uzunluğa sahip `0123456789` stringini koyunca, 10 karakterlik stringe ve 5 karakterlik boşluğa sahip şu output'u verir: `'0123456789     '`
```py
print("'{:<15}'" .format("0123456789"))
```
Aşağıdaki kodda sola yaslama işlemi aşağıda gösterilmiştir. `15` karakterlik alan yaratır ve bu alana 10 karakter uzunluğa sahip `0123456789` stringini koyunca, 10 karakterlik stringe ve 5 karakterlik boşluğa sahip şu output'u verir: `'     0123456789'`
```py
print("'{:>15}'" .format("0123456789"))
```
Aşağıdaki kodda ortalama işlemi aşağıda gösterilmiştir. `15` karakterlik alan yaratır ve bu alana 5 karakter uzunluğa sahip `01234` stringini koyunca, 5 karakterlik stringe ve 5'i sağda 5'i solda olmak üzere 10 karakterlik boşluğa sahip şu output'u verir: `'     01234     '`. Toplam boşluk karakteri tek sayıysa, sağdaki ve soldaki boşluk karakteri sayıları aynı olmaz.
```py
print("'{:^15}'".format("01234"))
```
Eski string formatlamada olduğu gibi yeni formatlama yöneteminde de belirtilen boşluk uzunluğu, stringin uzunluğundan az olursa sıkıntılar baş gösterir. Örnek:
```py
l1 = ["0123456789abcdefghjk", "0123456789abcde", "0123456789"]
for i in l1:
	print("'{:^10}'".format(i))
```
**Output:**
```
'0123456789abcdefghjk'
'0123456789abcde'
'0123456789'
```
Görüldüğü gibi ortalama işlemi istenildiği gibi olmadı çünkü ilk iki string 10 karakterden uzundu.

### Biçimlendirme Harfleri
`format()` methodunun `%` formatlama yöneteminden en önemli farklarından birisi, koda, `%` ile kullanılan harfin belirttiği data type dışında bir data type verirseniz, genellikle hata vermez ve tip dönüşümü yapmaya çalışır. Bu tip dönüşümleri bazen hatalı sonuç verebilir. Ama `format()` methodu buna izin vermez. Süslü parantez içinde belirtilen harfin dışında bir değer atanmaya çalışırsa python hata mesajı döndürür.
#### `s` Harfi
Bu harf sayesinde süslü parantez `{}` sadece string değerleri kabul eder. String dışındaki bir değer atanmaya çalışıldığında da python `ValueError` hatası verir. Örnek:
```py
print("{:s} ve {:s} iyi bir ikilidir!".format("Python", "Django"))
# Output: Python ve Django iyi bir ikilidir!

print("{:s} ve {:s} iyi bir ikilidir!".format("Python", 1))
# Output: ValueError: Unknown format code 's' for object of type 'int'
```

#### `c` Harfi
Bu harf, kendisine verilen decimal sayıların ASCII tablosundaki karşılıklarını döndürür. Örnek:
```py
print("{:c}".format(65)) # Output: "A"
```

#### `d` Harfi
Bu harf, sadece integer data type'ına sahip değerleri kabul eder. Örnek:
```py
print("{:d}" .format(65)) # Output: 65
```

#### `o` Harfi
Bu harf, decimal sayıları octal sayılara çevirir. Farklı sayı formatlarında hata vermez ama doğru sonuç verip vermediğinden emin olamadım. Örnek:
```py
print("{:o}" .format(10)) # Output: 12
```

#### `x` ve `X` Harfi
Bu harfler, decimal sayıları hexadecimal sayılara çevirir. Örnek:
```py
print("{:x}".format(65)) # Output: 41
print("{:X}".format(65)) # Output: 41
```

#### `b` Harfi
Bu harfler, decimal sayıları binary sayılara çevirir. Örnek:
```py
print("{:b}".format(2)) # Output: 10
```

#### `f` Harfi
Bu harf, floating point type sayıların virgülden sonra kaç basamağını istediğimizi belirleyebilmemize olanak tanır. Örnek:
```py
print("{:.2f}".format(50)) # Output: 50.00
print("{:.2f}".format(50.25463)) # Output: 50.25
```
Ayrıca basamak ayracı olarak da kullanılabilir. Örnek:
```py
print("{:,}".format(1234567890))
# Output: 1,234,567,890
```

## f-string
Python'un 3.6 sürümünde eklenmiştir.Bir string'in başına `f` ya da `F` harfi koyduğunuzda, o string artık bir **f-string** olur. `format()` methoduna benzer çalışır. Örnek:
```py
yaş = 10
isim = "Ali"
print(f"Selam ben {isim}, {yaş} yaşındayım.)

# Output: Selam ben Ali, 10 yaşındayım.
```

# Karakter Dizilerinin Methodları

## `replace("old str", "new str", değiştirme_adeti)`
`"old str"`'yi `"new str"` ile değiştirir. `değiştirme_adeti`'ni belirtmezseniz, ilgili bütün değerleri değiştirir; belirtirseniz, soldan sağa doğru belirtilen kadar değiştirir. Örnekler:
```py
metin = "Seleme"
metin = metin.replace("e", "E")
print(metin) # Output: SElEmE

metin = "Seleme"
metin = metin.replace("e", "E", 2)
print(metin) # Output: SElEme
```
Programınızda yeni değerin kullanılmasını istiyorsanız, yeni değeri ilgili variable'ye atamanız gerekmektedir. Yani:
```py
metin = "Seleme"
print(metin.replace("e", "E")) # Output: SElEmE
print(metin) # Output: Seleme

metin = "Seleme"
metin = metin.replace("e", "E")
print(metin) # Output: SElEmE
```

## `split(bölme_referansı, bölme_adeti)`
Stringleri parçalarına ayırıp bir liste şeklinde döndürür. `bölme_referansı` parametresi belirtilmezse, default değer olarak boşluk karakteri `" "` kullanır. Örnek:
```py
metin = "Selam ben Python"
metin = metin.split()
print(metin) # Output: ['Selam', 'ben', 'Python']
```
`bölme_referansı` belirtilirse, belirtilen string değerini referans alarak ayırma işlemi yapar. Örnek:
```py
metin = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
metin = metin.split(", ",3)
print(metin)
# Output: ['Bolvadin', 'Kilis', 'Siverek', 'İskenderun', 'İstanbul']
```
Girilen parametre değeri string içinde yer almıyorsa hiçbir işlem yapmaz ve stringi direkt liste içinde döndürür.
```py
metin = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
metin = metin.split(": ")
print(metin)
# Output: ['Bolvadin, Kilis, Siverek, İskenderun, İstanbul']
```
`bölme_adeti` parametresi belirtilmezse, `bölme_referansı` ile eşleşen bütün parçaları değerlendirir ama belirtilirse, belirtilen kadar parçayi işler ve kalan değerleri tek bir liste elemanı olarak verir. Örnek
```py
metin = "aaa00bbb00ccc00ddd00eee"
metin = metin.split("00")
print(metin)
# Output: ['aaa', 'bbb', 'ccc', 'ddd', 'eee']

metin = "aaa00bbb00ccc00ddd00eee"
metin = metin.split("00", 3)
print(metin)
# Output: ['aaa', 'bbb', 'ccc', 'ddd00eee']
```
Gördüğünüz gibi `bölme_adeti` parametresine `3` değerini verdiğimizde, `bölme_referansı` ile eşleşen 3 parçayı referans alarak bölme işlemi yaptı ve kalan `ddd00eee` kısmını da tek bir liste elemanı olarak ekledi. Buradaki `bölme_adeti` parametresinde belirtilen sayı, listedeki virgül sayısı birbirine eşit, liste elemanı sayısından da 1 eksiktir. Yani `bölme_adeti = virgül sayısı = len(metin)-1`

## `rsplit(bölme_referansı, bölme_adeti)`
`split()` ile aynı çalışır. Tek farkı, bölme işlemini soldan sağa değil, **sağdan sola** yapar.

## `splitlines(boolean_value)`
Karakter dizilerini satır satır ayırmak için kullanılır. Bu ayırma işlemini `\n` karakterini referans alarak yapar. Örnek:
```py
metin = """Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin
Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını
düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından
gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz
komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek
adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama
dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek
halini almıştır diyebiliriz."""

metin = metin.splitlines()
print(metin)
```
**Output:**
```
['Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı',
 "tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin",
 'Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını',
 'düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından',
 'gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz',
 "komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek",
 'adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama',
 'dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek',
 'halini almıştır diyebiliriz.']
```
Görüldüğü gibi, `\n` karakterini referans alarak her satırı ayrı ayrı alıp bir liste döndürdü. Burada dikkat çeken şey, bazı liste elemanları tek tırnak `' '` içinde gösterilirken bazılarının çift tırnak `" "` içinde gösterilmesi.  Bunu python otomatik ayarlıyor. Çünkü bazı liste elemanlarında `90'lı` veya `Python's` gibi karakter dizilerinde tek tırnak `'` kullanıldığı için python bu elemanı çift tırnak içinde gösterir. Örnek: `"komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek"`

`boolean_value` parametresi default olarak `False` değeri alır. `boolean_value` parametresi `True` değeri alırsa, döndürdüğü listenin her elemanındaki karakter dizisinin sonuna bir `\n` ekler. Örnek Output:
```
['Python programlama dili Guido Van Rossum adlı Hollandalı bir programcı\n',
 "tarafından 90'lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan, isminin\n",
 'Python olmasına bakarak, bu programlama dilinin, adını piton yılanından aldığını\n',
 'düşünür. Ancak zannedildiğinin aksine bu programlama dilinin adı piton yılanından\n',
 'gelmez. Guido Van Rossum bu programlama dilini, The Monty Python adlı bir İngiliz\n',
 "komedi grubunun, Monty Python's Flying Circus adlı gösterisinden esinlenerek\n",
 'adlandırmıştır. Ancak her ne kadar gerçek böyle olsa da, Python programlama\n',
 'dilinin pek çok yerde bir yılan figürü ile temsil edilmesi neredeyse bir gelenek\n',
 'halini almıştır diyebiliriz.']
```

## `lower()`
String'in bütün karakterlerini küçük harf yapar. Örnek:
```py
exp = "SeLaMlArRrR"
print(exp.lower()) # Output: selamlarrrr
```
Türkçe karakterleri küçültürken hatalarla karşılaşabilirsiniz. Basit çözüm:
```py
iller = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"
print(iller.replace("I", "ı").replace("İ", "i").lower())

# Output: ısparta, adıyaman, diyarbakır, aydın, balıkesir, ağrı
```
## `upper()`
String'in bütün karakterlerini büyük harf yapar. Örnek:
```py
exp = "SeLaMlArRrR"
print(exp.lower()) # Output: SELAMLARRRR
```
Türkçe karakterleri büyütürken hatalarla karşılaşabilirsiniz. Basit çözüm:
```py
iller = "ısparta, adıyaman, diyarbakır, aydın, balıkesir, ağrı"
print(iller.replace("i", "İ").upper())

# Output: ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI
```

## `islower()`
Karakter dizisi tamamen küçük harflerden oluşuyorsa `True`, diğer durumlarda `False` döndürür.
```py
metin1="selamlar"
metin2="Selamlar"
print(metin1.islower()) # Output: True
print(metin2.islower()) # Output: False
```
## `isupper()`
Karakter dizisi tamamen büyük harflerden oluşuyorsa `True`, diğer durumlarda `False` döndürür.
```py
metin1="SELAMLAR"
metin2="Selamlar"
print(metin1.islower()) # Output: True
print(metin2.islower()) # Output: False
```

## `endswith("string", başlangiç_değeri, bitiş_değeri)`
Karakter dizisinin sonu `"string"` parametresinde belirtilen string ile bitiyorsa `True`, diğer durumlarda `False` döndürür. Bu sorgulamayı, `başlangiç_değeri` ve `bitiş_değeri` parametrelerinde belirtilen indexler arasında yapar. Örnek:
```py
metin="Merhaba ben Python"
print(metin[2:-3])               # Output: rhaba ben P
print(metin.endswith("on",2,-3)) # Output: False
print(metin)				     # Output: Merhaba ben Python
print(metin.endswith("on"))      # Output: True
```

## `startswith("string", başlangiç_değeri, bitiş_değeri)`
Karakter dizisinin başı `"string"` parametresinde belirtilen string ile başlıyorsa `True`, diğer durumlarda `False` döndürür. Bu sorgulamayı, `başlangiç_değeri` ve `bitiş_değeri` parametrelerinde belirtilen indexler arasında yapar. Örnek:
```py
metin="Merhaba ben Python"
print(metin[1:4])                   # Output: erh
print(metin.startswith("Me", 1, 4)) # Output: False
print(metin)				        # Output: Merhaba ben Python
print(metin.startswith("Me"))       # Output: True
```

## `capitalize()`
Bir karakter dizisinin ilk karakterini büyük harfe çevirir. İlk karakterinin üstünde `upper()` methodu uygulanmuş gibi düşünebilirsiniz. Türkçe karakterlerde sıkıntı olabilir. Örnekler:
```py
metin = "istisnalar kaideyi bozmaz."
print(metin.capitalize())

# Output: Istisnalar kaideyi bozmaz.

metin = "istisnalar kaideyi bozmaz."
print(metin.replace("i", "İ").capitalize())

# Output: İsti̇snalar kai̇deyi̇ bozmaz.
```

## `title()`
Birden fazla kelimeden oluşan karakter dizilerinin her kelimesinin ilk harflerini büyütür. Türkçe karakterlerde sıkıntı çıkarabilir.
```py
metin = "selam ben python."
print(metin.title())
```
Türkçe karakter sorununu çözmek için alternatif kod:
```py
metin = "on iki ada"
  
for kelime in metin.split():
	if kelime.startswith("i"):
		kelime = "İ" + kelime[1:]
	kelime = kelime.title()
	print(kelime, end=" ")

# Output: On İki Ada
```

## `swapcase()`
Karakter dizisi içindeki büyük harfleri küçük harfe; küçük harfleri de büyük harfe dönüştürür. Türkçe karakterlerde sıkıntı çıkabilir.
```py
metin = "SelaMLar"
print(metin.swapcase())

# Output: sELAmlAR
```
Türkçe sorununa alternatif çözüm:
```py
metin = "istanbul"
  
for a in metin:
	if a == 'İ':
		metin = metin.replace('İ', 'i')
	elif a == 'i':
		metin = metin.replace('i', 'İ')
	else:
		metin = metin.replace(a, a.swapcase())
print(metin)

# Output: İSTANBUL
```

## `casefold()`
`lower()` methodu ile aynıdır. Tek farkı, başka dillerdeki harflerde farklı sonuçlar vermesi. Örneğin Almanca'da ki `ß` harfi için `ss` sonucunu veriyor. Türkçe karakter sorunu vardır.

## `strip("string")`
Bir karakter dizisindeki her satırın başındaki ve sonundaki `"string"` parametresine tanımlanan karakter dizisini kırpmaya yarar. Default değer olarak boş string `" "` ve kaçış dizilerini alır. Nasıl bir output vereceğini tahmin etmek zor. Bu yüzden kullanıldığında nasıl bir çıktı vereceğini test etmek önem arz ediyor.
```py
metin = ".. salamlar .."
metin = metin.strip(".. ")
print(metin) # Output: salamlar
```

## `lstrip("string")` ve `rstrip("string")`
`strip("string")`'den tek farkı, `lstrip("string")` sadece soldaki kısmı kırpar, `rstrip("string")` ise sadece sağdaki kısmı kırpar.

## `join("string")`
list, tuple ya da set içine tanımlanmış elementlerler arasına basılmasını istediğiniz şeyi `"string"` parametresine tanımlayarak kullandığınız bir methoddur. Örnek:
```py
m1 = ["1","2","3"]
m2 = ("1","2","3")
m3 = {"1","2","3"}
print("--".join(m1)) # Output: 1--2--3
print("--".join(m2)) # Output: 1--2--3
print("--".join(m3)) # Output: 1--3--2 (rastgele olmasının sebebi set'in bir özelliği)
```

## `count("string", Başlama_indeksi, Bitiş_indeksi)`
Bir karakter dizisi içinde belli bir karakterin kaç kez geçtiğini sorgular. Karakter dizisinin belli bir bölümünü sorgulamak için `Başlama_indeksi` ve `Bitiş_indeksi` parametrelerini kullanabilirsiniz.
```py
metin="Kahramanmaraş"
print(metin.count("a"))# Output: 5```
```

## `index("string", Başlama_indeksi, Bitiş_indeksi)`
Bir karakterin, bir karakter dizisi içinde ilk kaçıncı indexte bulunduğunu öğrenmek için kullanılır. parametre olarak bir kelime verirseniz, o kelimenin ilk harfinin kaçıncı indexte olduğunu verir. Örnek:
```py
metin = "selam ben python"
print(metin.index("ben"))

# Output: 6
```
Sorulan karakter o karakter dizisinde bulunmuyorsa `ValueError` hatası verir. Karakter dizisinin belli indexleri arasında arama yapmak için `Başlama_indeksi` ve `Bitiş_indeksi` parametrelerini kullanabilirsin.

## `rindex("string", Başlama_indeksi, Bitiş_indeksi)`
`index()` methodunun yaptığı işi **sağdan sola** yapar.

## `find("string", Başlama_indeksi, Bitiş_indeksi)`
`index()` methodunun yaptığı işi yapar. Tek farkı, `ValueError` döndürmek yerine `-1` output'unu verir.

## `rfind("string", Başlama_indeksi, Bitiş_indeksi)`
`find()` methodunun **sağdan sola** versiyonudur.

## `center(sayı, "string")`
Bir karakter dizisini ortalamaya yarar. `"string"` parametresinin default değeri boşluk `" "` karakteridir.
```py
for i in  range(1,11,2):
	print("S".center(i,"-"))
```
**Output:**
```
S
-S-
--S--
---S---
----S----
```
Burada dikkat edilmesi gereken şey, `range(1,11,2)` fonksiyonundan çıkan sayıların 1, 3, 5, 7, 9 olması. Buradan anlamamız gereken şey, `center()` methodu, `"string"` parametresine girilen değeri de işin içine katması. Örnek:
```py
for i in  range(1,11,2):
	print("Selam".center(i,"-"))
```
**Output:**
```
Selam
Selam
Selam
-Selam-
--Selam--
```
Gördüğünüz gibi `"string"` parametresinde belirtilen karakter dizisinin uzunluğuna göre ortalama işlemi yapılır.

## `rjust(sayı, "string")`
`center()` methoduna benzer çalışır. `center()` methodundan tek farkı, `"string"` karakterini, method olarak kullanıldığı string'in soluna `sayı` kadar ekleyerek, o string'i sağa yaslamış olması. Örnek:
```py
print("S".rjust(5,"-")
print("Sal".rjust(5,"-")
```
**Output:**
```
----S
--Sal
```

## `ljust(sayı, "string")`
`center()` methoduna benzer çalışır. `center()` methodundan tek farkı, `"string"` karakterini, method olarak kullanıldığı string'in sağına `sayı` kadar ekleyerek, o string'i sola yaslamış olması. Örnek:
```py
print("S".ljust(5,"-")
print("Sal".ljust(5,"-")
```
**Output:**
```
S----
Sal--
```

## `zfill(sayı)`
Method olarak kullanıldığı string'in soluna `sayı` kadar sıfır `0` ekler. Sadece string data type'ına sahip value'lerde method olarak kullanılabilir.
```py
print("S.zfill(5))
print("219".zfill(5))
```
**Output:**
```
0000S
00219
```
string'de `-` ya da `+` prefixleri varsa, bunları algılar ve output'un en soluna yerleştirir. Örnek:
```py
print("-290".zfill(8))
print("+290".zfill(8))
print("--random+text".zfill(20))
```
**Output:**
```
-0000290
+0000290
-0000000-random+text
```

## `partition("string")`
`"string"`'de belirtilen referansa göre bir karakter dizisini üçe böler. `"string"`'de belirtilen referansa ilk gördüğü yerden böler. Output'u tuple data type'ına sahiptir. Örnek:
```py
print("İstanbul".partition("an"))
# Output: ('ist', 'an', 'bul')
```
`"string"`'de belirtilen referans, method olarak kullanıldığı string içinde yoksa aşağıdaki gibi davranır:
```py
print("İstanbul".partition("fil"))
# Output: ('İstanbul', '', '')
```

## `rpartition("string")`
`partition()` ile aynı çalışır. Tek farkı, karakter dizisini, `"string"`'de belirtilen referansa ilk gördüğü yerden değil, son gördüğü yerden böler.
```py
print("Anakonanda".partition("na"))
# Output: ('A', 'na', 'konanda')

print("Anakonanda".rpartition("na"))
# Output: ('Anako', 'na', 'nda')
```
`"string"`'de belirtilen referans, method olarak kullanıldığı string içinde yoksa aşağıdaki gibi davranır:
```py
print("İstanbul".rpartition("fil"))
# Output: ('', '', 'İstanbul')
```

## `encode(encoding='UTF-8',errors='strict')`
Karakter dizisini istenilen kodlama sistemine göre kodlamamıza imkan tanır. `encoding` parametresinde istediğiniz kodlama sistemini seçersiniz. Bu değer default olarak `"UTF-8"`'e ayarlıdır. `errors` parametresinde, karakter dizisi `encoding`'de belirtilen kodlama sisteminde kodlanamazsa, python'un nasıl davranacağını belirlersiniz . Bu değer default olarak `"strict"`'e ayarlıdır. `errors` parametresine girilebilecek parametrelerin neler olduğunu ve ne anlama geldiklerini öğrenmek için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/kullanicidan_girdi_almak/tip_donusumleri.md#strobject-encodingutf-8-errorsstrict).
```py
print("çilek".encode("ascii", "replace"))
print("çilek".encode("utf-8"))
```
```
b'?ilek'
b'\xc3\xa7ilek'
```

## `expandtabs(tabsize)`
Bir karakter dizisinin içindeki TAB `\t` boşluklarını `tabsize` kadar genişletir.
```py
print("elma\tbir\tmeyvedir.".expandtabs(10))
#Output: elma      bir       meyvedir.
```

## `maketrans(x, y, z)`
Dictionary oluşturmak için kullanılır.

Sadece `x` parametresi kullanılacaksa, bu parametreye bir dictionary girmek zorunludur. 
```py
d1 = str.maketrans({"a": "a harfi", "b": "b harfi", "c": "c harfi"})
print(d1) # Output: {97: 'a harfi', 98: 'b harfi', 99: 'c harfi'}
```
`x` ve `y` parametreleri kullanılacaksa, bu parametrelere girilen string değerleri index'leyip, aynı index numarasına sahip olanları birbiri ile eşleştirerek bir dictionary oluşturur. Ama bu işlemin hatasız gerçekleşebilmesi için `x` ve `y` stringlerinin aynı uzunlukta olması gerekiyor. Aksi durumda `ValueError: the first two maketrans arguments must have equal length` hatası verir.
```py
d1 = str.maketrans("abc", "123")
print(d1)
```
`maketrans()` bir string methodu olduğu için ya `str.maketrans("abc", "123")` şeklinde kullanacaktık ya da ilk başta `d1 = str()` şeklinde bir tanımlama (definition) işlemi yapacaktır. Diğer türlü hata alırdık. Yukarıdaki kodda `"abc"` ve `"123"` stringlerinin indekslerini birbiri ile eşleştirip `{97: 49, 98: 50, 99: 51}` şeklinde bir dictionary döndürür. Buradaki sayılar, karakter dizisindeki karakterlerin UNICODE karşılıklarıdır. Bu sayıları tekrar karakterlere dönüştürmek için `chr()` fonksiyonunu kullanabilirsiniz. Bu fonksiyon, UNICODE karakterlere karşılık gelen sayıları tekrardan karaktere dönüştürmekte kullanılır. Örnek:
```py
print(chr(97))
# Output: a
```
`x`, `y` ve `z` parametreleri kullanılacaksa, `x` ve `y` parametreleri önceden anlatılan işlemlerden geçip bir dictionary oluşturur. Sonra `z` parametresine tanımlanmış string değer indexlenir ve value'leri `None` olacak şekilde mevcut dictionary'e eklenir. Örnek:
```py
m1 = "abc"
m2 = "123"
m3 = "dfe"
sonuc = str.maketrans(m1, m2, m3)
print(sonuc)
# Output: {97: 49, 98: 50, 99: 51, 100: None, 102: None, 101: None}
```

## `translate(maketrans_tablosu)`
`maketrans_tablosu` parametresine, `maketrans()` ile oluşturulan dictionary'lerin formatında bir dictionary tanımlandığında, method olarak kullanıldığı karakter dizisindeki her bir karakteri bu dictionary'e göre tekrardan oluşturur. Örnek
```py
m1 = "abc"
m2 = "123"
m2 = str.maketrans(m1,m2)
print(m2) # Output: {97: 49, 98: 50, 99: 51}

m1 = m1.translate(m2)
print(m1) # Output: 123
print(type(m1)) # Output: <class 'str'>
```
Dictionary'de tanımlanmamış karakterlerle karşılaşırsa hiçbir şey yapmaz. Örnek:
```py
m1 = "abc"
m2 = "ABC"
m2 = str.maketrans(m1,m2)
print("abcç".translate(m2))
# Output: ABCç
```

### Örnek Program
```py
büyük_harfler = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
küçük_harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
bk= str.maketrans(büyük_harfler,küçük_harfler)
kb= str.maketrans(küçük_harfler,büyük_harfler)
  
istek=input("Büyükten küçüğe mi küçükten to büyüğe mi? (bk or kb): ")
if istek=="bk":
	metin = input("Metin girin: ").translate(bk)
	print(metin)
elif istek=="kb":
	metin = input("Metin girin: ").translate(kb)
	print(metin)
else:
	print("Yanlış girdiniz. 'bk' ya da 'kb' dan birini giriniz. ")
```

## `isalpha()`
Eğer bir karakter dizisi içinde yalnızca alfabe harfleri *(a, b, c, ...)* varsa o karakter dizisi için **alfabetik** denir. Bu method, bir karakter dizisinin alfabetik olup olmadığını kontrol eder. Alfabetik ise `True`, diğer durumlarda `False` döndürür.

## `isdigit()`
**Numeric**, sayısal demektir. Bir karakter dizisinin **numeric** olup olmadığını kontrol eder. Numeric ise `True`, diğer durumlarda `False` döndürür. UNICODE'daki fraction (`/` kesir. Örnek: `½, 0.5`), roma rakamları ve currency numerators (para birimi işaretleri. $, € ₺ gibi) `digit` olarak kabul edilmediği için `False` döndürür. 

## `isalnum()`
Hem **numeric** hem **alfabetik** karakterleri içeren karakter dizilerine **alfanumeric** denir. Bir karakter **numeric** ya da **alfabetik** ya da **alfanumeric** karakterlerden oluşuyorsa `True`, `<!+$` gibi işaretler içeriyorsa `False` döndürür.

## `isdecimal()`
Karakter dizisi sadece doğal sayılar (0, 1, 2, 3, ...) içeriyorsa `True`, diğer durumlarda `False` döndürür.

## `isidentifier()`
Herhangi bir obje tanımlarken, o objeye verdiğiniz isme **identifier** denir. Bu işlemi yaparken belli başlı kurallar vardır (kurallar için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/temel_kavramlar/temel_kavramlar.md#i%CC%87simlendirme-kurallar%C4%B1)). `isidentifier()`, method olarak kullanıldığı karakter dizininde belirtilen identifier kurala uygun olup olmadığını kontrol eder. Uygunsa `True`, değilse `False` döndürür. Örnek:
```py
print("1vrb".isidentifier())   # Output: False
print("vr b".isidentifier())   # Output: False
print("vr:b".isidentifier())   # Output: False
print("vrb".isidentifier())    # Output: True
```
Keyword'ler identifier olarak kullanılamaz. `isidentifier()` bunu denetleyemediği için aşağıdaki kod `True` döndürür.
```py
print("global".isidentifier()) # Output: True
```

## `isnumeric()`
Bir karakter dizisinin **numeric** olup olmadığını kontrol eder. Numeric ise `True`, diğer durumlarda `False` döndürür. UNICODE'daki fraction (`/` kesir. Örnek: `½, 0.5`), roma rakamları ve currency numerators (para birimi işaretleri. $, € ₺ gibi) `numeric` olarak kabul edildiği için `True` döndürür. 

## `isspace()`
Karakter dizisinin tamamen boşluklardan oluşup oluşmadığını denetler. Karakter dizisi tamamen boşluklardan oluşuyorsa `True`, diğer durumlarda `False` döndürür.

## `isprintable()`
Python'da `\n`, `\t`, `\r` gibi karakterlere **non-printing characters** *(basılmayan karakter)* denir. Bu fonksiyon, karakter dizisi içinde non-printing characters olup olmadığını denetler. non-printing characters varsa `False`, yoksa `True` döndürür.
