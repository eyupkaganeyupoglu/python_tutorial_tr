# Abstract Class (Sınıf):

####### 1.1
Abstract sınnıflar aynı özellikleri taşıyan nesneleri aynı çatı altında toplayıp, Nesnelere bir şablon çizerek çizilen  şablondan çıkmadan istediğimiz gibi şekil vermemizi sağlar.

####### 1.2
Hayvan dediğimizde hepimizin aklına genel, elle tutulamaz soyut bir kavram gelir dimi? Evet hayvan genel bir kavramdır. Kuş dediğimizde ise aklımıza hayvanların kuş sınıfına ait canlılar gelir ve bu yöntemle hayvan kavramı kuş olarak somutlaştırılır. Yani Hayvan kavramı soyutken kuş kavramı somuttur. Abstraction kavramıyla ilgili verebileceğim en iyi örneğin bu olacağını düşündüm.

## Abstract Class Özellikleri:

####### 2
Abstract class‘ların içi ya boş bırakılır yada methodlarla donatılır. Abstract class olmak için en az 1 tane abstract method bulundurmak şarttır.  Abstract Class içerisinde kullanılan methodları kalıtım verdiği bütün sınıflarda kullanmak zorundadır. Asla Abstract sınıftan örnek yaratamayız (new kelimesiylede oluşturamayız)

------------------------------------

# Abstract Class

####### 1.1
Abstract class'lar, diğer class'lar için bir template (şablon) olara düşünülebilir.

####### 1.2 ?
It allows you to create a set of methods that must be created within any child classes built from the abstract class. (Soyut sınıftan oluşturulmuş herhangi bir alt sınıf içinde oluşturulması gereken bir dizi yöntem oluşturmanıza olanak tanır.)

####### 1.3
Bir veya daha fazla abstract method içeren class'a abstract class denir.

####### 1.4
An abstract method is a method that has a declaration but does not have an implementation. (Soyut bir yöntem, bildirimi olan ancak uygulaması olmayan bir yöntemdir.)

## declaration 
####### 1.4.1

## implementation
####### 1.4.2
Yazılımlarda **specification** ve **implementation** olmak üzere 2 kavram vardır. Specification, yazılımın doğal bir dille yapısal bir şekilde yazılmasıdır. Buna yazılımın tasarımı da diyebiliriz. Örneğin Python dökümanları bir specification'dır. Implementation ise, yazılımın, o yazılım için üretilmiş specification'dan yararlanarak bir programlama dili ile yazılmasıdır. Örneğin C dili ile yazılmış CPython bir implementation'dır.

####### 1.5
Büyük functional unit'ler hazırlarken abstract class'lar kullanılır.

####### 1.6
When we want to provide a common interface for different implementations of a component, we use an abstract class. (Bir bileşenin farklı uygulamaları için ortak bir arayüz sağlamak istediğimizde, soyut bir sınıf kullanırız.)

####### 1.7
By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. (Soyut bir temel sınıf tanımlayarak, bir dizi alt sınıf için ortak bir Uygulama Programı Arayüzü (API) tanımlayabilirsiniz.)

####### 1.8
Bütün class'ların methodlarını aklınızda tutmanızı zorlaştıran büyük programlarda çalışırken size kolaylık sağlar. (bütün class'lar bu template'i miras alırlarsa kullanmak zorunda kalacakları için)

####### 1.9
Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC. (Python, Soyut Temel sınıfları (ABC) tanımlamak için temel sağlayan bir modülle birlikte gelir ve bu modül adı ABC'dir.)

####### 1.10
ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations of the abstract base. (ABC, temel sınıfın yöntemlerini soyut olarak süsleyerek ve ardından somut sınıfları soyut tabanın uygulamaları olarak kaydederek çalışır.)

####### 1.11
Bir class'ı abstract hale getirmek için `@abstractmethod` decorator'unu kullanırız. Örnek:
```py

```

https://www.geeksforgeeks.org/abstract-classes-in-python/

https://startupvadisi.com/python-oop-soyutlama-abstraction/

https://www.obenseven.com.tr/yazilim/python/nesne-tabanli-programlama/python-kompozisyon-composition/

https://www.sinanerdinc.com/python-abc-modulu-kullanimi