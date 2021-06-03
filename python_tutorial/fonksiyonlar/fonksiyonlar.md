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

## Scope Kavramı
Python'da, local ve global olmak üzere 2 çeşit scope (alan) vardır. Global scope'daki değerlere programın her yerinden erişilebilirken, local scope'daki değerlere programın her yerinden erişilemez. Local scope'lar arasında da böyle bir ilişki vardır. Bir local scope, kendi bloğundaki başka bir local scope'da tanımlı bir değere erişemez. `def` ile tanımlanan fonksiyonun bloğu, `class` ile tanımlanan class'ın bloğu, for döngüsündeki initializer variable, local scope'a örnektir.
```py
a = 1 # global variable
print(a) # Output: 1
print(b) # Output: NameError: name 'b' is not defined
def  func():
	b = 2  # local variable
	print(a, b) # Output: 1 2
	
func() # Output: 1 2
```
Gördüğünüz gibi `NameError` veren `print(b)` fonksiyonunun hata verme nedeni, `func()` fonksiyonunda bulunan local `b` variable'ını görememesidir. Ama `func()` fonksiyonunun içindeki `print(a, b)` fonksiyonu, global scope'daki `a` variablesini görür. Bu da kanıtlıyor ki, local scope'dan global scope'a yaklaştıkça görünürlük artarken, tam tersinde azalır.

### Farklı Scope'lardaki Variable'larda İşlemler
Aynı ada sahip farklı objeler söz konusu olduğunda, python önce o objenin talep edildiği scope'a bakar, o objenin talep edildiği scope'da yoksa bir üstteki scope'a bakar.
```py
x = 1
def  func1():
	x = 2
	return (x)
  
def  func2():
	return (x)
  
print(x) # Output: 1
print(func1()) # Output: 2
print(func2()) # Output: 1
```
Burada `func1()` fonksiyonunda `return` deyimiyle `x` variable'ı talep ediliyor ve python ilk bulunduğu scope'a bakıyor. Bulunduğu scope'da bu değer yoksa, `func2()`'deki gibi bir üst scope'da arar. Bu yüzden `func2()`, global scope'da bulunan `x` variable'ının değerini döndürdü.  Bu iki `x` variable'ı, farklı scope'larda oldukları için farklı objelerdir. Bu olay sadece veri talep ettiğinde geçerlidir. Mevut veriyi değiştirmeye kalktığında farklı durumlar oluşur. Örneğin:
```py
x = 1
def  func1():
	x += 2
	return (x)
	
print(x) # Output: 1
print(func()) # Output: UnboundLocalError: local variable 'x' referenced before assignment
```
Buradaki `x += 2` kodu `x = x + 2` koduyla aynı anlama geldiği için ikinci kod üzerinden anlatacağım. `UnboundLocalError` hatası almamızın sebebi, Python'un `x = x + 2` işlemini okuma şeklidir. Python, `x = x + 2` kısmını okurken ilk olarak `x =` kısmını okuyup, bunu *"Burada bir variable tanımlanıyor"* şeklinde yorumlar. Bu yüzden bir variable tanımlamaya çalışırken `x = x + 2` işlemiyle karşılaşınca, henüz tanımlamadığı variable'a `2` eklemeye çalışıyor ve böyle bir şey mümkün olmayacağı için `UnboundLocalError: local variable 'x' referenced before assignment` hatası alıyorsunuz. Bu durum birçok data type'da geçerlidir çünkü hataya sebep olan şey data type değil `x +=` kısmıdır. Bu durum, local scope'dan global scope'a ya da alt local scope'dan üst local scope'a ulaşmaya çalışırken oluşabilir. Bu durumları çözmek için `global` ve `nonlocal` keyword'lerinden yararlanılabilir.

**Not:** Python da `bool`, `int`, `float`, `tuple`, `str`, `frozenset` gibi data değiştirilemez (immutable) type'ların değerini değiştirmek için onu yeniden tanımlamak zorundasınız. Bu global scope'da da, local scope'da da böyledir. Local scope'da ek olarak, global scope'da tanımladığınız immutable bir data type'ı local scope'da yeniden tanımlayamazsınız. Örnek:

```py
x = "Eski"
x += "Yeni"  # x, yaniden tanımlanarak değişti.
print(x) # Output: EskiYeni
```
```py
x = "Eski"
def  fonk():
	x += "Yeni"  # x, yeniden tanımlanamadığı için değişmedi.
	return x
print(fonk()) # Output: UnboundLocalError: local variable 'x' referenced before assignment
```
Bir listeye `append()` methoduyla bir öğe ekleyeceğiniz zaman `UnboundLocalError` hatası almazsanız çünkü `list`, `set` ve `dict` data type'lar değiştirilebilir (mutable) data type'lardır:

```py
x = []
print(f"X'in eski hali: {x}")
def  func():
	x.append("öğe")
	return (x)
func()
print(f"X'in yeni hali: {x}")
```
**Output:**
```
X'in eski hali: []
X'in eski hali: ['öğe']
```

