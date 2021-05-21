# Dosya İşlemleri

## `open()` Fonksiyonu
`open()` fonksiyonu, dosya açmak veya oluşturmak için kullanılır. Eğer `open()` fonksiyonunda belirtilen uzantıda, belirtilen isimde bir dosya yoksa, belirtilen isimde bir dosya oluşturur. Syntax:
```py
open(r"file", mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
Buradaki parametreleri teker teker açıklamak gerekirse:
- `"file"`, dosya dizinini (path) temsil eder. Path yazarken `\` ayracını kaçış dizisi olarak algılayabilir. Bu yüzden her path yazdığınızda en başa `r` kaçış dizisini koyun. Yani `r"D:\falan_filan..."` şeklinde kullanın.
- 
- `mode`, default değeri `"r"` olarak ayarlıdır. Dosyayı açarken hangi modda (örneğin okuma ya da yazma) açacağınızı belirlersiniz. `mode` parametresine girilebilecek argümanlar için [tıklayınız](asd). Devam etmeden önce bu argumanları öğrenmenizde fayda var.

- `buffering`, default değeri `-1` olarak ayarlıdır. Buffering policy ayarlamak için kullanılır.

- `encoding`, dosyayı hangi kod çözücüyle açacağını belirlediğiniz parametredir.

- `errors`, `encoding` parametresinde belirtilen kod çözücü uygun değilse döndürülecek hatanın belirlendiği parametredir. Bu parametrenin alabileceği argumanlara [buradan](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/.md/kullanicidan_girdi_almak/tip_donusumleri.md#strobject-encodingutf-8-errorsstrict) ulaşabilirsiniz.

- `newline`, dosyada yazılı olan her satırın sonundaki kaçış dizilerini etkiler. Default değeri `None` olarak ayarlıdır ve bu arguman kullanılırsa, son satır hariç her satırın sonunda `\n` kaçış dizisi olur. Boş string `""` argumanı verilirse, son satır hariç her satırın sonunda `\r\n` kaçış dizileri olur. `"\n"` argumanı verilirse, son satır hariç her satırın sonunda `\r\n` kaçış dizileri olur. `"\r"` argumanı verilirse, son satır hariç her satırın sonunda `\r` kaçış dizisi olur. `\r\n` argumanı verilirse, son satır hariç her satırın sonunda `\r\n` kaçış dizileri olur. Bu argumanlardan başka arguman kabul etmez.a

- `closefd`,  ?

- `opener`,  ?

`open()` ile açtığınız dosyayı programınızda kullanabilmek için bir variable'a `dosya = open(...)` şeklinde atamanız gerekmektedir.

**DİKKAT:** Bir dosyayı `open()` ile açtıktan sonra kapatmayı kesinlikle unutmayın. Aksi taktirde geri döndürülemez hatalarla karşılaşabilirsiniz.

## Dosyaya Yazmak
Yazılabilir dosyalara bir şeyler yazabilmek için kullanılan bazı fonksiyonlar vardır. Burada dikkat edilmesi gereken en önemli şeylerden birisi, `encoding` parametresidir. Bir dosyaya Türkçe karakterler içeren bir şeyler yazmak veya Türkçe karakterler içeren bir dosyayı okumak istiyorsanız, doğru sonuçlar elde etmek için `encoding` parametresini doğru kullanmalısınız.

### `write("string")` Methodu
Dosyaya bir adet string girebilmenizi sağlar. O anda imleç, yazılacak dosyanın neresindeyse, oradan yazmaya başlar. İmlecin bulunduğu yerde yazı varsa, `write()` methoduna girilen değer, bu yazının üzerine yazılır. Yani:
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

dosya.write("Deneme")

dosya.close()
```
**Eski Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Yeni Dosya:**
```
Denemeatır
İkinci Satır
Üçüncü Satır.
```

### `writelines([list])` Methodu
Dosyaya birden fazla string girebilmenizi sağlar. Girmek istenilen stringler, bir liste içinde gösterilir. O anda imleç, yazılacak dosyanın neresindeyse, oradan yazmaya başlar. İmlecin bulunduğu yerde yazı varsa, `writelines()` methoduna girilen değer, bu yazının üzerine yazılır. Yani:
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

dosya.writelines(["deneme1", "\ndeneme2"])

dosya.close()
```
**Eski Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Yeni Dosya:**
```
deneme1
deneme2inci Satır
Üçüncü Satır.
```
**Dikkat:** Bu üzerine yazma olayında, üzerine yazılan satırın uzunluğu, üzerine yazdığının uzunluğundan küçükse (`İlk Satır`'ın `deneme1deneme2`'den küçük olması gibi) aşağıdaki gibi absürt durumlar oluşabilir.
```
deneme1deneme2�kinci Satır
Üçüncü Satır.
```

### `writable()` Methodu
Dosyanın yazılabilir olup olmamasını sorgulayabilmemizi sağlar. Yazılabilir bir doyaysa `True`, değilse `False` döndürür.
```py
dosya = open(r"deneme.txt", mode="w", encoding="utf-8")

print(dosya.writable()) # Output: True

dosya.close()
```

## Dosyayı Okumak
Okunulabilir dosyaları okuyabilmek için kullanılan bazı fonksiyonlar vardır. Burada dikkat edilmesi gereken en önemli şeylerden birisi, `encoding` parametresidir. Bir dosyaya Türkçe karakterler içeren bir şeyler yazmak veya Türkçe karakterler içeren bir dosyayı okumak istiyorsanız, doğru sonuçlar elde etmek için `encoding` parametresini doğru kullanmalısınız.

### `read(sayı)` Methodu
Bir dosyanın içeriğini okuyup döndürür. Bu output, string data type'ındadır. Bu output'da kaçış dizileri gibi python'un gördüğü ama kullanıcının göremediği şeyler görünmez. Yani output, **kullanıcının gözünden** verilir. Eğer `sayı` parametresi belirtilirse, imlecin güncel konumundan, bu parametreye girilen integer'ın belirttiği uzunluk kadar karakteri okur ve döndürür. `sayı` parametresine `None` ya da negatif bir integer değer girilirse, boş parametre girildiği zamanki davranışın aynısını sergiler.
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

print(dosya.read())
print(dosya.read(11))

dosya.close()
```
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.read())` Output:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.read(11))` Output:**
```
İlk Satır
İ
```

