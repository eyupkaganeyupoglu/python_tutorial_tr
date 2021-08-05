# Python'un Çalışma Mantığı
Python, kodları yukarıdan aşağıya okur. İç içe yazılmış fonksiyonları da aşağıdaki örnekteki gibi okur:
```py
print(complex(float(int(str(10)))))
```
1. `print` var, aha parantez, `print`'i geç ve parantezin içine bak,
2. `complex` var, aha bir parantez daha, `complex`'i geç ve parantezin içine bak,
3. `float` var, aha bir parantez daha, `float`'ı geç ve parantezin içine bak,
4. `int` var, aha bir parantez daha, `int`'i geç ve parantezin içine bak,
5. `str` var, aha bir parantez daha, str'yi geç ve parantezin içine bak,
6. 10 var, tamam,
7. `str(10) --> "10"`,
8. `int("10") --> 10`,
9. `float(10) --> 10.0`,
10. `complex(10.0) --> 10+0j`,
11. `print(10+0j)` var, o zaman `10+0j`'yi `sys.stdout`'a bas.

## Block Mantığı
Python'da `if`, `elif`, `else`, `while`, `for`, `def`, `class` etc. gibi statementlere yazılacak kodlar, bu statementlerin **blocklarına** yazılır. Bu blockları oluşturmak için **Indentation** dediğimiz girintileme işlemi yapılır. Bu girintilere **Indent** denir. Bu indentler genelde 2 ya da 4 space'den oluşur. Bu indentler, bloğuna tanımlandığı statement'e bağımlıdır. Burada **Global** ve **Local** block kavramları devreye giriyor. Bunlar daha sonra anlatılacak.
```py
a = int(input()) # Blok 1'e ait kod (Global block)
if (a == 2):
	print("Doğru") # Blok 2'ye ait kod (Local block)
	
print("'Doğru' yazdıysa doğru değeri girmişsinizdir.") # Blok 1'e ait kod (Global block)
```

# Variable'lar (Değişkenler)
Variable'lar, en küçük depolama birimleridir. Belli bir data type'dan veri depolar. Bir değişkene bir değer atadıktan sonra aynı değişkene farklı bir değer atayabilirsin. Örnek:
```py
i = 15 # i'nin değeri 15
i = 30 # i'nin değeri 30
```
Variable'ları kullanarak işlem yapabilirsiniz. Örneğin:
```py
i = 15
j = 30
k = i + j
print(k) # Output: 45
```
İki variable'ın değerlerini birbiriyle değiştirebilirsiniz. Örnek:
```py
a = 5
b = 10
a,b = b,a
```
Bir variable'yi silmek istiyorsanız:
```py
a = 1
del a
```

# İsimlendirme kuralları
- Variable isimleri rakam (digit) ile başlayamaz ve sadece rakamlardan oluşamaz. Örnek: `1vrb`
- Variable isimlerinde boşluk karakteri kullanılamaz. Örnek: `vrb exp`
- `:`, `'`, `”`, `,`, `<`, `>`, `/`, `?`, `|`, `\`, `(`, `)`, `!`, `@`, `#`, `$`, `%`, `^`, `&`, `*`, `~`, `-`, `+` sembolleri kullanılamaz. Sadece `_` (alt çizgi) kullanılabilir. Aksi durumda `SyntaxError: invalid syntax` hatası verir.
- Keyword'ler identifier olarak kullanılamaz. Örnek: `global = 1`

# Implementation
"Uygulamak" anlamına gelir. Örneğin kurduğunuz bir algoritmayı koda döktüğünde algoritmayı implemente etmiş olursun. En basit tanımıyla bu. Ayrıntılı bilgi için kendiniz araştırabilirsiniz.

# Yorum (Comment) Satırları
### Tek satır yorum satırı:
```py
# Tekli Yorum Satırı
'Tekli Yorum Satırı'
"Tekli Yorum Satırı"
```

### Çoklu Yorum satırı
```py
"""
Çoklu
Yorum
Satırı
"""
```
**Dikkat:** Block kodlarda (Örneğin bir `if` bloğu) aralara tırnak içinde açıklama yazmamaya çalış. Mümkün oldukça `#` kullan.

# CMD ile çalışmak
- Herhangi bir klasör içinde ya da desktop'ta cmd açmak için `shift`'e basılı tutarken ekrana sağ tıklarsanız, karşınıza çıkan arayüzde PowerShell'i açabilirsiniz.
<img src="https://i.ibb.co/vPjX3nS/resim-2021-05-02-123605.png" alt="resim-2021-05-02-123605" border="0">

- Herhangi bir klasör açıkken arama çubuğuna cmd yazarsanız, o konuma ayarlı bir cmd penceresi açılır. O konumdaki bir Python dosyasını çalıştırmak için `python dosya_ismi.py` komutunu kullanabilirsiniz.
<img src="https://i.ibb.co/JQczTMn/resim-2021-05-02-124133.png" alt="resim-2021-05-02-124133" border="0">

- cmd'yi çalıştırdıktan sonra herhangi bir adrese gitmek istiyorsanız `cd adres` komutunu kullanabilirsiniz. Örnek: `cd desktop/Files`

