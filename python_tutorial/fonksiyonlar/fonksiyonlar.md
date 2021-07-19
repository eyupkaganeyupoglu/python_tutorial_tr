# Fonksiyonlar
Belli başlı görevleri yapmak için tanımlanmış işlevsel yapıya **fonksiyon** denir. Farklı programlama dillerinde fonksiyonlar, **rutin** ya da **prosedür** olarak da isimlendirilebilir. Bir fonksiyonu kullanmadan önce onu tanımlamanız gerekmektedir. Bu işlemi, tanımlama anlamına gelen *"definition"* kelimesinden esinlenilmiş `def` keyword'ü ile yapıyoruz. Örnek:
```py
def func ():
	print("func() çağırıldı.")

func() # Output: func() çağırıldı.
```
Birbiri ardına aynı isimde iki fonksiyon tamınlandığında, python en son tanımlananı kabul eder. Örnek:
```py
def func ():
	print("İlk tanımlanan fonksiyon.")

def func ():
	print("İkinci tanımlanan fonksiyon.")

func() # Output: İkinci tanımlanan fonksiyon.
```
**Not:** `print()` içinde çağırdığınız fonksiyonun da içinde bir `print()` fonksiyonu çalışıyorsa, ilk `print()`, `None` değeri döndürür. Bunun sebebi, `print()` fonksiyonuna, yazdırabileceği hiçbir değer verilmemiş olmasıdır. Bu değerin `return` statement ile nasıl verileceği ileriki zamanlarda gösterilecek. Örnek:
```py
def func ():
	print("func() çağırıldı.")

print(func())
```
**Output:**
```
func() çağırıldı.
None
```
Fonksiyonlar, bazen bu işlevleri yapabilmek için bazı input'lara ihtiyaç duyar. Örneğin iki sayının toplamını veren bir fonksiyon, çalışabilmek için iki adet numeric type input'a ihtiyaç duyar. Fonksiyona tanımladığınız bu şeylere **parametre** denir. Örnek:
```py
def toplama (birinci_sayi, ikinci_sayi):
	return (birinci_sayi + ikinci_sayi)

print(toplama(3,5)) # Output: 8
```
İki sayının toplamını veren bir fonksiyona, toplamak istediğiniz iki sayıyı illa parametre olarak girmenize gerek yok. Bu işlemi daha sonra göreceğiniz `global` deyimiyle de gerçekleştirebilirsiniz. Örnek:
```py
birinci_sayi = 3
ikinci_sayi = 5
def toplama ():
	global birinci_sayi, ikinci_sayi
	return (birinci_sayi + ikinci_sayi)

print(toplama()) # Output: 8
```
Gördüğünüz gibi fonksiyonlar parametresiz de çalışabilir. Bir fonksiyonda, ihtiyacınıza göre parametre kullanmayı veya kullanmamayı tercih edebilirsiniz.

**Not:** `def func (p1, p2):` şeklinde tanımlanmış bir fonksiyonun `p1` ve `p2` adında iki parametresi vardır. Bu fonksiyon çağırıldığında, parametrelere girilen değerlere **argüman** denir. Yani `func("arg1", "arg2")` şeklinde çağırılan fonksiyonun `p1` parametresine `"arg1"` argümanı, `p2` parametresine `"arg2"` argümanı girilmiştir.

## Parametreler
Bir fonksiyon tanımlarken, fonksiyonun parantezine girilen değerlere parametre denir. Bu parametrelere girilen argümanları, fonksiyon içinde kullanabilirsin. Genel olarak parametrelere argüman girerken, bu argümanları girdiğiniz sıraya dikkat etmelisiniz. Çünkü Python, hangi argümanı hangi parametreye girmek istediğinizi otomatik algılayacak kadar zeki değildir. Ya `func(p1 = "arg1", p2 = "arg2", p3 = "arg3")` örneğindeki gibi, hangi parametreye hangi argümanı hangi parametreye girmek istediğinizi belirtmelisiniz (böylece `func(p2 = "arg2", p3 = "arg3", p1 = "arg1")` örneğindeki gibi parametreleri rastgele sırada girebilirsiniz) ya da `func("arg1", "arg2", "arg3")` örneğindeki gibi, argümanları doğru sırada girmelisiniz. Böylece bir sorun yaşamazsınız. Örnek:
```py
def func (p1,p2,p3):
	return f"{p1} {p2} {p3}"

print(func(p1="Selam", p2="Ben", p3= "Python")) # 1
print(func(p3= "Python", p1="Selam", p2="Ben")) # 2
print(func("Selam", "Ben", "Python")) # 3
print(func("Python", "Selam", "Ben")) # 4
```
**Output:**
```
Selam Ben Python
Selam Ben Python
Selam Ben Python
Python Selam Ben
```
**Not:** Python, `def` ile tanımlanmış bir fonksiyonu okurken, ilk olarak fonksiyonun parametrelerini belleğe atıp sonra o fonksiyonun bloğundaki işlemleri gerçekleştiriyor. Bu yüzden `print(func(p1="Selam", p2="Ben", p3= "Python"))` işlemi ile `print(func(p3= "Python", p1="Selam", p2="Ben"))` işlemi aynı sonucu verdi.