### `readline(sayı = -1)` Methodu
Bir dosyanın bir satırını okuyup döndürür. Bu output, string data type'ındadır. Bu output'da kaçış dizileri gibi python'un gördüğü ama kullanıcının göremediği şeyler görünmez. Yani output, **kullanıcının gözünden** verilir. Aynı progress içerisinde her çağırıldığında bir sonraki satırı döndürür. Eğer dosya sonuna ulaşılmışsa, sonraki çağırılışlarında boş string `""` döndürür. Eğer `sayı` parametresi belirtilirse, imlecin bulunduğu satırdaki güncel konumundan, bu parametreye girilen integer'ın belirttiği uzunluk kadar karakteri okur ve döndürür. `sayı` parametresine negatif bir integer değer girilirse, boş parametre girildiği zamanki davranışın aynısını sergiler. `readline()` methoduna, `read()` methodundaki gibi `None` parametresi gürülemez. Girilirse `TypeError` hatası verir.
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

print(dosya.readline())
print(dosya.readline(3))
print(dosya.readline(100))

dosya.close()
```
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.readline())` Output:**
```
İlk Satır
```
**`print(dosya.readline(3))` Output:**
```
İlk
```
**`print(dosya.readline(100))` Output:**
```
'İlk Satır
'
```
**Not:** En son output'da da gördüğünüz gibi, `readline()` methodu, sadece bir satırı okuduğu için `sayı` parametresine o satırdan daha uzun bir değer girilirse, satırın en sonuna kadar alır ve döndürür.

### `readlines(sayı = -1)` Methodu
Bir dosyanın bütün satırını okuyup döndürür. Bu output, list data type'ındadır. Bu output'da kaçış dizileri gibi python'un gördüğü ama kullanıcının göremediği şeyler görünür. Yani output, **Python'un gözünden** verilir. Eğer `sayı` parametresi belirtilirse, imlecin güncel konumundan, bu parametreye girilen integer'ın belirttiği uzunluktaki karakterleri içeren bütün satırları döndürür. `sayı` parametresine `None` ya da negatif bir integer değer girilirse, boş parametre girildiği zamanki davranışın aynısını sergiler. Bu durumu örnekleyelim:
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

print(dosya.readlines())
print(dosya.readlines(9))
print(dosya.readlines(10))

dosya.close()
```
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.readlines())` Output:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.readlines(9))` Output:**
```
['İlk Satır\n']
```
**`print(dosya.readlines(10))` Output:**
```
['İlk Satır\n', 'İkinci Satır\n']
```
Gördüğünüz gibi, dosya içindeki ilk index'e 1 numaralı karakter dersek, 9 numaralı karaktere kadarki alan birinci satır olarak kabul ediliyor. Bu yüzden `sayı` parametresine `10` sayısını girdiğimizde, 2. satıra geçtiğimiz için 2. satırın tamamını alıyor. Yani bir satırı alması için o satıra geçmiş olmamız yetiyor.


### `readable()` Methodu
Dosyanın okunabilir olup olmamasını sorgulayabilmemizi sağlar. Okunabilir bir doyaysa `True`, değilse `False` döndürür.
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

print(dosya.readable()) # Output: True

dosya.close()
```

## Dosyaları Otomatik Kapatmak
Dosyaları kapatmazsanız fata error gibi ciddi sorunlarla uğraşmak zorunda kalırsınız. Bu yüzden bir dosya açtığınızda o dosyayı kapatmayı unutmayıp, bu alışkanlığı kazanmanız için bazı pratik yöntemler vardır.

### `try` - `except <ErrorCode>` - `finally` Yapısı
`finally` statement'inde dosya kapama işlemi yapabilirsiniz. Bu sayede hem hata ayıklama sisteminin nimetlerinden faydalanırken, hem dosyanızı her durumda kapatan bir kod elde etmiş olacaksınız. Örnek:
```py
try:
	dosya = open(r"deneme.txt", "r")
	# Burada dosyayla bazı işlemler yapıyoruz ve ansızın bir hata oluşuyor.
except IOError:
	print("bir hata oluştu!")
finally:
	dosya.close()
```
Buradaki dosya işlemlerinde oluşabilecek hatalara karşı bir savunma mekanizması ayarlamakla kalmayıp, `finally` statement sayesinde, hata çıksa da çıkmasa da dosyayı kapatmış oluyorsunuz.

### `with` Statement
`with` statement sayesinde, açtığınız dosyada hata oluşsa bile python dosyayı güvenli bir şekilde kapatacaktır. Syntax:
```py
with open("deneme.txt", "r") as dosya:
	# Dosya işlemleri
```
`as` keyword'ü, `with` bloğunda açtığın dosyayı kullanabilmen için `dosya` adında bir variable'a atıyor. Bu sayede dosya üzerinde `vrb = dosya.read()` gibi işlemler yapabilirsin. Burada dikkat edilmesi gereken yer, bu `dosya` adındaki variable'ı sadece `with` bloğunda kullanabilirsin. Çünkü `with` bloğu sonlandığında dosya otomatik olarak kapanacaktır. Bu yüzden mantıken `with` dışında kullanamıyorsun. Ama `with` bloğunda tanımladığın variable'ları, programın başka yerlerinde kullanabilirsin. Sadece `dosya` variable'sini, dosya kapandığı için kullanamıyorsun.

## Dosyadaki İmleç Konumu
Dosya işlemlerinde **imleç** dediğimiz bir kavram var. Bir dosyayı okurken veya yazarken imlecin yeri sürekli değişir. Örneğin:
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
`readline()` methodu bu dosyada bir kere çalıştığına, dosyanın başlangıcında olan imleç, 2. satırın başına geliyor. Tekrar çalıştığında da 3. satırın başına geliyor. Tekrar çalıştığında da 4. satır olmadığı için 3. satırın sonuna geliyor. Bu imlecin yeriyle oynayabilseydik, örneğin `readline()` gibi methodların sürekli aynı satırı bastırmasını sağlayabilirdik. Bunu yapabilmemizi sağlayan bazı methodlar var:

### `tell()` Methodu
İmlecin, o anda bulunduğu byte konumunu söyler. Örnek:
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Kod:**
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

dosya.readline(100)
print(dosya.tell()) # Output: 12

