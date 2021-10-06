# İçindekiler
- [Print-Input İşlemleri](#1)
- [`print()` Fonksiyonu](#2)
    - [`*values` Parametresi](#2.1)
    - [`sep` Parametresi](#2.2)
    - [`end` Parametresi](#2.3)
    - [`file` Parametresi](#2.4)
    - [`flush` Parametresi](#2.5)
- [`input()` Fonksiyonu](#3)

<h1 id="1">Print-Input İşlemleri</h1>

Programınıza girdi (input) almak için `input()`, çıktı (output) almak için `print()` adlı build-in fonksiyonlardan faydalanılır.

<h1 id="2"><code>print()</code> Fonksiyonu</h1>

`print()` build-in fonksiyonu, `print(*values, sep=' ', end='\n', file=sys.stdout, flush=False)` syntax'ına sahiptir. `print()` fonksiyonu `file` parametresinde belirtilen, default değeri `sys.stdout` olan yere bir şeyler yazdırmak için kullanılan bir build-in (gömülü) fonksiyondur. Örnek:
```py
print(35)
print("Merhaba")
print("""
[H]=========PYTHON========[-][o][x]
|                                 |
|      Programa Hoşgeldiniz!      |
|            Sürüm 0.8            |
|    Devam etmek için herhangi    |
|        bir düğmeye basın.       |
|                                 |
|=================================|
""")
```
**Output:**
```
35
Merhaba

[H]=========PYTHON========[-][o][x]
|                                 |
|      Programa Hoşgeldiniz!      |
|           Sürüm 3.9.2           |
|    Devam etmek için herhangi    |
|        bir düğmeye basın.       |
|                                 |
|=================================|

```

<h2 id="2.1"><code>*values</code> Parametresi</h2>

`*values` parametresi bir yıldızlı parametredir. Yıldızlı parametrelerin tam olarak ne olduğunu daha sonra [burada](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/fonksiyonlar/functions.md#yıldızlı-parametreler "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/fonksiyonlar/functions.md#yıldızlı-parametreler") açıklanacak. `print()` fonksiyonu, `*values` parametresine girilen normal ya da yıldızlı argümanları yazdırır. Örnek:
```py
print("T" , "B" , "M" , "M") # Output: T B M M
print(*"TBMM") # Output: T B M M
```

**Not:** Daha sonra göreceğiniz `len()` gibi fonksiyonlar `len(*"Python")` gibi argümanlar kabul etmezler. Bu fonksiyonun nasıl tanımlandığıyla (definition) alakalıdır. Bu notu anlamadıysanız takılmayın, tutorial'a devam edin.

<h2 id="2.2"><code>sep</code> Parametresi</h2>

`sep` parametresi, `*values` parametresine girilen argümanlar arasına gelecek string'i belirlediğimiz parametredir. Default değeri (yani bu parametreye argüman girmediğiniz taktirde kullandığı argüman) bir adet boşluk (space) `" "` karakteridir. Örnek:
```py
print(1 , 2 , 3 , 4 , 5 , 6 , sep = "/") # Output: 1/2/3/4/5/6
print(1 , 2 , 3 , 4 , 5 , 6 , sep = "+") # Output: 1+2+3+4+5+6
print(1 , 2 , 3 , 4 , 5 , 6 , sep = "Q") # Output: 1Q2Q3Q4Q5Q6
print(1 , 2 , 3 , 4 , 5 , 6 , sep = "%") # Output: 1%2%3%4%5%6
```
`sep` parametresine argüman olarak `\n` ya da `\t` gibi kaçış dizileri de (Escape Sequences) girebilirsiniz.
```py
print("Selam" , "Ben" , "Python!" , sep = "\n", end="\n\n")
print("Selam" , "Ben" , "Python!" , sep = "\t")
```
**Output:**
```
Selam
Ben
Python!

Selam   Ben     Python!
```
Bu parametreye sadece string type (karakter dizisi türü) argümanlar girebilirsiniz. Aksi halde `TypeError` hatası yükseltilir. Örnek:
```py
print(1 , 2 , 3 , 4 , 5 , 6 , sep = 1) # TypeError: sep must be None or a string, not int
```
**Not:** `sep` parametresine argüman olarak `None` verirseniz, default değeri geçerli olur. Örnek:
```py
print(1 , 2 , 3 , 4 , 5 , 6 , sep = None) # Output: 1 2 3 4 5 6
```

<h2 id="2.3"><code>end</code> Parametresi</h2>

`end` parametresi, `*values` parametresine girilen argümanların sonuncusu yazdırıldıktan sonra yazdırılacak string'i belirlediğimiz parametredir. Default değeri `\n` kaçış dizisidir (Escape Sequences).
```py
print(1 , 2 , 3 , 4 , 5 , 6 , sep=", ", end = ", 7\n")
print(1 , 2 , 3 , 4 , 5 , 6,  sep=", ")
```
**Output:**
```
1, 2, 3, 4, 5, 6, 7
1, 2, 3, 4, 5, 6
```
Bu parametreye sadece string type (karakter dizisi türü) argümanlar girebilirsiniz. Aksi halde `TypeError` hatası yükseltilir. Örnek:
```py
print(1 , 2 , 3 , 4 , 5 , 6 , sep=", ", end = 1) # TypeError: end must be None or a string, not int
```
**Not:** `end` parametresine argüman olarak `None` verirseniz, default değeri geçerli olur. Örnek:
```py
print(1 , 2 , 3 , 4 , 5 , 6 , end = None)
print(1 , 2 , 3 , 4 , 5 , 6 , end = None)
```
**Output:**
```
1, 2, 3, 4, 5, 6
1, 2, 3, 4, 5, 6

```

<h2 id="2.4"><code>file</code> Parametresi</h2>

`print()` fonksiyonu, outputlarını default olarak `sys.stdout`'a yani **standart çıktı konumu**'na yazdırır. `sys.stdout` VSCode'da terminalken, başka bir yerde başka bir şey olarak ayarlı olabilir. `file` parametresine girdiğimiz argüman ile `print()` fonksiyonunun outputlarını nereye yazdıracağını belirleyebiliriz. Örnek:
```py
dosya = open("deneme.txt", "w")
print("Merhaba Ben Python!", file = dosya)
dosya.close()
```
**deneme.txt:**
```
Merhaba Ben Python!

```

`stdout`, kodlarımızın çıktılarının gönderildiği yerdir. Örnek:
```py
import sys
print(sys.stdout, flush=True)
```
Bu kod bize `sys.stdout` ile ilgili bilgiler verir: `<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>`
- `name`, `sys.stdout`'un o anki adını verir.
- `mode`, `sys.stdout`'un hangi kipe sahip olduğunu gösterir. `sys.stdout`'u genellikle yazma kipinde (`w`) bulunur.
- `encoding` `sys.stdout`'un sahip olduğu kodlama biçimini gösterir. Kodlama biçimleri uyuşmazsa, bazı karakterler hatalı gösterilebilir.

`sys.stdout`'a kalıcı olarak bir dosya atarsanız, bundan sonra programınızın bütün çıktıları o dosyaya aktarılır. Örnek:
```py
dosya = open("deneme.txt", "w")
sys.stdout = dosya
print("Merhaba Ben Python!", flush=True)
```
**deneme.txt:**
```
Merhaba Ben Python!

```
Bu şekilde yaparsanız, `sys.stdout` methodunun atıfta bulunduğu değeri tamamen kaybedeceğiniz için (çünkü `sys.stdout` methoduna `dosya` variable'ının value'sunu atıyorsunuz) geri döndürme şansınız kalmıyor. Bunu çözümü:
```py
dosya = open("deneme.txt", "w")
sys.stdout, dosya = dosya, sys.stdout
print("Kalıcı dosya işlemi başarılı!", flush=True)
```
**deneme.txt:**
```
Merhaba Ben Python!

```
Bu şekilde yaparsanız, `sys.stdout` methodunun value'su ile `dosya` variable'ının value'sunu birbiriyle değiştirdiğiniz için (swap) tekrar aynı kodu (`sys.stdout, dosya = dosya, sys.stdout`) çalıştırdığınızda `sys.stdout` methodu ile `dosya` variable'ı eski haline geri dönmüş olur. Bunun mantığını daha önce anlattım. Bunu yapmak yerine `sys.stdout` methodunun value'sunu herhangi bir variable'a atayıp da saklayabilirsiniz.

<h2 id="2.5"><code>flush</code> Parametresi</h2>

Python'da `open()` build-in fonksiyonu ile bir dosya açtığımızda, o dosyayı kapatmadığımız sürece `print()` fonksiyonunun dosyaya yazdırdığı şeyler dosyada görünmez (dosyaya işlenmez/yazılmaz). Çünkü dosyayı kapatmadığımız sürece işlenen bilgiler buffer (tampon) adı verilen bir bölgede bekletiliyor ve dosyayı kapattığımızda da dosyaya işleniyor/yazılıyor. `flush` parametresinin default değeri `False`'dır. `flush` parametresi `False` ise bahsettiğim durum geçerlidir. Ama `flush` parametresi `True` ise, `print()` fonksiyonunun dosyaya yazdırdığı şeyler anında dosyaya işlenir/yazılır.

**Not:** `flush` parametresinin `True` olması, `print()` fonksiyonunun dosyaya bir şeyler yazdırdıktan sonra dosyayı kapattığı anlamına gelmiyor. Dosyayı kapatmak için `close()` methodunu kullanmanız gerekiyor. Kanıtı:
```py
dosya = open("deneme.txt", "w")
print("Merhaba Ben Python!", file=dosya, flush=True)
print(dosya.closed) # Output: False (Yani dosya açık)
dosya.close()
print(dosya.closed) # Output: True (Yani dosya kapalı)
```
**deneme.txt:**
```
Merhaba Ben Python!

```

**Not:** Dosya işlemleri konusunu öğrendikten sonra bu kısımları daha iyi anlayacaksınız.

`print()` build-in fonksiyonu ile ilgili daha fazla Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#print "https://docs.python.org/3/library/functions.html#print").

<h1 id="3"><code>input()</code> Fonksiyonu</h1>

`input()` build-in fonksiyonu, `input(prompt)` syntax'ına sahiptir. Bu fonksiyon, kullanıcıdan girdi (input) almanı sağlayan bir build-in (gömülü) fonksiyondur. `prompt` parametresi, `input()` fonksiyonu çağırıldığında (call) argüman olarak `stdout`'a yazdırılacak string'i alır. Bu fonksiyon ile kullanıcıdan alınan verileri kullanabilmek için bu fonksiyonu bir variable'a atayarak kullanabilirsiniz. Örnek:
```py
var = input("Bir sayı giriniz: ")
print("Girdiğiniz sayı:", var)
```
**Output:**
```
Bir sayı giriniz: 15
Girdiğiniz sayı: 15
```
`input()` fonksiyonu, kullanıcının girdiği verileri string type olarak programa verir. Örnek:
```py
var = input("Bir veri giriniz: ")
print("Girdiğiniz verinin türü:", type(var))
```
**Output:**
```
Bir veri giriniz: 15
Girdiğiniz verinin türü: <class 'str'>
```
Gördüğünüz gibi integer bir veri girsek bile `input()` fonksiyonunun programam verdiği verinin string type bir veri olduğunu görüyoruz. Kullanıcıdan aldığınız verinin integer type olmasını istiyorsanız, `input()` fonksiyonunun programa verdiği verinin türünü (type) değiştirmelisiniz. Örnek:
```py
var = input("Bir veri giriniz: ")
var = int(var)
print("Girdiğiniz verinin türü:", type(var))
```
**Output:**
```
Bir veri giriniz: 15
Girdiğiniz verinin türü: <class 'int'>
```
Ama şimdi de kullanıcı harflerden oluşan bir veri girerse, harfleri integer'a dönüştüremeyeceğimiz için hata yükseltilecek. Örnek:
```py
var = input("Bir veri giriniz: ")
var = int(var) # ValueError: invalid literal for int() with base 10: 'selam'
print("Girdiğiniz verinin türü:", type(var))
```
Bunun gibi tip dönüşümlerini (type conversions) daha sonra anlatacağım. `var = int(var)` gibi fazladan bir statement tanımlamak yerine `var = int(input("Bir veri giriniz: "))` şeklinde tek statementte de halledebilirsiniz.

Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#input "https://docs.python.org/3/library/functions.html#input").