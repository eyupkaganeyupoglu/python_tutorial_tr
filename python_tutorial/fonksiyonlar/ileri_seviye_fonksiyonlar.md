# `lambda` fonksiyonu
Bu fonksiyon, `lambda arguments : expression` syntax'ına sahiptir.
```py
def func1 (p1,p2):
    return (p1 + p2)
print(func1(2,3)) # Output: 5
print(func1) # Output: <function func1 at 0x000002243DB2BEE0>

func2 = lambda p1,p2: (p1 + p2)
print(func2(2,3)) # Output: 5
print(func2) # Output: <function <lambda> at 0x000002243DB2BF70>
```
`func1` ile `func2` aynı işleve sahiptir. `lambda` fonksiyonuna tanımlanan `arguments`, `def` ile tanımlanan fonksiyonlardaki parametre kısmına denk gelmektedir. `:`'dan sonraki kısım da `def` ile tanımlanan fonksiyonlardaki `return` keyword'ünü temsil eder. Örnek:
```py
func1 = lambda p1: ("Bu 2'dir.") if p1==2 else ("Bu 2 değildir.")
print(func1(1)) # Output: Bu 2 değildir.
print(func1(2)) # Output: Bu 2'dir.
```
Burada tek satırlık `if` - `else` yapısı kullanılarak `lambda` fonksiyonuna farklı `return` değerleri tanımlanabildi. Bu gibi kullanımlar, `sorted()` fonksiyonundaki `key` parametresi gibi yerlerde kullanılır. Örnek:
```py
elemanlar = [("bir", 1),
             ("dört", 4),
             ("üç", 3),
             ("iki", 2),
             ("beş", 5)]

def sırala(liste):
    return liste[1]
    
print(*sorted(elemanlar, key=sırala), sep='\n')
```
**Output:**
```
('bir', 1)
('iki', 2)
('üç', 3)
('dört', 4)
('beş', 5)
```
Yukarıdaki kodu `lambda` kullanarak şöyle yazarız:
```py
elemanlar = [("bir", 1),
             ("dört", 4),
             ("üç", 3),
             ("iki", 2),
             ("beş", 5)]
    
print(*sorted(elemanlar, key=lambda p1:(p1[1])), sep='\n')
```
**Output:**
```
('bir', 1)
('iki', 2)
('üç', 3)
('dört', 4)
('beş', 5)
```

# Recursive (Özyinelemeli) Fonksiyonlar
Bir fonksiyon çalıştığında, kendi scope'unda başka bir fonksiyonu çağırabilir. Örnek:
```py
def selamla():
    print("Selam")
selamla() # Output: Selam
```
Görüldüğü gibi `selamla()` fonksiyonu `print()` fonksiyonunu çağırabiliryor. Bu durum, bir fonksiyon kendi scope'unda kendisini çağırdığı durumlarda da geçerkidir. Örnek:
```py
def selamla():
    print("selam")
    selamla()
selamla()
```
Yukarıdaki fonksiyona **recursive (Özyinelemeli) fonksiyon** nedir. Yukarıdaki fonksiyon sürekli kendini yeniden çalıştırır. Bu fonsiyon, `RecursionError` hatası vermeden önce belli bir maksimum çalışma sayısına sahiptir. Bu sınırı aşağıdaki kodla öğrenebilirsiniz:
```py
import sys
print(sys.getrecursionlimit()) # Output: 1000
```
Recursive fonksiyon sonsuz döngüye girerse `RecursionError: maximum recursion depth exceeded while calling a Python object` hatası verir. Başka bir örnek:
```py
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

# Nasted (İç İçe) Fonksiyonlar
İç içe fonksiyonlarda, en dıştaki (yani global scope'da tanımlanan) fonksiyon **enclosing**, enclosing'in scope'una tanımlanan bütün fonksiyonlar da **nasted** olarak isimlenirilir.
```py
def yazıcı():
    print("Yazıcı Çalıştı.")
    def yaz(mesaj):
        print(mesaj)
    return yaz
```
Yukarıdaki fonksiyonda, `yazıcı()` fonksiyonunu çağırmadan `yaz()` fonksiyonunu çağıramayız. Bu her yerde böyledir. Çünkü `yazıcı()` fonksiyonunu çağırdığımızda onu tanımlamış oluyoruz ve `yazıcı()` fonksiyonunu tanımlamadan `yaz()` fonksiyonunu direkt çağıramayız. `yazıcı()` fonksiyonu her çağırıldığında `yaz()` fonksiyonu baştan tanımlanır. Yani `yazıcı()` fonksiyonunu ilk çağırışınızdaki `yaz()` fonksiyonu ile  `yazıcı()` fonksiyonunu ikinci çağırışınızdaki `yaz()` fonksiyonu birbirinden farklı objelerdir. Bu objeler `<function yazıcı.<locals>.yaz at 0x00000210D9235558>` şeklindedir.