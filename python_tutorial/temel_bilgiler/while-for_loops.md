# İçindekiler

- [Loop Yapısı](#1)
    - [`while` Loop](#1.1)
    - [`for` Loop](#1.2)
        - [String'lere Davranışı](#1.2.1)
        - [List'lere Davranışı](#1.2.2)
        - [Dictionary'lere Davranışı](#1.2.3)
    - [Loop Control Statements](#1.3)
        - [`break` Statement](#1.3.1)
        - [`continue` Statement](#1.3.2)
        - [`pass` Statement](#1.3.3)
    - [`else` statement'ın Loop'larda Kullanımı](#1.4)
    - [Nested Loops](#1.5)

<h1 id="1">Loop Yapısı</h1>

Birbirini tekrar eden döngüler oluşturmamızı sağlayan yapılara döngü (loop) denir. Bazı örnekler:
```py
a = 0
while a < 5:
    if a == 4:
        print(a)
        a += 1
    else:
        print(a, end=", ")
        a += 1

for i in range(5,10):
    if i == 9:
        print(i)
    else:
        print(i, end=", ")
```
**Output:**
```
0, 1, 2, 3, 4
5, 6, 7, 8, 9
```

<h2 id="1.1"><code>while</code> Loop</h2>

`while`, "... olduğu sürece" anlamına gelmektedir. Syntax:
```py
while (condition):
    # Expression
```
`while` loop, belirli bir koşul sağlandığı sürece tekrar eden loop'lar oluşturmamızı sağlar. `condition` sağlandığı (`True`) sürece loop yinelenmeye devam edecektir. Örnek:
```py
a = 0
while a < 5:
    print(a, end=" ")
    a += 1
```
**Output:**
```
0 1 2 3 4 
```

**Not:** Herhangi bir nedenden dolayı loop'un sonsuza kadar kendini tekrarlamasına **sonsuz döngü (infinite loop)** denir. `while` loop kolayca infinite loop'a girebilen bir yapıdır. Yukarıdaki örnekte `a += 1` statement olmasaydı, bu loop sonsuza kadar `0` yazdırılmasına sebep olacaktı. Infinite loop'a girmekten bizi koruyan ve loop'u isteğe bağlı kontrol etmemizi sağlayan variable'a **loop control variable** denir. Yukarıdaki örnekteki `a` variable'ı loop control variable'a örnektir. Bazı örnekler:
```py
max_number = int(input("Kaça kadar sayalım?: "))
min_number = 1
while (min_number != max_number):
	print(min_number, end=", ")
	min_number += 1
print(max_number)
```
**Output:**
```
Kaça kadar sayalım?: 10
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```
Bu kodda, 1'den başlayıp `max_number` variable'ına atadığınız input değerinde belirtilen sayıya kadar yazdıran bir `while` loop vardır. Başka bir örnek:
```py
liste_exp = [12,15,18,26,38]
index = 0
while (index != (len(liste_exp)-1)):
	print(liste_exp[index], end=", ")
	index += 1
print(liste_exp[index])
```
**Output:**
```
12, 15, 18, 26, 38
```
Bu kodda, `liste_exp` variable'ına atanmış bir listenin elemanlarını sırayla yazdıran bir `while` loop vardır. Ama bu işlem için `for` loop yapısı daha kullanışlıdır. `for` loop yapısının ne olduğu daha sonra anlatılacak.

**Not:** Infinite loop'a giren programlarınızı sonlandırmak için `CTRL + C` tuş kombinasyonunu kullanabilirsiniz. Bu tuş kombinasyonu, terminal'de ve cmd'de infinite loop'a girmiş programlarınızı sonlandırır.

İsteyerek infinite loop'a girebilirsiniz. Bunun için `while True` statement kullanılır. Bu yapı, `while` loop yapısının `condition` kısmına `True` tanımlamakla elde edilir. Yani `while` loop'dan farklı ya da özelleşmiş bir yapı değildir (aynı `if True:` gibi).  Örnek:
```py
while True:
    sayı = int(input("Bir sayı giriniz: "))
    print("Girdiğiniz sayı:", sayı)
```
**Output:**
```
Bir sayı giriniz: 1
Girdiğiniz sayı: 1
Bir sayı giriniz: 2
Girdiğiniz sayı: 2
Bir sayı giriniz: 5
Girdiğiniz sayı: 5
Bir sayı giriniz: 7
Girdiğiniz sayı: 7
Bir sayı giriniz: a
ValueError: invalid literal for int() with base 10: 'a'
```
Gördüğünüz gibi hata yükseltene veya elle sonlandırana kadar sonsuza kadar devam eden bir döngü elde ettik. Bu kodu şöyle geliştirebiliriz:
```py
while True:
    try:
        sayı = input("Bir sayı giriniz: ")
        print("Girdiğiniz sayı:", int(sayı))

    except ValueError:
        if sayı == "çıkış":
            print("Loop sonlandırılıyor...")
            break
        else:
            print("Lütfen bir sayı giriniz!")
            continue
```
**Output:**
```
Bir sayı giriniz: 1
Girdiğiniz sayı: 1
Bir sayı giriniz: 2
Girdiğiniz sayı: 2
Bir sayı giriniz: a
Lütfen bir sayı giriniz!
Bir sayı giriniz:
Lütfen bir sayı giriniz!
Bir sayı giriniz: çıkış
Loop sonlandırılıyor...
```
Buradaki bilmediğiniz kodlar daha sonra anlatılacak. Yukarıdaki kodda, input olarak sayı girmediğimizde Python, hata yükseltip programı sonlandırmak yerine `Lütfen bir sayı giriniz!` yazdırdı ve loop'a devam etti. Input olarak `çıkış` string'ini girdiğimizde de `break` statement (daha sonra anlatılacak) sayesinde loop'u sonlandırdı.

**Not:** `while` loop'ın kapsamında (scope) tanımlanan variable'lar local namespace'de değildir. Yani loop sonlandıktan sonra bile bellekten silinmezler. Örnek:
```py
while True:
    a = 0
    break

print(a) # Output: 0
```

<h2 id="1.2"><code>for</code> Loop</h2>

`for` loop, kendisine verilen **Iterable** (yinelenebilir) bir objeden loop içinde kullanmak için bir **Iterator** objesi (daha sonra anlatılacak) oluşturur. Bu işlemler arka planda gerçekleştiği için kullanıcılar tarafından direkt gözlemlenemez. Bu iterator objesi, `StopIteration` hatası yükseltilene kadar yinelemeye (next) devam eder. `for` loop syntax'ı:
```py
for loop_control_variable in iterable_object:
	# Expression
```
Buradaki `iterable_object`, `for` loop'ın iterator oluşturmakta kullandığı iterable bir objedir. `loop_control_variable` ise, bu iterator'ın içerisindeki her gezinildiğinde elde edilen value'nun atandığı variable'dır. `loop_control_variable`, `for` loop'un kapsamında (scope) kullanılabilir.

**Not:** `for` loop'ın kapsamında (scope) tanımlanan variable'lar local namespace'de değildir. Yani loop sonlandıktan sonra bile bellekten silinmezler. Örnek:
```py
for i in range(5):
    pass

print(i) # Output: 4
```

Şimdi iterator ve iterable kavramlarını açıklayalım:

**Ön bilgi:** Bu bölümü anlayabilmek için iterator ve iterable kavramlarını bilmeniz gerekmektedir. Gerekli bilgiler için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/iterators.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/functions/iterators.md").

Python'daki `for` loop mantığı `C` gibi low level programlama dillerindeki **for-each** loop mantığına dayanır. For-each loop ile ilgili bilgi için [**buraya**](https://en.wikipedia.org/wiki/Foreach_loop "https://en.wikipedia.org/wiki/Foreach_loop"), for loop'un çalışma mantığıyla ilgili ayrıntılı bilgi için de [**buraya**](https://towardsdatascience.com/python-basics-iteration-and-looping-6ca63b30835c "https://towardsdatascience.com/python-basics-iteration-and-looping-6ca63b30835c") tıklayınız.

Aşağıdaki `for` ve `while` loop kodları biribiriyle tamamen aynı çalışır:
```py
a = [1,2,3,4,5]
for i in a:
	print(i)
```
```py
a = [1,2,3,4,5]
b = iter(a)
while True:
	try:
		i = next(b)
	except StopIteration:
		break
	print(i)
```

Bir `for` loop'un `loop_control_variable` veya `iterable_object` kısımlarına comma (`,`) operator'ı kullanarak birden fazla şey girdiğinizde, Python'ın davranışları değişir. Bazı örnekler:

<h3 id="1.2.1">String'lere Davranışı</h3>

```py
a1 = "123"
a2 = "456"
a3 = "789"

for i in a1:
    print(i, end=", ")
```
**Output:**
```
1, 2, 3,
```
`for` loop `a1` string'ini iterator objesine dönüştürdükten sonra indexleri içinde geziniyor. Bu basit bir örnek, anlamışsınızdır zaten. Başka bir örnek:
```py
a1 = "123"
a2 = "456"
a3 = "789"

for i in a1,a2,a3:
    print(i, end=", ")
```
**Output:**
```
123, 456, 789, 
```
`for` loop'ın `a1,a2,a3` karşı tepkisini `(a1, a2, a3)` şeklinde düşünebilirsiniz. Yani `for` loop sırayla `a1`, `a2` ve `a3` string'lerinde gezinmek yerine `(a1, a2, a3)` tuple'ının içinde geziniyor. Bu yüzden `i` variable'ına her seferinde sırasıyla bu `a1`, `a2` ya da `a3` string'leri atanıyor. Başka bir örnek:
```py
a1 = "123"
a2 = "456"
a3 = "789"

for i,j in a1,a2,a3:
    print(i,j, sep=", ")
```
**Output:**
```
ValueError: too many values to unpack (expected 2)
```
Burada `i` variable'ının `(a1, a2, a3)` yapısının içinde gezineceğini, `j` variable'ının da bu yapının içindeki `a1`, `a2` ve `a3` string'lerinin içinde gezineceğini ve `1 2 3 4 5 6 7 8 9` gibi bir output elde edeceğinizi düşünmüş olabilirsiniz ama işler öyle yürümüyor. Bu statement'in çalışması için basitçe, `for` loop'ın `loop_control_variable` kısmına tanımlanan variable sayısı ile `iterable_object` kısmına girilen objelerin her birinin eleman sayısı birbirine eşit olmalı. Buradaki hatanın sebebi ise 2 tane `loop_control_variable` tanımlıyken `iterable_object` kısmına girilen objelerin eleman sayısının 3 olmasıdır. Başka bir hatalı örnek:
```py
a1 = "1"
a2 = "4"
a3 = "7"

for i,j in a1,a2,a3:
    print(i,j, sep=", ")
```
**Output:**
```
ValueError: not enough values to unpack (expected 2, got 1)
```
Buradaki hatanın sebebi ise 2 tane `loop_control_variable` tanımlıyken `iterable_object` kısmına girilen objelerin eleman sayısının 1 olmasıdır. Başka bir hatalı örnek:
```py
a1 = "12"
a2 = "34"
a3 = "5678"

for i,j in a1,a2,a3:
    print(i,j, sep=", ")
```
**Output:**
```
1, 2
3, 4
ValueError: too many values to unpack (expected 2)
```
Buradaki hatanın sebebi ise 2 tane `loop_control_variable` tanımlıyken `iterable_object` kısmına girilen `a3` objesinin eleman sayısının tutarsız olmasıdır. Doğru kullanım örneği:
```py
a1 = "12"
a2 = "45"
a3 = "78"

for i,j in a1,a2,a3:
    print(i,j, sep=", ", end=", ")
```
**Output:**
```
1, 2, 4, 5, 7, 8, 
```
Buradaki `for` loop'da 2 tane `loop_control_variable` tanımlıdır ve `iterable_object` kısmına girilen objelerin eleman sayıları 2'dir. Sayılar tutarlı olduğu için hata yükseltilmedi. Başka bir doğru kullanım örneği:
```py
a1 = "123"
a2 = "456"
a3 = "789"

for i,j,k in a1,a2,a3:
    print(i,j,k, sep=", ")
```
**Output:**
```
1, 2, 3
4, 5, 6
7, 8, 9
```
Buradaki `for` loop'da 3 tane `loop_control_variable` tanımlıdır ve `iterable_object` kısmına girilen objelerin eleman sayıları 3'dir. Sayılar tutarlı olduğu için hata yükseltilmedi.

**Not:** Yukarıdaki koddan yola çıkarak `a1,a2,a3` kısmını `("123","456","789")` olarak, `i,j,k` kısmını da `(i,j,k)` olarak düşün ve `i=1`,`j=2`,`k=3` / `i=4`,`j=5`,`k=6` / `i=7`,`j=8`,`k=9` tarzında bir mantığın işlediğini kabul edin. Bu sayede kafanıza oturur sanırım.

**Örnek Program:** Aşağıdaki program, `cümle` variable'ına girdiğiniz input değerindeki boşluk (`" "`) karakterlerini, underscore (`"_"`) karakteri ile değiştirip, son durumu yazdırır.
```py
cümle = list(input("Bir cümle yazınız: "))

release,index="", 0
	
for j in cümle:
	if j == " ":
		cümle[index] = "_"
	release += cümle[index]
	index += 1
	
print(release)
```
**Output:**
```
Bir cümle yazınız: Selam Ben Python
Selam_Ben_Python
```

**Örnek Program:** Aşağıdaki program, `ilk_metin` variable'ında olan ve `ikinci_metin` variable'ında olmayan karakterleri tespit edip, bu kadarketleri `fark` variable'ında toplar. Bunu yaparken tespit edilen karakter `fark` içinde zaten varsa bu karakteri tekrar eklemez.
```py
# İki string arasındaki farkları bulmak
ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
fark = ""
  
for s in ikinci_metin:
	if  not s in ilk_metin:
		if  not s in fark:
			fark += s
			
print(fark)
```
**Output:**
```
uıorye
```

<h3 id="1.2.2">List'lere Davranışı</h3>

```py
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

for i in l1:
    print(i, end=", ")
```
**Output:**
```
1, 2, 3,
```
`for` loop `l1` listesini iterator objesine dönüştürdükten sonra indexleri içinde geziniyor. Bu basit bir örnek, anlamışsınızdır zaten. Başka bir örnek:
```py
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

for i in l1,l2,l3:
    print(i, end=", ")
```
**Output:**
```
[1, 2, 3], [4, 5, 6], [7, 8, 9], 
```
`for` loop'ın `l1,l2,l3` girdisine karşı tepkisini `(l1, l2, l3)` şeklinde düşünebilirsiniz. Yani `for` loop sırayla `l1`, `l2` ve `l3` listelerinde gezinmek yerine `(l1, l2, l3)` tuple'ının içinde geziniyor. Başka bir örnek:
```py
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

for i,j in l1,l2,l3:
    print(i,j, sep=", ")
```
**Output:**
```
ValueError: too many values to unpack (expected 2)
```
Buradaki hatanın nedeni önceden anlattığım string'lerdeki hatanın nedeniyle aynıdır. Başka bir hatalı örnek:
```py
l1 = [1]
l2 = [4]
l3 = [7]

for i,j in l1,l2,l3:
    print(i,j, sep=", ")
```
**Output:**
```
ValueError: not enough values to unpack (expected 2, got 1)
```
Buradaki hatanın nedeni önceden anlattığım string'lerdeki hatanın nedeniyle aynıdır. Başka bir hatalı örnek:
```py
l1 = [1,2]
l2 = [3,4]
l3 = [5,6,7,8]

for i,j in l1,l2,l3:
    print(i,j, sep=", ")
```
**Output:**
```
1, 2
3, 4
ValueError: too many values to unpack (expected 2)
```
Buradaki hatanın nedeni önceden anlattığım string'lerdeki hatanın nedeniyle aynıdır. Doğru kullanım örneği:
```py
l1 = [1,2]
l2 = [4,5]
l3 = [7,8]

for i,j in l1,l2,l3:
    print(i,j, sep=", ", end=", ")
```
**Output:**
```
1, 2, 4, 5, 7, 8, 
```
Buradaki `for` loop'da 2 tane `loop_control_variable` tanımlıdır ve `iterable_object` kısmına girilen objelerin eleman sayıları 2'dir. Sayılar tutarlı olduğu için hata yükseltilmedi. Başka bir doğru kullanım örneği:
```py
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

for i,j,k in l1,l2,l3:
    print(i,j,k, sep=", ", end=", ")
```
**Output:**
```
1, 2, 3
4, 5, 6
7, 8, 9
```
Buradaki `for` loop'da 3 tane `loop_control_variable` tanımlıdır ve `iterable_object` kısmına girilen objelerin eleman sayıları 3'dir. Sayılar tutarlı olduğu için hata yükseltilmedi.

**Not:** Yukarıdaki koddan yola çıkarak `l1,l2,l3` kısmını `([1,2,3],[4,5,6],[7,8,9])` olarak, `i,j,k` kısmını da `(i,j,k)` olarak düşün ve `i=1`,`j=2`,`k=3` / `i=4`,`j=5`,`k=6` / `i=7`,`j=8`,`k=9` tarzında bir mantığın işlediğini kabul edin. Bu sayede kafanıza oturur sanırım.

İç içe oluşturulan listelere **nested list** denir. Bu listelerin içinde de yukarıdaki gibi gezinebilirsiniz. Örnek:
```py
l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [[1,2],[3,4],[5,6]]

for i,j,k in l1:
    print(i,j,k, sep=", ", end=", ")
print()
for i,j in l2:
    print(i,j, sep=", ", end=", ")
```
**Output:**
```
1, 2, 3, 4, 5, 6, 7, 8, 9, 
1, 2, 3, 4, 5, 6,
```
Daha karmaşık bir örnek:
```py
l1 = [( (1,2) , (3,4) ) , ( (7,8) , (9,10) )]

for x,y,z in l1:
    print(x,y,z, sep=", ", end=", ")
```
**Output:**
```
ValueError: not enough values to unpack (expected 3, got 2)
```
Böyle bir yapının içinde gezinebilmek için **nested `for` loop** yapısını (daha sonra anlatılacak) kullanmalısınız. Burada `l1` listesinin öğelerinin 2 öğesi olduğu için 2 `loop_control_variable` kullanmalıyız. Örnek:
```py
l1 = [( (1,2) , (3,4) ) , ( (7,8) , (9,10) )]

for x,y in l1:
    print(x,y, sep=", ", end=", ")
```
**Output:**
```
(1, 2), (3, 4), (7, 8), (9, 10), 
```

[List'lere Davranışı](#1.2.2) başlığından şimdiye kadar anlatılan şeyler `tuple`, `set`, `frozenset`, `range` gibi data type'larda da geçerlidir. sadece `set` ve `frozenset`'de olduğu gibi `list` data type'ı ile %100 aynı şekilde sonuçlanmaz. Örnek:
```py
s1 = {1,2,3}
s2 = {4,5,6}
s3 = {7,8,9}

for i,j,k in s1,s2,s3:
    print(i,j,k, sep=", ", end=", ")
```
**Output:**
```
1, 2, 3, 4, 5, 6, 8, 9, 7, 
```

<h3 id="1.2.3">Dictionary'lere Davranışı</h3>

```py
dict_exp = {"bir": 1,"iki": 2,"üç": 3,"dört": 4}
  
for i in dict_exp:
	print(i, end=", ")
```
**Output:**
```
bir, iki, üç, dört,
```
`for` loop `dict_exp` dictionary'sini iterator objesine dönüştürdükten sonra indexleri içinde geziniyor. Bu basit bir örnek. Dictionary konusu daha sonra anlatılacak, o zaman daha iyi anlarsınız bu kodu. Yukarıda kodda `iterable_object` kısmına `dict_exp` yerine `dict_exp.keys()` (`keys` methodunun ne olduğu daha sonra anlatılacak) yazsanız da aynı sonucu alırdınız. `dict_exp.values()` (`values` methodunun ne olduğu daha sonra anlatılacak) yazsanız `1, 2, 3, 4, ` output'unu alırdınız. Başka bir örnek:
```py
dict_exp = {"bir": 1,"iki": 2,"üç": 3,"dört": 4}

for i,j in dict_exp.items():
	print(i,j, sep=", ", end=" | ")
```
**Output:**
```
bir, 1 | iki, 2 | üç, 3 | dört, 4 | 
```
Buradaki `dict_exp.items()` kodu `dict_items([('bir', 1), ('iki', 2), ('üç', 3), ('dört', 4)])` objesini döndürür. `loop_control_variable` kısmında tanımlanan `i,j` variable'larının bu liste içinde nasıl gezdiğini daha önce anlattım.


<h2 id="1.3">Loop Control Statements</h2>

<h3 id="1.3.1"><code>break</code> Statement</h3>

`break` statement, kapsamında (scope) bulunduğu ilk loop'u bir anda sonlandırır. Böylelikle loop, hiçbir koşula bağlı kalmadan sonlanmış olur. Örnek:
```py
a = 0
while a < 5:
    if a == 2:
        print(a)
        break
    else:
        print(a, end=", ")
        a += 1

for i in range(5,10):
    if i == 7:
        print(i)
        break
    else:
        print(i, end=", ")
```
**Output:**
```
0, 1, 2
5, 6, 7
```

`break` statement, kapsamında bulunduğu **ilk loop'u** bir anda sonlandırır demiştim. Örnek:
```py
for i in ["bir", "iki", "üç"]:
    for j in [1,2,3]:
        if j == 3:
            break
        print(j, end=" ")
    print(i, end=" ")
```
**Output:**
```
1 2 bir 1 2 iki 1 2 üç 
```
Gördüğünüz gibi `j == 3` koşulu sağlandığınıda `if` statement, dolayısıla `break` statement çalıştı ve nasted `for` loop sonlandırıldı. Bu yüzden son durumda output'ta `3` yok. Buradan anlıyoruz ki, `break` statement sadece kapsamında bulunduğu **ilk loop'u** etkiliyor. Başka bir örnek:
```py
a = 1
while a <= 3:
    b = 1
    while b <= 3:
        if b == 2:
            break
        print(b, end=" ")
        b += 1
    print("|-", a, end=" -| ")
    a += 1
```
**Output:**
```
1 |- 1 -| 1 |- 2 -| 1 |- 3 -| 
```
Gördüğünüz gibi `b == 2` koşulu sağlandığınıda `if` statement, dolayısıla `break` statement çalıştı ve nasted `while` loop sonlandırıldı. Bu yüzden son durumda output `1 2 3 |- 1 -| 1 2 3 |- 2 -| 1 2 3 |- 3 -| ` yerine `1 |- 1 -| 1 |- 2 -| 1 |- 3 -| ` şeklinde.

<h3 id="1.3.2"><code>continue</code> Statement</h3>

`continue` statement, `break` statement gibi kapsamında bulunduğu ilk loop'u etkiler. Bir loop `continue` statement ile karşılaşınca yinelenir. Bu yüzden Python, `continue` statement'dan sonraki işlemleri çalıştırmaz. Örnek:
```py
for i in range(11):
    if i % 2 == 0:
        continue
    print(i, end=" ")

print()

sayı = 0
while sayı <= 10:
    if sayı % 2 == 0:
        sayı += 1
        continue
    print(sayı, end=" ")
    sayı += 1
```
**Output:**
```
1 3 5 7 9 
1 3 5 7 9
```
Gördüğünüz gibi `for` ve `while` statement'lara tanımlanan `continue` statement her çalıştığında loop yinelendi. Bu yüzden tek sayılar yazdırılmadı. Başka bir örnek:
```py
for i in ["a","b","c"]:
    for j in [1,2,3]:
        if j == 2:
            continue
        print(j, end=" ")
    print(i, end=" ")
```
**Output:**
```
1 3 a 1 3 b 1 3 c
```
Gördüğünüz gibi `j == 2` koşulu sağlandığınıda `if` statement, dolayısıla `continue` statement çalıştı ve Python loop'u yineledi. Bu yüzden son durumda output'ta `2` yok. Buradan anlıyoruz ki, `continue` statement sadece kapsamında bulunduğu **ilk loop'u** etkiliyor. Başka bir örnek:
```py
a = 1
while a <= 3:
    b = 1
    while b <=3:
        if b == 2:
            b += 1
            continue
        print(b, end=" ")
        b += 1
    print("|-", a, end=" -| ")
    a += 1
```
**Output:**
```
1 3 |- 1 -| 1 3 |- 2 -| 1 3 |- 3 -|
```
Gördüğünüz gibi `b == 2` koşulu sağlandığınıda `if` statement, dolayısıla `continue` statement çalıştı ve Python nasted `while` loop'u yineledi. Bu yüzden son durumda output `1 2 3 |- 1 -| 1 2 3 |- 2 -| 1 2 3 |- 3 -| ` yerine `1 3 |- 1 -| 1 3 |- 2 -| 1 3 |- 3 -| ` şeklinde.

<h3 id="1.3.3"><code>pass</code> Statement</h3>

`pass` statement, "hiçbir şey yapma, geç." anlamına gelmektedir. Python, program içinde herhangi bir yerde `pass` statement ile karşılaşırsa, hiçbir şey yapmadan devam eder. Örnekler:
```py
class A:
    pass

def func():
    pass

a = 0
while a < 3:
    a += 1
    pass

for i in range(10):
    pass
```

**Not:** `pass` statement çok boş ve basit gözükse bile bir algoritmayı koda dönüştürürken bazı durumlarda kullanılması zorunludur.

<h2 id="1.4"><code>else</code> statement'ın Loop'larda Kullanımı</h2>

`while` loop, `condition`'a tanımlanan işlem sağlandığı (`True`) sürece; `for` loop ise, `iterable_object` kısmına girilen obje `StopIteration` hatası yükseltilmediği sürece yineleniyordu. `while` ve `for` loop'dan sonra tanımlayacağımız bir `else` statement, `while` loop'un `condition` kısmına tanımlanan işlem sağlanmadığında (`False`), `for` loop'un `iterable_object` kısmına girilen obje `StopIteration` hatası yükselttiğinde çalışır. Örnek:
```py
for i in range(10):
    print(i, end=" ")
else:
    print("Bitti")

a = 0
while a < 10:
    print(a, end=" ")
    a += 1
else:
    print("Bitti")
```
**Output:**
```
0 1 2 3 4 5 6 7 8 9 Bitti
0 1 2 3 4 5 6 7 8 9 Bitti
```

**Not:** Burada dikkat edilmesi gereken şey, `while` ve `for` loop bir şekilde `break` statement ile karşılaşıp sonlanırsa, `else` statement çalışmaz. Örnek:
```py
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
else:
    print("Bitti")

a = 0
while a < 10:
    if a == 5:
        break
    print(a, end=" ")
    a += 1
else:
    print("Bitti")
```
**Output:**
```
0 1 2 3 4 0 1 2 3 4 
```

<h2 id="1.5">Nested Loops</h2>

İç içe loop'larda, en dıştaki (yani diğer bütün loop'ları kapsayan) loop'lar **enclosing loop**, enclosing loop'un scope'una tanımlanan bütün loop'lar da **nested loop** olarak isimlenirilir. Örnek:
```py
for i in range(2):
    for j in range(2):
        for k in range(2):
            print(3, end=" ")
        print(2, end=" ")
    print(1, end=" ")
```
**Output:**
```
3 3 2 3 3 2 1 3 3 2 3 3 2 1 
```
Başka bir örnek:
```py
a = 0
while a <= 1:
    b = 0
    while b <= 1:
        c = 0
        while c <= 1:
            print(3, end=" ")
            c += 1
        print(2, end=" ")
        b += 1
    print(1, end=" ")
    a += 1
```
**Output:**
```
3 3 2 3 3 2 1 3 3 2 3 3 2 1 
```
Nested loop'lar sayesinde nested `list`, `tuple`, `dict` vs. gibi objelerin içinde rahatlıkla gezebiliriz. Daha önce içinde gezemediğimiz bir liste örneğini verelim:
```py
l1 = [( (1,2) , (3,4) ) , ( (5,6) , (7,8) ) , ( (9,10) , (11,12) )]
for i in l1:
    for j in i:
        for k in j:
            print(k, end=", ")
```
**Output:**
```
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
```
Buradaki püf nokta nested `for` loop ile nested `list` sayısı aynı olmak zorunda. Aksi duruma bir örnek:
```py
l1 = [( (1,2) , (3,4) ) , (5,6)]
for i in l1:
    for j in i:
        for k in j:
            print(k, end=", ")
```
**Output:**
```
    for k in j:
TypeError: 'int' object is not iterable
```
Bu `for` loops yapısı ilk çalıştığında `i:( (1,2) , (3,4) )`, `j:(1,2)` ve `k:1` şeklinde gezinir. Gezinirken bir ara `i:(5,6)` ve `j:5` olur ama `5` iterable bir obje olmadığı için `k` `5`'in içinde gezinemez ve `TypeError: 'int' object is not iterable` hatası yükseltilir. Diğer data type'larda da benzer sorunlarla karşılaşabilirsiniz. Bu yüzden "nested `for` loop ile nested `list` sayısı aynı olmak zorunda" kuralına uyunuz.