# Python sürümleri
Python’ın `2.x` serisi ile çalışan bir program Python’ın `3.x` serisi ile muhtemelen çalışmayacaktır. Aynı şekilde bunun tersi de geçerlidir. Bu gibi durumlarda kullanıcıya bir uyarı mesajı göstermek gerekebilir. Kodlarınıza `#!/usr/bin/env pythonX.X veya #! pythonX.X` gibi bir satır eklemek bir çözüm olabilir ama yeterli değildir. Bu satırlar programınızın PythonX.X sürümünde çalışmadığını belirtmiş oluyorsunuz ama eğer çalıştırılırsa ne olacağını belirtmiyorsunuz. Buna çözüm olarak "sys" modülündeki "versiyon_info" değişkeninden yararlanabiliriz.
```py
sys.version_info(major=|major2|, minor=|minor2|, micro=|micro2|, releaselevel='final', serial=0)
```
Buradaki `major`, kullanılan Python serisinin ana sürüm numarasını; `minor`, alt sürüm numarasını; `micro`, kullanılan Python serisinin en alt sürüm numarasını verir. Bu değerlere:
```py
sys.version_info.major
sys.version_info.minor
sys.version_info.micro
```
komutlarıyla ulaşılabilir.
```py
import sys
_2x_metni = u" Python'ın 2.x sürümlerinden birini kullanıyorsunuz. Programı çalıştırabilmek için sisteminizde Python'ın 3.x sürümlerinden biri kurulu olmalı."

_3x_metni = "Programa hoşgeldiniz."

if (sys.version_info.major < 3):
	print(_2x_metni)
else:
	print(_3x_metni)
```
Program py2.x de çalıştırılırsa, `_2x_metni` variable'ına tanımlanmış karakter dizisinin düzgün gösterilmesi için `u` harfini eklememiz gerek. Bu sayede UNICODE olarak çalıştırmış olacak.

**Önemli Not:** Python’ın 2.7 öncesi sürümlerinde `sys` modülünün `version_info()` metodu farklı çıktılar verir. Mesela Python’ın 2.7 öncesi sürümlerinde `version_info()` metodunun `major`, `minor` veya `micro` gibi nitelikleri bulunmaz. Bu nitelikler Python programlama diline 2.7 sürümüyle birlikte geldi. Dolayısıyla yukarıdaki programı Python’ın 2.7 öncesi sürümlerinden biriyle çalıştıran kullanıcılarınız istediğiniz çıktıyı alamayacak, Python bu kullanıcılara hata mesajı göstererek programın çökmesine sebep olacaktır.
```py
import sys
  
_2x_metni = """ Python'ın 2.x sürümlerinden birini kullanıyorsunuz. Programı çalıştırabilmek için sisteminizde Python'ın 3.x sürümlerinden biri kurulu olmalı.""" 
_3x_metni = "Programa hoşgeldiniz."
  
try:
	if (sys.version_info.major < 3):
		print(_2x_metni)
	else:
		print(_3x_metni)
except  AttributeError:
	print(_2x_metni)
```
Veya kesin çözüm olarak, Python'un bütün sürümlerinde çalışan aşağıdaki yöntemi kullanabilirsiniz:
```py
import sys

major = sys.version_info[0]
minor = sys.version_info[1]
micro = sys.version_info[2]  

print(major, minor, micro, sep=".") # Python sürümünü gösterir
```

