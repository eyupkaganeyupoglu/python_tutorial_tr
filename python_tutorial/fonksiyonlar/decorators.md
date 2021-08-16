# Decorators
Python, mevcut bir koda işlevsellik (functionality) eklemek için decorator adı verilen ilginç bir özelliğe sahiptir. Buna **metaprogramming** da denir. Çünkü programın bir kısmı, compile time sırasında programın başka bir kısmını değiştirmeye (modify) çalışır.

Python'da (Class'lar dahil) her şey bir objedir ve bir obje farklı isimlere (identifier) sahip olabilir. Örnek:
```py
def first(msg):
    print(msg)

second = first
first("Hello") # Output: Hello
second("Hello") # Output: Hello
```
Buradaki `first` ve `second` identifier'ları aynı fonksiyon objesine atıfta bulunmaktadır (refers to).

Bir fonksiyon başka bir fonksiyona argüman olarak verilebilir. Diğer fonksiyonları argüman olarak alan fonksiyonlara **higher order function** denir.
```py
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc, 3)) # Output: 4
print(operate(dec, 3)) # Output: 2
```
Buradaki `operate` higher order function'dır.

Ayrıca bir fonksiyon başka bir fonksiyonu döndürebilir. Örnek:
```py
def is_called():
    def is_returned():
        print("Hello")
    return is_returned

var = is_called()
var() # Output: Hello
```
Yukarıdaki gibi bir enclosing fonksiyonun içinde tanımlı nested fonksiyonu direkt `return` statement ile döndürmeye ve döndürülen fonksiyonu yukarıdaki gibi kullanmaya **Closure** denir. Closure'lar, global value'ların kullanımını önleyebilir ve bu sayede bir tür veri gizleme (data hiding) sağlar. Çünkü closure fonksiyondaki value'lar, fonksiyon çalışmayı sonlandırdıktan sonra bellekten silinir.

Closure'ın 3 şartı vardır:
- Nested fonksiyona sahip olmak
- Nested fonksiyon, enclosing fonksiyondaki en az bir value'ya atıfta bulunmalıdır (refers to).
- enclosing fonksiyon, nested fonksiyonu döndürmelidir.

Bu üç şartı sağlayan nested fonksiyonlar closure olur. Bütün fonksiyon objeleri `__closure__` methoduna sahiptir. Bu method, closure fonksiyonun kullandığı enclosing fonksiyondaki objeleri (variable, fonksiyon vs.) içeren cell'leri içeren bir `tuble`'dır. Bu cell'lerdeki objelere de `cell_contents` methodu ile ulaşabilirsiniz. Örnek:
```py
def make_multiplier_of(x,y,z,r):
    toplam = x+y+z
    çarpım = toplam * r

    def number_two():
        return 2

    def multiplier():
        result = ((toplam+x+y+z)*çarpım)+number_two()
        return result

    return multiplier

var = make_multiplier_of(1,2,3,4)
print(var.__closure__[0], ":", var.__closure__[0].cell_contents) # Output: <cell at 0x00000161CABE9FD0: function object at 0x00000161CABE5040> : <function make_multiplier_of.<locals>.number_two at 0x00000161CABE5040>
print(var.__closure__[1], ":", var.__closure__[1].cell_contents) # Output: <cell at 0x00000161CABE9FA0: int object at 0x00000161CA5F69D0> : 6 (toplam)
print(var.__closure__[2], ":", var.__closure__[2].cell_contents) # Output: <cell at 0x00000161CABE9E50: int object at 0x00000161CA5F6930> : 1 (x)
print(var.__closure__[3], ":", var.__closure__[3].cell_contents) # Output: <cell at 0x00000161CABE9E20: int object at 0x00000161CA5F6950> : 2 (y)
print(var.__closure__[4], ":", var.__closure__[4].cell_contents) # Output: <cell at 0x00000161CABE9DF0: int object at 0x00000161CA5F6970> : 3 (z)
print(var.__closure__[5], ":", var.__closure__[5].cell_contents) # Output: <cell at 0x00000161CABE9DC0: int object at 0x00000161CA5F6C10> : 24 (çarpım)
```
**Not:** Closure olma şartlarının hepsini sağlayamayan fonksiyonlar closure olamazlar. Closure olmayan fonksiyonların `__closure__` methodu `None` value'suna sahiptir.

