# Kaçış Dizisileri
Özel anlamları ve işlevleri olan işaretlerdir. ASCII'de tanımlanmıştır. ASCII tablosu:
<img src="https://i.ibb.co/k8GSbKw/ASCII.jpg" alt="ASCII" border="0">

## `\` İşareti
Bu işaret Python'a, kendinden sonra gelen terimi görmezden gelmesini söyler. Örneğin, `\'` ve `\"` gibi kullanımla tırnak işaretlerinin işlevlerini bloke edip string içinde kullanabiliriz.
```py
print("Bu \" ve bu \' tırnak işaretidir.")
print('İstanbul\'un insanları...')
print("Bu \\ backslash işaretidir.")
```
** Outputs:**
```
Bu " ve bu ' tırnak işaretidir.
İstanbul'un insanları...
Bu \ backslash işaretidir.
```
Çift tırnak kullanılan `print()` fonksiyonlarına çok uzun cümleler girerken, kullanıcının görüşünün dışına taşan karakter dizilerini bölmek için kaçış dizilerinden faydalanılabilir.
```py
print("Python 1990 yılında Guido Van Rossum tarafından geliştirilmeye başlanmış, oldukça güçlü ve yetenekli bir programlama dilidir. ")

print("Python 1990 yılında Guido Van Rossum \
tarafından geliştirilmeye başlanmış, oldukça \
güçlü ve yetenekli bir programlama dilidir. ")
```
## `\n` Satır Atlama
Bir alt satıra geçmek için kullanılır.
```py
print("Selam\nBen\n\nPython")
```
**Output:**
```
Selam
Ben

Python
```

## `\t` TAB
Kendinden sonra bir `TAB` boşluk bırakır. Bu boşluğun boyutu IDE'den IDE'ye farklılık gösterebilir. En genel kullanılan `TAB` boyutları 2 ya da 4 space (boşluk).
```
SıfırBoşluk
İkili  Boşluk
Dörtlü    Boşluk
```

## `\a` Alert
Bir adet '*bip*' sesi ya da alert mesajı üretir. Her işletim sisteminde çalışmadığı için tercih edilmeyen bir komuttur.

## `\r` Aynı Satırın Başı
Kendinden sonra gelen ifadeyi kesip, satır başındaki kelimenin üstüne yapıştırır. Yani `"Selamlar\rNaber"` karakter dizisindeki `Naber` karakter dizisi `Selamlar`'ın üstüne yazılıp `Naberlar` olur.
```py
print("garip Keloğlan.\rBir ")
# Output: Bir p Keloğlan.
```

## `\v` Düşey Sekme
```
düşey
	 sekme
```
şeklinde bir görüntü elde edilir ama her işletim sisteminde çalışmadığı için tercih edilmez.

## `\b` İmleç Kaydırma
Kendinden önceki harfi silip cümleye devam eder.
```py
print("google.com\b.tr") # Output: google.co.tr
print('google' , '\b.' , '\bcom') # google.com
```

## `\u` Küçük UNICODE
Karakterlerin UNICODE karşılıklarını yazdırmamızı sağlar. 4 karakterden oluşur.
```py
print("\u0130") # Output: İ
print("\u0070") # Output: P
```

## `\U` Büyük UNICODE
Karakterlerin UNICODE karşılıklarını yazdırmamızı sağlar. 8 karakterden oluşur.
```py
print("\U00000130") # Output: İ
print("\U00000070") # Output: P
```
## `\N` Uzun Ad
UNICODE sisteminde her karakterin tek ve benzersiz bir kod konumu olduğu gibi, tek ve benzersiz bir de uzun adı vardır. `\N` kaçış dizisi de bu uzun adları kullanarak, karşılık gelen değeri bize verir.
```py
print("\N{LATIN SMALL LETTER A}") # Output: a
print("\N{LATIN CAPITAL LETTER S WITH CEDILLA}") # Output: Ş
```
Bu uzun adlara ulaşmak için `unicodedata` modülünden yararlanabilirsiniz.
```py
import unicodedata
print(unicodedata.name('a'))
print(unicodedata.name('Ş'))
```
## `\x` Hexadecimal Karakter
Onaltılı (hexadecimal) sayma sistemindeki bir sayının karakter karşılığını gösterebilirsiniz. ASCII tablosundaki Hex kısmındaki ifadeler kullanılır.
```py
print("\x41") # Output: A
print("\x4E") # Output: N
```

## `\f` Sayfa Başı
Kendinden önceki ve sonraki ifadeleri farklı sayfalara yazdırır.
```py
f = open("deneme.txt", "w")
print("deneme\fdeneme", file=f)
f.close()
```
programını çalıştırdıktan sonra *deneme.txt* dosyasını *.docx* formatında çalıştırırsanız, deneme yazılarının farklı sayfalara yazdırıldığını görürsünüz. Günümüzde pek kullanılmaz.

## Etkisizleştirme `r`
`r` kaçış dizisi, karakter dizisi içinde geçen kaçış dizilerinin işlevlerini yerine getirmesine engel olarak, istediğimiz çıktıyı elde etmemizi sağlıyor.
```py
print("Kaçış dizisi: '\'")  # Output: Kaçış dizisi: ''
print(r"Kaçış dizisi: '\'") # Output: Kaçış dizisi: '\'
```
### Farklı Çözümler
Kaçış dizisinden sonra bir adet boşluk yerleştirmek:
```py
print("Kaçış dizisi: \ ")
# Output: Kaçış dizisi: \ 
```
Çift kaçış dizisi kullanmak:
```py
print("Kaçış dizisi: \\")
# Output: Kaçış dizisi: \ 
```
karakter dizilerini birbiri ile toplayıp, çift kaçış dizisi kullanmak:
```py
print("Kaçış dizisi: " + "\\")
# Output: Kaçış dizisi: \ 
```
karakter dizilerini farklı argüman olarak girip, çift kaçış dizisi kullanmak:
```py
print("Kaçış dizisi:", "\\")
# Output: Kaçış dizisi: \ 
```
karakter dizilerini birbirine ekleyip, çift kaçış dizisi kullanmak:
```py
print("Kaçış dizisi: " "\\")
# Output: Kaçış dizisi: \ 
```
