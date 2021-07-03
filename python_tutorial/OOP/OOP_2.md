# Class Methods
Bir class içinde tanımlanan user-defined (kullanıcı tanımlı) fonksiyonlar, aksi belirtilmediği sürece Python tarafından instance method olarak kabul edilir ve bu yüzden bu methodların ilk parametresi `self` olmak zorundadır. Aksi halde `TypeError: func() takes 0 positional arguments but 1 was given` gibi bir hata alırsınız. Instance methodlara doğrudan class üzerinden ulaşmak için `self` parametresine ilgili instance'yi argüman olarak tanımlamamız gerektiğini (`(Class.func(Class()))` gibi) öğrenmiştik. Herhangi bir instance ile uğraşmadan, doğrudan class üzerinden bir methoda ulaşmak istenildiğinde class methodlar kullanılır. Bu methodlar yerine göre kullanışlı olabilir. Örnek:
```py
class Class():
    liste = []

    def __init__(self, list_item):
        self.list_item = list_item
        self.listeye_ekle()

    def liste_uzunluğu(self):
        print(len(self.liste))

    def listeye_ekle(self):
        self.liste.append(self.list_item)

var1 = Class("var1")
var1.liste_uzunluğu() # Output: 1
```
Bu kodda `len(self.liste)` kodunun `0` döndürdüğü bir durum elde edemezsiniz çünkü `liste_uzunluğu()` fonksiyonu bir instance method olduğu için bu methodu ancak bir insance türetildikten sonra kullanabilirsiniz. Dolayısıyla `liste_uzunluğu()` methodunu kullanmak için bir insance türettiğinizde `len(self.liste)` kodunun döndürdüğü değer `1` olur. `listeye_ekle()` gibi tek bir instance'yi değil, class'ın genelini ilgilendiren methodları `@classmethod` decorator'ı ile class method olarak Python'a tanıtmamız bu sorunu çözer. Bunun dışında alternatif bir çözüm vardır. Örnek:
```py
def liste_uzunluğu():
    print(len(Class.liste))

class Class():
    liste = []

    def __init__(self, list_item):
        self.list_item = list_item
        self.listeye_ekle()

    def listeye_ekle(self):
        self.liste.append(self.list_item)

liste_uzunluğu() # Output: 0
var1 = Class("var1")
liste_uzunluğu() # Output: 1
```
Global scope'da tanımlanan `liste_uzunluğu()` fonksiyonu sayesinde main class olan `Class`'ın `liste` attribute'unun eleman sayısına ulaşabildik ama bu yöntem tercih edilmez çünkü bu yöntem main class'ın bütünlüğünü bozmaktadır. Main class'ın bütünlüğünün bozulması aşağıdakiler gibi sorunlara yol açar:
- `liste_uzunluğu()` fonksiyonu main class dışında tanımlandığı için `dir(Class)` kodunun döndürdüğü liste içerisinde `liste_uzunluğu()` fonksiyonunu göremezsiniz. Bu da `dir(Class)` kullandığımız kısımlarda bize dezavantaj sağlar.
-  `liste_uzunluğu()` fonksiyonu main class dışında tanımlandığı için başka bir dosyada (örneğin bir modül dosyasında) tanımlanmış main class'ı `form madul import Class` şeklinde import ettiğimizde, `liste_uzunluğu()` fonksiyonu main class dışında tanımlandığı için içeri import edilmez ve dolayısıyla bu fonksiyonu ayrıyetten `form madul import liste_uzunluğu` şeklinde import etmeden kullanamayız.

## `@classmethod` Decorator ve `cls`
Python'da önünde `@` işareti olan isimlere 'bezeyici' (decorator) adı verilir. Bir class method tanımlamak için `@classmethod` decorator'ı kullanılır. `@classmethod` decorator, kendinden hemen sonra gelen fonksiyonu class method olduğunu Python'a bildirir. Örnek:
```py
class Class():
    class_attribute = 0

    def __init__(self):
        self.instance_attribute = 0

    def instance_method(self):
        self.instance_attribute += 1
        return self.instance_attribute

    @classmethod
    def class_method(cls):
        cls.class_attribute += 1
        return cls.class_attribute

print(Class.class_attribute) # Output: 0
print(Class.class_method()) # Output: 1
print(Class().instance_method()) # Output: 1
```
Yukarıdaki kodun outputlarının sebebini teker teker açıklamak gerekirse:
- `print(Class.class_attribute)`
    - `Class.class_attribute` kodu, bize `class_attribute` class attribute'sinin değerini verir.