**Dikkat:** Birden fazla parametreye sahip fonksiyonları çağırırken, ilgili fonksiyonun parametrelerine argüman girme formatı hakkında, aşağıdaki duruma dikkat ediniz:
```py
func(parametre1 = "arguman1", parametre2 = "arguman2", "arguman3") # SyntaxError: non-keyword arg after keyword arg
func(parametre1 = "arguman1", parametre2 = "arguman2", parametre3 = "arguman3") # Doğru kullanım
```

### İsimli ve İsimsiz Parametreler
İsimsiz parametrelere isimli parametrelere **Keyword Arguments**,

### Default Value'ye Sahip Parametreler
Fonksiyon tanımlarken, ilgili fonksiyona tanımladığın parametrelere default argümanlar tanımlayabilirsiniz. Bu sayede o fonksiyonu çağırdığında, ilgili parametreye bir argüman atanmazsa, ilgili parametre default değerini kullanır. Örneğin, `print()` fonksiyonunun çoğu parametresinin default değeri tanımlıdır. Bu fonksiyonu `print("Python")` şeklinde kullansanız bile, Python bunu aşağıdaki gibi görür:
```py
print("Python", sep=" ", end="\n", file=sys.stdout, flush=False)
```
Çünkü diğer `sep`, `end`, `file` ve `flush` parametrelerinin default value'ye sahip oldukları için, o parametrelere argüman atamazsanız python bu default değerleri kullanır.

### Yıldızlı parametreler
Bir parametreye birden fazla argüman girmeni sağlayan parametre türüne, yıldızlı parametreler denir. Örneğin, `print()` fonksiyonunda `sep`, `end`, `file` ve `flush` parametreleri haricinde sınırsız string argüman girebiliyorsun. Bu durum, `*objects` yıldızlı parametre sayesinde mümkün oluyor. Yıldızlı parametreler 2'ye ayrılır. `*args` formatındaki tek yıldızlı parametrelere **Non Keyword Arguments**, `**kwargs` formatındaki çift yıldızlı parametrelere ise **Keyword Arguments** denir.

#### Non Keyword Arguments
`*args` formatındaki parametreye **Non Keyword Arguments** denir. Bu parametre, kendisine girilen argümanları içeren bir `tuple` verir. Bu `tuple`'ı fonksiyonun içinde, yıldızlı parametrenin ismiyle kullanabilirsiniz. Örneğin `*isimler` yıldızlı parametresine girilen argümanları içeren `tuple` objesini, `isimler` identifier'i ile (ismiyle) çağırabilirsiniz/kullanabilirsiniz. Örnek program:
```py
# Toplama İşlemi
def toplama(*num):
	toplam = 0
	for i in num:
		toplam += i
	print("toplam:", toplam)

toplama(1,2,3)
```
**Output:**
```
(1, 2, 3)
Toplam: 6
```

#### Keyword Arguments
`**kwargs` formatındaki parametreye **Keyword Arguments** denir. Bu parametre, kendisine girilen argümanları içeren bir `dict` verir. Bu `dict`'ı fonksiyonun içinde, yıldızlı parametrenin ismiyle kullanabilirsiniz. Örneğin `**bilgiler` yıldızlı parametresine girilen argümanları içeren `dict` objesini, `bilgiler` identifier'i ile (ismiyle) çağırabilirsiniz/kullanabilirsiniz. Örnek program:
```py
# CV Çıktısı
def cv_info(**bilgiler):
	print(bilgiler)
	for i,j in bilgiler.items():
		print(f"{i}: {j})
cv_info(İsim="Python", Soyisim="Çöp", Yaş="20", Boy="185cm", Kilo=95 )
```
**Output:**
```
{'İsim': 'Python', 'Soyisim': 'Çöp', 'Yaş': '20', 'Boy': '185cm', 'Kilo': 95}
İsim: Python
Soyisim: Çöp
Yaş: 20
Boy: 185cm
Kilo: 95
```

