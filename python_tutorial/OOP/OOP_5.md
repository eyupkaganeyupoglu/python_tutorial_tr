# Inheritance (Miras Alma)
Bir class'ın method ve class attribute'larını, başka bir class'ın miras almasına **Inheritance (Miras Alma)** denir. Method ve class attribute'ları miras alınan class; Parent class, super class, base class olarak isimlendirilir. Base class'ın method ve class attribute'larını miras alan class'da child class, derived class, subclass olarak isimlendirilir. Ben tutorial boyunca bunlardan **base class** ve **subclass** olarak bahsedeceğim. Inheritance (Miras Alma), belli method'ları ya da class attribute'ları her class'a tekrar tekrar yazma zahmetinden bizi kurtarır. Örnek:
```py
class Class1():
    def __init__(self):
        pass

    def func1(self):
        pass

    def func2(self):
        pass

    def func3(self):
        pass

class Class2(Class1):
    pass
```
Gördüğünüz gibi `Class1` class'ını `Class2` class'ının parantezine yazarak, `Class2` class'ın `Class1` class'ındaki bütün method ve class attribute'larını miras almasını sağladık.

Inheritance (Miras Alma) işleminde subclass, base class'ın method ve class attribute'larının kopyasını kendi class objesinde oluşturmaz, base class'daki method ve class attribute'lara referans verir. Örnek:
```py
class Class1():
    cs1 = "Class Attribute 1"

    def __init__(self):
        print("init çalıştı...")

    def func1(self):
        print("func1 Çalıştı...")


class Class2(Class1):
    pass
```
`Class2` subclass'ındaki instance method objesi, `Class1` base class'ındaki instance method objesidir. Kanıtı:

<img src="https://i.ibb.co/VwQgtXv/image.png" alt="image" border="0">

Gördüğünüz gibi `Class2` subclass'ındaki instance method objesinde `Class1.func1` yazmaktadır. Buradaki `Class1.func1` ifadesi, `func1` methodunun `Class1`'in instance method objesi olduğunu söylemektedir. Yani `Class2` subclass'ındaki `func1` objesi, `Class1` base class'ındaki `func1` objesine referanstır. Referans durumu söz konusu olduğu için base class'da bir değişiklik yapılırsa, bundan subclass'da etkilenir. Örneğin Yukarıdaki koda `Class1.cs1 = "Yeni Class Attribute 1"` kodunu ekleyip çalıştırırsak, hem `Class1` base class'ının hem de `Class2` subclass'ının `cs1` class attribute'unun değeri değişir. Kanıtı:

<img src="https://i.ibb.co/CwZGwxM/image.png" alt="image" border="0">

En başta `Class1` ve `Class2` birbirinden üstün olmamasına rağmen, inheritance (miras alma) işleminden sonra `Class2` class'ının subclass rütbesine düştüğünü, `Class1` class'ının da base class rütbesine yükseldiğini söyleyebiliriz. Tabi bu, lafta böyle. Python bunları base class ya da subclass olarak değerlendirmez. `Class2` class'ı `Class1` class'ından miras almış olarak değerlendirir.

Inheritance (Miras Alma)'nın çeşitleri vardır. Bir subclass, bir base class'ın bütün method ve class attribute'larını olduğu gibi miras alabilir. Örnek:
```py
class Class1():
    def __init__(self, p1, p2):
        print("init çalıştı...")
        self.a = p1
        self.b = p2
        self.c = 0

    def func1(self):
        print("func1 Çalıştı...")

    def func2(self):
        print("func2 Çalıştı...")

    def func3(self):
        print("func3 Çalıştı...")

class Class2(Class1):
    pass

print(dir(Class1) == dir(Class2)) # Output: True

var = Class2("parametre 1", "parametre 2") # Output: init çalıştı...
print(var.a) # Output: parametre 1
print(var.b) # Output: parametre 2
print(var.c) # Output: 0
var.func1() # Output: func1 Çalıştı...
var.func2() # Output: func2 Çalıştı...
var.func3() # Output: func3 Çalıştı...
```
Gördüğünüz gibi `Class2` subclass'ı, `Class1` base class'ının sahip olduğu bütün method ve class attribute'ları değiştirmeden direkt miras aldı.

Bir subclass'da tanımlanmış method veya class attribute'lar (kısaca item diyelim), subclass'ın miras aldığı base class'daki item'larla çakışıyorsa (yani ikisinde de aynı isimde item'lar varsa), inheritance (miras alma) işleminden sonra subclass'ın item'ları base class'daki item'ların üzerine yazıldığı için base class'ın item'larını değil, subclass'ın item'larını kullanabilirsiniz. Örnek: 
```py
class Class1():
    def __init__(self):
        print("Class1 init çalıştı...")

    def func1(self):
        print("func1 Çalıştı...")

class Class2(Class1):

    def func1(self):
        print("Class2'deki func1 Çalıştı...")

print(dir(Class1) == dir(Class2)) # Output: True
var1 = Class1() # Output: Class1 init çalıştı...
var2 = Class2() # Output: Class1 init çalıştı...
var1.func1() # Output: func1 Çalıştı...
var2.func1() # Output: Class2'deki func1 Çalıştı...
```
Gördüğünüz gibi `Class2` subclass'ında `func1` instnace methodu zaten tanımlı olduğu için inheritance (miras alma) işleminden sonra `Class2` subclass'ının `func1` instnace methodu, `Class1` base class'ının `func1` instnace methodunun üzerine yazıldı ve `var.func1()` kodu `Class1` base class'ının `func1` instnace methodundaki `print("func1 Çalıştı...")` kodunu değil, `Class2` base class'ının `func1` instnace methodundaki `print("Class2'deki func1 Çalıştı...")` kodunu çalıştırdı. Aynı şey class attribute'lar için de geçerlidir. Örnek:
```py
class Class1():
    cs1 = "Class Attribute 1"
    def __init__(self):
        print("init çalıştı...")
        pass

class Class2(Class1):
    cs1 = "Class2'nin Class Attribute 1"

print(dir(Class1) == dir(Class2)) # Output: True

var = Class2() # Output: init çalıştı...
print(Class1.cs1) # Output: Class Attribute 1
print(var.cs1) # Output: Class2'nin Class Attribute 1
```