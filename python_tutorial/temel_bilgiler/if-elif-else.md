# İçindekiler
- [`if` Statement](#1)
- [`elif` Statement](#2)
- [`else` Statement](#3)
- [Tek satırda `if` - `else` tanımlamak](#4)

<h1 id="1"><code>if</code> Statement</h1>

"Eğer ..." anlamına gelmektedir. Syntax'ı:
```py
if (condition):
	# Expression
``` 
`condition`'a girilen koşul sağlanıyorsa (`True`) Python, `if` statement kod block'unu okur ve çalıştırır; sağlanmıyorsa (`False`) okunmaz ve bir sonraki statement'a geçer. Örnek:
```py
sayı = int(input("Sayı gir: "))
if sayı == 0:
    print("Girdiğiniz sayı 0'dır.")
if sayı < 0:
    print("Girdiğiniz sayı 0'dan küçüktür.")
if sayı > 0:
    print("Girdiğiniz sayı 0'dan büyüktür.")
```
**Outputs:**
```
Sayı gir: 0
Girdiğiniz sayı 0'dır.
```
```
Sayı gir: 1
Girdiğiniz sayı 0'dan büyüktür.
```
```
Sayı gir: -1
Girdiğiniz sayı 0'dan küçüktür.
```

**Not:** Bir `if` statement'ın çalışması diğer `if` statement'ları etkilemez. Yani her `if` statement bağımsızdır. Örnek:
```py
sayı = int(input("Sayı gir: "))
if sayı == 0:
    print("Girdiğiniz sayı 0'dır.")
if sayı < 10:
    print("Girdiğiniz sayı 10'dan küçüktür.")
if sayı > -10:
    print("Girdiğiniz sayı -10'dan büyüktür.")
```
**Output:**
```
Sayı gir: 0
Girdiğiniz sayı sıfırdır.
Girdiğiniz sayı 10'dan küçüktür.
Girdiğiniz sayı -10'dan büyüktür.
```
Gördüğünüz gibi `condition`'a girilen koşulu sağlayan bütün `if` statement'lar çalıştı.

<h1 id="2"><code>elif</code> Statement</h1>

`else if`'den türemiştir. "... değilse, eğer ..." anlamına gelmektedir. Syntax:
```py
# else if syntax:
else: # daha sonra anlatılacak
	if (condition):
		# Expression
```
```py
# elif statement
elif (condition):
	# Expression
```
`if` statement gibi tak başına kullanılamaz, `if` statement'a bağımlıdır. Sadece kendinden önceki `if` ya da `elif` statement çalışmazsa ve `condition`'a girilen koşul sağlanıyorsa çalışır. Örnek:
```py
sayı = int(input("Sayı gir: "))
if sayı == 0:
    print("Girdiğiniz sayı 0'dır.")
elif sayı < 0:
    print("Girdiğiniz sayı 0'dan küçüktür.")
elif sayı > 0:
    print("Girdiğiniz sayı 0'dan Büyüktür.")
```
**Outputs:**
```
Sayı gir: 0
Girdiğiniz sayı 0'dır.
```
```
Sayı gir: 1
Girdiğiniz sayı 0'dan Büyüktür.
```
```
Sayı gir: -1
Girdiğiniz sayı 0'dan küçüktür.
```
Bu kısmın, `elif` yerine `if` statement kullandığımız seferkinden output olarak farkı yok gibi gözüküyor. Başka bir örnek:
```py
sayı = int(input("Sayı gir: "))
if sayı == 0:
    print("Girdiğiniz sayı 0'dır.")
elif sayı < 10:
    print("Girdiğiniz sayı 10'dan küçüktür.")
elif sayı > -10:
    print("Girdiğiniz sayı -10'dan büyüktür.")
```
**Outputs:**
```
Sayı gir: 0
Girdiğiniz sayı 0'dır.
```
```
Sayı gir: 9
Girdiğiniz sayı 10'dan küçüktür.
```
```
Sayı gir: 11
Girdiğiniz sayı -10'dan büyüktür.
```
`sayı` variable'ına input olarak `0` value'sunu girdiğimizde, `0` sayısı `10`'dan küçük ve `-10`'dan büyük olmasına rağmen sadece `if` statement çalıştı. Benzer şey `9` value'sunda da oldu. `9` sayısı `10`'dan küçük ve `-10`'dan büyük olmasına rağmen sadece ilk `elif` statement çalıştı. Çünkü `elif` statement sadece kendinden önceki `if` ya da `elif` statement çalışmazsa ve `condition`'a girilen koşul sağlanıyorsa çalışır.

**Not:** `if` ve `elif` statement'ların `condition` kısmına yazacağınız koşulları parantez içine almakla almamak arasında bir fark yoktur. örnek:
```py
if True:
    print("Hello")

if (False):
    pass
elif (True):
    print("World")
```
**Output:**
```
Hello
World
```

<h1 id="3"><code>else</code> Statement</h1>

"... değilse ..." anlamına gelmektedir. Syntax:
```py
else:
	# Expression
```

`if` statement gibi tak başına kullanılamaz, `if` statement'a bağımlıdır. `else` statement sadece kendinden önceki `if` ya da `elif` statement çalışmazsa çalışır. Örnek:
```py
sayı = int(input("Sayı gir: "))
if sayı == 0:
	print("Girdiğiniz sayı 0'dır.")
else:
	print("Girdiğiniz sayı 0 değildir.")
```
**Outputs:**
```
Sayı gir: 0
Girdiğiniz sayı 0'dır.
```
```
Sayı gir: 1
Girdiğiniz sayı 0 değildir.
```

Başka bir örnek:
```py
sayı = int(input("Sayı gir: "))
if sayı == 0:
	print("Girdiğiniz sayı 0'dır.")
elif sayı == 1:
	print("Girdiğiniz sayı 1'dir.")
else:
	print("Girdiğiniz sayı 0 ya da 1 değildir.")
```
**Outputs:**
```
Sayı gir: 0
Girdiğiniz sayı 0'dır.
```
```
Sayı gir: 1
Girdiğiniz sayı 1'dir.
```
```
Sayı gir: 2
Girdiğiniz sayı 0 ya da 1 değildir.
```

**Not:** [`elif` Statement](#2) başlığında da gördüğünüz gibi herhangi bir `if` veya `if` - `elif` statement, `else` statement olmadan da çalışabilir ama `else` statement'ın tek çalışma koşulu kendinden önceki `if` ya da `elif` statement çalışmaması olduğu için kendinden önce çalışmayan bir `if` ya da `elif` statement'a ihtiyaç duyuyor.

**Not:** Her `else` statement, kendinden önceki `if` ya da `elif` statement'ı dikkate alır. Örnek:
```py
if False: # 1. `if` statement
    pass
else:
    print("1. `else` çalıştı.")

if False: # 2. `if` statement
    pass
else:
    print("2. `else` çalıştı.")

if False:
    pass
elif False:
    pass
else:
    print("3. `else` çalıştı.")
```
**Output:**
```
1. `else` çalıştı.
2. `else` çalıştı.
3. `else` çalıştı.
```
Gördüğünüz gibi her `else` statement, kendinden hemen önceki ilk `if` ya da `elif` statement'ı dikkate alır. Yukarıdaki kodda tanımlanmış 2. `else` statement'ın 1. `if` statement'ı değil 2. `if` statement'ı dikkate alması bunun kanıtıdır.

<h1 id="4">Tek satırda <code>if</code> - <code>else</code> tanımlamak</h1>

`(Expression) if (condition) else (Expression)` yapısını kullanarak tek satırda `if` - `else` yapısı oluşturabilirsiniz. Örnek:
```py
(print(1)) if True else (print(2)) # Output: 1
print(1) if True else print(2) # Output: 1

(print(1)) if False else (print(2)) # Output: 2
print(1) if False else print(2) # Output: 2
```
`Expression` kısımlarını parantez içine almakla almamak arasında işlevsel olarak bir fark yoktur. Parantezler sadece, kullanıcının kodu anlamasını kolaylaştırır. Daha karmaşık bir örnek:
```py
((print(1)) if True else (print(2))) if True else ((print(3)) if True else print(4)) # Output: 1
((print(1)) if False else (print(2))) if True else ((print(3)) if True else print(4)) # Output: 2
((print(1)) if False else (print(2))) if False else ((print(3)) if True else print(4)) # Output: 3
((print(1)) if False else (print(2))) if False else ((print(3)) if False else print(4)) # Output: 4
```