#### `*args` ve `**kwargs` Beraber Kullanımı
Bu iki parametre türünü beraber kullanırken kullanmanız gerekn syntax `func(*args, **kwargs)` şeklindedir. `func(**kwargs, *args)` şeklindeki kullanımlar `SyntaxError: invalid syntax`'e sebep olur. `func(*args, **kwargs)` fonksiyonuna parametre girerken, önce `*args` parametresine **non keyword argument**'leri girersiniz, sonra `**kwargs` parametresine **keyword argument**'leri girersiniz. **keyword argument**'leri girmeye başladığınızda python otomatik olarak `*args` parametresine **non keyword argument**'leri girmeyi bıraktığınızı anlar. Örnek:
```py
def  func(*args, **kwargs):
	print(args)
	print(kwargs)
  
func(1, 2, 3, Bir=1, İki=2, Üç=3)
```
**Output:**
```
(1, 2, 3)
{'Bir': 1, 'İki': 2, 'Üç': 3}
```

**Not:** Bir fonksiyona max 256 tane argüman girebilirsin (bu şey parametre tanımlama sınırı da olabilir, bilmiyorum), ama bu durum **Python 3.7**'de kaldırıldı. Yani **Python 3.7**'den sonra böyle bir sınırlama yok.

## `return` Deyimi
Bir fonksiyonun içindeki local değerler, fonksiyon sonlandıktan sonra bellekten silinir. Bu yüzden bu değerleri, fonksiyon sonlandıktan sonra kullanamazsınız. Bu değerleri prgoramın herhangi bir yerinde kullanabilmek için ilgili fonksiyonun içinden almanız gerekmektedir. Bu işlemi `return` deyimiyle basitçe halledebilirsiniz. `return` deyimi, bir fonksiyonun içindeki local değerleri programa kazandırmak için kullanılabilir. Örnek:
```py
def func():
	local_vrb = 1
	return (local_vrb)
print(func()) # Output: 1
```
Eğer `return` değerinin sağına bir şey eklenmezseniz, o fonksiyon `None` değeri döner:
```py
def func():
	return
print(func()) # Output: None
```
**Not:** Bir fonksiyon `return` deyimi ile karşılaşırsa, `return` deyiminden sonra yazılan ifadeyi döndürdükten sonra sonlanır.

## Namespace Kavramı
Python'da her nesnenin geçerli olduğu bir namespace (isim alanı) vardır. Aynı isme (identifier) sahip objelerin birbirine karışmamasının sebebi, farklı namespace'lerde (isim alanlarında) bulunmalarıdır. **Local** ve **Global** olmak üzere 2 çeşit namespace (isim alanı) vardır. Global namespace'deki objelere programın her yerinden erişilebilirken, Local namespace'lerdeki objelere programın her yerinen erişilemez, sadece bulundukları scope'dan ve bulundukları scope'un kapsamındaki scope'lardan erişilebilir.

## Scope Kavramı
Scope, "kapsam" anlamına gelmektedir. Global namespace aynı zamanda "her şeyi kapsayan" anlamına gelen "global scope" olarak da adlandırılabilir. `def` ve `class` keyword'leri ile tanımladığımız fonksiyon ve class'lar, for loop'un initializer variable'ı local scope'a örnektir. Bir local scope, kendisini kapsayan bütün scope'ların (başka bir değişle "kapsamında bulunduğu bütün scope'ların") içerdiği objelere erişebilir. Örnek:
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
Gördüğünüz gibi `print(a,b,c,d, sep=", ")` kodu, kapsamında bulunduğu bütün scope'lara erişebildiği için `a`, `b`, `c` ve bulunduğu scope'daki `d` variable'larının hepsine erişebildi ve yazdırdı. Başka bir örnek:
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
        f4()
    f2()
f1() # Error
```
**Output:**
```
    print(a,b,c,d,e, sep=", ") # NameError: name 'd' is not defined
NameError: name 'd' is not defined
```
`print(a,b,c,d,e, sep=", ")` kodu, kapsamında bulunduğu scope'lardaki `a`, `b`, `c` ve bulunduğu scope'daki `e` variable'larına erişebilse de, `f4` fonksiyonu `f3` fonksiyonunun kapsamında bulunmadığı için `d` variable'ına erişemiyor ve `print(a,b,c,d,e, sep=", ")` fonksiyonu `NameError: name 'd' is not defined` hatası yükseltiyor.

### Farklı Scope'lardaki Variable'larda İşlemler
Python, bulunduğu scope'da talep edilen bir obje'yi bulamazsa, bulunduğu scope'u kapsayan scope'ları kontrol eder. Örnek:
```py
a = "a"
def f1():
    def f2():
        def f3():
            print(a) # Output: a
        f3()
    f2()
