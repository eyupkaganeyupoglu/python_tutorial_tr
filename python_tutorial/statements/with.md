with deyiminin dosya işlemleri dışında da kullanıldığı yerler var:

- Context managerlar
- Descriptorlar ve property methodları
- __slots__
- __new__() özel metodu
- Singleton sınıflar (ve metaclasslar)
- Enumerationlar (enum modülü)
- Dekoratör fonksiyonlar

https://realpython.com/python-with-statement/

https://medium.com/bilişim-hareketi/python-context-manager-159facf118bb

# `with` Statement
Python'da, kaynak kullanımı ve kaynakların geri iadesi için with deyimi bulunmaktadır. With deyimi bu işlemleri **context management** protocol’üne uygun olarak yapmaktadır.

## Context Manager
Context manager kullanılan kaynakların geri iade edilmesi için ortaya çıkmış bir protokoldür. Bu protokolü kullanabilmemiz için belli kurallara uygun sınıflar, yapılar oluşturmamız gerekir. Context manager protokolüne uygun yazdığımız sınıflarımızı kullanırken de with deyiminden yararlanacağız.

`with` statement, bilgisayarınızdaki harici kaynakları (external resources) yönetmek için kullanışlı bir araçtır. It allows you to take advantage of existing context managers to automatically handle the setup and teardown phases whenever you’re dealing with external resources or with operations that require those phases.