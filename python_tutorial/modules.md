# Modules (Modüller)
Bazı işlevleri kolaylıkla yerine getirmemizi sağlayan birtakım function'ları ve attribute'ları içinde barındıran araçlardır/kütüphanelerdir. Bir fonksiyonu farklı python dosyalarında kullanabilmek için o fonksiyonu her dosyada tekrardan tanımlamak yerine modül olarak kullanılabilir. Kullanacağınız fonksiyonları bir python dosyasına tanımladıktan sonra o dosyayı `import` ederek içindeki fonksiyonları kullanabilirsiniz. Yani python ile yazdığınız her dosya, potansiyel bir modüldür. İmport ettiğin dosya **Module (Modül)** olarak isimlendirilir. Python3'deki standart modüller için [tıklayınız](https://docs.python.org/3/library/).

## `import` Statement
Modülleri içe aktarmak için `import` keyword'ünü kullanırız.
```py
import random # random modülündeki her şeyi içe aktarır.
print(dir(random)) # random ile ilgili bütün fonksiyon ve nitelikleri ekrana basar.
```
Bu şekilde import edilen modüller `module_name.function_or_attribute` syntax'ıyla kullanılır. Örnek:
```py
import random
print(random.randint(3, 9)) #  Output: 4
```
Bir modülü, function ya da class gibi bir local scope'da da import edebiliriz. Örnek:
```py
def module_imported():
    import random
```
**Not:** Bir modül dosyasını programınızın içine import edebilmeniz için 3 seçeneğiniz vardır.
1. Modül dosyasıyla program dosyası aynı path'da (dizin, dosyaların konumu.) olmalıdır.
2. Modül dostası Python Lib'de olmalıdır. Bu klasör HP bilgisayarlarda `C:\Users\HP\AppData\Local\Programs\Python\Python39\Lib` path'ında bulunabilir. Buradaki `Python39`, python sürümünüze göre değişiklik gösterebilir.
3. `sys.path`, python, import edilmeye çalışılan bir modül dosyasını ararken baktığı path'ların tuttuğu, `sys` modülünde bulunan bir listedir. Modül dosyası ile program dosyası, `D:\main_dosya\modules\modul.py` ve `D:\main_dosya\program\main.py` gibi birbiriyle alakasız iki klasör içindeyse `sys` modülündeki `sys.path` methoduna, modülünüzün bulunduğu path'ı `sys.path.append(r"D:\main_dosya\modules")` örneğindeki gibi eklerseniz, daha sonra o path'da bulunan modülünüzü normal `import modul` şeklinde import edip kullanabilirsiniz. Pylance gibi extension'lar bu yöntemi algılayamayıp, `import modul` kodundaki `modul` modülünü bulamadığı için `Import "modul" could not be resolved` hatası verebilirler. Bunlara aldırmanıza gerek yoktur çünkü kodunuz çalışır. Yine de her ihtimale karşı `print(sys.path)` kodunun döndürdüğü liste'de, `sys.path.append()` ile eklediğiniz path varmı diye kontrol etmekte fayda var.

## `as` Keyword'ü
Bir modülü, programınız içerisinde başka bir isimle kullanmak için `as` keyword'ü kullanılır.
```py
import random as sallama # artık 'random' modülünü 'sallama' adıyla kullanabiliriz.
print(sallama.randint(3, 9)) # Output: 6
```

## `from` Keyword'ü
Bir modüldeki spesifik bir function ya da attribute'ü import etmek için kullanılır. Bu şekilde import edilen function ya da attribute, direkt kullanılabilir. Örnek:
```py
from random import randint # random modülündeki randint() function'ını içe aktarır.
print(randint(3, 9)) # Output: 7
```
İmport ettiğiniz function ya da attribute'ün ismini değiştirmek için:
```py
from random import randint as sayi_sec # random modülündeki randint() function'ını, 'sayi_sec' adıyla içe aktarır.
print(sayi_sec(3, 9)) # Output: 5
```
Bir modülden, birden fazla spesifik function ya da attribute import etmek için:
```py
from os import name, listdir, getcwd # os modülündeki name attribute'ünü, listdir ve getcwd function'larını içe aktarır.
```
Modüldeki her şeyi aktarmak için:
```py
from random import *

print(random()) # Output: 0.4278806407713517
print(uniform(2.965, 3.117)) # Output: 2.995864919051282
print(randint(3,9)) # Output: 8
print(randrange(3,9)) # Output: 7 
```
Modüldeki her şeyi, function ya da class gibi bir local scope'da import etmeye çalışırsak `SyntaxError: import * only allowed at module level` hatası alırız çünkü yıldızlı içe aktarma işlemleri ancak modül seviyesinde, yani global scope'da gerçekleştirilebilir. Örnek:
```py
def module_imported():
    from random import *
```
**Not:** Bu tavsiye edilen bir yöntem değildir çünkü ihtiyacınız olan olmayan her şeyi python dosyasının içine aktardığınız için performans dostu bir yöntem sayılmaz. Ek olarak, `from modül_adı import *` şeklinde import ettiğiniz modülün function ve attribute'leri ile, sizin yazdığınız function ve attribute'ler çakışabilir. Örnek:
```py
from random import randint

def randint(p1,p2):
    return p1+p2

print(randint(3,9)) # Output: 12
```
```py
def randint(p1,p2):
    return p1+p2

from random import randint

print(randint(3,9)) # Output: 6
```
