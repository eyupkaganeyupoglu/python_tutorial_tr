# Numpy Data Types

Numpy birçok data type'ı destekler. Bu data type'lara ulaşmak için [tıklayınız](https://numpy.org/doc/stable/user/basics.types.html "https://numpy.org/doc/stable/user/basics.types.html"). Bunlardan 5 tanesi temel data type'lardır:
- Boolean (bool)
- Integer (int)
- Unsigned integer (uint)
- Floating point (float)
- Complex.

Bir array oluştururken array'e tanımladığınız data'ların type'ına göre Numpy, o array'in data type'ını otomatik olarak belirler ve bütün data'ları o type'a göre yeniden düzenler. Örnek:
```py
import numpy as np

A = np.array([1, 2, 3, 4])
print(A) # Output: [1 2 3 4] 
print(A.dtype) # Output: int32

A = np.array([1.0, 2.0, 3.0, 4.0])
print(A) # Output: [1. 2. 3. 4.]
print(A.dtype) # Output: float64
```
Gördüğünüz gibi array'in elementlerinin type'ı Numpy tarafından otomatik olarak belirlendi.

**Not:** Bir array'in elementlerinin sağ tarafında bir adet nokta işerati varsa, o element `float` type'dır demektir (`[1., 2., 3.]`).

Bir array tanımlarken element olarak farklı type'larda data'lar tanımlarsanız, Numpy bu elementler arasında en fazla veri alanına (data area, data field) sahip type'ı asıl type olarak seçer ve bütün elementleri o type'a dönüştürür. Buna **Upcasting** denir. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4])
print(A.dtype) # Output: int32
print(A) # Output: [1 2 3 4]  

B = np.array([1,"2",3,4])
print(B.dtype) # Output: <U11
print(B) # Output: ['1' '2' '3' '4']

C = np.array([1,2.0,3,4])
print(C.dtype) # Output: float64
print(C) # Output: [1. 2. 3. 4.]   

D = np.array([1,"2",3.0,4])
print(D.dtype) # Output: <U32
print(D) # Output: ['1' '2' '3.0' '4']
```
Bu dönüştürme işlemini manipüle edebilirsiniz. Bunun için neredeyse her Numpy fonksiyonunda olan `dtype` parametresini veya `astype` methodunu kullanabilirsiniz. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4], dtype=np.float64)
print(A) # Output: [1. 2. 3. 4.]
print(A.dtype) # Output: float64

A = A.astype(np.int32)
print(A) # Output: [1 2 3 4]
print(A.dtype) # Output: int32
```
`astype` methodunun ilk parametresi de `dtype`'dır.

**Not:** Hangi data type'ın daha fazla veri alanına sahip olduğunu öğrenmek için `nbytes` property'sini kullanabilirsiniz. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4], dtype=np.float64)
print(A) # Output: [1. 2. 3. 4.]
print(A.nbytes) # Output: 32
print(A.dtype) # Output: float64
```

Daha fazla veri alanına sahip type elementlerin bulunduğu bir array'in elementlerini daha az veri alanına sahip bir type'a dönüştürmeye **Downcasting** denir. Örnek:
```py
import numpy as np

A = np.array([1.0, 2.0, 3.0, 4.0])
print(A) # Output: [1. 2. 3. 4.]
print(A.nbytes) # Output: 32
print(A.dtype) # Output: float64

A = A.astype(np.int32)
print(A) # Output: [1 2 3 4]
print(A.nbytes) # Output: 16
print(A.dtype) # Output: int32
```

**Not:** Bir array oluşturduktan (create) sonra o array objesinin type'ını değiştiremeyiz. Sadece o array'in kopyasını oluştururken (create), kopyasını farklı bir type'da oluşturabiliriz. Örnek: 
```py
import numpy as np

A = np.array([1.0, 2.0, 3.0, 4.0])
print(A) # Output: [1. 2. 3. 4.]
print(A.nbytes) # Output: 32
print(A.dtype) # Output: float64

B = A.astype(np.int32)
print(B) # Output: [1 2 3 4]
print(A) # Output: [1. 2. 3. 4.]
print(B.nbytes) # Output: 16
print(B.dtype) # Output: int32
```
Gördüğünüz gibi `A` array'inin kopyasının type'ını değiştirip `B` variable'ına atadık ama `A` array'i aynı kaldı.

**Not:** Upcasting işlemi, array'ler arasında yaptığımız aritmetik işlemlerde (daha sonra anlatılacak) de karşımıza çıkar. Örnek:
```py
import numpy as np

A = np.array([1, 2, 3, 4], dtype=np.int32)
B = np.array([1.1, 2.2, 3.3, 4.4], dtype=np.float64)
print(A+B) # Output: [2.1 4.2 6.3 8.4]
print((A+B).dtype) # Output: float64
```
Gördüğünüz gibi işlem sonucu `float64` type olarak oldu.