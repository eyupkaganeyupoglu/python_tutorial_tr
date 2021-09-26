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
- [Type Hints ve Function Annotations](#2)

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

Bir fonksiyon veya class tanımlarken o fonksiyon veya class'ın kod bloğunda tanımlanan local namespace'deki objeler, o kod bloğundan çıkıldıktan sonra bellekten silinir. Bu yüzden local namespace'deki objeleri global namespace'de doğrudan kullanamayız. Local namespace'deki verileri global namespace'de kullanabilmek için o veri `return` statement ile döndürmemiz (returned) gerekmektedir. Yani `return` statement, bir fonksiyonun local namespace'indeki verileri global namespace'e kazandırır. Örnek:
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

Python'da her nesnenin geçerli olduğu bir namespace (isim alanı) vardır. Aynı isme (identifier) sahip objelerin birbirine karışmamasının sebebi, farklı namespace'lerde (isim alanlarında) bulunmalarıdır. Genelden özele doğru **Build-in**, **Global** ve **Local** olmak üzere 3 çeşit namespace (isim alanı) vardır. Build-in namespace'e, [`site` modülü](https://docs.python.org/3/library/site.html#module-site)'nün constant'ları eklediği namespace'dir. Bu constant'lar, build-in fonksiyonlardır. Global namespace, programınızdaki her şeyi (class'lar, fonksiyonlar, variable'lar) kapsayan namespace'dir. Local namespace, class veya fonksiyonların kod blokları'dır. Oluşturulur, işlemler yapılır ve yok edilir. Global namespace'deki objelere programın her yerinden erişilebilirken, Local namespace'lerdeki objelere programın her yerinen erişilemez, sadece bulundukları scope'dan ve bulundukları scope'un kapsamındaki scope'lardan erişilebilir.

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
- Python, assignment operator'den sonraki `a + 2` ifadesindeki toplama işlemini gerçekleştirmek için bulunduğu scope'da `a` variable'ını arar ama bulamadığı için `UnboundLocalError: local variable 'a' referenced before assignment` hatası yükseltir. Python'da `bool`, `int`, `float`, `tuple`, `string`, `frozenset`, `range`, `complex`... gibi değiştirilemez (immutable) data type'ların değerini değiştirmek için onu yeniden tanımlamak (redefinition) zorundasınız. Olmayan bir şeyi yeniden tanımlayamayacağınız için yukarıdaki örnekteki gibi, bildirmediğiniz (declare) bir variable'ı da yeniden tanımlayamazsınız (redefinition).

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
- Fonksiyonlar çağırıldıklarında kod block'larındaki objeler belleğe kaydedilir. Kod block'larındaki işlemlerin hepsi yapıldığında fonksiyon sonlanır ve belleğe kaydedilen objeler bellekten silinir.
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
- Fonksiyonlar çağırıldıklarında kod block'larındaki objeler belleğe kaydedilir. Kod block'larındaki işlemlerin hepsi yapıldığında fonksiyon sonlanır ve belleğe kaydedilen objeler bellekten silinir.
- `f1` fonksiyonu her çağırıldığında farklı bir `f2` objesi yaratılır (create) ve bu fonksiyon objesi `return f2` statement çalışınca döndürülür (döndürülen `f2` fonksiyon objelerine kısaca "`f2`" diyeceğim). Bu işlem sonrasında `f1()()` işlemi Python'un gözünde `f2()` işlemine dönüşür.
- `f2` fonksiyon objesi çalıştırıldığında ise kod bloğundaki işlemler yapılır ve bu fonksiyon objesi önceki örnekteki gibi `var1` gibi bir variable'a atanmadığı için bellekten silinir. Bu yüzden "1, 2, 3" gibi output'lar yerine "1, 1, 1" output'unu aldık.

Namespace ve Scope kavramlarıyla alakalı daha fazla bilgi işin [tıklayınız](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces).

<h1 id="2">Type Hints ve Function Annotations</h1>

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