- `print(Class.class_method())`
    - `class_method()` fonksiyonu `@classmethod` decorator'ı kullanılarak Python'a class method olarak tanıtılmıştır.
    - `class_method()` fonksiyonundaki `cls` parametresi, instance methodlarda kullanılan `self` parametresi arasında işlevsel olarak hiçbir fark yoktur. `self` parametresi instance method'lardaki instace attribute'lerde prefix olarak kullanılırken, `cls` parametresi (eğer ilgili fonksiyon `@classmethod` decorator'ı ile Python'a class method olarak tanıtılmışsa) class method'lardaki class attribute'lerde prefix olarak kullanılır. `cls` aynı `self` gibi değiştirilebilir. Yani `self`'deki gibi `cls` yerine de istediğiniz kelimeyi yazabilirsiniz. Instance method'larda `self` parametresini tanımlamanızın zorunlu olması gibi, class method'larda da `cls` parametresini tanımlamanız zorunludur. Aksi halde hata alırsınız.
- `print(Class().instance_method())`
    - `instance_method()` instance method'u, `__init__` fonksiyonunda tanımlanmış `instance_method` instance attribute'unun üzerinde işlem yapar. Sürecin nasıl işlediğini [Instance Attributes](asd) ve [Instance Methods](asd) konu başlıklarını öğrendiyseniz biliyorsunuzdur.

`cls` prefix'i ile tanımlanan attribute'lar, `self` ile tanımlanan attribute'lar gibi class attribute'lara referanstır. Örnek:
```py
class Class():
    class_attribute = 0

    def __init__(self):
        self.class_attribute

    def instance_method(self):
        return self.class_attribute

    @classmethod
    def class_method(cls):
        return cls.class_attribute
var = Class()
print("Class.class_attribute:    ", Class.class_attribute, "id:", id(Class.class_attribute))
print("var.class_attribute:      ", var.class_attribute, "id:", id(var.class_attribute), end="\n\n")

var.class_attribute = 1
print("`var.class_attribute = 1` kodundan sonra")
print("Class.class_attribute:    ", Class.class_attribute, "id:", id(Class.class_attribute))
print("var.class_attribute:      ", var.class_attribute, "id:", id(var.class_attribute), end="\n\n")
print("var.instance_method():    ", var.instance_method(), "id:", id(var.instance_method()))
print("var.class_method():       ", var.class_method(), "id:", id(var.class_method()))
print("Class.class_method():     ", Class.class_method(), "id:", id(Class.class_method()), end="\n\n")

Class.class_attribute = 2
print("`Class.class_attribute = 2` kodundan sonra")
print("Class.class_attribute:    ", Class.class_attribute, "id:", id(Class.class_attribute))
print("Class.class_method():     ", Class.class_method(), "id:", id(Class.class_method()))
print("var.class_attribute:      ", var.class_attribute, "id:", id(var.class_attribute))
print("var.instance_method():    ", var.instance_method(), "id:", id(var.instance_method()))
print("var.class_method():       ", var.class_method(), "id:", id(var.class_method()))
```
**Output: (Aynı olan ID'ler aynı harfla işaretlenmiştir)**
```
Class.class_attribute:     0 id: 1966859512080 (a)
var.class_attribute:       0 id: 1966859512080 (a)

`var.class_attribute = 1` kodundan sonra
Class.class_attribute:     0 id: 1966859512080 (a)
var.class_attribute:       1 id: 1966859512112 (b)

var.instance_method():     1 id: 1966859512112 (b)
var.class_method():        0 id: 1966859512080 (a)
Class.class_method():      0 id: 1966859512080 (a)

`Class.class_attribute = 2` kodundan sonra
Class.class_attribute:     2 id: 1966859512144 (c)
Class.class_method():      2 id: 1966859512144 (c)
var.class_attribute:       1 id: 1966859512112 (b)
var.instance_method():     1 id: 1966859512112 (b)
var.class_method():        2 id: 1966859512144 (c)
```
Buradaki output'ları parça parça açıklamak gerekirse:
- Gördüğünüz gibi main class'da tanımlı olan `class_attribute` ile `__init__`'de tanımlı olan `self.class_attribute` ilk başta aynı attribute'ü temsil etse de, `var.class_attribute = 1` kodundan sonra main class'da tanımlı olan `class_attribute` ile `__init__`'de tanımlı olan `self.class_attribute` birbirlerinden farklı iki attribute'ü temsil eder hale geliyor. Çünkü main class'da tanımlı olan `class_attribute` `0` değerini içerirken, `__init__`'de tanımlı olan `self.class_attribute` `1` değerini içerir.
- `Class.class_attribute = 2` kodundan sonra instance attribute olan `self.class_attribute` attribute'unun değeri ve ID'si aynı kalırken, main class'daki class attribute'sinin değeri ve ID'si değişir. Bundan şu çıkarımı yapabiliriz;
    - Bir instance attribute, class attribute'a referans verse bile bu instance attribute'ü yeniden tanımladığımızda (redefinition) class attribute'dan bağımsız bir attribute'a dönüşür.
    - Class method içinde tanımlanmış ve class attribute'e referans veren bir attribute (`class_attribute`'e referans veren `cls.class_attribute` gibi), referans verdiği class attribute'un değeri değiştirilse değişir (`class_attribute`'un değeri değiştirilince `cls.class_attribute`'un da değerinin değişmesi gibi) ya da kendisi değiştirilirse referans verdiği class attribute'un değeri değişir (`cls.class_attribute`'un değeri değiştirilince `class_attribute`'un da değerinin değişmesi gibi).