dosya.close()
```

### `seek(offset, whence = SEEK_SET)` Methodu
`seek()` methodu, imleci, `offset` parametresinde belirtilen konumdaki byte'a konumlandırmanızı sağlar. Bu konumlandırmayı yaparken kaçış dizilerini de dikkate alır. Örneğin, `offset` parametresine `2` değerini girersek, imleci 2. index'deki byte'a konumlandırır ve sonrasında yapılacak **write** (yazma) ve **read** (okuma) işlemlerini, 2. index'deki byte'ı dahil ederek yapar. Bu konumlandırmayı, index'lerdeki karakterlere göre değil, byte'lara göre yapar. Örneğin `"i"` karakteri, `utf-8` kod çözücüde 1 byte ile temsil edilirken, `"İ"` karakteri, `utf-8` kod çözücüde 2 byte ile temsil edilir. Bu yüzden aşağıdaki gibi bir durumla karşılaşılabilir:

**Dosya:**
```
ilk Satır
İkinci Satır
Üçüncü Satır.
```
**Kod:**
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

dosya.seek(2)
print(dosya.read())

dosya.close()
```
**Output:**
```
k Satır
İkinci Satır
Üçüncü Satır.
```
Buradaki `"i"` karakteri, `utf-8` kod çözücüde 1 byte ile temsil edildiği için sıfırıncı ve birinci index'lerdeki byte'ları (`"il"`) atlayıp, 2. index'deki byte'dan itibaren (2. index'deki byte dahil) `read()` methodunu çalıştırdı.
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Kod:**
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

dosya.seek(2)
print(dosya.read())

dosya.close()
```
**Output:**
```
lk Satır
İkinci Satır
Üçüncü Satır.
```
Buradaki `"İ"` karakteri, `utf-8` kod çözücüde 2 byte ile temsil edildiği için sıfırıncı ve birinci index'lerdeki byte'ları (`"İ"`) atlayıp, 2. index'deki byte'dan itibaren (2. index'deki byte dahil) `read()` methodunu çalıştırdı.

`whence` parametresinde ise, imleci konumlandırırken kullanacağı ölçütü belirleyebilirsiniz. `whence` parametresine `SEEK_SET` ya da `0` girilirse, dosyanın başını referans alır ve `offset` sıfır ya da positif integer'lar olmalıdır; `SEEK_CUR` ya da `1` girilirse, mevcut (current) konumu (reading, writing işlemlerinde ya da `seek()` methoduyla değişen konum) referans alır ve `offset` negatif integer'lar olabilir; `SEEK_END` ya da `2` girilirse, dosyanın sonunu referans alır ve `offset` genellikle negatif integer'lardır. `whence` parametresine 1 ya da 2 argumanlar kullanılacaksa, dosya binary (rb, wb, ab, xb, rb+, wb+, ab+, xb+) modda açılmalıdır. Dosya binary modda açılmazsa, bu argumanları kullandığınızda `io.UnsupportedOperation: can't do nonzero end-relative seeks` hatası alırsınız.

## Dosyaya Ekleme yapma
Python'da, zaten var olan ve boş olmayan bir dosyanın içeriğine ekleme yapmak istediğimizde, o dosyayı `a` kipiyle açarız.

### Dosyanın Sonunda Değişiklik yapmak
Dosyayı açtığınızda imleç, dosyanın en sonundadır. Bu yüzden `write()` ya da `writelines()` methodlarıyla dosyaya bir şey yazmak isterseniz, bu yazı, dosyanın sonuna eklenir. Burada dikkat edilmesi gereken, dosyanın son satırındaki karakter dizisinde `\n` bulunmadığı için ekleyeceğiniz karakter dizilerinde bu kaçış dizilerine yer vermeyi unutmayın. Örnek:
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`\n` kullanmadan:**
```py
dosya = open(r"deneme.txt", mode="a", encoding="ascii")

dosya.write(r"\n yok")

dosya.close()
```
**Output:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.\n yok
```
**`\n` kullanarak:**
```py
dosya = open(r"deneme.txt", mode="a", encoding="ascii")

dosya.write("\n\\n var")

dosya.close()
```
**Output:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
\n var
```

### Dosyanın Başında Değişiklik yapmak
Dosya başında değişik yapmanın yöntemi:
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

veri = dosya.read()
dosya.seek(0)
dosya.write("Dosyanın başında değişiklik yapıldı.\n" + veri)

dosya.close()
```
**Output:**
```
Dosyanın başında değişiklik yapıldı.
İlk Satır
İkinci Satır
Üçüncü Satır.
```
Bu kodda `read()` işleminden sonra imleç, dosyanın sonuna gitmiştir. Bu yüzden `seek(0)` işlemi önemlidir. Aksi taktirde istenilen string dosyanın sonundan yazılmaya başlanırdı ve böyle bir görüntü oluşurdu:
```
İlk Satır
İkinci Satır
Üçüncü Satır.Dosyanın başında değişiklik yapıldı.
İlk Satır
İkinci Satır
Üçüncü Satır.
```

### Dosyanın Ortasında Değişiklik yapmak
Dosyanın başı ve sonu dışındaki herhangi bir yerinde değişiklik yapmak için birkaç yöntem mevcuttur. Örneğin, eğer dosyanın içindeki herhangi iki paragraf arasında yeni bir paragraf eklemek istiyorsanız:
**Eski Dosya:**
```
Bu birinci paragraf.
Bu ikinci paragraf.
Bu üçüncü paragraf.
```
**Program:**
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

veri = (dosya.readlines())
dosya.seek(0)
veri.insert(1, "Artık bu paragraf ikinci paragraf.\n")
dosya.writelines(veri)

dosya.close()
```
**Yeni Dosya:**
```
Bu birinci paragraf.
Artık bu paragraf ikinci paragraf.
Bu ikinci paragraf.
Bu üçüncü paragraf.
```
Eğer spesifik bir yere, örneğin iki kelime arasına ekleme yapmak istiyorsanız, `string` ve `list` methodlarıyla oluşturacağınız bir programla bunu halledebilirsiniz. Örnek:
**Eski Dosya:**
```
Bu birinci satır.
Bu ikinci satır.
Bu üçüncü satır.
```
**Program:**
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

# 1. Kısım (Aşağıda açıklandı)
veri1 = (dosya.readlines())
string_temp = str()
dosya.seek(0)

# 2. Kısım (Aşağıda açıklandı)
veri2 = list(veri1[0].partition("birinci"))
veri2.insert(1, "en ")

# 3. Kısım (Aşağıda açıklandı)
for i in veri2:
	string_temp += i

# 4. Kısım (Aşağıda açıklandı)
veri1[0] = string_temp
dosya.writelines(veri1)
  
dosya.close()
```
**Yeni Dosya:**
```
Bu en birinci satır.
Bu ikinci satır.
Bu üçüncü satır.
```
1. `readlines()` methodu ile dosyanın bütün satırlarını okuyup her satırın bir liste elemanı olduğu obje'yi `veri1` variable'ına eşitliyoruz.

2. Stringlerdeki `partition()` methodu, `veri[0]` index'indeki liste elemanının içerdiği string'i `"birinci"` kelimesini referans alarak 3'e bölüyor ve bize, bu öğeleri içeren bir tuple objesi veriyor. Bu obje, `('Bu ', 'birinci', ' paragraf.\n')` içeriğine sahiptir. En son bu objeyi `list()` ile listeye çeviriyoruz ki üzerinde değişiklik yapabilelim. Daha sonra bu listenin 1. indexine `veri2.insert(1, "en ")` koduyla `"en"` stringini ekleyip `['Bu ', 'en ', 'birinci', ' paragraf.\n']` listesini elde ediyoruz.

3. `veri2` variable'ının içindeki `['Bu ', 'en ', 'birinci', ' paragraf.\n']` listesinin öğelerini teker teker `for` loop ile alarak `string_temp` variable'sine ekliyoruz ve bu sayede elimizde `"Bu en birinci paragraf.\n"` şeklinde bir string oluyor. Bu stringi `veri1[0]` koduyla, eski index'in yerine atamış oluyoruz ve böylece istediğimiz sonucu elde etmiş oluyoruz.

4. Son olarak `writelines()` methoduyla `veri1`'i dosyaya yazdırıyoruz. Bunu yapmadan önce `seek(0)` ile imleci dosyanın en başına götürmeyi unutmayın. Aksi halde sondan yazmaya başlar ve istediğiniz sonucu alamazsınız. Son olarak dosyayı `close()` methodu ile kapatmayı unutmayın.

## Dosyaya Erişim Kipleri

### `r` kipi
Default dosya açma kipidir. Bu kip, bir dosyayı **read** (okuma) yetkisiyle açar. Bu kipi kullanabilmeniz için ilgili dosyanın, bulunduğunuz path'da halihazırda var olması gerekir. Belirttiğiniz dosya, bulunduğunuz path'da yoksa, Python `FileNotFoundError` hatası döndürür.

### `w` kipi
Bu kip, bir dosyayı **write** (yazma) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten varsa, Python hiçbir şey sormadan dosya içeriğini silecektir. Eğer belirttiğiniz adda bir dosya bulunduğunuz path'da yoksa, Python o adda bir dosyayı otomatik olarak oluşturur.  

### `a` kipi
Bu kip, bir dosyayı **append** (ekleme) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten mevcutsa, dosya içeriğinde herhangi bir değişiklik yapılmaz, yani `w` kipi gibi dosya içeriğini silmez. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da yoksa, Python otomatik olarak o adda bir dosya oluşturacaktır. Bu kipte açtığınız bir dosyaya yazmak istediğiniz veriler, dosyanın sonuna eklenir. Bu yüzden `seek(0)` gibi komutlarla dosya başına gitmek, dosyanın başına **append** (ekleme) işlemi yapmanızı sağlamaz. 

### `x` kipi
Bu kip, bir dosyayı **write** (yazma) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten varsa, Python varolan dosyayı silmek yerine size `FileExistsError` hatası döndürür. Belirttiğiniz adda bir dosya, bulunduğunuz path'da yoksa, belirttiğiniz isimde bir dosya oluşturur.

### `r+` kipi
Bu kip, bir dosyayı hem **write** (yazma) hem de **read** (okuma) yetkisiyle açar. Bu kipi kullanabilmeniz için ilgili dosyanın, bulunduğunuz path'da halihazırda var olması gerekir. Belirttiğiniz dosya, bulunduğunuz path'da yoksa, Python `FileNotFoundError` hatası döndürür.

### `w+` kipi
Bu kip, bir dosyayı hem **write** (yazma) hem de **read** (okuma) yetkisiyle açar. Eğer dosya, bulunduğunuz path'da mevcutsa, dosya içeriğı silinir,. Eğer dosya, bulunduğunuz path'da mevcut değilse, belirtilen adda bir dosya oluşturulur.

### `a+` kipi
Bu kip, bir dosyayı hem **append** (ekleme) hem de **read** (okuma) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten mevcutsa, içeriğinde herhangi bir değişiklik yapılmaz, yani `w+` kipi gibi dosya içeriğini silmez. Eğer belirttiğiniz adda bir dosya yoksa, Python otomatik olarak o adda bir dosya oluşturacaktır. Bu kipte açtığınız bir dosyaya yazmak istediğiniz veriler, dosyanın sonuna eklenir. Bu yüzden `seek(0)` gibi komutlarla dosya başına gitmek, dosyanın başına **append** (ekleme) işlemi yapmanızı sağlamaz. 

### `x+` kipi
Bu kip, bir dosyayı hem **write** (yazma) hem de **read** (okuma) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten varsa, Python varolan dosyayı silmek yerine size `FileExistsError` hatası döndürür. Belirttiğiniz adda bir dosya, bulunduğunuz path'da yoksa, belirttiğiniz isimde bir dosya oluşturur.

### `rb` kipi
Bu kip, bir binary dosyayı **read** (okuma) yetkisiyle açar. Bu kipi kullanabilmeniz için ilgili dosyanın, bulunduğunuz path'da halihazırda var olması gerekir. Belirttiğiniz dosya, bulunduğunuz path'da yoksa, Python `FileNotFoundError` hatası döndürür.

### `wb` kipi
Bu kip, bir binary dosyayı **write** (yazma) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten varsa, Python hiçbir şey sormadan dosya içeriğini silecektir. Eğer belirttiğiniz adda bir dosya bulunduğunuz path'da yoksa, Python o adda bir dosyayı otomatik olarak oluşturur.  

### `ab` kipi
Bu kip, bir binary dosyayı **append** (ekleme) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten mevcutsa, dosya içeriğinde herhangi bir değişiklik yapılmaz, yani `w` kipi gibi dosya içeriğini silmez. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da yoksa, Python otomatik olarak o adda bir dosya oluşturacaktır. Bu kipte açtığınız bir dosyaya yazmak istediğiniz veriler, dosyanın sonuna eklenir. Bu yüzden `seek(0)` gibi komutlarla dosya başına gitmek, dosyanın başına **append** (ekleme) işlemi yapmanızı sağlamaz. 

### `xb` kipi
Bu kip, bir binary dosyayı **write** (yazma) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten varsa, Python varolan dosyayı silmek yerine size `FileExistsError` hatası döndürür. Belirttiğiniz adda bir dosya, bulunduğunuz path'da yoksa, belirttiğiniz isimde bir dosya oluşturur.

### `rb+` kipi
Bu kip, bir binary dosyayı hem **write** (yazma) hem de **read** (okuma) yetkisiyle açar. Bu kipi kullanabilmeniz için ilgili dosyanın, bulunduğunuz path'da halihazırda var olması gerekir. Belirttiğiniz dosya, bulunduğunuz path'da yoksa, Python `FileNotFoundError` hatası döndürür.

### `wb+` kipi
Bu kip, bir binary dosyayı hem **write** (yazma) hem de **read** (okuma) yetkisiyle açar. Eğer dosya, bulunduğunuz path'da mevcutsa, dosya içeriğı silinir,. Eğer dosya, bulunduğunuz path'da mevcut değilse, belirtilen adda bir dosya oluşturulur.

### `ab+` kipi
Bu kip, bir binary dosyayı hem **append** (ekleme) hem de **read** (okuma) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten mevcutsa, içeriğinde herhangi bir değişiklik yapılmaz, yani `w+` kipi gibi dosya içeriğini silmez. Eğer belirttiğiniz adda bir dosya yoksa, Python otomatik olarak o adda bir dosya oluşturacaktır. Bu kipte açtığınız bir dosyaya yazmak istediğiniz veriler, dosyanın sonuna eklenir. Bu yüzden `seek(0)` gibi komutlarla dosya başına gitmek, dosyanın başına **append** (ekleme) işlemi yapmanızı sağlamaz. 

### `xb+` kipi
Bu kip, bir binary dosyayı hem **write** (yazma) hem de **read** (okuma) yetkisiyle açar. Eğer belirttiğiniz adda bir dosya, bulunduğunuz path'da zaten varsa, Python varolan dosyayı silmek yerine size `FileExistsError` hatası döndürür. Belirttiğiniz adda bir dosya, bulunduğunuz path'da yoksa, belirttiğiniz isimde bir dosya oluşturur.

## Dosya Methodları
Dosyalar da bir data type (`<class '_io.TextIOWrapper'>`) oldukları için methodlara ve attribute'lara (class'lar konusunda bahsedilecek) sahiptir.

### `closed` Attribute
Dosyanın kapalı olup olmadığını sorgulamanızı sağlar.
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

print(dosya.closed) # Output: False

dosya.close()
```

### `mode` Attribute
Dosyanın hangi kipte açılacağına dair bilgi verir.
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

print(dosya.mode) # Output: r+

dosya.close()
```

### `name` Attribute
Dosyanın adını verir.
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

print(dosya.name) # Output: deneme.txt

dosya.close()
```

### `encoding` Attribute
Dosyanın hangi kod çözücü ile kodlandığı hakkında bilgi verir.
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

print(dosya.encoding) # Output: utf-8

dosya.close()
```

### `close()` Methodu
`open()` fonksiyonu ile açılmış bir dosyayo kapatmak için kullanılır. Dosya zaten kapatılmış ise, bu methodun bir etkisi olmaz.

### `detach()` Methodu
**Stream**, Python'da bir dosyayı açtığında sana açma moduna göre verilen I/O objesidir. Aynı zamanda **file object**, **file-like object** de denir.

Bir dosyayı `open()` fonksiyonu ile açtığınızda, `open()` fonksiyonunda belirtilen parametrelere göre özelleştirilmiş bir `<class '_io.TextIOWrapper'>` objesi (stream, file object, file-like object) oluşturuluyor. Bu objenin methodları ve attribute'ları sayesinde, hedef dosya üzerinde **write** (yazma) ve **read** (okuma) işlemleri yapabiliyoruz. `detach()` merhodu kullanıldığında, ilgili dosyanın **raw-stream** objesi döndürülür. Bu obje, ilgili dosya **read** (okuma) yetkisine sahip bir kiple açılmışsa `io.BufferedReader`, **write** (yazma) yetkisine sahip bir kiple açılmışsa `io.BufferedWriter`, hem **write** (yazma) hem **read** (okuma) yetkisine sahip bir kiple açılmışsa `io.BufferedRandom` objesidir. Bu method uygulandığında, sonraki bütün işlemler **raw-stream** üzerinden yapılır. Yani en başta `open()` fonksiyonu ile oluşturulan dosya objesi kullanılamaz. Bu yüzden en başta `open()` fonksiyonu ile oluşturulan dosya objesini kullanarak işlem yapmaya çalışırsanız `ValueError: underlying buffer has been detached` hatası alırsınız. `detach()` methodu ile oluşturulan **raw-stream** objesi, üzerinde daha detaylı dosya işlemleri yapılmasına olanak tanır. Kısaca, zaten en başta `open()` fonksiyonu ile oluşturulan dosya objesinin üzerinde yapılabilen işlemleri, daha çok ayrıntıya girmene izin vererek yapmana izin verir ama daha çok uğraştırır. Bu metod `io.IOBase` class'ından inherit edildiği için high level programming language (örneğin python) ile uğraşanların bilmesi ya da kullanması gerekmemektedir. `io` modülündeki class'lara aşına olmak isteyenler araştırabilir. Daha ayrıntılı için [**`io` modülüne**](https://docs.python.org/3/library/io.html) bakabilirsiniz.

### `fileno()` Methodu
**File descriptor** numarası, underlying implementation tarafından işletim sisteminden `I/O` işlemlerini talep etmek için kullanılır. Bu method, ilgili dosya için **File descriptor** integer değeri döndürür. `open()` ile bir dosyayı açmaya çalıştığında, açma iznin olmadığı için ilgili dosyayı açamadığında, ilgili dosyayı kapatmadan önce (Yani `open()` fonksiyonu ile `close()` methodu arasına) `fileno()` methodu kullanılırsa, `-1` outputunu verir.

### `flush()` Methodu
`open()` fonksiyonu ile bir dosyayı açtıktan sonra o dosyada yaptığınız değişiklikler, **buffer** (tampon) adı verilen bir bölgede bekletilir ve dosya `close()` methodu ile kapatıldığında, bu değişiklikler dosyaya işlenir. `flush()` methodu, bufferdaki değişikliklerin dosyaya işlenmesini sağlar. Bu sayede, dosyada yapılan değişiklikleri, dosyayı `close()` methodu ile kapatmak zorunda kalmadan dosyaya işleyebilirsiniz.

### `isatty()` Methodu
File stream'ın, interactive olup olmadığını döndürür. Stream eğer interactive ise (yani bir terminale veya tty cihazına bağlıysa) `True`, değilse `False` döner. Örneğin bu method, consol stream'ında `True` döndürürken, normal bir dosya açıp kullanıldığında `False` döndürür.

**Not:** **consol stream'ı** ve [**terminal stream'ı**](https://docs.python.org/3/library/sys.html#sys.stdin) aynı şeylerdir. Terminale girilen `stdin` ve `stdout` verileri, **consol stream'ı**, diğer bir ismiyle **terminal stream'ı** oluşturuyor. **Terminal stream'a** yazı yazmak için `print()`, **Terminal stream'ı** okumak için `input()` kullanıyoruz gibi düşünebilirsiniz.

### `read(sayı)` Methodu
Bir dosyanın içeriğini okuyup döndürür. Bu output, string data type'ındadır. Bu output'da kaçış dizileri gibi python'un gördüğü ama kullanıcının göremediği şeyler görünmez. Yani output, **kullanıcının gözünden** verilir. Eğer `sayı` parametresi belirtilirse, imlecin güncel konumundan, bu parametreye girilen integer'ın belirttiği uzunluk kadar karakteri okur ve döndürür. `sayı` parametresine `None` ya da negatif bir integer değer girilirse, boş parametre girildiği zamanki davranışın aynısını sergiler.
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

print(dosya.read())
print(dosya.read(11))

dosya.close()
```
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.read())` Output:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.read(11))` Output:**
```
İlk Satır
İ
```

