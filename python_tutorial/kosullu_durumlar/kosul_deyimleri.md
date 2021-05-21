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

### Örnek `if` - `elif` - `else` programı
```py

note = float(input("Notunuzu giriniz: "))
if (note >= 90):
	print("AA")
elif (note >= 85):
	print("BA")
elif (note >= 90):
	print("BA")
elif (note >= 80):
	print("BB")
elif (note >= 75):
	print("CB")
elif (note >= 70):
	print("CC")
elif (note >= 65):
	print("DC")
elif (note >= 60):
	print("DD")
else:
	print("Dersten Kaldınız")
```