**Not:** Yukarıdaki kodda görüldüğü gibi class methodlara illa main class'dan (`Class.class_method()` gibi) ulaşacaksınız diye bir kural yok. Class methodlara instance'lardan da ulaşabilirsiniz (`var.class_method()` gibi). Ama hata riskini en aza indirmek için class methodlara main class'dan ulaşmak daha akıllıca bir seçimdir.

## alternative constructor
[inşacı](https://python-istihza.yazbel.com/nesne_tabanli_programlama2.html) kavramını öğrendikten sonra tekrar bak.

## Statik Metotlar
Bir class içinde tanımladığınız fonksiyon, o class'ın class attribute'larına ya da instance attribute'larına erişmesi gerekmiyorsa bu fonksiyonu static method olarak tanımlayabilirsiniz. Class method tanımlarken `@classmethod` decorator'ını kullandığımız gibi static method tanımlarken de `@staticmethod` decorator'ını kullanırız. Örnek:
```py
class Class():
    
    @staticmethod
    def static_method():
        print("Static method tanımlandı.")

Class.static_method() # Output: Static method tanımlandı.
Class().static_method() # Output: Static method tanımlandı.
```
Static method'ların, class methodlarda class attribute'ların prefix'i için kullanılan `cls` ya da instance methodlarda instance attribute'ların prefix'i için kullanılan `self` parametrelerine ihtiyacı yoktur. Python, static method'a girilen parametrelerin hepsine normal bir parametre muamelesi yapar. Örnek:
```py
class Class():
    
    @staticmethod
    def static_method(p1):
        name = p1
        print(f"Selam {name}! Static method tanımlandı.")

Class.static_method("Ahmet") # Output: Selam Ahmet! Static method tanımlandı.
Class().static_method("Ali") # Output: Selam Ali! Static method tanımlandı.
```
**Not:** Python bir class içine tanımlanan methodları, aksi belirtilmediği sürece instance method olarak değerlendirilir ve bu methodların ilk parametresi, instance attribute'lerin prefix'i olan `self` kelimesi olmak zorundadır. Bir methodu, `@classmethod` decorator'ını kullanarak Python'a class method olarak tanıtabiliyoruz ve bu methodların ilk parametresi, class attribute'lerin prefix'i olan `cls` kelimesi olmak zorundadır. Eğer static method olmasaydı, instance method'ların ve class method'ların ilk parametre kısıtlaması yüzünden python içine instance attribute'larla ya da class attribute'larla uğraşmadan, sadece belli görevleri yapan ve kendi içinde özelleşmiş (Bunun anlamı; static methodun içine hiçbir class ya da instance attribute tanımlanamaması) bir fonksiyonu main class içinde tanımlayamazdık, imkansız olurdu. Bunun gibi bir fonksiyonu ancak class'ın dışına tanımlayabilirdik ama bunun dezavantajlı olduğunu biliyoruz. Bu dezavantajları daha önce anlattım (`dir(Class)` ve `from modul import Class` dezavantajları).

Static methodlar, class methodlar gibi main class'ın her yerinden erişilebilir. Yani bir instance'ye method olarak ya da doğrudan main class'a bir method olarak tanımlanabilir. Örnek:
```py
class Mat():

    @staticmethod
    def pi():
        return 22/7

    @staticmethod
    def karekök(sayı):
        return sayı ** 0.5

print(Mat.karekök(4)) # Output: 2
print(Mat().karekök(4)) # Output: 2
```
Gördüğünüz gibi static method'lar böyle işlerde kullanılmak için ideal seçeneklerdir. Başka bir örnek:
```py
class Class():
    class_attribute = "Class Attribute Data"

    def __init__(self, data):
        self.data = data

    def instance_method(self):
        return f"instance_method data: {self.data}"

    @classmethod
    def class_method(cls):
        return f"class_method data: {cls.class_attribute}"

    @staticmethod
    def static_method(p1):
        return f"static_method data: {p1}"

print(f"Class Attribute: {Class.class_attribute}") # Output: Class Attribute: Class Attribute Data
print(f"Intance Attribute: {Class('Instance Attribute Data').data}") # Output: Intance Attribute: Instance Attribute Data
print(f"{Class('Instance Attribute Data').instance_method()}") # Output: instance_method data: Instance Attribute Data
print(f"{Class.class_method()}") # Output: class_method data: Class Attribute Data
print(f"{Class.static_method('Static Attribute Data')}") # Output: static_method data: Static Attribute Data
print(f"{Class('Instance Attribute Data').static_method('Static Attribute Data')}") # Output: static_method data: Static Attribute Data
```