### `readline(sayı = -1)` Methodu
Bir dosyanın bir satırını okuyup döndürür. Bu output, string data type'ındadır. Bu output'da kaçış dizileri gibi python'un gördüğü ama kullanıcının göremediği şeyler görünmez. Yani output, **kullanıcının gözünden** verilir. Aynı progress içerisinde her çağırıldığında bir sonraki satırı döndürür. Eğer dosya sonuna ulaşılmışsa, sonraki çağırılışlarında boş string `""` döndürür. Eğer `sayı` parametresi belirtilirse, imlecin bulunduğu satırdaki güncel konumundan, bu parametreye girilen integer'ın belirttiği uzunluk kadar karakteri okur ve döndürür. `sayı` parametresine negatif bir integer değer girilirse, boş parametre girildiği zamanki davranışın aynısını sergiler. `readline()` methoduna, `read()` methodundaki gibi `None` parametresi gürülemez. Girilirse `TypeError` hatası verir.
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

print(dosya.readline())
print(dosya.readline(3))
print(dosya.readline(100))

dosya.close()
```
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.readline())` Output:**
```
İlk Satır
```
**`print(dosya.readline(3))` Output:**
```
İlk
```
**`print(dosya.readline(100))` Output:**
```
'İlk Satır
'
```
**Not:** En son output'da da gördüğünüz gibi, `readline()` methodu, sadece bir satırı okuduğu için `sayı` parametresine o satırdan daha uzun bir değer girilirse, satırın en sonuna kadar alır ve döndürür.