f1()
```
**Output:**
```
a
```
Gördüğünüz gibi `print(a)` fonksiyonu, talep ettiği `a` variable'ını bulana kadar sırasıyla `f3 -> f2 -> f1 -> global` scope'lara bakar ve ilk bulduğu yer olan global scope'dan kullanır. Burada dikkat çekilmesi gereken şey; `a` variable'ını bulduğu ilk scope'dan çekmesi. Örnek:
```py
a = "a"
def f1():
    a = "f1 scope a"
    def f2():
        def f3():
            print(a) # Output: f1 scope a
        f3()
    f2()
f1()
```
**Output:**
```
f1 scope a
```
Gördüğünüz gibi `print(a)` fonksiyonu, talep ettiği `a` variable'ını ilk bulduğu `f1` fonksiyonunun scope'undan kullanır. `a` ismindeki bu iki obje, farklı scoplarda oldukları için aynı isimde (identifier) farklı objelerdir.

Mevcut data'yı talep etmek ile değiştirmek farklı şeylerdir. Kapsam dahilinde ama farklı bir scope'da bulunan variable'lar üzerinde yeniden tanımlama (redefinition) işlemi yapamayız. Örnek:
```py
a = "a"
def f1():
    a = "f1 scope a"
    def f2():
        def f3():
            a += 2 # UnboundLocalError: local variable 'a' referenced before assignment
            print(a)
        f3()
    f2()
f1()
```
**Output:**
```
f1 scope a
```
`UnboundLocalError: local variable 'a' referenced before assignment` hatası, local bir variable'ı bildirmeden (declare) önce değer atamaya (assignment) çalıştığımızda ortaya çıkan hatadır. Python `a += 2` kodunu şöyle yorunlar:
- `a += 2` kodu ile `a = a + 2` aynı şeylerdir. Python, `a = a + 2` kodunu soldan sağa doğru okurken ilk olarak `a = ` ifadesindeki assignment operator (`=`) ile karşılaştığı için bir atama işlemi yapmaya hazırlanıyor.
- Python, assignment operator'den sonraki `a + 2` ifadesindeki toplama işlemini gerçekleştirmek için bulunduğu scope'da `a` variable'ını arar ama bulamadığı için `UnboundLocalError: local variable 'a' referenced before assignment` hatası yükseltir. Python'da `bool`, `int`, `float`, `tuple`, `str`, `frozenset` gibi değiştirilemez (immutable) data type'ların değerini değiştirmek için onu yeniden tanımlamak (redefinition) zorundasınız. Olmayan bir şeyi yeniden tanımlayamayacağınız için yukarıdaki örnekteki gibi, bildirmediğiniz (declare) bir variable'ı da yeniden tanımlayamazsınız (redefinition).

Peki neden Python her zaman yaptığı gibi bulunuduğu scope'u kapsayan scope'lara bakmıyor? Python'a "bunu bul" dediğinizde onu bulur, "bunu değiştir" dediğinizde onu değiştirir. Sadece "bunu değiştir" komutunu verdiğinizde, "dur ben bunu bulayım sonra değiştireyim" diyecek kadar zeki değildir Python. Bu yüzden Python'a hem "bunu bul" hem de "bunu değiştir" komutlarını sırayla vermelisiniz. Bunu `nonlocal` ve `global` keyword'leri ile yapabilirsiniz.

değiştirilebilir (mutable) data type'ların değerini, yeniden tanımlama (redefinition) işlemi yapmadan da değiştirebildiğiniz için bu sorunla karşılaşmazsınız. Ama değiştirilebilir (mutable) data type'ın değerini yeniden tanımlama (redefinition) yöntemi ile değiştirmeye çalışırsanız yine aynı sebepten dolayı hata alırsınız. Örnek:
```py
def f1():
    a = ["f1 scope a"]
    b = ["f1 scope b"]
    def f2():
        def f3():
            a.append("Yeni f1 scope a")
            print(a) # 
            b += ['Yeni f1 scope b'] # UnboundLocalError: local variable 'b' referenced before assignment
            print(b)
        f3()
    f2()
