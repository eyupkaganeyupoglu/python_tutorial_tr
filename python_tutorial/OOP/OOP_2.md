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
Bu kodda `len(self.liste)` kodunun `0` döndürdüğü bir durum elde edemezsiniz çünkü `liste_uzunluğu()` fonksiyonu bir instance method olduğu için bu methodu ancak bir insance türetildikten sonra kullanabilirsiniz. Dolayısıyla `liste_uzunluğu()` methodunu kullanmak için bir insance türettiğinizde `len(self.liste)` kodunun döndürdüğü değer `1` olur. `listeye_ekle()` gibi tek bir instance'yi değil, class'ın genelini ilgilendiren methodları class method olarak Python'a tanıtmamız bu sorunu çözer.

## `@classmethod` Decorator ve `cls`
Bir class method tanımlamak için `@classmethod` decorator'ı kullanılır. `@classmethod` decorator, kendinden hemen sonra gelen fonksiyonu class method olduğunu Python'a bildirir. Örnek:
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
print(Class().class_method()) # Output: 1
```
Yukarıdaki kodun outputlarının sebebini teker teker açıklamak gerekirse:
- 
- 
- 





Bu methodu class method olarak tanımlamamız dışında alternatif bir çözüm vardır. Örnek:
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