### `readlines(sayı = -1)` Methodu
Bir dosyanın bütün satırını okuyup döndürür. Bu output, list data type'ındadır. Bu output'da kaçış dizileri gibi python'un gördüğü ama kullanıcının göremediği şeyler görünür. Yani output, **Python'un gözünden** verilir. Eğer `sayı` parametresi belirtilirse, imlecin güncel konumundan, bu parametreye girilen integer'ın belirttiği uzunluktaki karakterleri içeren bütün satırları döndürür. `sayı` parametresine `None` ya da negatif bir integer değer girilirse, boş parametre girildiği zamanki davranışın aynısını sergiler. Bu durumu örnekleyelim:
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

print(dosya.readlines())
print(dosya.readlines(9))
print(dosya.readlines(10))

dosya.close()
```
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.readlines())` Output:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**`print(dosya.readlines(9))` Output:**
```
['İlk Satır\n']
```
**`print(dosya.readlines(10))` Output:**
```
['İlk Satır\n', 'İkinci Satır\n']
```
Gördüğünüz gibi, dosya içindeki ilk index'e 1 numaralı karakter dersek, 9 numaralı karaktere kadarki alan birinci satır olarak kabul ediliyor. Bu yüzden `sayı` parametresine `10` sayısını girdiğimizde, 2. satıra geçtiğimiz için 2. satırın tamamını alıyor. Yani bir satırı alması için o satıra geçmiş olmamız yetiyor.


