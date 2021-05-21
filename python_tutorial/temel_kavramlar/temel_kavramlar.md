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

# Python sürümleri
Python’ın `2.x` serisi ile çalışan bir program Python’ın `3.x` serisi ile muhtemelen çalışmayacaktır. Aynı şekilde bunun tersi de geçerlidir. Bu gibi durumlarda kullanıcıya bir uyarı mesajı göstermek gerekebilir. Kodlarınıza `#!/usr/bin/env pythonX.X veya #! pythonX.X` gibi bir satır eklemek bir çözüm olabilir ama yeterli değildir. Bu satırlar programınızın pythonX.X sürümünde çalışmadığını belirtmiş oluyorsunuz ama eğer çalıştırılırsa ne olacağını belirtmiyorsunuz. Buna çözüm olarak "sys" modülündeki "versiyon_info" değişkeninden yararlanabiliriz.
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
Veya kesin çözüm olarak, python'un bütün sürümlerinde çalışan aşağıdaki yöntemi kullanabilirsiniz:
```py
import sys

major = sys.version_info[0]
minor = sys.version_info[1]
micro = sys.version_info[2]  

print(major, minor, micro, sep=".") # Python sürümünü gösterir
```

# CMD ile çalışmak
- Herhangi bir klasör içinde ya da desktop'ta cmd açmak için `shift`'e basılı tutarken ekrana sağ tıklarsanız, karşınıza çıkan arayüzde PowerShell'i açabilirsiniz.
<img src="https://i.ibb.co/vPjX3nS/resim-2021-05-02-123605.png" alt="resim-2021-05-02-123605" border="0">

- Herhangi bir klasör açıkken arama çubuğuna cmd yazarsanız, o konuma ayarlı bir cmd penceresi açılır. O konumdaki bir python dosyasını çalıştırmak için `python dosya_ismi.py` komutunu kullanabilirsiniz.
<img src="https://i.ibb.co/JQczTMn/resim-2021-05-02-124133.png" alt="resim-2021-05-02-124133" border="0">

- cmd'yi çalıştırdıktan sonra herhangi bir adrese gitmek istiyorsanız `cd adres` komutunu kullanabilirsiniz. Örnek: `cd desktop/Files`

