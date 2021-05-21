# `input()` Nedir?
Kullanıcıdan girdi (input) almanı sağlayan bir build-in (gömülü) fonksiyondur. `input()` gibi sade bir şekilde kullanılabileceği gibi `input("Lütfen bir sayı giriniz: ")` şeklinde de kullanılabilir. Kullanıcıdan alınan değerleri bir variable'a atayabilirsiniz. Örneğin:
```py
inp = input("Bir input giriniz: ") # 15 girersek,
print("Girdiğiniz input: ", inp)
```
**Output:**
```
Bir input giriniz: 15
Girdiğiniz input: 15
```
**Not:** `input()` fonksiyonu, kendisine girilen değerleri `str` veri tipinde programa verir. Yani bir `int` değere ihtiyacınız varsa, kullanıcıdan aldığınız değeri kullanmadan önce  `int` data type'a dönüştürmelisiniz.
```py
s1 = int(input("İlk sayı: ")) # 2 girersek,
s2 = int(input("İkinci sayı: ")) # 3 girersek
print("Girdiğiniz sayıların toplamı: ", s1 + s2)
# Output: Girdiğiniz sayıların toplamı: 5
```


