# Composition (Dahil Etme)
Bir class'ın görevini/sorumluluklarını başka bir class'a devretmeye (delegated) **Composition** denir. Örnek:
```py
class Gelir:
    def __init__(self, maaş, bonus):
        self.maaş = maaş
        self.bonus = bonus

    def yıllık_gelir(self):
        return (self.maaş*12) + self.bonus

class Çalışan:
    def __init__(self, isim, yaş, maaş, bonus):
        self.isim=isim
        self.yaş=yaş
        self.obj_Gelir = Gelir(maaş, bonus)

    def toplam_gelir(self):
        return self.obj_Gelir.yıllık_gelir()

var = Çalışan('Ali', 25, 2825, 250)
print(var.isim, var.yaş, var.obj_Gelir.maaş, var.obj_Gelir.bonus, sep=", ") # Output: Ali, 25, 2825, 250
print(var.toplam_gelir()) # Output: 34150
```
İçinde diğer class'lardan türetilmiş instance'ları barındıran class'lara (yani buradaki `Çalışan` class'ına) **Composite Class**, barındırdığı instance'lara (yani buradaki `obj_Gelir` variable'ına atanmış `Gelir` class'ından türetilmiş instance) **Component** denir.

Composition kavramının Python'da Inheritance kavramı ile yakından ilişkisi vardır. Her ikisi de iki class arasındaki ilişkiyi tanımlayarak, kodun yeniden kullanılabilmesini sağlarlar fakat bunu farklı şekillerde yaparlar.

Composition, herhangi bir class'daki objeleri miras almak yerine, herhangi bir class'dan türetilen instance'ı (component) composite class içinde başka bir objeye atayarak kullanmamıza olanak tanır. Bu sayede farklı tür objeleri birleştirerek kompleks class'lar oluşturabiliriz.

İki class arasındaki Composition ilişkisinin gevşek bir şekilde bağlı olduğu kabul edilir. Bu, component'ların nadiren composite class'ları etkilediği, composite class'ın ise component'ları hiçbir zaman etkilemediği anlamına gelir. Bu durum, mevcut kodu etkilemeden yeni gereksinimlere uygun bir şekilde programın değiştirilmesine daha iyi uyum sağlar. Aynı zamanda composite class'ı sildiğimizde, composite class'ın component'larını da silmiş olacağımız için herhangi bir sorun yaşamayız.

Daha fazla bilgi için [tıklayınız](https://realpython.com/inheritance-composition-python/).