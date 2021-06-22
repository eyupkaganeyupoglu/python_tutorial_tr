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

**Not:** Bir modülü import ettikten sonra, modül dosyasında bir değiliklik yaparsanız (Örneğin yeni bir fonksiyon eklerseniz), modülü import ettiğiniz dosya bu değişiklikleri tanımaz (yani yeni eklediğiniz fonksiyonu kullanamazsınız). Bunun önüne geçmek için, `importlib.reload(modül_adı)` modül methodunu kullanarak modülünüzü **reload** yapabilirsiniz. Modülü tekrardan `import modul` şeklinde import etmek işe yaramaz. `importlib.reload(modül_adı)` kullanın.

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

# Bazı Attribute'ler

## `__all__` Attribute
Python'da `import modul` ile `from modul import *` komutlarının içeri aktardıkları, içinde function ve attribute'ların bulunduğu grup birbirinden farklıdır.
```py
import_modul = ['__builtins__', '__cached__', '__doc__', '__file__', '__fonk7', '__loader__', '__name__', '__package__', '__spec__', '_fonk6', 'fonk1', 'fonk2', 'fonk3', 'fonk4', 'fonk5', 'fonk8_']
form_modul_import =['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'fonk1', 'fonk2', 'fonk3']
for i in import_modul:
    if not i in form_modul_import: # import_modul'de olup, form_modul_import'de olmayan. 
        print(i, end=" , ") 
```
**Output:**
```
__cached__ , __file__ , __fonk7 , _fonk6 , fonk4 , fonk5 , fonk8_
```
`import modül` de her şeyi içeri import ederken, `from modül import *` da test ve private olanları (yani `_` ile başlayanları) import etmez. Spesifik olarak import etmek istediklerinizi `from modül import _örnek` şeklinde import edebilirsiniz. Tabi böyle yapabilmek için fonksiyonun ismini biliyor olmalısınız. `__all__` , import edilmesini istediğiniz ve istemediğiniz fonksiyonları belirlemenize izin verir. Örneğin `modül.py`'nin en başına `__all__ = ['fonk1', 'fonk2', 'fonk3']` eklerseniz, `from modül import *` yaptığınızda `form_modul_import` listesindekiler import edilir. `__all__ = []` kullanımında, modülün kendi varsayılan fonksiyonları hariç hiçbir fonksiyon içe aktarılmaz.

**Not:** Örneğin Bir fonksiyon yazdınız. Bu fonksiyonu öyle yazıyorsunuz ki, başka birisi bu fonksiyonu sadece kopyala yapıştır yaparak kendi programına entegre edebiliyor. Buna **code reusability** denir. Yani kodların yeniden kullanılabilir özellikte olmasına **code reusability** denir. Bu kodların kolayca test edilebilmesine de **code testability** denir. Daha fazla bilgi için [tıklayınız](https://medium.com/aykiri-yazilimcilar/kaliteli-yazılım-tasarımı-ve-anti-patternler-üzerine-notlar-a8f9ccfb6847)

## `__import__(name, globals=None, locals=None, fromlist=(), level=0)` Attribute
`__import__`, modül adını `name` parametresine girerek, herhangi bir modülü içe aktarmamızı sağlayan bir araçtır. Örneğin `vrb = __import__('random')` yaptıktan sonra random modülünün fonksiyonlarını ve attribute'lerini `vrb.randint(45, 500)` örneğindeki gibi kullanabilirsiniz. Bir variable'a atamadan kullanmak istiyorsanız `__import__('random').randint(45, 500)` şeklinde kullanabilirsiniz. Daha fazla bilgi için [tıklayınız](https://docs.python.org/3/library/functions.html#__import__)

## `__doc__` Attribute
**Ön Bilgi:** Teknik dilde, üç tırnak `""" Falan Filan """` içinde gösterilen karakter dizilerine belge dizisi (docstring) veya belgelendirme dizisi (documentation string) adı verilir.

Modüllerin `__doc__` niteliğini kullanarak, bir modül dosyasının en başında bulunan belgelendirme dizilerine erişebiliriz. Bu belgelendirme dizileri, modülle ilgili açıklamalar içerir. Aynı şeye `help()` fonksiyonunu kullanarak da erişebilirsiniz. Örneğin `help(os)` kullanarak `os` modulündeki bu bilgilendirme belgesine ulaşabilirsiniz. Bu belgelendirme dizileri, üç tırnak içinde belirtilir. Örnek:
```py
# Modül Dosyası
"""
Falan
Filan
"""
```
```py
# Program Dosyası
import modul
print(modul.__doc__)
```
**Output:**
```
Falan
Filan
```
çift veya tek tırnak ile belirlediğimiz karakter dizilerine __doc__ ile erişmek istersek sadece ilk satırdaki karakter dizisine erişebiliriz. Örnek:
```py
# Modül Dosyası
"Falan"
"Filan"
```
```py
# Program Dosyası
import modul
print(modul.__doc__)
```
**Output:**
```
Falan
```

## `__name__` Attribute
Her fonksiyon ve modül `__name__` attribute'sine sahiptir. Bu basitçe o fonksiyon ya da modülün ismi ya da spesifik bir şey olabilir.
```py
import modul
print(modul.__name__) # Output: modul
```

## `__loader__` Attribute
Bu attribute, ilgili modülü içe aktaran mekanizma hakkında bize çeşitli bilgiler veren birtakım araçlar sunar. Örnek:
```py
import os
yükleyici = os.__loader__
print(dir(yükleyici))
```
**Output:**
```
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__weakref__', '_cache_bytecode',
 'exec_module', 'get_code', 'get_data', 'get_filename', 'get_source',
 'is_package', 'load_module', 'name', 'path', 'path_mtime', 'path_stats',
 'set_data', 'source_to_code']
```

## `__spec__` Attribute
`__spec__` attribute, modüller hakkında çeşitli bilgiler sunan birtakım araçları içinde barındırır.
```py
import random
print(dir(random.__spec__))
```
**Output:**
```
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
 '_cached', '_initializing', '_set_fileattr', 'cached', 'has_location',
 'loader', 'loader_state', 'name', 'origin', 'parent', 'submodule_search_locations']
```
Mesela bir modülün ad ve konum bilgilerine ulaşmak için bu niteliği kullanabiliriz.
```py
import random
print(random.__spec__.name, random.__spec__.origin, sep="\n")
```
**Output:**
```
random
C:\Users\XXX\AppData\Local\Programs\Python\Python39\lib\random.py
```