### `readable()` Methodu
Dosyanın okunabilir olup olmamasını sorgulayabilmemizi sağlar. Okunabilir bir doyaysa `True`, değilse `False` döndürür.
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

print(dosya.readable()) # Output: True

dosya.close()
```


### `seek(offset, whence = SEEK_SET)` Methodu
`seek()` methodu, imleci, `offset` parametresinde belirtilen konumdaki byte'a konumlandırmanızı sağlar. Bu konumlandırmayı yaparken kaçış dizilerini de dikkate alır. Örneğin, `offset` parametresine `2` değerini girersek, imleci 2. index'deki byte'a konumlandırır ve sonrasında yapılacak **write** (yazma) ve **read** (okuma) işlemlerini, 2. index'deki byte'ı dahil ederek yapar. Bu konumlandırmayı, index'lerdeki karakterlere göre değil, byte'lara göre yapar. Örneğin `"i"` karakteri, `utf-8` kod çözücüde 1 byte ile temsil edilirken, `"İ"` karakteri, `utf-8` kod çözücüde 2 byte ile temsil edilir. Bu yüzden aşağıdaki gibi bir durumla karşılaşılabilir:

**Dosya:**
```
ilk Satır
İkinci Satır
Üçüncü Satır.
```
**Kod:**
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

dosya.seek(2)
print(dosya.read())

dosya.close()
```
**Output:**
```
k Satır
İkinci Satır
Üçüncü Satır.
```
Buradaki `"i"` karakteri, `utf-8` kod çözücüde 1 byte ile temsil edildiği için sıfırıncı ve birinci index'lerdeki byte'ları (`"il"`) atlayıp, 2. index'deki byte'dan itibaren (2. index'deki byte dahil) `read()` methodunu çalıştırdı.
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Kod:**
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

dosya.seek(2)
print(dosya.read())

dosya.close()
```
**Output:**
```
lk Satır
İkinci Satır
Üçüncü Satır.
```
Buradaki `"İ"` karakteri, `utf-8` kod çözücüde 2 byte ile temsil edildiği için sıfırıncı ve birinci index'lerdeki byte'ları (`"İ"`) atlayıp, 2. index'deki byte'dan itibaren (2. index'deki byte dahil) `read()` methodunu çalıştırdı.

`whence` parametresinde ise, imleci konumlandırırken kullanacağı ölçütü belirleyebilirsiniz. `whence` parametresine `SEEK_SET` ya da `0` girilirse, dosyanın başını referans alır ve `offset` sıfır ya da positif integer'lar olmalıdır; `SEEK_CUR` ya da `1` girilirse, mevcut (current) konumu (reading, writing işlemlerinde ya da `seek()` methoduyla değişen konum) referans alır ve `offset` negatif integer'lar olabilir; `SEEK_END` ya da `2` girilirse, dosyanın sonunu referans alır ve `offset` genellikle negatif integer'lardır. `whence` parametresine 1 ya da 2 argumanlar kullanılacaksa, dosya binary (`rb`, `wb`, `ab`, `xb`, `rb+`, `wb+`, `ab+`, `xb+`) modda açılmalıdır. Dosya binary modda açılmazsa, bu argumanları kullandığınızda `io.UnsupportedOperation: can't do nonzero end-relative seeks` hatası alırsınız.

### `seekable()` Methodu
`seek()` methodundaki gibi, bir dosya, file stream'a erişime (access) izin veriyorsa, o dosya seekable'dir. `seekable()` methodu, bir dosya seekable ise `True`; seekable değilse, yani `seek()`, `tell()` ve `truncate()` methodları `OSError` döndürüyorsa, `False` döndürür.

### `tell()` Methodu
İmlecin, o anda bulunduğu byte konumunu söyler. Örnek:
**Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Kod:**
```py
dosya = open(r"deneme.txt", mode="r", encoding="utf-8")

dosya.readline(100)
print(dosya.tell()) # Output: 12

dosya.close()
```

### `truncate(size = None)` Methodu
Uygulandığı dosyayı byte cinsinden yeniden boyutlandırmak için kullanılır. Size parametresi girilmezse (Yani default değer olan `None` değerine eşitse), current position'un konumunu değiştirmeden, current position'dan (current position'u **dahil etmeden**) itibaren siler. 

**Eski Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Kod:**
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

dosya.seek(6)
dosya.truncate()

dosya.close()
```
**Yeni Dosya:**
```
İlk S
```
`size` parametresi girilirse, bu parametreye girilen integer değerin belirttiği index'deki byte'dan itibaren (belirtilen index'deki byte'ı **dahil etmeden**) siler.
**Eski Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Kod:**
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

dosya.truncate(6)

dosya.close()
```
**Yeni Dosya:**
```
İlk S
```

### `write("string")` Methodu
Dosyaya bir adet string girebilmenizi sağlar. O anda imleç, yazılacak dosyanın neresindeyse, oradan yazmaya başlar. İmlecin bulunduğu yerde yazı varsa, `write()` methoduna girilen değer, bu yazının üzerine yazılır. Yani:
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

dosya.write("Deneme")

dosya.close()
```
**Eski Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Yeni Dosya:**
```
Denemeatır
İkinci Satır
Üçüncü Satır.
```

### `writelines([list])` Methodu
Dosyaya birden fazla string girebilmenizi sağlar. Girmek istenilen stringler, bir liste içinde gösterilir. O anda imleç, yazılacak dosyanın neresindeyse, oradan yazmaya başlar. İmlecin bulunduğu yerde yazı varsa, `writelines()` methoduna girilen değer, bu yazının üzerine yazılır. Yani:
```py
dosya = open(r"deneme.txt", mode="r+", encoding="utf-8")

dosya.writelines(["deneme1", "\ndeneme2"])

dosya.close()
```
**Eski Dosya:**
```
İlk Satır
İkinci Satır
Üçüncü Satır.
```
**Yeni Dosya:**
```
deneme1
deneme2inci Satır
Üçüncü Satır.
```
**Dikkat:** Bu üzerine yazma olayında, üzerine yazılan satırın uzunluğu, üzerine yazdığının uzunluğundan küçükse (`İlk Satır`'ın `deneme1deneme2`'den küçük olması gibi) aşağıdaki gibi absürt durumlar oluşabilir.
```
deneme1deneme2�kinci Satır
Üçüncü Satır.
```

### `writable()` Methodu
Dosyanın yazılabilir olup olmamasını sorgulayabilmemizi sağlar. Yazılabilir bir doyaysa `True`, değilse `False` döndürür.
```py
dosya = open(r"deneme.txt", mode="w", encoding="utf-8")

print(dosya.writable()) # Output: True

dosya.close()
```

## İkili (Binary) Dosyalar
Dosyalar, metin ve ikili (binary) dosyalar olarak ikiye ayrılır. Metin dosyalarının satır sonu işlemleri, GNU/Linux dağıtımlarında `\n`, Windows işletim sisteminde `\r\n` karakterleriyle gösterir. Python herhangi bir dosyayı açarken, eğer o dosya bir metin dosyası ise, satır sonlarını gösteren karakterleri, dosyanın açıldığı işletim sistemine göre ayarlar. Yani satır sonlarını standart bir hale getirerek `\n` karakterine dönüştürür. Bir binary dosyayı metin dosyası gibi (`r`, `w`, `a`, `x`, `r+`, `w+`, `a+`, `x+`) açarsanız, metin ve binary dosyalardaki satır sonu işlemleri farklı olduğu için binary dosya bozulabilir. Binary dosyaları binary kipine sahip modlarda (`rb`, `wb`, `ab`, `xb`, `rb+`, `wb+`, `ab+`, `xb+`) açarsanız, Python satır sonlarına herhangi bir değiştirme-dönüştürme işlemi uygulamaz ve dolayısıyla dosya bozulma riskine girmez.

### PDF Dosyaları
PDF belgelerinde, o belge hakkında bazı önemli bilgiler veren birtakım özel etiketler bulunur. Bu etiketler şunlardır:
| Etiket | Anlamı |
|--------|--------|
| `/Creator` | Belgeyi oluşturan yazılım |
| `/Producer` | Belgeyi PDF’e çeviren yazılım |
| `/Title` | Belgenin başlığı |
| `/Author` | Belgenin yazarı |
| `/Subject` | Belgenin konusu |
| `/Keywords` | Belgenin anahtar kelimeleri |
| `/CreationDate` | Belgenin oluşturulma zamanı |
| `/ModDate` | Belgenin değiştirilme zamanı |
Bu etiketlerin tamamı bütün PDF dosyalarında tanımlı değildir. Ama özellikle `/Producer` etiketi her PDF dosyasında bulunur. `/Producer` etiketinin devamı `b'/Producer (Acrobat Distiller 2.0 for Macintosh)\r/T` şeklinde olabilir. `/Producer` ifadesinin dosya içinde geçtiği noktanın sıra numarasını bulmak için:
```py
with  open("xxx.pdf", "rb") as dosya:
	okunan = dosya.read()
	producer_index = okunan.index(b"/Producer")
	print(producer_index) # Output Örneği: 4077883
```
**Not:** Buradaki `producer_index` variable'ı, `index()` methodu sayesinde `b"/Producer"` ifadesinin ilk bayt'ının dosya içindeki konumunu tutuyor. Yani `/` karakterini tutuyor. Sağlamasını yapmak için `print(chr(okunan[producer_index]))` kodunu çalıştırırsanız, `/` outputunu alırsınız.

### JPEG Dosyaları
JPEG dosyalarının en başında aşağıdaki veriler bulunur:
```
FF D8 FF E0 ? ? 4A 46 49 46 00 (Heksadesimal)
255 216 255 224 ? ? 74 70 73 70 0 (Decimal)
```
JPEG dosyası bir CANON fotograf makinesi ile oluşturulmuşsa bu veriler aşağıdaki gibidir:
```
FF D8 FF E0 ? ? 45 78 69 66 00 (Heksadesimal)
255 216 255 224 ? ? 45 78 69 66 0 (Decimal)
```
Bir JPEG dosyasını diğer resim dosyalarından ayırt etmek için JPEG dosyasının ilk 4 byte'ttan sonra gelen 2 byte'ı atlayıp, sonraki 5 byte'ı kontrol etmemiz yeterlidir. Bu ilk 11 byte'ın 7-10 byte'ları araında (7 ve 10 dahil) `"JFIF"` ya da `"Exif"` ifadelerine karşılık gelen byte'lar varsa bu dosya bir JPEG dosyasıdır. Bunu kontrol etmek için şöyle bir kod yazılabilir:
```py
with  open("xxx.jpeg", "rb") as dosya:
	data = dosya.read()
	if data[6:11] in [b"JFIF", b"Exif"]:
		print("Bu bir JPEG dosyasıdır.")
	else:
		print("Bu bir JPEG dosyası değildir.")
```
**Not:** Bir JPEG dosyasının ilk 10 byte'ını okuttuğunuzda karşınıza aşağıdaki gibi output'lar gelebilir:
```
b'\xff\xd8\xff\xe0\x00\x10JFIF'
b'\xff\xd8\xff\xe1T\xaaExif'
```
Buradaki `/x` kısımlarını temizlersek `'ff d8 ff e0 00 10 J F I F'` tarzı bir format elde ederiz.

**Not:** JPEG dosya biçimi ile ilgili bilgi edinmek için [bu siteyi](https://jpeg.org/) ve yardımcı kaynak için [bu siteyi](http://www.faqs.org/faqs/jpeg-faq/part1/section-15.html) kullanabilirsiniz.

### PNG Dosyaları
PNG dosyasının ilk 8 byte'ı mutlaka aşağıdaki değerleri içerir:
```
"137 80 78 71 13 10 26 10" (decimal)
"89 50 4e 47 0d 0a 1a 0a" (hexadecimal) (b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a")
"\211 P N G \r \n \032 \n" (string)(b"\211PNG\r\n\032\n")
```
Bir dosyanın PNG dosyası olup olmadığını sorgulamak için aşağıdaki kodu kullanabilirsiniz:
```py
with  open("xxx.png", "rb") as dosya:
	okunan = dosya.read(8)
	if okunan == b"\211PNG\r\n\032\n":
		print("Bu bir PNG dosyasıdır.")
	else:
		print("Bu bir PNG dosyası değildir.")
```
**Not:** PNG dosya biçiminin teknik şartnamesine ulaşmak için [bu siteyi](http://www.libpng.org/pub/png/spec/) ve yardımcı kaynak için [bu siteyi](https://www.fileformat.info/format/png/egff.htm) kullanabilirsiniz.

### GIF Dosyaları
Bir GIF dosyasının ilk üç byte'ı `GIF` karakterlerinden oluşur. Dolayısıyla bir dosyanın GIF dosyası olup olmadığını anlamak için ilk üç byte'ını okumak yeterlidir:
```py
with  open("xxx.gif", "rb") as dosya:
	okunan = dosya.read(3)
	if okunan == b'GIF':
		print("Bu bir GIF dosyasıdır.")
	else:
		print("Bu bir GIF dosyası değildir.")
```
**Not:** GIF standartlarının Mayıs 1987 sürümünde, bir GIF dosyasının ilk altı baytı `GIF87a`; Temmuz 1989 sürümünde, bir GIF dosyasının ilk altı baytı `GIF89a` karakterlerinden oluşur. GIF şartnamesine ulaşmak için [bu siteyi](https://www.w3.org/Graphics/GIF/spec-gif89a.txt) kullanabilirsiniz.

### TIFF Dosyaları
Bir TIFF dosyasının ilk iki byte'ı `II` ya da `MM` karakterlerinden oluşur:
```py
with  open("xxx.tiff", "rb") as dosya:
	okunan = dosya.read(2)
	if okunan in [b'II', b'MM']:
		print("Bu bir TIFF dosyasıdır.")
	else:
		print("Bu bir TIFF dosyası değildir.")
```
**Not:** TIFF şartnamesine  ulaşmak için [bu siteyi](https://partners.adobe.com/public/developer/en/tiff/TIFF6.pdf) kullanabilirsiniz.

### BMP Dosyaları
Bir BMP dosyasının ilk iki byte'ı `BM` karakterlerinden oluşur:
```py
with  open("xxx.bmp", "rb") as dosya:
	okunan = dosya.read(2)
	if okunan == b'BM':
		print("Bu bir BMP dosyasıdır.")
	else:
		print("Bu bir BMP dosyası değildir.")
```
**Not:** BMP türündeki resim dosyalarına ilişkin bilgi için [bu siteyi](https://www.loc.gov/preservation/digital/formats/fdd/fdd000189.shtml) kullanabilirsiniz.
