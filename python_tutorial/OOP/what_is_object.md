# İçindekiler

- [Nesne/Obje Nedir?](#1)
    - [First Class Objects](#1.1)

<h1 id="1">Nesne/Obje Nedir?</h1>

Python'da belli birtakım methodlara ve/veya attribute'lara sahip olan şeylere nesne/obje adı verilir. Yani 'nesne' kelimesi, içinde birtakım method ve/veya attribute'lar barındıran öğeleri tanımlamak için kullanılan bir tabirden, basit bir isimlendirmeden ibarettir. İngilizcesi **object**'dir. Örnek:
```py
class A():
    pass

print(dir(A()))
```
**Output:**
```
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```
Gördüğünüz gibi kod block'una hiçbir şey tanımlamadığımız bir class bile içerisinde birçok fonksiyon ve attribute'e sahiptir. İşte nesne/obje tam olarak budur.

**Not:** Python'da `if`, `def`, `and`, `or` gibi keyword, statement ve operator'lar hariç her şey bir objedir. Bunlara ulaşmak için [tıklayınız](https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/statements/statements_and_keywords.md "https://github.com/e-k-eyupoglu/python_tutorial/blob/main/python_tutorial/statements/statements_and_keywords.md").

<h2 id="1.1">First Class Objects</h2>

Python'un yaratıcısı Guido van Rossum şöyle bir şey söylemiş:

> "Python'a ilişkin hedeflerimden bir tanesi de, bu dili, bütün nesneler 'birinci sınıf' olacak şekilde tasarlamaktı. Bununla kastettiğim, dil içinde kendisine bir isim verilebilen bütün nesnelerin (örn. tam sayılar, karakter dizileri, fonksiyonlar, sınıflar, modüller, methodlar, vb.) eşit statüye sahip olmasıdır. Yani, bütün nesnelerin değişkenlere atanabilmesi, listelerin içine yerleştirilebilmesi, sözlükler içinde depolanabilmesi, argüman olarak atanabilmesi vesaire…"

Buradan anlamamız gereken şey, Python'un asıl amacının bütün nesnelerin eşit statüde olması ve bu sayede birbiriyle kolayca etkileşime geçebilmesidir. Örneğin:
- Başka bir fonksiyona veya class'a parametre olarak verilebilirler.
```py
class Class1():
    def __init__(self):
        print("Başarılı!!!")

class Class2(Class1): # Class'a parametre olarak verilebilmesi (Buna parametre olarak verilmekten ziyade miras alma deniyor. Daha sonra anlatılacak)
    def __init__(self):
        print("Başarılı!!!")
        
print(Class2()) # fonksiyona parametre olarak verilebilmesi
```
**Output:**
```
Başarılı!!!
<__main__.Class2 object at 0x000001677129DFD0>
```
- Bir fonksiyondan döndürülebilirler.
```py
class Class():
    def __init__(self):
        print("Başarılı!!!")

def func():
    return Class()

func() # Output: Başarılı!!!
```
- Bir variable'a atanabilirler.
```py
class Class():
    def __init__(self):
        print("Başarılı!!!")

değişken = Class() # Output: Başarılı!!!
```
First Class Object özelliğine sahip olmayan Python dışındaki dillerin şöyle sıkıntıları vardır:
- Öğelerin kullanımına ilişkin çeşitli kısıtlamalar vardır ama Python'da her nesneyi her nesneyle beraber kullanabilirsiniz.
- Yeni öğeler arasında ayrım yapılır ama Python'da bütün öğeler aynı haklara sahiptir.
- Variable'lar, fonksiyonlar ve class'lar aynı haklara sahip değildir ama Python'da her şey bir nesnedir ve her nesne aynı haklara sahiptir.
- Bir variable'ı ya da value'yu kullanabildiğiniz her yerde fonksiyon ya da class kullanamazsınız ama Python'da her şey bir nesnedir ve her nesne her yerde eşit muamele görür.
- Kısaca Yeni fonksiyon ve/veya class'lar First Class Object değildir.