#### `global` keyword
`global` keyword'ü, global scope'da bulunan değerlerin local scope'da kullanılmasına imkan sağlayan bir keyword'dür.
```py
x = 1
def  func():
	global x
	print(x)
func() # Output: 1
```

#### `nonlocal` keyword
`nonlocal` keyword'ü, üst local scope'da bulunan değerlerin alt local scope'da kullanılmasına imkan sağlayan bir keyword'dür. Bu keyword, nested fonksiyonlarda kullanılabilir.
```py
def  func1():
	x = 1
	def  func2():
		nonlocal x
		x += 1
		print(x)
	func2()
func1() # Output: 2
```
Başka bir örnek:
```py
def yazıcı(mesaj):
    def yaz():
        nonlocal mesaj
        mesaj += " Dünya"
        print(mesaj)
    return yaz
```
Yukarıdaki kodda `nonlocal` keyword'ünü kullanmasaydık `UnboundLocalError: local variable 'mesaj' referenced before assignment` hatası alırdık. Çünkü daha önce de bahsettiğim gibi `+=` operatörü, `mesaj` variable'ını tanımlamadan, `+` operatörü aracılığıyla henüz tanımlamadığı bir variable'a `" Dünya"` stringini eklemeye çalışıyor. `+=` operatörünün sıkıntı çıkarmaması için önce `mesaj` variable'ını tanımlamamız gerekiyor. Bunu da `nonlocal` keyword'ünü kullanarak yapıyoruz.

Önemli bir örnek:
```py
def fonk1():
    sayı = 0
    def fonk2():
        nonlocal sayı # sayı = 0
        sayı += 1
        return sayı
    return fonk2

s1 = fonk1()
s2 = fonk1()

print(s1()) # Output: 1
print(s1()) # Output: 2
print(s1()) # Output: 3

print(s2()) # Output: 1
print(s2()) # Output: 2
print(s2()) # Output: 3

```
Yukarıdaki fonksiyon şöyle çalışır:
- Önce `def fonk1():` okunur ve `<function fonk1 at 0x000001D8E02135E0>` objesi oluşturulur.
- Sonra, `s1 = fonk1()` okunur ve sırasıyla şöyle çalışır:
	- Python bu satırdaki `fonk1()` kodu yüzünden `fonk1()` fonksiyonunu çalıştırır. Bu fonksiyon `<function fonk1 at 0x000001D8E02135E0>` objesini çağırır.
	- Sonra, `sayı = 0` satırı okunur ve `sayı = 0` kodu yüzünden `sayı: 0` değeri locals'de tutulur.
	- Sonra `def fonk2():` satırı okunur ve bu fonksiyonun `<function fonk1.<locals>.fonk2 at 0x000002A4834C39D0>` objesi oluşturulur. Bu obje, `s1 = sayıcı()` kodu ile çağırılan `<function fonk1 at 0x000001D8E02135E0>` objenin o anki durumunu geçerli kabul eder (Örneğin `sayı` variablesinin `0`'a eşit olduğu kabul eder).
	- Sonra, `return fonk2` kodu ile `<function fonk1.<locals>.fonk2 at 0x000002A4834C39D0>` objesi `s1`'e atanır.
- Sonra, `s2 = fonk1()` okunur ve sırasıyla şöyle çalışır:
	- Python bu satırdaki `fonk1()` kodu yüzünden `fonk1()` fonksiyonunu çalıştırır. Bu fonksiyon `<function fonk1 at 0x000001D8E02135E0>` objesini çağırır.
	- Sonra, `sayı = 0` satırı okunur ve `sayı = 0` kodu yüzünden `sayı: 0` değeri locals'de tutulur.
	- Sonra `def fonk2():` satırı okunur ve bu fonksiyonun `<function fonk1.<locals>.fonk2 at 0x000001CC0CDC3940>` objesi oluşturulur. Bu obje, `s1` variable'ına atanan objeden farklı bir objedir. Bu obje, `s2 = sayıcı()` kodu ile çağırılan `<function fonk1 at 0x000001D8E02135E0>` objenin o anki durumunu geçerli kabul eder (Örneğin `sayı` variablesinin `0`'a eşit olduğu kabul eder).
	- Sonra, `return fonk2` kodu ile `<function fonk1.<locals>.fonk2 at 0x000001CC0CDC3940>` objesi `s2`'e atanır.
