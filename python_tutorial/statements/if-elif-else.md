# `if` Deyimi
*'eğer'* anlamına gelmektir. Kendisine tanımlanan koşul doğruysa (`True`) çalışır, yanlışsa (`False`) çalışmaz. Syntax'ı:
```py
if (koşul):
	# Kodlar
``` 
**Bazı örnekler:**
```py
yas = int(input("Yaşınızı giriniz: "))
  
if (yas >= 18):
print("Girebilirsiniz.")
if (0 <= yas < 18):
print("Yaşınız 18'den küçük olduğu için giriş yapamazsınız.")
if (yas < 0):
print("Yaşınız negatif bir değer olamaz.")
```

# `elif` Deyimi
`if` deyimi çalışmazsa çalışan deyimdir. Dolayısıyla `elif` deyimini kullanmak için `elif` deyiminin üstünde bir `if` deyimine ihtiyacın var. Syntax'ı:
```py
if (koşul):
	# Kodlar
elif (koşul):
	# Kodlar
```
`if` ile `elif` deyimi arasındaki mantıksal fark şudur:
```py
if (5 < 4): # False, çalışmaz
	print("Birinci if block'u çalıştı.")
if (5 < 3): # False, çalışmaz
	print("İkinci if block'u çalıştı.")
if (5 < 6): # True, çalışır.
	print("Üçüncü if block'u çalıştı.")
if (5 < 7): # True, çalışır.
	print("Dördüncü if block'u çalıştı.")
```
**Output:**
```
Üçüncü if block'u çalıştı.
Dördüncü if block'u çalıştı.
```
Yukarıdaki kodda, bütün `if` deyimleri değerlendirilir ve `True` olanlar çalışır.
```py
if (5 < 4): # False, çalışmaz
	print("if block'u çalıştı.")
elif (5 < 3): # False, çalışmaz
	print("Birinci elif block'u çalıştı.")
elif (5 < 6): # True, çalışır.
	print("İkinci elif block'u çalıştı.")
elif (5 < 7): # True, çalışmaz.
	print("Üçüncü elif block'u çalıştı.")
```
**Output:**
```
İkinci elif block'u çalıştı.
```
Yukarıdaki kodda, en sondaki `elif` deyimi `True` olsa bile çalışmaz çünkü `elif` deyiminin özelliği, bir `elif` deyimi çalıştıktan sonra kendinden sonraki `elif` deyimleri `True` olsa bile, kendinden sonraki `elif` deyimleri çalışmaz. `elif` deyimini `if` deyiminden en önemli özelliktir.

# `else` Deyimi
`if` deyiminden ya da `if` - `elif` yapısından oluşan bir yapıda, hiçbir `if` ve `elif` deyiminin çalışmaması durumunda çalışan deyimdir.  Kısaca `else` deyimi, çalışmak için kendinden önce çalışmayan bir duruma ihtiyaç duyar. Çalışma koşulu sadece buna bağlı olduğu için `if (koşul)` ya da `elif (koşul)` deyimlerindeki gibi bir `(koşul)`'a ihtiyaç duymaz. Syntax'ı:
```py
if (koşul):
	# Kodlar
elif (koşul):
	# Kodlar
else:
	# Kodlar
```
**Not:** Herhangi bir `if` deyimi ya da `if` - `elif` yapısı, `else` deyimi olmadan da çalışabilir çünkü `else` deyiminin tek amacı, `if` deyiminden ya da `if` - `elif` yapısından oluşan bir yapıda, hiçbir `if` deyiminin ya da `if` - `elif` yapısının çalışmaması durumunda çalışmasıdır. Kısaca ihtiyaca göre kullanımı tercih edilebilir.

**Not:** `else` deyimi, kendinden önceki `if` deyimini referans alır. Yani:
```py
if (5 < 4):
	print("Birinci if block'u çalıştı.")
else:
	print("Birinci else block'u çalıştı.")
if (5 < 6):
	print("İkinci if block'u çalıştı.")
else:
	print("İkinci else block'u çalıştı.")
if (5 < 2):
	print("Üçüncü if block'u çalıştı.")
else:
	print("Üçüncü else block'u çalıştı.")
```
**Output: **
```
Birinci else block'u çalıştı.
İkinci if block'u çalıştı.
Üçüncü else block'u çalıştı.
```
Görüldüğü gibi, bir `else` deyimi, kendinden önceki ilk `if` deyimini referans alır ve referans aldığı `if` deyimi çalışmazsa çalışır.

# Tek satırda `if` - `else` kullanmak
Belli bir koşulu tek satırsa basit ve pratik bir şekilde kontrol etmek için `if` - `else` yapısını kullanabilirsiniz. Bu yapı özellikle `lambda` fonksiyonlarında çok kullanışlıdır. `(işlemler) if (koşul) else (işlemler)` syntaxına sahiptir. Parantezler olmadan da kullanılabilir ama kodun anlaşılırlığı açısından parantezlerle beraber kullanılmalıdır. Örnek:
```py
(print(1)) if True else (print(2)) # Output: 1
print(1) if True else print(2) # Output: 1
```
Çalışma mantığını anlamak için basit bir örnek:
```py
(print(1)) if True else (print(2)) 
(print(1)) if False else (print(2)) # Output: 2
```
Aşağıdaki örneklerde, `if` ve `else` statementleri soldan sağa olarak birinici, ikinci ve üçüncü olarak numalandırıldığını düşünün:
```py
((print(1)) if True else (print(2))) if True else ((print(3)) if True else print(4)) # Output: 1
```
Yukarıda,
- İkinci `if` çalışır,
- Birinci `if` çalışır,
- `print(1)` çalışır.
```py
((print(1)) if False else (print(2))) if True else ((print(3)) if True else print(4))# Output: 2
```
Yukarıda,
- İkinci `if` çalışır,
- Birinci `if` çalışmadığı için birinci `else` çalışır,
- `print(2)` çalışır.
```py
((print(1)) if True else (print(2))) if False else ((print(3)) if True else print(4))# Output: 3
```
Yukarıda,
- İkinci `if` çalışmadığı için ikinci `else` çalışır,
- Birinci `if` çalışır,
- `print(3)` çalışır.
```py
((print(1)) if True else (print(2))) if False else ((print(3)) if False else print(4))# Output: 4
```
Yukarıda,
- İkinci `if` çalışmadığı için ikinci `else` çalışır,
- Birinci `if` çalışmadığı için üçüncü `else` çalışır,
- `print(4)` çalışır.