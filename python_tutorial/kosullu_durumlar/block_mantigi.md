# Python Programlarının çalışma mantığı
Python programları çalışmaya başladığı zaman kodlarımız yukardan başlayarak teker teker çalıştırılır ve çalıştıracak kod kalmayınca programımız sona erer.

Çoğu zaman Python programlarımız belirli bloklardan oluşur ve bu bloklar her zaman çalışmak zorunda olmaz. Peki bu bloklar nasıl tanımlanır? Python'da bir blok tanımlama işlemi girintiler (Indentation. TAB tuşu ile oluşan 2 ya da 4 space boyutunda boşluk) sayesinde olmaktadır.
```py
a = int(input()) # Blok 1'e ait kod
if (a == 2):
	print("Doğru") # Blok 2'ye ait kod
	
print("'Doğru' yazdıysa doğru değeri girmişsinizdir.") # Blok 1'e ait kod
```
