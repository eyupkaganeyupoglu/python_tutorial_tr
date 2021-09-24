# İçindekiler

- [Context Manager ve `with` Statement](#1)

<h1 id="1">Context Manager ve <code>with</code> Statement</h1>

Context manager, kullanılan kaynakların geri iade edilmesi için ortaya çıkmış bir protocol'dür. Kaynaklar sınırsız değildir ve işletim sistemiden işletim sistemine boyutu değişir. Devamlı kaynak edinip geri iade etmezseniz, işletim sisteminiz bir noktadan sonra size engel (`OSError`) olacaktır.

Context manager, işletim sistemi kaynağının sadece belitlenen bir context'de geçerli olmasını sağlar ve bu context'den çıkınca bu kaynak, Python tarafından otomatik olarak yok ediliyor. Bu protocol'ü kullanabilmemiz için belli kurallara uygun class'lar, construction'lar oluşturmamız gerekir. Context manager protocol'üne uygun yazdığımız class'ları kullanırken de `with` statement'den yararlanacağız.

Python'da, harici kaynak (external resources) kullanımı ve kaynakların geri iadesi için kullanılan `with` statement bulunmaktadır. `with` statement, bu işlemleri **context management** protocol'üne uygun olarak yapmaktadır. `with` statement'in syntax'ı:
```py
with <expression> as <identifier>:
    # processes
```

Aşağıdaki yapı, Context manager protocol'üne uygun bir yapıdır:
```py
try:
    # Dosyayı aç
    dosya = open(r"{}deneme.txt".format(__file__[:-6]), mode="r+", encoding="utf-8")
    # Dosya işlemleri
    dosya.write("Falan filan")
except IOError:
    # Exception IO HATA MESAJI
finally:
    # Dosyayı kapat
    dosya.close()
```
Bu yapıyı `with` statement ile de oluşturabiliriz. Örnek:
```py
with open("deneme.txt", "w") as fw:
    fw.write("falan filan")
```

Context manager oluşturmanın 2 yöntemi vardır:
- Class Kullanmak
- `contexmanager` decorator kullanmak

**İlk yöntem:** Bir class'ın context manager protocol'üne uygun olabilmesi için `__enter__(self)` ve `__exit__(self, exc_type, exc_value, traceback)` method'larını bulundurması gerekiyor. Örnek:
```py
class A:
    def __init__(self):
        print("init çalıştı...")

    def __enter__(self):
        print('`__enter__` çağırıldı...')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('`__exit__` çağırıldı...')

with A() as f:
    print("with bloğunun içindeyim...")
```
**Output:**
```
init çalıştı...            (`A()`dan dolayı)
`__enter__` çağırıldı...   (`__enter__`den dolayı)
with bloğunun içindeyim... (with statement'ın kod bloğundan dolayı)
`__exit__` çağırıldı...    (`__exit__`den dolayı)
```
Çalışma mantığı böyle. Şimdi dosya işlemlerine entegre edelim. Örnek:
```py
class File:

    # Constructor metodumuzu yazalim
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        # Islemleri yapildigi metod
        self.f_obj = open(self.file_name, self.mode)
        return self.f_obj

    def __exit__(self, exc_type, exc_val, traceback):
        # Dosya kapama islemi
        self.f_obj.close()


with File('deneme.txt', 'w') as f_write:
    f_write.write('Test...')
    print(f"Dosya kapatıldı mı? [With Body] -> {f_write.closed}") # Output: Dosya Kapatildi mi? [With Body] -> False

print(f"Dosya kapatıldı mı? [Out of with body] -> {f_write.closed}") # Output: Dosya kapatıldı mı? [Out of with body] -> True
```
Burada `with File('deneme.txt', 'w')` kısmında `__init__` kısmı, `as f_write` kısmında `__enter__` kısmı çalışıyor ve `return self.f_obj` kodundaki döndürülen `f_obj` dosya objesi `f_write` identifier'ına atanıyor. `with` bloğunda birtakım işlemler yaptıktan sonra `with`'den çıkınca dosya objesi otomatik olarak kapatıldığı için `__exit__` çalışıyor ve dosya objesi yok ediliyor (iade ediliyor, yok ediliyor (destroy) vs.)

İkinci yöntem: `contextmanager` decorator'ı:
```py
from contextlib import contextmanager

@contextmanager
def dosyaisleme(dosya_adi, mod):
    dosya = open(dosya_adi, mod)  # contextmanager decorator'ı bu kısmı __init__ işleminde kullanır
    yield dosya                   # contextmanager decorator'ı bu kısmı __enter__ işleminde kullanır
    dosya.close()                 # contextmanager decorator'ı bu kısmı __exit__ işleminde kullanır

with dosyaisleme('deneme.txt', 'w') as f_write:
    f_write.write('Test...')
    print(f"Dosya kapatıldı mı?[With Body] -> {f_write.closed}") # Output: Dosya kapatıldı mı?[With Body] -> False

print(f"Dosya kapatıldı mı?[Out of with body] -> {f_write.closed}") # Output: Dosya kapatıldı mı?[Out of with body] -> True
```
Burada `with File('deneme.txt', 'w')` kısmına kadar `dosya = open(dosya_adi, mod)` kısmı, `as f_write` kısmında `yield dosya ` kısmı çalışıyor ve `dosya` objesi `f_write` identifier'ına atanıyor. `with` bloğunda birtakım işler yaptıktan sonra `with`'den çıkınca dosya otomatik olarak kapatıldığı için `dosya.close()` çalışıyor ve dosya objesi yokediliyor (iyade ediliyor, yok ediliyor (destroy) vs.). Python'da zaten `open` fonksiyonu olduğu için `dosyaisleme` gibi bir fonksiyona ihtiyacınız yok. (Buradaki `yield` statement'i daha sonra göreceksiniz)

`@contextmanager` decorator yapısının kodunu incelersek `contextlib.py` içerisindeki `_GeneratorContextManager` isimli class'ı kullandığını göreceğiz. Class kodunu incelersek tıpkı bizim yazdığımız yapı gibi `__init__`, `__enter__` ve `__exit__` methodlarını göreceksiniz.

with deyiminin dosya işlemleri dışında da kullanıldığı bazı yerler:
- Context managerlar
- Descriptorlar ve property methodları
- `__slots__`
- `__new__()` özel metodu
- Singleton sınıflar (ve metaclasslar)
- Enumerationlar (enum modülü)
- Dekoratör fonksiyonlar
- Database, API bağlantıları

Yararlanabileceğiniz diğer kaynaklar:
- [Real Python](https://realpython.com/python-with-statement/)
- [Kerem Vatandas](https://medium.com/bilişim-hareketi/python-context-manager-159facf118bb)
- [Barış Şimşek](https://www.youtube.com/watch?v=XcY4jDj4VkE)
- [Python Tips](https://book.pythontips.com/en/latest/context_managers.html)
- [Geeks for Geeks](https://www.geeksforgeeks.org/with-statement-in-python/)