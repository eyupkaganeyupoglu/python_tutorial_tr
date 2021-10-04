# İçindekiler

- [Fonksiyonlar](#1)
    - [Parametreler](#1.1)
        - [Keyword Parameter](#1.1.1)    
        - [Non Keyword Parameter](#1.1.2)
        - [Yıldızlı (Asterisk) Parametreler](#1.1.3)
    - [`return` Statement](#1.2)
    - [Namespace Kavramı](#1.3)
    - [Scope Kavramı](#1.4)
    - [`global` Keyword](#1.5)
    - [`nonlocal` Keyword](#1.6)
- [`lambda` Fonksiyonu](#2)
- [Nested (İç İçe) Fonksiyonlar](#3)
- [Recursive (Özyinelemeli) Fonksiyonlar](#4)
- [Type Hints ve Function Annotations](#5)

<h1 id="1">Fonksiyonlar</h1>

Belli başlı görevleri yapmak için tanımlanmış işlevsel yapıya **fonksiyon** denir. Farklı programlama dillerinde fonksiyonlar, **rutin** ya da **prosedür** olarak da isimlendirilebilir. Bir fonksiyonu kullanmadan önce onu tanımlamanız (definition) gerekmektedir. Bu işlemi, tanımlama anlamına gelen "definition" kelimesine itefen yapılmış `def` keyword'ü ile yapıyoruz. Syntax:
```py
def identifier(parameters):
    # expression

identifier()
```
`identifier` tek başına o fonksiyon objesine atıfta bulunur. Fonksiyon objeleri çağırılabilir (callable) objelerdir. Fonksiyonu çağırmak için `identifier`'ın yanına parantez aç kapat. Örnek:
```py
def func():
	print("func() çağırıldı.")

print(func) # Output: <function func at 0x000002387A0CBF70>
func() # Output: func() çağırıldı.
```

Bir programda aynı isimde iki fonksiyon tamınlandığında, Python en son tanımlananı geçerli sayar. Çünkü en son tanımlanan, kendinden öncekini geçersiz kılar (override). Örnek:
```py
def func():
	print("İlk tanımlanan fonksiyon.")

def func():
	print("İkinci tanımlanan fonksiyon.")

func() # Output: İkinci tanımlanan fonksiyon.
```

Bir scope, kendisi kapsayan scope'lardaki değerlere erişebilir (daha önce anlattım). Fonksiyonlarda'da bu geçerlidir. Kendisini kapsayan scope'daki değerlere erişebilirler. Örnek:
```py
birinci_sayi = 3
ikinci_sayi = 5
def toplama():
	birinci_sayi, ikinci_sayi
	return (birinci_sayi + ikinci_sayi)

print(toplama()) # Output: 8
```

<h2 id="1.1">Parametreler</h2>

Bir fonksiyon tanımlarken, fonksiyonun parantezinin içine tanımlanan şeylere **parametre** denir. Örnek:
```py
def func (p1,p2,p3):
	pass
```
Fonksiyonları çağırırken her parametre için parantezin içine yazdığınız değerlere **argüman** denir. Parametrelere girilen argümanları fonksiyonun local scope'unda kullanabilirsiniz. Örnek:
```py
def func (p1,p2,p3):
	return f"{p1} {p2} {p3}"

print(func("Selam", "Ben", "Python")) # Output: Selam Ben Python
```
Parametrelere argüman girerken hangi parametreye hangi argümanı girdiğinizi özellikle belirtmezseniz, Python bu argümanları parametrelere soldan sağa doğru otomatik dağıtacaktır. Örnek:
```py
def func (p1,p2,p3):
	return f"{p1} {p2} {p3}"

print(func("Selam", "Ben", "Python")) # Output: Selam Ben Python
print(func("Ben", "Selam", "Python")) # Output: Ben Selam Python
print(func("Python", "Selam", "Ben")) # Output: Python Selam Ben
```
Hangi parametreye hangi argümanı girdiğinizi belirtirseniz, bu sıra problemi ile karşılaşmazsınız.Örnek:
```py
def func (p1,p2,p3):
	return f"{p1} {p2} {p3}"

print(func(p1="Selam", p2="Ben", p3= "Python")) # Output: Selam Ben Python
print(func(p3= "Python", p1="Selam", p2="Ben")) # Output: Selam Ben Python
```
Python, `def` ile tanımlanmış bir fonksiyonu okurken ilk olarak fonksiyonun parametrelerine girilen argümanları bellekte depolayıp sonra o fonksiyonun kod bloğundaki işlemleri gerçekleştiriyor. Bu yüzden `print(func(p1="Selam", p2="Ben", p3= "Python"))` işlemi ile `print(func(p3= "Python", p1="Selam", p2="Ben"))` işlemi aynı sonucu verdi.

**Dikkat:** Bir fonksiyonu çağırırken, o fonksiyonun parametrelerine girilen argümanları nasıl girdiğiniz önemlidir. "Keyword Parameter" (örnek: `func(p1 = "asd")`) ve "Non keyword Parameter" (örnek: `func("asd")`) olmak üzere 2 çeşit parametre vardır. Bu parametrelere argüman tanımlarken önce "Non keyword" sonra "Keyword" argümanları tanımlamalısınız. Aksi halde `SyntaxError` hatası yükseltilir. Örnek:
```py
def func (p1,p2,p3):
	return f"{p1} {p2} {p3}"

print(func("Selam", "Ben", "Python")) # Output: Selam Ben Python
print(func("Selam", "Ben", p3 = "Python")) # Output: Selam Ben Python
print(func("Selam", p2 = "Ben", p3 = "Python")) # Output: Selam Ben Python
print(func(p1 = "Selam", p2 = "Ben", p3 = "Python")) # Output: Selam Ben Python
print(func(p1 = "Selam", "Ben", p3= "Python")) # SyntaxError: positional argument follows keyword argument
print(func(p1 = "Selam", p2 = "Ben", "Python")) # SyntaxError: positional argument follows keyword argument
```

<h3 id="1.1.1">Keyword Parameter</h3>

Parametrelere default değerler tanımlayabilirsiniz. Parametrelere tanımladığınız default değerler, o fonksiyon çağırılırken (call) ilgili parametrelere argüman girilmemesi halinde kullanılacak argümanı temsil etmektedir. Böyle oluşturulmuş parametrelere **Keyword Parameter** denir. Örnek:
```py
def func(p1 = "Argüman girilmedi!"):
    print(p1)

func("Selam") # Output: Selam
func(p1 = "Selam") # Output: Selam
func() # Output: Argüman girilmedi!
```
Gördüğünüz gibi `p1` parametresine argüman girilmemesi halinde default değeri olan `"Argüman girilmedi!"` geçerli oluyor.

<h3 id="1.1.2">Non Keyword Parameter</h3>

Default değer tanımlamadığınız parametrelere **Non Keyword Parameter** denir. Fonksiyonu çağırırken bu parametrelere argüman girmezseniz Python `TypeError` hatası yükseltir.
```py
def func(p1):
    print(p1)

func("Selam") # Output: Selam
func(p1 = "Selam") # Output: Selam
func() # TypeError: func() missing 1 required positional argument: 'p1'
```
Gördüğünüz gibi `p1` parametresine argüman girilmemesi halinde Python `"func() gerekli 1 konumsal bağımsız arguman eksik: 'p1'"` anlamına gelen `TypeError: func() missing 1 required positional argument: 'p1'` hatasını yükseltir.

<h3 id="1.1.3">Yıldızlı (Asterisk) Parametreler</h3>

Python'da **Asterisk Operator**'ını kullanarak sınırsız sayıda argüman kabul eden parametreler tanımlayabilirsiniz. Bu operator ile ilgili bilgilere ulaşmak için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/operators.md#3 "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/operators.md#3").

**Not:** Bir fonksiyona max 256 tane argüman girebilirsin (bu şey parametre tanımlama sınırı da olabilir, bilmiyorum), ama bu durum **Python 3.7**'de kaldırıldı. Yani **Python 3.7**'den sonra böyle bir sınırlama yok.

<h2 id="1.2"><code>return</code> Statement</h2>

Bir fonksiyon veya class tanımlarken o fonksiyon veya class'ın kapsamında (kod block'larından bahsediyorum) tanımlanan local namespace'deki objeler, o kapsamından (kod block'larından bahsediyorum) çıkıldıktan sonra bellekten silinir. Bu yüzden local namespace'deki objeleri global namespace'de doğrudan kullanamayız. Local namespace'deki verileri global namespace'de kullanabilmek için o veri `return` statement ile döndürmemiz (returned) gerekmektedir. Yani `return` statement, bir fonksiyonun local namespace'indeki verileri global namespace'e kazandırır. Örnek:
```py
def func(p1):
    temp = p1*2
    return temp

print(func(2)) # Output: 4
```
Eğer `return` statement kullanırsanız ama bir şey döndürmezseniz (yani return statement'in sağına bir şey yazmazsanız), `return` statement `None` değerini döndürür. Örnek:
```py
def func(p1):
    temp = p1*2
    return 

print(func(2)) # Output: None
```
Bir fonksiyon `return` statement ile karşılaşırsa, `return` statement'in sağındaki ifadeyi döndürür ve sonlanır. Bu yüzden `return` statement'den sonra tanımlanmış işlemler yapılmaz. Örnek:
```py
def func(p1):
    temp = p1*2
    return temp
    print("Selam")

print(func(2)) # Output: 4
```

<h2 id="1.3">Namespace Kavramı</h2>

Python'da her nesnenin geçerli olduğu bir namespace (isim alanı) vardır. Aynı isme (identifier) sahip objelerin birbirine karışmamasının sebebi, farklı namespace'lerde (isim alanlarında) bulunmalarıdır. Genelden özele doğru **Build-in**, **Global** ve **Local** olmak üzere 3 çeşit namespace (isim alanı) vardır. Build-in namespace'e, [`site` modülü](https://docs.python.org/3/library/site.html#module-site)'nün constant'ları eklediği namespace'dir. Bu constant'lar, build-in fonksiyonlardır. Global namespace, programınızdaki her şeyi (class'lar, fonksiyonlar, variable'lar) kapsayan namespace'dir. Local namespace, class veya fonksiyonların kapsamlarıdır (kod block'larından bahsediyorum). Oluşturulur, işlemler yapılır ve yok edilir. Global namespace'deki objelere programın her yerinden erişilebilirken, Local namespace'lerdeki objelere programın her yerinen erişilemez, sadece bulundukları scope'dan ve bulundukları scope'un kapsamındaki scope'lardan erişilebilir.

**Not:** Local namespace'deki objeler, local namespace'den çıkıldıktan sonra global namespace'e kazanadırılmadıkları sürece bellekten silinir (istisnalar var mı bilmiyorum).

**Not:** Build-in objelerin identifier'larını başka bir işlemde identifier olarak kullanılamaz demiştim. Build-in objelerin identifier'larını global namespace'de başka bir işlem için identifier olarak kullanırsanız, Build-in namespace'deki o objeyi geçersiz kılmış (override) olursunuz ve asıl işlevini kaybeder. Global namespace'deki o objeyi yokederseniz (`del`), Build-in namespace'de olanı tekrar işlevini geri kazanır. Örnek:
```py
print(list((1,2,3))) # Output: [1, 2, 3]

try:
    list = 1
    print(list) # Output: 1
    print(list((1,2,3))) # TypeError: 'int' object is not callable
except:
    print("TypeError: 'int' object is not callable")

del list
print(list((1,2,3))) # Output: [1, 2, 3]
```
**Output:**
```
[1, 2, 3]
1
TypeError: 'int' object is not callable
[1, 2, 3]
```
Gördüğünüz gibi `list` build-in class'ının identifier'ına global namespace'de `1` integer'ını atadığımız için build-in namespace'deki `list` class'ını geçersiz kılmış (override) olduk ve eski işlevinde kullanmaya çalıştığımızda `TypeError: 'int' object is not callable` hatası yükseltildi. Global namespace'deki `list` objesini `del` statement ile sildiğimizde ise tekrar build-in namespace'deki `list` build-in class'ı geçerli oldu ve eski işlevini kullanabilmeye başladık.

<h2 id="1.4">Scope Kavramı</h2>

Scope, "kapsam" anlamına gelmektedir. Global namespace aynı zamanda "her şeyi kapsayan" anlamına gelen "global scope" olarak da adlandırılabilir. `def` ve `class` statement'leri ile tanımladığımız fonksiyon ve class'lar, for loop'un initializer variable'ı local scope'a örnektir. Bir local scope, kendisini kapsayan bütün scope'ların (başka bir deyişle, kapsamında bulunduğu bütün scope'ların) içeriğine erişebilir. Örnek:
```py
a = "a"
def f1():
    b = "b"
    def f2():
        c = "c"
        def f3():
            d = "d"
            print(a,b,c,d, sep=", ") # Output: a, b, c, d
        f3()
    f2()
f1() 
```
**Output:**
```
a, b, c, d
```
Gördüğünüz gibi `print(a,b,c,d, sep=", ")` kodunun bulunduğu scope, kapsamında bulunduğu bütün scope'lara erişebildiği için `a`, `b`, `c` ve bulunduğu scope'daki `d` variable'larının hepsine erişebildi. Başka bir örnek:
```py
a = "a"
def f1():
    b = "b"
    def f2():
        c = "c"
        def f3():
            d = "d"

        def f4():
            e = "e"
            print(a,b,c,d,e, sep=", ") # NameError: name 'd' is not defined
        f4() #                           ∧
    f2() #                               |
f1() # Error ----------------------------|
```
`print(a,b,c,d,e, sep=", ")` kodunun bulunduğu scope, kapsamında bulunduğu scope'lardaki `a`, `b`, `c` ve bulunduğu scope'daki `e` variable'larına erişebilse de, `f4` fonksiyonu `f3` fonksiyonunun kapsamında bulunmadığı için `d` variable'ına erişemiyor ve `print(a,b,c,d,e, sep=", ")` fonksiyonu `NameError: name 'd' is not defined` hatası yükseltiyor.

Python, o an bulunduğu scope'da talep edilen bir obje'yi bulamazsa, bulunduğu scope'u kapsayan diğer scope'ları özelden genele doğru kontrol eder. Örnek:
```py
a = "a"
def f1():
    def f2():
        def f3():
            print(a)
        f3()
    f2()
f1() # Output: a
```
Gördüğünüz gibi `print(a)` fonksiyonu, talep ettiği `a` variable'ını bulana kadar sırasıyla `f3 -> f2 -> f1 -> global` scope'lara bakar ve ilk bulduğu yer olan global scope'daki `a` variable'ını kullanır. Burada dikkat çekilmesi gereken şey, `a` variable'ını bulduğu ilk scope'dan çekmesi. Örnek:
```py
a = "a"
def f1():
    a = "f1 scope a"
    def f2():
        def f3():
            print(a)
        f3()
    f2()
f1() # Output: f1 scope a
```
Gördüğünüz gibi `print(a)` fonksiyonu, talep ettiği `a` variable'ını ilk bulduğu yer olan `f1` fonksiyonunun scope'undanki `a` variable'ını kullanır. `a` ismindeki bu iki obje farklı scoplarda oldukları için aynı identifier'a sahip olan farklı objelerdir.

Mevcut veriyi talep etmek ile değiştirmek farklı şeylerdir. Kapsam dahilinde ama farklı bir scope'da bulunan variable'lar üzerinde yeniden tanımlama (redefinition) işlemi yapamayız. Örnek:
```py
temp_var = "temp_var"
def f1():
    temp_var = "f1 scope temp_var"
    def f2():
        def f3():
            temp_var += 2 # UnboundLocalError: local variable 'temp_var' referenced before assignment
            print(a)#       ∧
        f3()#               |
    f2() #                  |
f1() # Error ---------------|
```
**Output:**
```
f1 scope a
```
`UnboundLocalError: local variable 'a' referenced before assignment` hatası, local bir variable'ı bildirmeden (declare) önce değer atamaya (assignment) çalıştığımızda ortaya çıkan hatadır. Python `a += 2` kodunu şöyle yorumlar:
- `a += 2` kodu ile `a = a + 2` aynı şeylerdir. Python, `a = a + 2` kodunu soldan sağa doğru okurken ilk olarak `a = ` ifadesindeki assignment operator (`=`) ile karşılaştığı için bir atama işlemi yapmaya hazırlanıyor.
- Python, assignment operator'den sonraki `a + 2` ifadesindeki toplama işlemini gerçekleştirmek için bulunduğu scope'da `a` variable'ını arar ama bulamadığı için `UnboundLocalError: local variable 'a' referenced before assignment` hatası yükseltir. Python'da `bool`, `int`, `float`, `tuple`, `str`, `frozenset`, `range`, `complex`... gibi değiştirilemez (immutable) data type'ların değerini değiştirmek için onu yeniden tanımlamak (redefinition) zorundasınız. Olmayan bir şeyi yeniden tanımlayamayacağınız için yukarıdaki örnekteki gibi, bildirmediğiniz (declare) bir variable'ı da yeniden tanımlayamazsınız (redefinition).

Değiştirilebilir (mutable) objelerin değerini yeniden tanımlama (redefinition) işlemi yapmadan da değiştirebildiğiniz için bu sorunla karşılaşmazsınız. Ama değiştirilebilir (mutable) objelerin değerini yeniden tanımlama (redefinition) yöntemi ile değiştirmeye çalışırsanız yine aynı sebepten dolayı hata alırsınız. Örnek:
```py
def f1():
    a = ["f1 scope a"]
    b = ["f1 scope b"]
    def f2():
        def f3():
            a.append("Yeni f1 scope a")
            print(a) # Output: ['f1 scope a', 'Yeni f1 scope a']
            b += ['Yeni f1 scope b'] # UnboundLocalError: local variable 'b' referenced before assignment
            print(b)
        f3()
    f2()
f1()
```
Gördüğünüz gibi sorun değiştirilebilir (mutable) ya da değiştirilemez (immutable) data type'larda değil, yeniden tanımlama (redefinition) işleminden kaynaklanıyormuş.

Peki neden Python her zaman yaptığı gibi bulunuduğu scope'u kapsayan scope'lara bakmıyor? Python'a "bunu bul" dediğinizde onu bulur, "bunu değiştir" dediğinizde onu değiştirir. Python, `a += 2` kodundaki gibi sadece "bunu değiştir" komutunu verdiğinizde "dur ben bunu bulayım sonra değiştireyim" diyecek kadar zeki değildir. Bu yüzden Python'a hem "bunu bul" hem de "bunu değiştir" komutlarını sırayla vermelisiniz. Bunu `nonlocal` ve `global` keyword'leri ile yapabilirsiniz.

<h2 id="1.5"><code>global</code> Keyword</h2>

`global` keyword'ü, global namespace'de tanımlanmış objeleri local namespace'de kullanabilmemizi sağlar.
```py
a = 1
def f1():
    def f2():
        def f3():
            global a
            a += 1
            print(a)
        f3()
    f2()
f1() # Output: 2
```
`global a` statement, global namespace'de bulunan `a` variable'ının `f3` fonksiyonunun scope'unda bildirir (declare). Bu sayede `a += 1` kodunun bulunduğu scope'da `a` variable'ı olmadığı için aldığımız `UnboundLocalError: local variable 'x' referenced before assignment` gibi hatalar almıyoruz.

<h2 id="1.6"><code>nonlocal</code> Keyword</h2>

`nonlocal` keyword'ü, `global` keyword'ü ile benzer mantıkta çalışır. `nonlocal` keyword'ü, local namespace'de bulunan alt scope'ların, üst scope'lardaki objelere erişmesine imkan verir. Örnek:
```py
def  f1():
	a = 1
	def  f2():
		nonlocal a
		a += 1
		print(a)
	f2()
f1() # Output: 2
```
`nonlocal a` statement, local namespace'de bulunan `a` variable'ının `f3` fonksiyonunun scope'unda bildirir (declare). Bu sayede `a += 1` kodunun bulunduğu scope'da `a` variable'ı olmadığı için aldığımız `UnboundLocalError: local variable 'x' referenced before assignment` gibi hatalar almıyoruz. Başka bir örnek:
```py
def  f1(p1):
	def  f2():
		nonlocal p1
		p1 += 1
		print(p1)
	f2()
f1(1) # Output: 2
```
`f1` fonksiyonunun `p1` parametresine girilen argüman (`p1: 1`) da artık local namespace'in bir parçası olduğu için `nonlocal` statement ile kullanılabilir. Başka bir örnek:
```py
def f1():
    s = 0
    def f2():
        nonlocal s
        s += 1
        return s
    return f2

var1 = f1()
var2 = f1()

print(var1()) # Output: 1
print(var1()) # Output: 2
print(var1()) # Output: 3

print(var2()) # Output: 1
print(var2()) # Output: 2
print(var2()) # Output: 3
```
Bu örnekle ilgili bazı önemli bilgiler:
- Fonksiyonlar çağırıldıklarında kapsamlarındaki (kod block'larından bahsediyorum) objeler belleğe kaydedilir. Kod block'larındaki işlemlerin hepsi yapıldığında fonksiyon sonlanır ve belleğe kaydedilen objeler bellekten silinir.
- `f1` fonksiyonu her çağırıldığında farklı bir `f2` objesi yaratılır (create) ve bu fonksiyon objesi `return f2` statement çalışınca döndürülür. Bu döndürülen birbirinden farklı objeler `var1` ve `var2` variable'larına atanır. Bu objeler sırasıyla `<function f1.<locals>.f2 at 0x000001BED3B99EE0>` ve `<function f1.<locals>.f2 at 0x000001BED3B99E50>` şeklindedir.
- `var1` ve `var2` variable'larına atanan `f2` fonksiyon objeleri, `f1` fonksiyonunun ilk halini geçerli kabul eder. Yani ilk `f2` fonksiyonu `s += 1` işlemini gerçekleştirse bile ikinci `f2` fonksiyonu `s` variable'ını `0` değeri olarak kabul etmektedir. Durumla ilgili başka bir örnek:
    ```py
    def f1():
        s = 0
        def f2():
            nonlocal s
            s += 1
            return s
        s += 1
        print(s)
        return f2

    var1 = f1() # Output: 1
    print(var1()) # Output: 2
    print(var1()) # Output: 3
    print(var1()) # Output: 4

    var2 = f1() # Output: 1
    print(var2()) # Output: 2
    print(var2()) # Output: 3
    print(var2()) # Output: 4
    ```
    Global namespace içindeki objelere doğrudan erişimimiz olduğu için programın life-time'ı boyunca nasıl değiştiklerini gözlemleyebiriz ama aynı şeyi local namespace'de yapamayız (örneğin debugger ile falan gözlemleyemeyiz). Local namespace'deki işlemlere sadece local namespace'deki objeler erişebilir.

Başka bir örnek:
```py
def f1():
    s = 0
    def f2():
        nonlocal s
        s += 1
        return s
    return f2

print(f1()()) # Output: 1
print(f1()()) # Output: 1
print(f1()()) # Output: 1
```
Bu örnekle ilgili bazı önemli bilgiler:
- Fonksiyonlar çağırıldıklarında kapsamlarındaki (kod block'larından bahsediyorum) objeler belleğe kaydedilir. Kod block'larındaki işlemlerin hepsi yapıldığında fonksiyon sonlanır ve belleğe kaydedilen objeler bellekten silinir.
- `f1` fonksiyonu her çağırıldığında farklı bir `f2` objesi yaratılır (create) ve bu fonksiyon objesi `return f2` statement çalışınca döndürülür (döndürülen `f2` fonksiyon objelerine kısaca "`f2`" diyeceğim). Bu işlem sonrasında `f1()()` işlemi Python'un gözünde `f2()` işlemine dönüşür.
- `f2` fonksiyon objesi çalıştırıldığında ise kod bloğundaki işlemler yapılır ve bu fonksiyon objesi önceki örnekteki gibi `var1` gibi bir variable'a atanmadığı için bellekten silinir. Bu yüzden "1, 2, 3" gibi output'lar yerine "1, 1, 1" output'unu aldık.

Namespace ve Scope kavramlarıyla alakalı daha fazla bilgi işin [tıklayınız](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces).

<h1 id="2"><code>lambda</code> Fonksiyonu</h1>

`lambda` fonksiyonu, `lambda arguments : expression` syntax'ına sahiptir. Örnek:
```py
def func1 (p1,p2):
    return (p1 + p2)

func2 = lambda p1,p2: (p1 + p2)

print(func1(2,3)) # Output: 5
print(func2(2,3)) # Output: 5

print(func1) # Output: <function func1 at 0x000002243DB2BEE0>
print(func2) # Output: <function <lambda> at 0x000002243DB2BF70>
```
`func1` ile `func2` aynı işleve sahiptir. `lambda` fonksiyonuna tanımlanan `arguments`, `def` ile tanımlanan fonksiyonlardaki `parameters` kısmına denk gelmektedir. `:` işaretinden sonraki kısım da `def` ile tanımlanan fonksiyonlardaki `return` statement'ına denk gelmektedir.

Tek satırda oluşturulan `if` - `else` yapısı kullanılarak `lambda` fonksiyonun `return` değeri manipüle edilebilir. Örnek:
```py
func1 = lambda p1: ("Bu 2'dir.") if p1==2 else ("Bu 2 değildir.")
print(func1(1)) # Output: Bu 2 değildir.
print(func1(2)) # Output: Bu 2'dir.
```
Bu gibi kullanımlar, `sorted()` fonksiyonundaki `key` parametresi gibi yerlerde kullanılır. Örnek:
```py
elemanlar = [("bir", 1),
             ("dört", 4),
             ("üç", 3),
             ("iki", 2),
             ("beş", 5)]

def sırala(p1):
    return p1[1]
    
print(*sorted(elemanlar, key=sırala), sep=', ') # Output: ('bir', 1), ('iki', 2), ('üç', 3), ('dört', 4), ('beş', 5)
print(*sorted(elemanlar, key=lambda p1:(p1[1])), sep=', ') # Output: ('bir', 1), ('iki', 2), ('üç', 3), ('dört', 4), ('beş', 5)
```

**Not:** Bir `lambda` fonksiyonunun objesi `<function <lambda> at 0x0000021BAD0ABF70>` gibidir.

<h1 id="3">Nested (İç İçe) Fonksiyonlar</h1>

Bir fonksiyon başka bir fonksiyonun kapsamına (kod block'larından bahsediyorum) tanımlanabilir. Bunlara nested (iç içe) fonksiyonlar denir. En dıştaki fonksiyona **enclosing**, enclosing fonksiyonun scope'una tanımlanan diğer bütün fonksiyonlar **nested** fonksiyon denir. Örnek:
```py
def enclosing_func():
    print("Enclosing fonksiyon çalıştı.")

    def nested_func():
        print("Nested fonksiyon çalıştı.")
    
    return nested_func

var = enclosing_func() # Output: Enclosing fonksiyon çalıştı.
var() # Output: Nested fonksiyon çalıştı.
```
Yukarıdaki kodda `enclosing_func` fonksiyonunu çağırdığımızda (call), bu fonksiyonun kod block'undaki `print` fonksiyonu çalıştıktan sonra `nested_func` fonksiyon objesi oluşturulur ve döndürülür. Bu objeyi yukarıdaki gibi bir variable'a atıyarak kullanabilirsiniz. Örnek Program:
```py
def four(p1 = None): return 4 if not p1 else p1(4)
def five(p1 = None): return 5 if not p1 else p1(5)
def plus(y): return lambda x: x+y

print(four(plus(five()))) # Output: 9
print(five(plus(four()))) # Output: 9
print(four(plus(four()))) # Output: 8
print(five(plus(five()))) # Output: 10
```
Python'un bir kodu nasıl okuyup çalıştırdığını [Temel Kavramlar](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/basic_concepts.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/basic_concepts.md")'da anlatıldı. Yukarıdaki `print(four(plus(five())))` şöyle çalışır:
- En içteki `five()` çalışır ve parametre olarak bir şey girilmediği için `5` döndürür.
- `plus()` çalışır ve parametre olarak aldığı `5`'i kullanarak `lambda x : x + 5` `lambda` fonksiyonunu döndürür.
- `four()` çalışır ve parametre olarak `lambda` fonksiyonu objesi aldığı için `p1` parametresinin değeri default değeri olan `None` değeri değil, `lambda` fonksiyonu objesi olur. Bu yüzden `if` çalışmaz, `else` çalışır.
- `else`'de tanımlı olan `p1(4)` Python gözünde `(lambda x : x + 5)(4)` anlamına gelmektedir. Buradaki `4` argümanı `lambda` fonksiyonunun `x` parametresine argüman olarak girilir ve `lambda` fonksiyonu kendisine tanımlanan işlemleri gerçekleştirip `9` integer'ını döndürür.
- `print` fonksiyonu `9` integer'ını yazdırır.

**Not:** `(lambda x : x + 5)(4)` ile `plus(5)(4)` aynı şeydir.

<h1 id="4">Recursive (Özyinelemeli) Fonksiyonlar</h1>

Bir fonkiyon çağırıldığında kapsamında (kod block'larından bahsediyorum) başka bir fonksiyonu çağırabilir. Örnek:
```py
def func():
    print("Print fonksiyonu çağırıldı!")
func() # Output: Print fonksiyonu çağırıldı!
```
Gördüğünüz gibi `func` fonksiyonu çağırıldığında, kod block'unda bulunan `print` fonksiyonunu da çağırabiliyoruz. Bu durum, bir fonksiyonun kendi scope'unda kendisini çağırdığı durumlarda da geçerkidir. Örnek:
```py
temp_num = 0
def func():
    global temp_num
    if temp_num == 10:
        print(temp_num, end=", ")
        return
    else:
        print(temp_num, end=", ")
        temp_num += 1
        func()

func() # Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
```
Burada `temp_num` integer'ı `10`'a eşit olana kadar `temp_num` integer'ına 1 ekleyip kendisini yeniden çalıştıran bir recursive fonksiyon yazdık.

Recursive fonksiyonları çalıştırmanın bir sınırı vardır. Bu fonksiyonlar `RecursionError` hatası yükseltilmeden önce belli bir maksimum çalışma sayısına sahiptir. Bu sınırı aşağıdaki kodla öğrenebilirsiniz:
```py
import sys
print(sys.getrecursionlimit()) # Output: 1000
```
`RecursionError` hatasına örnek:
```py
temp_num = 0
def func():
    global temp_num
    if temp_num == 999999:
        print(temp_num, end=", ")
        return
    else:
        print(temp_num, end=", ")
        temp_num += 1
        func()
func()
```
**Output:**
```
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 
46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 
68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 
90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 
109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 
126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 
143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 
160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 
177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 
194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 
211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 
228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 
245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 
262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 
279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 
296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 
313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 
330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 
347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 
364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 
381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 
398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 
415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 
432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 
449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 
466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 
483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 
500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 
517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 
534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 
551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 
568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 
585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 
602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 
619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 
636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 
653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 
670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 
687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 
704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 
721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 
738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 
755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 
772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 
789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 
806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 
823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 
840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 
857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 
874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 
891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 
908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 
925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 
942, 943, 944, 945, 946, 947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 
959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 
976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 
993, 994, 995, Traceback (most recent call last):
    func()
  File "d:/TP1.md", line 10, in func
    func()
  File "d:/TP1.md", line 10, in func
    func()
  File "d:/TP1.md", line 10, in func
    func()
  [Previous line repeated 993 more times]
  File "d:/TP1.md", line 8, in func
    print(temp_num, end=", ")
RecursionError: maximum recursion depth exceeded while calling a Python object
```
Başka örnekler:
```py
# `s` parametresine girilen string'i şekilli şukullu yazdırmak
def azalt(s):
    if len(s) < 1:
        return s
    else:
        print(s)
        return azalt(s[:-1])
print(azalt("selam"))
```
**Output:**
```
selam
sela
sel
se
s
```

<hr>

```py
# Karmaşık nested listeyi tek bir liste haline getirmek
def fixed(liste):
    if not isinstance(liste, list):
        return [liste]
    elif not liste:
        return []
    else:
        return fixed(liste[0]) + fixed(liste[1:])

l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, [14, 15]]

print(fixed(l)) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
```

<h1 id="5">Type Hints ve Function Annotations</h1>

Python, **dynamic type checking** yapmaktadır. Yani variable'ların type'ları runtime sırasında belirmektedir. Bu yüzden low level programlama dillerindeki gibi, bir variable tanımladığımızda onun type'ını belirtmek zorunda değiliz. O variable'a verdiğimiz data'nın type'ı ne ise, variable'ın type'ı Python tarafından otomatik olarak o type olarak güncellenecektir. **Type Hint** (`:`) ve **Function Annotation** (`->`), tek başına koda işlevsel olarak bir katkıda bulunmasa da kodu okuyan kişinin neyin ne olduğunu anlamasına büyük katkı sağlar. Örnek:
```py
def func(name:str, number:int, boolean:bool = True) -> str:
    return "Outputs: " + name + ", " + str(number) + ", " + str(boolean)

print(func("Ali", 23)) # Output: Outputs: Ali, 23, True
print(func("Ali", 23, False)) # Output: Outputs: Ali, 23, False
```
Yukarıdaki kodda:
- `name:str` kodu, `name` isimli variable'ın `str` type bir argüman alması gerektiğini,
- `number:int` kodu, `number` isimli variable'ın `int` type bir argüman alması gerektiğini,
- `boolean:bool` kodu, `boolean` isimli variable'ın `bool` type bir argüman alması gerektiğini (ayrıca `boolean` parametresinin default değeri `True`'dur),
- `-> str` kodu, `func` isimli fonksiyonun `str` type bir değer döndürmesi gerektiğini ifade etmektedir.

**Type Hint** (`:`) ve **Function Annotation** (`->`)'ın kullanıcıyı bilgilendirmek dışında bir işlevi olmasa bile, **mypy** modülü etkisiyle anlam kazanır. `mypy` sayesinde:
- **Type Hint** (`:`) ve **Function Annotation** (`->`) ile belirtilen durumlara aykırı durumlar oluşunca `mypy` harekete geçer. Örneğin `name:str` şeklinde tanımladığınız `name` parametresine string type dışında bir argüman girerseni `mypy` bir hata raporu oluşturur.
- `mypy` modülü Python'dan bağımsız olarak çalışır. Yani `mypy` modülünün aykırı durumlarla karşılaşınca bir hata raporu oluşturması, Python'un çalışmasına engel teşkil etmez. Python her zaman yaptığı gibi kodları çalıştırmaya devam eder.

**mypy** Modülü:
- [`mypy` pypi linki](https://pypi.org/project/mypy/#description)
- [`mypy` documentation](https://mypy.readthedocs.io/en/stable/getting_started.html)
- [`mypy` GitHub](https://github.com/python/mypy)

**Not:** Python'un kaynak dosyalarında sık sık gördüğümüz "`Any`" kelimesi de bir type hint'dir. Ama yine de type hint deyip geçmemek lazım. `Any`, `typing.pyi` dosyasında `Any = object()` şeklinde tanımlanmıştır. Bu yüzden bazı yerlerde `... -> Any` şeklinde type hint olarak kullanılırken, bazı yerlerde `__iter1: Iterable[Any]` şeklinde kullanılmıştır. Teorik olarak bu kullanımda bir type hint'dir ama `mypy` modülü ile anlam kazanırsa çok şey fark eder.