f1()
```
**Output:**
```
['f1 scope a', 'Yeni f1 scope a']
    b += ['Yeni f1 scope b']
UnboundLocalError: local variable 'b' referenced before assignment
```
Gördüğünüz gibi sorun değiştirilebilir (mutable) ya da değiştirilemez (immutable) data type'larda değil, yeniden tanımlama (redefinition) işleminden kaynaklanıyormuş.

#### `global` keyword
`global` keyword'ü, global namespace'de tanımlanmış objeleri local namespace'de kullanabilmemizi sağlar.
```py
a = 1
def f1():
    def f2():
        def f3():
            global a
            a += 1
            print(a) # Output: 2
        f3()
    f2()
f1()
```
**Output:**
```
2
```

#### `nonlocal` keyword
`nonlocal` keyword'ü, local namespace'de bulunan alt scope'ların üst scope'lardaki objelere erişmesine imkan verir. Örnek:
```py
def  f1():
	x = 1
	def  f2():
		nonlocal x
		x += 1
		print(x) # Output: 2
	f2()
f1()
```
**Output:**
```
2
```
Gördüğünüz gibi `nonlocal` keyword'ü sayesinde, daha önce aldığımız `UnboundLocalError: local variable 'x' referenced before assignment` gibi hatalar almıyoruz. Başka bir örnek:
```py
def  f1(p1):
	def  f2():
		nonlocal p1
		p1 += "Dünya!"
		print(p1) # Output: 2
	f2()
f1("Selam ")
```
**Output:**
```
Selam Dünya!
```
`nonlocal` keyword'ü ile üst scope'daki fonksiyonun parametresine de ulaşabiliyoruz. Başka bir örnek:
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
**Output:**
```
1
2
3
1
2
3
```
Bu örnekle ilgili bazı önemli noktalar var:
- Fonksiyonlar sadece çağırıldıklarında blocklarındaki kodları çalıştırırlar. Bu yüzden bir fonksiyonu çağırdığınızda, fonksiyonun local objeleri oluşturulup belleğe kaydedilir ve fonksiyon çalışmayı sonlandırdığında local objeler bellekten silinir.
- `f1` fonksiyon objesi `f1()` şeklinde her çağırıldığında farklı bir local `s` integer ve `f2` fonksiyon objesi oluşturulup belleğe kaydedilir ve fonksiyon çalışmayı sınlandırdığında local bellekten silinir. Bu yüzden `var1` ve `var2` variable'larında depolanan `f2` fonksiyon objeleri birbirinden farklı objelerdir. Bu `f2` fonksiyonu objeleri oluşturulurken, `f1` fonksiyonundaki `s` variable'ının sadece o anki value'sunu bilirler. `var1` ve `var2` variable'larına atanan `f2` fonksiyonlarının üzerinde yapılan işlemlerinin birbirine etki etmeyip bağımsız olmasının sebebi budur.

Anlamayanlar için sırasıyla `var1 = f1()` ve `var2 = f1()` kodları şöyle çalışır:
- `f1` fonksiyonu `f1()` kodu sayesinde çağırılır.
- Sırasıyla `s` variable'ı ve `f2` fonksiyon objesi oluşturulur.
- `return f2` kodu ile `f2` local fonksiyon objesi döndürülür ve `var1` variable'ına atanır. `var1`'e atanan `f2` local fonksiyon objesi (`<function f1.<locals>.f2 at 0x000001BED3B99EE0>`) için `s` variable value'su `0`'dır.
- Aynı şey `var2` variable'ı için de gerçekleşir. `var2`'ye atanan `f2` local fonksiyon objesi (`<function f1.<locals>.f2 at 0x000001BED3B99E50>`) için de `s` variable value'su `0`'dır. Kanıt:

    <img src="https://i.ibb.co/grySwBs/image.png" alt="image" border="0">

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
**Output:**
```
1
1
1
```
Burada her `print()` fonksiyonunun önceki koddaki gibi 1, 2, 3 şeklinde çıktı vermemesinin sebebi; her `f1()` kodu yeni bir `f2` local fonksiyon objesi döndürür. Sonrasında `f1()()` kodu Python'un gözünde `f2()` koduna dönüşür ve `f2()` koduyla `f2` local fonksiyon objesi çalıştırılır. Bu yüzden her `f2` local fonksiyon objesi bir kere çalıştığı için `1` output'unu verir.









Namespace ve Scope kavramlarıyla alakalı daha fazla bilgi işin [tıklayınız](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces).