# `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
`print()` fonksiyonu, bir şeyler yazdırmak için kullanılan bir build-in (gömülü) fonksiyondur.
```py
print(35) # Output 1
print("Merhaba")  # Output 2
print("""
[H]=========PYTHON========[-][o][x]
|                                 |
|      Programa Hoşgeldiniz!      |
|            Sürüm 0.8            |
|    Devam etmek için herhangi    |
|        bir düğmeye basın.       |
|                                 |
|=================================|
""")  # Output 3
```
**Output 1:**
```
35
```
**Output 2:**
```
Merhaba
```
**Output 3:**
```
[H]=========PYTHON========[-][o][x]
|                                 |
|      Programa Hoşgeldiniz!      |
|            Sürüm 0.8            |
|    Devam etmek için herhangi    |
|        bir düğmeye basın.       |
|                                 |
|=================================|
```
Birden fazla değer `print` etmek için:
```py
a = 20
b = 40
print(15, "Merhaba", 12,45, a+b)
```
**Output:**
```
15 Merhaba 12.45 60
```
## `print()` Parametreleri

### `*object` Parametresi
`print()` fonksiyonuna sınırsız sayıda string argüman girmene olanak tanır.

### `sep` Parametresi
`print()` fonksiyonundaki `*object` parametresi olarak eklenen her bir argümanın arasına gelecek olan ifadeyi belirlemekte kullanılıyor. `sep = "Herhangi bir şey"` şeklinde kullanılıyor. Ama bu parametreyi sadece `str` değerlere ve `None` değerine eşitleyebilirsin. Bir `int` veya `float` değere eşitleyemezsin. `None` değerini verdiğinde ise default değer olan boşluk `" "` değerini alır.
```py
print(1 , 2 , 3 , 4 , 5 , 6 , sep = "/")
print(1 , 2 , 3 , 4 , 5 , 6 , sep = "+")
print(1 , 2 , 3 , 4 , 5 , 6 , sep = "Q")
print(1 , 2 , 3 , 4 , 5 , 6 , sep = "%")
```
`sep` parametresine `\n` ya da `\t` gibi kaçış dizileri tanımlayabilirsiniz.
```py
print("Selam" , "Ben" , "Hiçkimse" , sep = "\n")
print("Selam" , "Ben" , "Hiçkimse" , sep = "\t")
```

### `end` Parametresi
Default olarak `\n`'e ayarlıdır. `print()` fonksiyonunun, `*object` parametresinin en son argümanından sonra gelecek ifadeyi belirlemekte kullanılır. `end = "Herhangi bir şey"` şeklinde kullanılıyor. Ama bu parametreyi sadece `str` değerlere ve `None` değerine eşitleyebilirsin. Bir `int` veya `float` değere eşitleyemezsin. `None` değerini verdiğinde ise default değer olan boşluk `"\n"` değerini alır.
```py
print("Selam", "ben", "Eyüp", end = ".")
# Output: Selam ben Eyüp.
```

### `file` Parametresi
`print()` fonksiyonu, outputlarını default olarak `sys.stdout` yani *standart çıktı konumu’na* yazar. Bu VSC'de terminalde, başka bir yerde etkileşimli kabukta veya komut satırında görünür. `file` parametresi ile bu outputların nereye yazılacağını seçebiliyorsunuz. Bu yer yukarıda belirtildiği gibi `sys.stdout` olabileceği gibi bir txt dosyası da olabilir. Örneğin:
```cpp
dosya1 = open("deneme.txt", "w")
print("Ben Python, Monty Python!", file = dosya1)
dosya1.close()
```
#### `sys.stdout`’u Kalıcı Olarak Değiştirmek
`sys.stdout`, kodlarımızın çıktılarının gönderildiği yerdir. Bu yeri kalıcı olarak bir dosyaya eşitlerseniz, bundan sonra programınızın bütün çıktıları o dosyaya aktarılır.
```py
import sys
print(sys.stdout, flush=True)
dosya3 = open("deneme3.txt", "w")
```
Bu kodun outputu: `<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>`
- `name`, standart çıktı konumunun o anki adını verir.
- `mode`, standart çıktı konumunun hangi kipe sahip olduğunu gösterir. Standart çıktı konumu genellikle yazma kipinde (`w`) bulunur.
- `encoding` standart çıktı konumunun sahip olduğu kodlama biçimini gösterir. Kodlama bişimleri uyuşmazsa, bazı karakterler hatalı gösterilebilir.
```py
sys.stdout = dosya3
print(sys.stdout, flush=True)
print("Kalıcı dosya işlemi başarılı!", flush=True)
```
`sys.stdout`'u ilk değiştirirken `sys.stdout = dosya3` yerine `sys.stdout, dosya3 = dosya3, sys.stdout` kullanırsanız, sonradan eski haline döndürmek istediğinizde tekrardan `sys.stdout, dosya3 = dosya3, sys.stdout` kullanarak bunu başarabilirsiniz. Aksi halde `sys.stdout = dosya3` şeklinde kullanacaksanız, `sys.stdout` değerini kaybetmemek için onu ilk başta bir variable'a eşitlemeniz gerekecek. Bunun mantığını basitçe:
```py
a = 10
b = 20

a = b
print(a) # Output: 20
```
`a`'nın değerini 20'ye eşitledikten sonra `10` değerini kaybediyorsunuz. `sys.stdout = dosya3` şeklinde kullanırken `sys.stdout`'ın değerini de böyle kaybetmemek için herhangi bir variable'a eşitleyin dememin sebebi bu. `sys.stdout, dosya3 = dosya3, sys.stdout` olayının mantığını **temel_kavramlar.md** dosyasındaki [**Variable'lar (Değişkenler)**](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/temel_kavramlar/temel_kavramlar.md#variablelar-değişkenler) başlığı altında anlatıldı.

### `flush` Parametresi
`dosya = open("deneme.txt", "w")` şeklinde bir dosya açtığımızda, o dosyaya print fonksiyonundaki bilgileri kaydettikten sonra kaydettiğimiz bilgilerin dosyada gözükmesi için dosyayı `dosya.close()` şeklinde kapatmamız gerekiyor. Çünkü dosyayı kapatmadığımız sürece işlenen bilgiler buffer (tampon) adı verilen bir bölgede bekletiliyor ve dosyayı kapattığımızda da dosyaya işleniyor/yazılıyor. `flush` paremetresinin default değeri `False`'dır. `False` olduğu için açtığımız dosyayı manuel olarak (`dosya.close()` ile) kapatmamız gerekir. Bu değeri `true` yaparsak, açtığımız dosyadaki bilgilerin gözükmesi için dosyayı manuel olarak kapatma komutuna ihtiyacımız kalmaz.
```py
dosya2 = open("deneme2.txt", "w")
print("Bu benim 2. dosyam.", file=dosya2, flush=True)
```

## Yıldızlı Parametreler
Yıldız işareti (`*`), kendinden sonra gelen argümanı parçalarına ayırır.
```py
print("T" , "B" , "M" , "M" , sep = ".") # Output: T.B.M.M.
print(*"TBMM" , sep = ".") # Output: T.B.M.M.
```
`len()` gibi fonksiyonlar tek bir parametre aldıkları için len(*"Python") gibi bir şey söz konusu değildir, hata verir.
Daha fazla Bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#print).

# `input(prompt)`
Kullanıcıdan girdi (input) almanı sağlayan bir build-in (gömülü) fonksiyondur. `input()` gibi sade bir şekilde kullanılabileceği gibi `input("Lütfen bir sayı giriniz: ")` şeklinde de kullanılabilir. Kullanıcıdan alınan değerleri bir variable'a atayabilirsiniz. Örneğin:
```py
inp = input("Bir input giriniz: ") # 15 girersek,
print("Girdiğiniz input: ", inp)
```
**Output:**
```
Bir input giriniz: 15
Girdiğiniz input: 15
```
**Not:** `input()` fonksiyonu, kendisine girilen değerleri `str` veri tipinde programa verir. Yani bir `int` değere ihtiyacınız varsa, kullanıcıdan aldığınız değeri kullanmadan önce  `int` data type'a dönüştürmelisiniz.
```py
s1 = int(input("İlk sayı: ")) # 2 girersek,
s2 = int(input("İkinci sayı: ")) # 3 girersek
print("Girdiğiniz sayıların toplamı: ", s1 + s2)
# Output: Girdiğiniz sayıların toplamı: 5
```
Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#input).