Fonksiyonlar ve methodlar çağırılabilir olduklarından **callable** olarak adlandırılırlar. Aslında special `__call__()` methodunun uygulanan (implements) herhangi bir obje çağırılabilir (callable) olarak adlandırılabilir. Yani bir decorator, callable döndüren bir callable'dir . Basitçe decorator, callable bir objeyi alır, bazı işlevsellik (functionality) ekler ve onu döndürür (`return`). Bir fonksiyonu decore etmek için `@{function_name}` kullanılır. Örnek:
```py
def decorator_maker(func):
    def inner():
        print("Artık bu bir", end=" ")
        func()
    return inner

def decorator_exp():
    print("DECORATOR")

decorator_exp = decorator_maker(decorator_exp)
decorator_exp() # Output: Artık bu bir DECORATOR
```
```py
def decorator_maker(func):
    def inner():
        print("Artık bu bir", end=" ")
        func()
    return inner

@decorator_maker
def decorator_exp():
    print("DECORATOR")

decorator_exp() # Output: Artık bu bir DECORATOR
```
Bu iki koddan `decorator_exp = decorator_maker(decorator_exp)` kodu ile `@decorator_maker` decorator'ının eşdeğer olduğu sonucunu çıkarabilirsiniz.

Parametreli fonksiyonları aşağıdaki örnekteki gibi decore edip kullanıyoruz:
```py
def bölme(func):
    def inner(a, b):
        print(a, "ve", b, "sayılarının, bölme işlemine göre sonucu:", end=" ")
        if b == 0:
            print("Ops! Bölünemiyor...")
            return
        return func(a, b)
    return inner

@bölme
def bölme_işlemi(a, b):
    print(a/b)

bölme_işlemi(4,2) # Output: 4 ve 2 sayılarının, bölme işlemine göre sonucu: 2.0
bölme_işlemi(2,0) # Output: 2 ve 0 sayılarının, bölme işlemine göre sonucu: Ops! Bölünemiyor...
```
Burada `inner` fonksiyonu ile decore edilmiş `bölme_işlemi` fonksiyonunun aynı parametrelere sahip olduğunu farketmişsinizdir. İstediğiniz kadar parametreyi `*args` ve `**kwargs` kullanarak tanımlayabilirsiniz. Örnek:
```py
def printer(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
    return inner

@printer
def prints(*args, **kwargs):
    print(*args, **kwargs)

prints("Merhaba", "Ben", "Python!") # Output: Merhaba Ben Python!
```
Burada `**kwargs` tanımlasam da kullanmadım çünkü işimi sadece `*args` görüyor.

Python'da birden fazla decorator zincirlenebilir (chaining). Yani bir fonksiyon birden fazla farklı (veya aynı) decorator ile decore edilebilir. Örnek:
```py
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

printer(f"{'|'*11} Python {'|'*11}")
```
**Output:**
```
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
||||||||||| Python |||||||||||
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
```
Buradaki decorator'lar `printer = star(percent(printer))` kodu ile eşdeğerdir. Yani en alttaki decorator en içe yazılır ve böyle dışa doğru devam eder. Bu sıra önemlidir, dikkat edin!

**Dikkat!** Buradan sonraki kısımları anlayabilmek için giriş seviye class bilginiz olmalıdır!

Callable olan objeler decore edilebilir demiştik. Class'lar da callable bir obje oldukları için decore edilebilirler. Kullanıcının bir function gibi davranan bir obje yaratabilmesi için bir function gibi davranan bir obje döndürmesi gerekir. Bu nedenle `__call__` yararlı olabilir. Bir class'ı decore etmek için `@{class_name}` kullanılır. Mantığını anlamak için basit bir örnek:
```py
class Class_Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        # `func` çağırmadan önce bazı kodlar ekleyebilirsin
        self.func()
        # `func` çağırmadan sonra hala bazı kodlar ekleyebilirsin

@Class_Decorator
def func_exp():
    print("Merhaba Python!")

func_exp() #Output: Merhaba Python!
```
Buradaki mantık fonksiyon decorator'ları ile benzerdir. `@Class_Decorator` decorator'ı ile `func_exp = Class_Decorator(func_exp)` kodu eşdeğerdir.

`*args` ve `**kwargs` parametrelerini de kullanabiliriz. Örnek:
```py
class Class_Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # `func` çağırmadan önce bazı kodlar ekleyebilirsin
        self.func(*args, **kwargs)
        # `func` çağırmadan sonra hala bazı kodlar ekleyebilirsin

@Class_Decorator
def func_exp(name, massage = "Merhaba"):
    print(f"{massage} {name}")

func_exp("Python!") #Output: Merhaba Python!
```

Eğer decore edilen fonksiyon bir değer döndürüyorsa ve döndürülen bu değeri kullanacaksak, `__call__` methoduna bir `return` statement tanımlayabiliriz. Örnek:
```py
class kare_al_decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # `func` çağırmadan önce bazı kodlar ekleyebilirsin
        return self.func(*args, **kwargs)

@kare_al_decorator
def kare_al(n):
    print(f"{n} sayısının karesi:", end=" ")
    return n * n

print(kare_al(2)) # Output: 2 sayısının karesi: 4
print(kare_al(4)) # Output: 4 sayısının karesi: 16
print(kare_al(8)) # Output: 8 sayısının karesi: 64
```