## Heap ve Stack Yöntemleri
Python programları sırasında kullanılan her değer, bellekte yer kaplar. Bu yerin boyutu kimi zaman belli yani değişmezken, kimi zaman ise kullanıcının program esnasında gireceği verilere göre değişebilecek durumdadır. Bu farkları sağlayan **Stack** ve **Heap** adında iki yöntem vardır. **Stack** ve **Heap**'in her ikisi de RAM bölgesinde bulunur. **Stack**, bellekten statik olarak yer tahsisi için kullanılırken, **Heap**, dinamik olarak yer tahsisi içindir. Bu yüzden program esnasında boyutları bildirilmiş, değişmez bir değer kullanacaksak ve bu değer çok büyük bir veri değilse (Stack alanı sınırlı olduğundan çok büyük sayıda ve büyük tiplerde veri atanması belleğin dolmasına sebep olabilir) **stack**, boyutu belli olmayan bir değer kullanıyorsak (ki OOP'de bunlara obje denir) o zaman derleyici otomatik olarak **Heap**’ten yer tahsisi yapar. **Stack**’te yer alan veriler direk bellek içine yerleştirilir, dolayısıyla erişimi çok hızlıdır ve programın derleme aşamasında belleğe yerleşirler. **Heap** ise runtime (çalışma zamanı) anında kullanılırlar ve dağınık bir bellek göz yapısı olduğu için erişimi **stack** kadar kolay olmaz, dolayısıyla yavaş çalışır. Daha fazla bilgi ve örnek için [tıklayınız](http://blog.bilgiyazan.com.tr/stack-ve-heap-kavrami/). Stack bellekteki veri hemen silinirken Heap bellekteki verinin silinmesi **Garbage Collector**’a (Çöp toplama mekanizmasına) bağlıdır. *Swift*, *Objective-C* gibi **Automatic Reference Counting**’e sahip mimarilerde bu konu derleyici tarafından otomatik olarak yapılır. **Stack** ve **Heap** bilgisi, dünyanın en vasat bellek yönetimine sahip scripting dillerinden birisi olan Python için çok gerekli bir şey değil. Python, bellekle uğraşmanızı gerektirecek bir dil değildir. Bellekle uğraşmanızı gerektirecek bir dil olan **C** dil ailesiyle işiniz olursa **Stack** ve **Heap** kavramlarına kafa yorunuz.

**Stack:**
- Kullanımı kolaydır.
- Tıpkı Heap gibi bilgisayarda RAM’de tutulur.
- Oluşturulan değişkinler stack kapsamından çıkınca otomatik olarak yok edilir.
- Ulaşılması Heap‘e göre oldukça hızlıdır.
- 20 boyutlu bir diziye 21 eleman atamak gibi, Stack üzerinde kullanım fazla olduğunda alan yeterli olmayabilir.
- Oluşturulan değişkenler pointer olmadan kullanılabilir.
- Derleme zamanında oluşturulur.
- Kullanacağınız yerin boyutunu tam olarak biliyorsanız Stack‘i kullanmak sizin için uygun olacaktır.
  
**Heap:**
- Kullanımı Stack'dan daha zordur.
- Bilgisayarda RAM’de tutulur.Tıpkı Stack gibi.
- Bir blok içerisinde oluşturulan heap değişkenler, bloğun dışına çıktığında otomatik olarak yok edilemez, bunun manuel olarak yapılması gerekir.
- Stack ile karşılaştırıldığında oldukça yavaştır.
- Doğru kullanılmaması durumunda bellek sorunları yaratır.
- Değişkenler pointer ile kullanılır.
- Çalışma zamanında oluşturulur.
- İhtiyacınız olan boyutu tam olarak bilmiyorsanız Heap kullanımı sizin için biçilmiş kaftandır.

### Garbage Collector
Bilgisayar programları, runtime sırasında bellek ihtiyacı duyarlar. Bellek sınırsız bir şey olmadığı için artık kullanılmayan bellek alanlarının, işletim sistemine geri iade edilmesi gerekir. Müsait bellek alanı bulma ve kullanılmayan bellek alanlarını işletim sistemine geri iade etme işlemleri, programcılar tarafından elle yapılması gerekiyordu. Örneğin bu işlem, **C** dilinde `malloc()` ve `free()` fonksiyonları ile yapılmaktadır. İşletim sistemine iade edilmiş bir alanın program tarafından tekrar kullanılması güvenlik açıklarını beraberinde getirmekteydi ve elle yapılan bu işlemin takibi, bir yerden sonra zorlaştığı için bu işi otomatik yapan bir sisteme ihtiyaç vardı. **Garbage Collector**, bu işlemi otomatik yapan bir sistemdir. Bu sistem sayesinde bir programcı, program yazarken hafıza alanını **Garbage Collection** mekanizmasından talep edip, iade işlemine karışılmamaktadır çünkü kalan tüm işlemler **Garbage Collection** mekanizması tarafından yapılmaktadır. **Garbage Collector**, kullanılan hafıza alanlarının izini sürerek, ihtiyaç duyulmayan alanları işletim sistemine iade etmektedir ve yeni bir talep geldiği zamanda bellekte yer bulup programa göndermektedir. **Garbage Collection** mekanizmasının işlemci kullanımı ile alakalı iki farklı yönetim yaklaşımı bulunmaktadır. 
- **stop-the-world** yaklaşımı, herhangi bir t zamanında **Garbage Collection** mekanizması devreye girdiği zaman sırasıyla, ilgili programdaki tüm işlemler durdurulur, hafıza yönetimi yapılır ve durdurulan işlemeler başlatılır. Bu çalışma yöntemi, kritik uygulamalar için bir dezavantaj oluşturmaktadır. Bu nedenle daha sonra **concurrent** algoritmalar geliştirilmiştir. 
- **Concurrent** yaklaşımı, programın çalışması durdurulmadan, programla eşzamanlı olarak  **Garbage Collection** işlemleri yapılır. Bu sayede **stop-the-world** yaklaşımının oluşturduğu dezavantaj ortadan kalkar.

# Hata Mesajlarının Önemi:
Python geliştirildikçe, hata mesajlarının çeşidi ve içeriğinin zenginliği de artmaktadır. Hata mesajlarını okumayı bilen ve bilmeyen kişiler arasındaki fark çok fazladır. Hata mesajlarını okumayı ve anlamayı becerebilmenin kişiye en büyük artısı **zamandır**. Çünkü Python bir hata yükseltince, hatanın hangi satırda ve kodun tam olarak neresinde olduğunu, hatanın neden oluştuğunu, hatta bazen hatanın çözümünü bile içeren bir hata mesajı gösterir kullanıcılara.