- Sonra, her `print(s1())` komutu çalıştırıldığında, outputlar 1, 2, 3, ... artarak bastırılır.
- Sonra, her `print(s2())` komutu çalıştırıldığında, outputlar, `print(s1())`'deki gibi 1, 2, 3, ... artarak bastırılır. Bir tane `<function fonk1 at 0x000001D8E02135E0>` objesi olmasına rağmen `s1` ve `s2`'nin birbirinden bağımsız `sayı` değerlerine sahip olmalasının nedeni şudur:
	- `global` statement'da, global scope'daki bir variable'nin değerini local scope'da değiştirdiğinizde, global scope'daki variable'ın da değeri değişiyordu. Birbiriyle tamamen aynı birden fazla global scope olsaydı, her bir global scope'un içindeki değerler, o scope'un kapsamında değişirdi.
	- `nonlocal` statement'i de `global` satetement mantıkla düşünmeliyiz. `fonk1()` her çağırıldığında, `<function fonk1 at 0x000001D8E02135E0>` objesinin ilk hali geçerli olur. `print(s1())` komutu her çalıştığında `sayı` variable'ının değeri bir arttığından, her output bir öncekinden bir fazladır. Ama `print(s1())` komutunu üç kere çalıştırdıktan sınra `print(s2())` komutunu çalıştırdığımızda `4` outputunu vermek yerine `1` outputunu verir. Bunun sebebi, `s1` ve `s2`'ye atanan birbirinden farklı `<function fonk1.<locals>.fonk2 at 0x000002A4834C39D0>` ve `<function fonk1.<locals>.fonk2 at 0x000001CC0CDC3940>` objeleri, `<function fonk1 at 0x000001D8E02135E0>` objesinin ilk halini tanımalarıdır. Bu yüzden `s1` ve `s2`'nin içindeki `nonlocal` statement'in çağırdığı `sayı` variableleri birbirinden bağımsız.
	- global scope'daki variable'lara erişimimiz olduğu için o variable'lerin programın life-time'ı boyunca nasıl değiştiriğini kontrol edebiliriz ama local variable'lara erişimimiz olmadığı için kontrol edemeyiz. Local variable'lere sadece nested fonksiyonların erişimi vardır. Bu yüzden `print(s1())` ve `print(s2())` komutları çalışırken, debugger'da `fonk2`'nin döndürdüğü sayıları görsek de, `fonk2`'nin yaptığı işlemleri göremeyiz.
```py
def fonk1():
    sayı = 0
    def fonk2():
        nonlocal sayı # sayı = 0
        sayı += 1
        return sayı
    return fonk2

print(fonk1()()) # Output: 1
print(fonk1()()) # Output: 1
print(fonk1()()) # Output: 1
```
Yukarıdaki fonksiyon şöyle çalışır:
- Önce `def fonk1():` okunur ve `<function fonk1 at 0x000001D8E02135E0>` objesi oluşturulur.
- Sonra, `print(fonk1()())` okunur ve sırasıyla şöyle çalışır:
	- `fonk1()()`'in `fonk1()` kısmı çalıştırılır ve bu fonksiyon `<function fonk1 at 0x000001D8E02135E0>` objesini çağırır.
	- Sonra, `sayı = 0` satırı okunur ve `sayı = 0` kodu yüzünden `sayı: 0` değeri locals'de tutulur.
	- Sonra `def fonk2():` satırı okunur ve bu fonksiyonun `<function fonk1.<locals>.fonk2 at 0x000002A4834C39D0>` objesi oluşturulur. Bu obje `<function fonk1 at 0x000001D8E02135E0>` objenin o anki durumunu geçerli kabul eder (Örneğin `sayı` variablesinin `0`'a eşit olduğu kabul eder).
	- Sonra, `return fonk2` kodu ile `<function fonk1.<locals>.fonk2 at 0x000002A4834C39D0>` objesi global scope'a gönderilir (bundan sonra bu objeye kısaca `fonk2` objesi diyeceğim).
	- `fonk1()()` fonksiyonunun `fonk1()` kısmındaki işlemler bittikten sonra global scope'a gönderilen `fonk2` objesi `fonks2()` şeklinde çalıştırılır. `fonk1()()`'deki 2 tane parantezin olayı budur. `fonk1()()`'deki `fonk1()` fonksiyonu `fonk2` objesin döndürdüğü için python `fonk1()()`'yi `fonk2()` olarak görür ve çalıştırır.
	- `fonk2()` çalıştıktan sonra `sayı` variable'ına 1 ekler ve `sayı` variable'ının değeri `1` olur.
	- Sonra, `return sayı` ile `sayı` variable'sini döndürür ve `print()` fonksiyonu bu değeri ekrana basar.
- `print(fonk1()())`'in `s2 = fonk1()` ya da `s2 = fonk1()`'den en büyük farkı:
	- `fonk1()` ile oluşturulan `fonk2` objesi bir `s1` ya da `s2` variable'larına atandığı için hafızada tutulur ve her çağırıldığında, `print()` ile ekrana bastırılan output farklı olur.
	- Ama `fonk1()()` kodundaki `fonk1()` ile oluşturulan `fonk2` objesi, ikinci parantez yüzünden `fonk2()` şeklinde kullanıldıktan sonra bellekten silinir. Bu yüzden her `print(fonk1()())` kodu `1` output'unu verir.

