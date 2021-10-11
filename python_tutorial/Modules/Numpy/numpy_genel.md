# Numpy

Numpy, normal Python ile yapacağınız işlemlerden çok daha hızlı çalışır çünkü çekirdeğinde **C** dili ile yazılmış bir kütüphanedir. Numpy [**vectorization**](https://stackoverflow.com/a/1422181/15170972 "https://stackoverflow.com/a/1422181/15170972")'ı desteklediği için bu kadar hızlı çalışır. Normal Python vectorization'ı desteklemediği için hızlı değildir. Örnek:
```py
import numpy as np
import time

start_time_1 = time.time()
A = np.arange(1000000)
A**2
time_1 = time.time() - start_time_1

start_time_2 = time.time()
B = range(1000000)
[i**2 for i in B]
time_2 = time.time() - start_time_2

print(f"time_1: {time_1}",
      f"time_2: {time_2}",
      f"Bu işlemde arange, range'den {time_2/time_1} kat daha hızlı çalıştı.", sep="\n")
```
**Output:**
```
time_1: 0.0020034313201904297
time_2: 0.2800407409667969
Bu işlemde arange, range'den 139.78055456384624 kat daha hızlı çalıştı.
```

Numpy [**vectorization**](https://stackoverflow.com/a/1422181/15170972 "https://stackoverflow.com/a/1422181/15170972")'ı desteklediği için bu kadar hızlı çalışır. Normal Python vectorization'ı desteklemediği için hızlı değildir.

Numpy kendi başına pek bir işe yaramaz. Veri manipülasyonu, veri bilimi, yapay zeka gibi alanlarda kullanılır. Gelen büyük verileri işlemek için Numpy kullanılır.

# NDArray (N-Dimensional Array)

Numpy kütüphanesinin temel veri yapısı (basic data structure) array'lerdir. NDArray, 'N-Dimensional Array' yani 'Çok Boyutlu Dizin' anlamına gelmektedir. NDArray'ler normal Python dizinlerinden (`list` vs.) daha hızlı çalışır. NDArray'ler aynı type data'ları tutabilirler. Bir NDArray oluştururken farklı type data'lar tanımlamaya kalkarsanız Numpy upcasting (daha sonra anlatılacak) yaparak bütün data'ları aynı type'a dönüştürür. NDArrayler tek veya çok boyutlu olabilir. Burada **Eksen** ve **Boyut** kavramları devreye giriyor.
- **Eksen:** NDArray'ler çok eksenli olabilir. Sahip olduğu eksene göre boyutu değişkenlik gösterir. Örneğin 1 eksenli ise 1D (bir boyutlu), 5 eksenli ise 5D (5 boyutlu) denir.
- **Boyut:** Matrixler çok boyutlu olabilir. Sadece satırlardan (X) oluşanlarına 1D (bir boyutlu), satır ve sütunlardan (X ve Y, row ve column) oluşanlarına 2D (iki boyutlu) veya matrix, birden fazla matrix'den (X, Y, Z) oluşanlarına da 3D (üç boyutlu) denir ve böyle devam eder.

`NDArray`'ler 2 şekilde oluşturulur:
- Klasik Python `list`'lerden yararlanılır.
- Build-in Numpy fonksiyonlarından (`zeros`, `ones`, `arange` vs.) yararlanılır.

Bir NDArray oluşturmak için `array` fonksiyonundan yararlanırız. Örnek:
```py
import numpy as np

A = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]], [[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(A.shape) # Output: (2, 3, 4)
print(A.ndim) # Output: 3
print(A) # Output: [[[1 2 3 4]
#                    [1 2 3 4]
#                    [1 2 3 4]]

#                   [[1 2 3 4]
#                    [1 2 3 4]
#                    [1 2 3 4]]]
```
Yukarıda `list` objelerinden yararlanarak 3D bir array oluşturulmuştur. `shape` methodu bu array'in eksenlerinin içerdiği eleman sayısını, `ndim` array'in boyutunu döndüren property'lerdir. Bu eksenler soldan sağa doğru genelden özele doğru sıralanır. Yani `(2,3,4)` 3 boyutlu array'de `Z:2`, `Y:3`, `X:4`'dür. Başka bir deyişle `4` satırlı `3` stunlu `2` matrix.

**Not:** Bir array'in her bir öğesine **element** denir. Bundan sonra 'element' kelimesini gördüğünüzde array'in öğeleri aklınıza gelsin.

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

# NDArray'leri Dilimlemek (Slicing)

Bir array'in belli bir elemanına ulaşabilirsiniz. Örnek:
```py
import numpy as np

A = np.arange(1,6)
print(A) # Output: [1 2 3 4 5]
print(A[2]) # Output: 3

A = np.arange(1,26).reshape((5,5))
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(A[2,1]) # Output: 12
```
Yukarıda `A[2,1]` 2. index'deki sütun, 1. index'deki satır anlamına gelmektedir.

- 1D array'i dilimlerken `array_exp[start:stop:step]`
- 2D array'i dilimlerken `array_exp[start:stop:step, start:stop:step]`
- 3D array'i dilimlerken` array_exp[start:stop:step, start:stop:step, start:stop:step]`

ve diğer boyutlarda da benzer syntax'lar kullanılır. Buna **slicing** (dilimleme) denir. Örnekler:
- 1D:
  ```py
  import numpy as np

  A = np.array([0,1,2,3,4,5,6,7,8,9])
  print(A) # Output: [0 1 2 3 4 5 6 7 8 9]

  # 4. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar array'i yazdırır.
  print(A[4:9]) # Output: [4 5 6 7 8]

  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (9. index'i dahil etmeden) 9. index'e kadar array'i yazdırır.
  print(A[:9]) # Output: [0 1 2 3 4 5 6 7 8]

  # Bitiş index'i belirtilmediği için 4. indexten başlar, en son index'e kadar array'i yazdırır.
  print(A[4:]) # Output: [4 5 6 7 8 9]

  # Başlangıç ve bitiş intex'i belirtilmediği için tüm array'i yazdırır.
  print(A[:]) # Output: [0 1 2 3 4 5 6 7 8 9]

  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (-1. index'i dahil etmeden) -1. index'e kadar (sonran bir önceki index) array'i yazdırır.
  print(A[:-1])# Output: [0 1 2 3 4 5 6 7 8]

  # Baştan sona index atlamadan array'i yazdırır.
  print(A[::1]) # [0 1 2 3 4 5 6 7 8 9]

  # Baştan sona 1 index atlaya atlaya array'i yazdırır.
  print(A[::2]) # Output: [0 2 4 6 8]

  # 4. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar 2 index atlaya atlaya array'i yazdırır.
  print(A[0:9:3]) # Output: [0 3 6]

  # Sondan başa index atlamadan array'i yazdırır. (array'i ters çevirme)
  print(A[::-1]) # Output: [9 8 7 6 5 4 3 2 1 0]
  ```
- 2D:
  ```py
  import numpy as np

  A = np.arange(25).reshape(5,5)
  print(A) # Output: [[ 0  1  2  3  4]
  #                   [ 5  6  7  8  9]
  #                   [10 11 12 13 14]
  #                   [15 16 17 18 19]
  #                   [20 21 22 23 24]]

  # 2 boyutlu array'lerde belli bir elemana atıfta bulunmak (daha önce gösterdim).
  print(A[3, 3]) # Output: 18

  # 0. index'ten başlar, (3. index'i dahil etmeden) 3. index'e kadar array'in stunlarını,
  # 0. index'ten başlar, (3. index'i dahil etmeden) 3. index'e kadar array'in satırlarını yazdırır.
  print(A[0:3, 0:3]) # Output: [[ 0  1  2]
  #                             [ 5  6  7]
  #                             [10 11 12]]

  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (4. index'i dahil etmeden) 4. index'e kadar array'in stunlarını,
  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (5. index'i dahil etmeden) 5. index'e kadar array'in satırlarını yazdırır.
  print(A[:4, :5]) # Output: [[ 0  1  2  3  4]
  #                           [ 5  6  7  8  9]
  #                           [10 11 12 13 14]
  #                           [15 16 17 18 19]]

  # Bitiş index'i belirtilmediği için 3. indexten başlar, en son index'e kadar array'in stunlarını,
  # Bitiş index'i belirtilmediği için 3. indexten başlar, en son index'e kadar array'in satırlarını yazdırır.
  print(A[3:, 3:]) # Output: [[18 19]
  #                           [23 24]]

  # Başlangıç ve bitiş intex'i belirtilmediği için array'in bütün satır ve stunlarını yazdırır.
  print(A[:, :]) # Output: [[ 0  1  2  3  4]
  #                         [ 5  6  7  8  9]
  #                         [10 11 12 13 14]
  #                         [15 16 17 18 19]
  #                         [20 21 22 23 24]]

  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (-1. index'i dahil etmeden) -1. index'e kadar (sonran bir önceki index) array'in stunlarını
  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (-1. index'i dahil etmeden) -1. index'e kadar (sonran bir önceki index) array'in satırlarını yazdırır.
  print(A[:-1, :-1]) # Output: [[ 0  1  2  3]
  #                             [ 5  6  7  8]
  #                             [10 11 12 13]
  #                             [15 16 17 18]]

  # Baştan sona index atlamadan array'in sütun ve satırlarını yazdırır.
  print(A[::1, ::1]) # Output: [[ 0  1  2  3  4]
  #                             [ 5  6  7  8  9]
  #                             [10 11 12 13 14]
  #                             [15 16 17 18 19]
  #                             [20 21 22 23 24]]

  # Baştan sona 1 index atlaya atlaya array'in sütun ve satırlarını yazdırır.
  print(A[::2, ::2]) # Output: [[ 0  2  4]
  #                             [10 12 14]
  #                             [20 22 24]]

  # 0. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar 2 index atlaya atlaya array'in stunlarını,
  # 0. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar 2 index atlaya atlaya array'in satırlarını yazdırır.
  print(A[0:9:3, 0:9:3]) # Output: [[ 0  3]
  #                                 [15 18]]

  # Sondan başa index atlamadan array'in sütun ve satırlarını yazdırır. (array'i ters çevirme)
  print(A[::-1, ::-1]) # Output: [[24 23 22 21 20]
  #                               [19 18 17 16 15]
  #                               [14 13 12 11 10]
  #                               [ 9  8  7  6  5]
  #                               [ 4  3  2  1  0]]
  ```

**Not:** Slicing yaparak oluşturduğunuz array'leri herhangi bir variable'a atarsanız, o variable'a atadığınız array parçası, asıl array'e atıfta bulunur (refers to). Yani birinde yaptığınız değişiklikler diğerini etkiler. Örnek:
```py
import numpy as np

A = np.arange(25).reshape(5,5)
print(A) # Output: [[ 0  1  2  3  4]
#                   [ 5  6  7  8  9]
#                   [10 11 12 13 14]
#                   [15 16 17 18 19]
#                   [20 21 22 23 24]]
B = A[:2,:2]
print(B) # Output: [[0 1]
#                   [5 6]]

B[:,:] = 99
print(A) # Output: [[99 99  2  3  4]
#                   [99 99  7  8  9]
#                   [10 11 12 13 14]
#                   [15 16 17 18 19]
#                   [20 21 22 23 24]]

print(B) # Output: [[99 99]
#                   [99 99]]
```

## Fancy Indexing

Bir array'i başka bir array kullanarak dilimlemeye **Fancy Indexing** denir. Örnek:
```py
import numpy as np

A = np.arange(10,21)
B = np.array([1,3,5])
print(A) # Output: [10 11 12 13 14 15 16 17 18 19 20]
print(A[B]) # Output: [11 13 15]

A = np.arange(25).reshape(5,5)
B = np.array([0,2,4])
print(A) # Output: [[ 0  1  2  3  4]
#                   [ 5  6  7  8  9]
#                   [10 11 12 13 14]
#                   [15 16 17 18 19]
#                   [20 21 22 23 24]]

print(A[:,B]) # Output: [[ 0  2  4]
#                        [ 5  7  9]
#                        [10 12 14]
#                        [15 17 19]
#                        [20 22 24]]

print(A[B,:]) # Output: [[ 0  1  2  3  4]
#                        [10 11 12 13 14]
#                        [20 21 22 23 24]]
```
Index'lenen array'in, index'lemek için kullanılan array'ın elementlerinin ifade ettiği index'leri alınır. Yukarıda 1D ve 2D için örnekler var.

**Not:** Fancy indexing yaparak oluşturduğunuz array'leri herhangi bir variable'a atarsanız, o variable'a atadığınız array parçası, asıl array'e atıfta bulunmaz (refers to). Yani birinde yaptığınız değişiklikler diğerini etkilemez. Örnek:
```py
import numpy as np

A = np.arange(25).reshape(5,5)
B = np.array([0,2,4])
print(A) # Output: [[ 0  1  2  3  4]
#                   [ 5  6  7  8  9]
#                   [10 11 12 13 14]
#                   [15 16 17 18 19]
#                   [20 21 22 23 24]]
C = A[:,B]
print(C) # Output: [[ 0  2  4]
#                   [ 5  7  9]
#                   [10 12 14]
#                   [15 17 19]
#                   [20 22 24]]
C[:,:] = 99
print(C) # Output: [[99 99 99]
#                   [99 99 99]
#                   [99 99 99]
#                   [99 99 99]
#                   [99 99 99]]

print(A) # Output: [[ 0  1  2  3  4]
#                   [ 5  6  7  8  9]
#                   [10 11 12 13 14]
#                   [15 16 17 18 19]
#                   [20 21 22 23 24]]
```

## Boolean Indexing

Bir boolean işlem tanımlayarak ve bu işleme göre `True` olan elementleri içeren bir array'i ifade eden index'leme işlemine **Boolean Indexing** denir. Örnek:
```py
import numpy as np

A = np.arange(10)

print(A) # Output: [0 1 2 3 4 5 6 7 8 9]
B = A[(A % 2 == 0)]
print(B) # Output: [0 2 4 6 8]

A = np.arange(25).reshape(5,5)

print(A) # Output: [[ 0  1  2  3  4]
#                   [ 5  6  7  8  9]
#                   [10 11 12 13 14]
#                   [15 16 17 18 19]
#                   [20 21 22 23 24]]
B = A[(A % 2 == 0)]
print(B) # Output: [ 0  2  4  6  8 10 12 14 16 18 20 22 24]
```

**Not:** Boolean indexing yaparak oluşturduğunuz array'leri herhangi bir variable'a atarsanız, o variable'a atadığınız array parçası, asıl array'e atıfta bulunmaz (refers to). Yani birinde yaptığınız değişiklikler diğerini etkilemez. Örnek:
```py
import numpy as np

import numpy as np

A = np.arange(25).reshape(5,5)
B = np.array([0,2,4])
print(A) # Output: [[ 0  1  2  3  4]
#                   [ 5  6  7  8  9]
#                   [10 11 12 13 14]
#                   [15 16 17 18 19]
#                   [20 21 22 23 24]]
C = A[A % 2 == 0]
print(C) # Output: [ 0  2  4  6  8 10 12 14 16 18 20 22 24]
C[:] = 99
print(C) # Output: [99 99 99 99 99 99 99 99 99 99 99 99 99]

print(A) # Output: [[ 0  1  2  3  4]
#                   [ 5  6  7  8  9]
#                   [10 11 12 13 14]
#                   [15 16 17 18 19]
#                   [20 21 22 23 24]]
```

# NDArray'lerde İşlemler

Bir array'in herhangi bir index'ine veya bir kısmına herhangi bir değeri atayabilirsiniz. Örnek:
```py
import numpy as np

A = np.arange(1,26).reshape((5,5))
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

A[2,1] = 99
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 99 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

A[0:3, 2:] = 99
print(A) # Output: [[ 1  2 99 99 99]
#                   [ 6  7 99 99 99]
#                   [11 99 99 99 99]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]
```

Bir array'in bütün elementlerini teker teker etkileyen aritmetik (matematiksel) işlemlere **elementwise** denir. Yani elementwise işlemler, bir array ile başka bir array'in  bütün elemenlarının teker teker veya bir array ile skaler bir sayının işleme sokulmasıdır. Örnek:
```py
import numpy as np

import numpy as np

A = np.arange(1,10)
B = np.arange(10,19)
print(A) # Output: [1 2 3 4 5 6 7 8 9]
print(B) # Output: [10 11 12 13 14 15 16 17 18]
print(A + B) # Output: [11 13 15 17 19 21 23 25 27]
print(np.add(A,B)) # Output: [11 13 15 17 19 21 23 25 27]
print(A + 100) # Output: [101 102 103 104 105 106 107 108 109]
print(np.add(A,100)) # Output: [101 102 103 104 105 106 107 108 109]

A = np.arange(1,10).reshape(3,3)
B = np.arange(10,19).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]

print(B) # Output: [[10 11 12]
#                   [13 14 15]
#                   [16 17 18]]

print(A + B) # Output: [[11 13 15]
#                       [17 19 21]
#                       [23 25 27]]

print(np.add(A,B)) # Output: [[11 13 15]
#                             [17 19 21]
#                             [23 25 27]]

print(A + 100) # Output: [[101 102 103]
#                         [104 105 106]
#                         [107 108 109]]

print(np.add(A,100)) # Output: [[101 102 103]
#                               [104 105 106]
#                               [107 108 109]]
```
Gördüğünüz gibi örneğin 1. index'deki elemanla 1. index'deki eleman toplanıyor.
- Toplama işlemi için `+` operator'ı ve [`add`](https://numpy.org/doc/stable/reference/generated/numpy.add.html?highlight=add#numpy-add "https://numpy.org/doc/stable/reference/generated/numpy.add.html?highlight=add#numpy-add") fonksiyonu,
- Çıkarma işlemi için `-` operator'ı ve [`subtract`](https://numpy.org/doc/stable/reference/generated/numpy.subtract.html?highlight=subtract#numpy.subtract "https://numpy.org/doc/stable/reference/generated/numpy.subtract.html?highlight=subtract#numpy.subtract") fonksiyonu,
- Çarpma işlemi için `*` operator'ı ve [`multiply`](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html?highlight=multiply#numpy.multiply "https://numpy.org/doc/stable/reference/generated/numpy.multiply.html?highlight=multiply#numpy.multiply") fonksiyonu,
- Bölme işlemi için `/` operator'ı ve [`divide`](https://numpy.org/doc/stable/reference/generated/numpy.divide.html?highlight=divide#numpy.divide "https://numpy.org/doc/stable/reference/generated/numpy.divide.html?highlight=divide#numpy.divide") fonksiyonu,
- Üs alma işlemi için `**` operator'ı ve [`power`](https://numpy.org/doc/stable/reference/generated/numpy.power.html?highlight=power#numpy.power "https://numpy.org/doc/stable/reference/generated/numpy.power.html?highlight=power#numpy.power") fonksiyonu,
- Tam bölme işlemi için `//` operator'ı ve [`floor_divide`](https://numpy.org/doc/stable/reference/generated/numpy.floor_divide.html?highlight=floor_divide#numpy.floor_divide "https://numpy.org/doc/stable/reference/generated/numpy.floor_divide.html?highlight=floor_divide#numpy.floor_divide") fonksiyonu,
- Kalan bulma işlemi için `%` operator'ı ve [`mod`](https://numpy.org/doc/stable/reference/generated/numpy.mod.html?highlight=mod#numpy.mod "https://numpy.org/doc/stable/reference/generated/numpy.mod.html?highlight=mod#numpy.mod") fonksiyonu kullanılır.

**Not:** İki array'i aritmetik bir işleme sokabilmek için bu iki array'in şekilleri (boyut, eksen uzunlukları vs.) aynı olmalı ya da **broadcastable** (daha sonra anlatılacak) olmalı. Aksi durum:
```py
import numpy as np

A = np.random.randint(0,10,(3,4))
B = np.random.randint(0,10,(4,3))
print(A+B) # ValueError: operands could not be broadcast together with shapes (3,4) (4,3) 
```
Bu iki array ne aynı şekildedir ne de broadcastable'dır.

## Broadcasting

Elementwise işlemler aynı şekilli matrix'lerde veya birbiri ile broadcast edilebilir (broadcastable) matrix'lerde çalışır.

![](https://i.ibb.co/yFDpxbB/image.png)

Şekillderi farklı olan matrix'ler arasında aritmetik işlem yapabilmek için bu matrix'leri birbirine benzermemiz gerekmektedir. Bu benzerme işlemi, bu matrix'i (görselde gördüğünüz gibi) X ya da Y ya da hem X hem Y ekseninde kendisi ile genişleterek yapılır. Bunu yapabildiğimiz matrix'lere **broadcastable** denir. Örnek (`{}` işaretleri o yönde genişletilmiş demektir.):
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)

print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]

B = np.array([10])
print(A+B) # Output: [[1 2 3]    [10]{10}{10}   [[11 12 13]
#                     [4 5 6]  + {10  10  10} =  [14 15 16] 
#                     [7 8 9]]   {10  10  10}    [17 18 19]]
B = np.array([10])
print(A+B) # Output: [[1 2 3]    [10]{10}{10}   [[11 12 13]
#                     [4 5 6]  + {10}{10}{10} =  [14 15 16] 
#                     [7 8 9]]   {10}{10}{10}    [17 18 19]]

B = np.array([10,10,10])
print(A+B) # Output: [[1 2 3]    [10 10 10]   [[11 12 13]
#                     [4 5 6]  + {10 10 10} =  [14 15 16] 
#                     [7 8 9]]   {10 10 10}    [17 18 19]]

B = np.array([[10],[10],[10]])
print(A+B) # Output: [[1 2 3]    [[10]{10}{10}    [[11 12 13]
#                     [4 5 6]  +  [10]{10}{10}  =  [14 15 16] 
#                     [7 8 9]]    [10]{10}{10}]    [17 18 19]]
```
Yukarıdaki `B` array çeşitleri haricinde diğer hiçbir varyasyon `A` array'i ile aritmetik işleme giremez çünkü broadcastable değillerdir (yani broadcasting yapılamaz). Kısaca iki matrix'in olduğu bir işlemde herhangi biri diğerinin boyutlarını karşılayacak kadar genişletilebiliyorsa, broadcasting yapılabilir demektir.

## Maskelemek (masking)

`bool` type bir array'i başka bir array'i index'lemek için kullanırsanız, buna Maskelemek (Masking) denir. Örnek:
```py
import numpy as np

A = np.random.randint(5, size=10)
B = np.random.randint(5, size=10)
C = (A==B)

print(A) # Output: [3 4 2 4 2 4 1 0 0 3]
print(B) # Output: [3 3 2 0 2 3 4 2 1 0]
print(C) # Output: [ True False  True False  True False False False False False]
print(C.dtype) # Output: bool
print(A[C]) # Output: [3 2 2] (masking)
print(A[C] == B[C]) # Output: [ True  True  True]
A[C], B[C] = 9,9
print(A) # Output: [9 4 9 4 9 4 1 0 0 3]
print(B) # Output: [9 3 9 0 9 3 4 2 1 0]
```

# Numpy Fonksiyonları

**Ön Bilgi:** `axis = 0` sütunları, `axis = 1` satırları ifade etmektedir. Örnek:
```
  | | |
  V V V
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```
`1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9` data'larının her biri bir satırı ifade etmektedir.

```
[ -> [1 2 3]
  -> [4 5 6]
  -> [7 8 9]]
```
`[1 2 3]`, `[4 5 6]`, `[7 8 9]` dilimlerinin her biri bir sütun'u ifade etmektedir.

## Array'ler Hakkında Bilgi Veren Fonksiyonlar

### `shape` Methodu

Uygulandığı array'in eksenlerinden bulunan elementlerin sayısını ifade eden bir `tuple` döndüren property'dir. Bu `tuple`'lar **Shape Like**'dır. Bundan sonra Shape Like dediğimde bu `tuple`'lar aklınıza gelsin. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4])
print(A) # Output: [1 2 3 4]
print(A.shape) # Output: (4,)
print(type(A.shape)) # Output: <class 'tuple'>

B = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(B) # Output: [[1 2 3]
#                   [1 2 3]
#                   [1 2 3]]
print(B.shape) # Output: (3,3)
print(type(B.shape)) # Output: <class 'tuple'>
```

### `size` Methodu

Uygulandığı array'in element sayısını ifade eden bir integer değer döndüren property'dir. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4])
print(A) # Output: [1 2 3 4]
print(A.size) # Output: 4
print(type(A.size)) # Output: <class 'int'>

B = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(B) # Output: [[1 2 3]
#                   [1 2 3]
#                   [1 2 3]]
print(B.size) # Output: 9
print(type(B.size)) # Output: <class 'int'>
```

### `ndim` Methodu

`ndip` 'number of dimensions' anlamına gelmektedir. Uygulandığı array'in boyutunu ifade eden bir integer değer döndüren property'dir. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4])
print(A) # Output: [1 2 3 4]
print(A.ndim) # Output: 1
print(type(A.ndim)) # Output: <class 'int'>

B = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(B) # Output: [[1 2 3]
#                   [1 2 3]
#                   [1 2 3]]
print(B.ndim) # Output: 2
print(type(B.ndim)) # Output: <class 'int'>
```

### `nbytes` Methodu

Uygulandığı array'in bellekte kaç byte yer kapladığını ifade eden integer değer döndüren property'dir. Örnek:
```py
import numpy as np

A = np.array([1])
print(A.nbytes) # Output: 4
A = np.array([1,2])
print(A.nbytes) # Output: 8
A = np.array([1,2,3])
print(A.nbytes) # Output: 12
A = np.array([1,2,3,4])
print(A.nbytes) # Output: 16
```

### `dtype` Methodu

`dtype` 'data type' anlamına gelmektedir. Uygulandığı array'in elementlerinin type'ını ifade eden class'ı döndüren property'dir. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4])
print(A.dtype) # Output: 16
print(type(A.dtype)) # Output: <class 'numpy.dtype[int32]'>
```

### `shares_memory(a, b, max_work=None)` Fonksiyonu

`a` ve `b` parametrelerine argüman olarak girilen variable'ların aynı array objesine atıfta bulunup bulunmadığını denetler. Bulunuyorsa `True`, aksi durumda `False` döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,26).reshape(5,5)
B = A[0:3, 0:3]
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(B) # Output: [[ 1  2  3]
#                   [ 6  7  8]
#                   [11 12 13]]

print(np.shares_memory(A,B)) # Output: True
B[:,:] = 99

print(A) # Output: [[99 99 99  4  5]
#                   [99 99 99  9 10]
#                   [99 99 99 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(B) # Output: [[99 99 99]
#                   [99 99 99]
#                   [99 99 99]]
```

## Array Oluşturmakta Kullanılan Fonksiyonlar

### `arange(start, stop, step, dtype=None, *, like=None)` Fonksiyonu

`arange` fonksiyonu, normal Python `range` fonksiyonuna benzer çalışır. `start`, `stop`, `step` parametrelerine girdiğiniz integer'ların belirttiği aralıktaki sayıları kullanarak bir array döndürür. `[start, stop)` aralığını dahil eder. `dtype` parametresini kullanarak array objesinin elementlerinin type'ını belirleyebilirsiniz. Örnek:
```py
import numpy as np

A = np.arange(10)
print(A) # Output: [0 1 2 3 4 5 6 7 8 9] 

A = np.arange(5,10)
print(A) # Output: [5 6 7 8 9] 

A = np.arange(5,10,2)
print(A) # Output: [5 7 9]

A = np.arange(5,10,2, dtype=np.float64)
print(A) # Output: [5. 7. 9.]
```

### `linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)` Fonksiyonu

`start` ve `stop` parametrelerinde belirtilen aralıkta `num` parametresinde kadar sayı içeren bir array döndürür. `num` parametresinin default değeri `50`'dir. `[start,stop]` aralığı dahil eder. `endpoint` parametresinin değeri `False` olarak değiştirilirse `stop` dahil edilmez (`[start,stop)`). Örnek:
```py
A = np.linspace(0,10,20)
print(A) # Output: [ 0.          0.52631579  1.05263158  1.57894737  2.10526316  2.63157895
#                    3.15789474  3.68421053  4.21052632  4.73684211  5.26315789  5.78947368
#                    6.31578947  6.84210526  7.36842105  7.89473684  8.42105263  8.94736842
#                    9.47368421 10.        ]
```
Bu elementler birbirine eşit uzaklıktadır. Kanıtı:
```py
import numpy as np

A = np.linspace(0,10,20)

adim = 0
for i in range(10):
    print(A[adim+1]-A[adim])
```
**Output:**
```
0.5263157894736842
0.5263157894736842
0.5263157894736842
0.5263157894736842
0.5263157894736842
0.5263157894736842
0.5263157894736842
0.5263157894736842
0.5263157894736842
0.5263157894736842
```
`axis` parametresine 1 değerini verirseniz işler karışır. Bu yüzden `axis` parametresi default değeri olan 0 iken tek boyutlu bir array oluşturup sonra o array'i `reshape` methodu ile yeniden boyutlandırmanız daha mantıklı bir tercihtir.

### `random(size)` Methodu

`size` parametresine argüman olarak girilen shape like tuple'a uygun boyutlarda, `[0,1)` aralığından rastgele seçilmiş sayılardan oluşan elementlere sahip bir array döndürür. Örnek:
```py
import numpy as np

A = np.random.random((3,3))
print(A) # Output: [[0.88235214 0.81570764 0.79655713]
#                   [0.95037606 0.58507694 0.29642059]
#                   [0.11532438 0.80199224 0.82846779]]
```

### `randint(low, high, size, dtype)` Methodu

`[low, high)` aralığında rastgele seçtiği elementleri kullanarak, `size` parametresine argüman olarak girilen shape like `tuple`'ın belirttiği boyutta ve `dtype` parametresine argüman olarak girilen type'da bir array döndürür. Örnek:
```py
import numpy as np

A = np.random.randint(3,12, size=(3,3))
print(A) # Output: [[ 9 11  4]
#                   [ 9  6  8]
#                   [ 4  3  9]]
```

### `zeros(shape, dtype=float, order='C', *, like=None)` Fonksiyonu

`shape` parametresine argüman olarak girilen shape like `tuple`'ın belirttiği boyutta, bütün elementleri `dtype` parametresine belirtilen type'da sıfır (`0`) sayısı olan array döndürür. Örnek:
```py
import numpy as np

A = np.zeros(3)
print(A) # Output: [0. 0. 0.]
print(A.dtype) # Output: float64

A = np.zeros((3,3))
print(A) # Output: [[0. 0. 0.]
#                   [0. 0. 0.]
#                   [0. 0. 0.]]
print(A.dtype) # Output: float64

A = np.zeros((3,3,3))
print(A) # Output: [[[0. 0. 0.]
#                    [0. 0. 0.]
#                    [0. 0. 0.]]
#
#                   [[0. 0. 0.]
#                    [0. 0. 0.]
#                    [0. 0. 0.]]
#
#                   [[0. 0. 0.]
#                    [0. 0. 0.]
#                    [0. 0. 0.]]]
print(A.dtype) # Output: float64

A = np.zeros(3, dtype=np.int32)
print(A) # Output: [0 0 0]
print(A.dtype) # Output: int32
```

### `ones(shape, dtype=None, order='C', *, like=None)` Fonksiyonu

`shape` parametresine argüman olarak girilen shape like `tuple`'ın belirttiği boyutta, bütün elementleri `dtype` parametresine belirtilen type'da bir (`1`) sayısı olan array döndürür. Örnek:
```py
import numpy as np

A = np.ones(3)
print(A) # Output: [1. 1. 1.]
print(A.dtype) # Output: float64

A = np.ones((3,3))
print(A) # Output: [[1. 1. 1.]
#                   [1. 1. 1.]
#                   [1. 1. 1.]]
print(A.dtype) # Output: float64

A = np.ones((3,3,3))
print(A) # Output: [[[1. 1. 1.]
#                    [1. 1. 1.]
#                    [1. 1. 1.]]
#
#                   [[1. 1. 1.]
#                    [1. 1. 1.]
#                    [1. 1. 1.]]
#
#                   [[1. 1. 1.]
#                    [1. 1. 1.]
#                    [1. 1. 1.]]]
print(A.dtype) # Output: float64

A = np.ones(3, dtype=np.int32)
print(A) # Output: [1 1 1]
print(A.dtype) # Output: int32
```

### `full(shape, fill_value, dtype=None, order='C', *, like=None)` Fonksiyonu

`shape` parametresine argüman olarak girilen shape like `tuple`'ın belirttiği boyutta, bütün elementleri `dtype` parametresine belirtilen type'da ve `fill_value` parametresine argüman olarak girilen data'dan oluşan bir array döndürür. Örnek:
```py
import numpy as np

A = np.full(3, 9)
print(A) # Output: [9 9 9]
print(A.dtype) # Output: int32

A = np.full((3,3), 9)
print(A) # Output: [[9 9 9]
#                   [9 9 9]
#                   [9 9 9]]
print(A.dtype) # Output: int32

A = np.full((3,3,3), 9)
print(A) # Output: [[[9 9 9]
#                    [9 9 9]
#                    [9 9 9]]
#
#                   [[9 9 9]
#                    [9 9 9]
#                    [9 9 9]]
#
#                   [[9 9 9]
#                    [9 9 9]
#                    [9 9 9]]]
print(A.dtype) # Output: int32

A = np.full(3, 9, dtype=np.float64)
print(A) # Output: [9. 9. 9.]
print(A.dtype) # Output: float64
```
`full` fonksiyonunun ürettiği sonucu aritmetik işlemler ile de elde edebiliriz. Örnek:
```py
import numpy as np

A = np.ones(5)
print(A) # Output: [1. 1. 1. 1. 1.]
A = A*10
print(A) # Output: [10. 10. 10. 10. 10.]
```

### `empty(shape, dtype=float, order='C', *, like=None)` Fonksiyonu

`shape` parametresine argüman olarak girilen shape like `tuple`'ın belirttiği boyutta, bütün elementleri `dtype` parametresine belirtilen type'da rastgele data'lardan oluşan bir array döndürür. `empty` ile oluşturulan array'ler 'boş array' olarak kullanılmak amacıyla oluşturulmuştur. Örnek:
```py
import numpy as np

A = np.empty((3,3),dtype=np.int32)
print(A) # Output: [[-189379744        524 -189385552]
#                   [       524 -189379104        524]
#                   [-189378384        524          0]]
```

### `identity(n, dtype=None, *, like=None)` Fonksiyonu

`n` parametresine girilen integer'ın belirttiği boyutta (`n x n`) birim matrix döndürür. Örnek:
```py
import numpy as np

A = np.identity(5)
print(A) # Output: [[1. 0. 0. 0. 0.]
#                   [0. 1. 0. 0. 0.]
#                   [0. 0. 1. 0. 0.]
#                   [0. 0. 0. 1. 0.]
#                   [0. 0. 0. 0. 1.]]
```

### `eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, like=None)` Fonksiyonu

Sadece `N` parametresine argüman (integer olmalı) girilirse, `N x N` boyutunda bir birim matrix döndürür. Örnek:
```py
import numpy as np

A = np.eye(3)
print(A) # Output: [[1. 0. 0.]
#                   [0. 1. 0.]
#                   [0. 0. 1.]]
```
`N` ve `M` parametresine argüman (integer olmalı) girilirse, `M x N` (`M` sütun, `N` satır) birim matrix döndürür. Örnek:
```py
import numpy as np

A = np.eye(3,5)
print(A)
```
**Output:**
```
[[1. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0.]
 [0. 0. 1. 0. 0.]]
```

**Not:** M ve N birbirinden farklı integer olursa birim matrix'in diagonal'ı (köşegeni) tam köşelere denk gelmez.

`k` parametresine girilen integer argüman ile diagonal'ı hareket ettirebilirsiniz. Pozitif integer girerseniz Y ekseninde pozitife doğru, negatif integer girerseniz Y ekseninde negatife doğru diyagonal'ı hareket ettirir. Örnek:
```py
import numpy as np

A = np.eye(N=5, M=5, k=2)
print(A) # Output: [[0. 0. 1. 0. 0.]
#                   [0. 0. 0. 1. 0.]
#                   [0. 0. 0. 0. 1.]
#                   [0. 0. 0. 0. 0.]
#                   [0. 0. 0. 0. 0.]]

A = np.eye(N=5, M=5, k=-2)
print(A) # Output: [[0. 0. 0. 0. 0.]
#                   [0. 0. 0. 0. 0.]
#                   [1. 0. 0. 0. 0.]
#                   [0. 1. 0. 0. 0.]
#                   [0. 0. 1. 0. 0.]]
```

`dtype` parametresi ile array'in elementlerinin type'ını değiştirebilirsiniz. Örnek:
```py
import numpy as np

A = np.eye(3, dtype=np.int32)
print(A) # Output: [[1 0 0]
#                   [0 1 0]
#                   [0 0 1]]
```

### `diag(v, k=0)` Fonksiyonu

`v` parametresine argüman olarak girilen array'in elementlerini diagonal'a yerleştirdiği bir array döndürür. Örnek:
```py
import numpy as np

A = np.diag([1,2,3,4,5])
print(A) # Output: [[1 0 0 0 0]
#                   [0 2 0 0 0]
#                   [0 0 3 0 0]
#                   [0 0 0 4 0]
#                   [0 0 0 0 5]]
```

`k` parametresine girilen integer argüman ile diagonal'ı hareket ettirebilirsiniz. Pozitif integer girerseniz Y ekseninde pozitife doğru, negatif integer girerseniz Y ekseninde negatife doğru diyagonal'ı hareket ettirir ama bu elementlerin kaybolmasına değil, matrix'in eksenlerinin uzunluğunun artmasına sebep olur. Örnek:
```py
import numpy as np

A = np.diag([1,2,3,4,5])
print(A) # Output: [[1 0 0 0 0]
#                   [0 2 0 0 0]
#                   [0 0 3 0 0]
#                   [0 0 0 4 0]
#                   [0 0 0 0 5]]

A = np.diag([1,2,3,4,5], k=2)
print(A) # Output: [[0 0 1 0 0 0 0]
#                   [0 0 0 2 0 0 0]
#                   [0 0 0 0 3 0 0]
#                   [0 0 0 0 0 4 0]
#                   [0 0 0 0 0 0 5]
#                   [0 0 0 0 0 0 0]
#                   [0 0 0 0 0 0 0]]

A = np.diag([1,2,3,4,5], k=-2)
print(A) # Output: [[0 0 0 0 0 0 0]
#                   [0 0 0 0 0 0 0]
#                   [1 0 0 0 0 0 0]
#                   [0 2 0 0 0 0 0]
#                   [0 0 3 0 0 0 0]
#                   [0 0 0 4 0 0 0]
#                   [0 0 0 0 5 0 0]]
```

## Array'lerde İşlemler

### `save(file, arr, allow_pickle=True, fix_imports=True)` Fonksiyonu

`arr` parametresine argüman olarak girilen array'i, `file` parametresine argüman olarak PATH girilirse, o PATH'da; dosya ismi girilirse, terminalin bulunduğu PATH'da dosya olarak yaratır. `file` parametresine argüman olarak PATH veya dosya ismi girmeniz farketmeksizin array dosyası olarak yaratır (create). Dosya uzantısı belirtip belirtmemeniz farketmez, o dosya `npy` uzantılı yaratılır.

Örnek:
```py
import numpy as np

A = np.array([[1,2,3],[1,2,3],[1,2,3]])
np.save("array_exp", A)
```
![](https://i.ibb.co/pW0HYdF/image.png)

### `load(file, mmap_mode=None, allow_pickle=False, fix_imports=True, encoding='ASCII')` Fonksiyonu

`file` parametresine argüman olarak PATH girilirse, o PATH'da bulunan `npy` uzantılı dosyayı; dosya ismi girilirse, terminalin bulunduğu PATH'da bulunan `npy` uzantılı dosyayı programa import eder. Bunu herhangi bir variable'a atayıp kullanabilirsiniz Örnek:
```py
import numpy as np

A = np.array([[1,2,3],[1,2,3],[1,2,3]])
np.save("array_exp", A)

B = np.load("array_exp.npy")
print(B) # Output: [[1 2 3]
#                   [1 2 3]
#                   [1 2 3]]
```

**Not:** Array dosyasının uzantısını `npy` olarak belirtmelisiniz. Aksi halde hata yükseltilir.

### `copy(a, order='K', subok=False)` Fonksiyonu

Aynı array objesini veya dilimlerini farklı variable'lara atasanır bile, bu variable'lar aynı array objesine atıfta bulunacağı (refers to) için herhangi birini kullanarak yapacağınız işlemler diğer variable'da da gözlemlenir (daha önce anlatmıştım). Bu sorunu çömek için array'i `copy` fonksiyonu kullanılabilir.

`copy` fonksiyonu, `a` parametresine girilen array'in kopyasını döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,26).reshape(5,5)
B = np.copy(A[0:3, 0:3])
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(B) # Output: [[ 1  2  3]
#                   [ 6  7  8]
#                   [11 12 13]]

print(np.shares_memory(A,B)) # Output: False
B[:,:] = 99

print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(B) # Output: [[99 99 99]
#                   [99 99 99]
#                   [99 99 99]]
```

`copy` fonksiyonunu method olarak da kullanabiliriz. Örnek:
```py
import numpy as np

A = np.arange(1,26).reshape(5,5)
B = A[0:3, 0:3].copy()
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(B) # Output: [[ 1  2  3]
#                   [ 6  7  8]
#                   [11 12 13]]

print(np.shares_memory(A,B)) # Output: False
B[:,:] = 99

print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(B) # Output: [[99 99 99]
#                   [99 99 99]
#                   [99 99 99]]
```

### `reshape(a, newshape, order='C')` Fonksiyonu

`a` parametresine argüman olarak girdiğiniz array'in elementlerini içeren `newshape` parametresine argüman olarak tanımlanan shape like tuple'a uygun olacak şekilde boyutlandırdığı array'i döndürür. Bu iki array, tek bir array'e atıfta bulunur (refers to). Yani birinde yapacağınız değişiklik diğerini de etkiler. Örnek:
```py
import numpy as np

A = np.arange(1,26)
B = np.reshape(A, (5,5))
print(A) # Output: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25]
print(B) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(np.shares_memory(A,B)) # Output: True

B[:3,:3] = 99

print(A) # Output: [99 99 99  4  5 99 99 99  9 10 99 99 99 14 15 16 17 18 19 20 21 22 23 24 25]
print(B) # Output: [[99 99 99  4  5]
#                   [99 99 99  9 10]
#                   [99 99 99 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]
```

**Not:** `reshape` fonksiyonunu kullanabilmek için bu fonksiyona argüman olarak verdiğiniz array'in element sayısı ile bu fonksiyondan istediğiniz array'in element sayısı tutarlı olmalıdır. Yani `reshape` fonksiyonunu kullanarak 25 elementten `(5,5)` matrix oluşturabilirken `(6,6)` matrix oluşturamazsınız.

**Not:** `reshape` fonksiyonunu method olarak da kullanabilirsiniz. Örnek:
```py
import numpy as np

A = np.arange(1,26).reshape((5,5))

print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]
```

### `fill(value)` Methodu

Uygulandığı array'in bütün elemetlerini, `value` parametresine argüman olarak girilen scalar sayı ile doldurur. Örnek:
```py
import numpy as np

A = np.empty((3,3))
print(A) # Output: [[0.00e+000 0.00e+000 0.00e+000]
#                   [0.00e+000 0.00e+000 2.67e-321]
#                   [0.00e+000 0.00e+000 0.00e+000]]
A.fill(3)
print(A) # Output: [[3. 3. 3.]
#                   [3. 3. 3.]
#                   [3. 3. 3.]]
```

### `append(arr, values, axis=None)` Fonksiyonu

`arr` parametresine argüman olarak girilen array'e, `values` parametresine argüman olarak girilen array'i ekler. Bu array'lerin boyut ve eksen uzunluğu tutarlı olmalı. Örnek:
```py
import numpy as np

A = np.arange(4)
print(A) # Output: [0 1 2 3]
B = np.append(A, 100)
print(B) # Output: [  0   1   2   3 100]
C = np.append(A, [200,300])
print(C) # Output: [  0   1   2   3 200 300]

A = np.arange(9).reshape((3,3))
print(A) # Output: [[0 1 2]
#                   [3 4 5]
#                   [6 7 8]]
B = np.append(A, [[100,200,300]], axis=0)
print(B) # Output: [[  0   1   2]
#                   [  3   4   5]
#                   [  6   7   8]
#                   [100 200 300]]
C = np.append(A, [[100],[200],[300]], axis=1)
print(C) # Output: [[  0   1   2 100]
#                   [  3   4   5 200]
#                   [  6   7   8 300]]
```
Gördüğünüz gibi append fonksiyonu eklemek istediğiniz array'i, `arr` parametresine argüman olarak girilen array'in sonuna ekliyor. (`axis = 0`) olursa sütun formatına uygun `[[100,200,300]]` gibi bir array, (`axis = 1`) olursa her satır için bir tane olacak şekilde `[[100],[200],[300]]` gibi bir formata uygun array kullanmak gerekiyor.

### `insert(arr, obj, values, axis=None)` Fonksiyonu

`arr` parametresine argüman olarak girilen array'in `obj` parametresinde belirtilen index'ine, `values` parametresine argüman olarak girilen array'i ekler. Bu array'lerin boyut ve eksen uzunluğu tutarlı olmalı. Örnek:
```py
A = np.arange(4)
print(A) # Output: [0 1 2 3]
A = np.insert(A, 0, 100)
print(A) # Output: [100   0   1   2   3]

A = np.arange(9).reshape((3,3))
print(A) # Output: [[0 1 2]
#                   [3 4 5]
#                   [6 7 8]]

B = np.insert(A, 1, [[100,200,300]], axis=0)
print(B) # Output: [[  0   1   2]
#                   [100 200 300]
#                   [  3   4   5]
#                   [  6   7   8]]

C = np.insert(A, 1, [[100, 200, 300]], axis=1)
print(C) # Output: [[  0 100   1   2]
#                   [  3 200   4   5]
#                   [  6 300   7   8]]
```
Burada dikkat edilmesi gereken şey, `append`'de `axis = 1` iken `[[100],[200],[300]]` formatını, `insert`'de `[[100, 200, 300]]` formanı kullanıyoruz. Aksi halde şöyle bir şey olur:
```py
import numpy as np

A = np.arange(9).reshape((3,3))
A = np.insert(A, 1, [[100],[200],[300]], axis=1)
print(A) # Output: [[  0 100 200 300   1   2]
#                   [  3 100 200 300   4   5]
#                   [  6 100 200 300   7   8]]
```
**Çözümü:**
```py
A = np.arange(9).reshape((3,3))
C = np.insert(A, [1,], [[100],[200],[300]], axis=1)
print(C) # Output: [[  0 100   1   2]
#                   [  3 200   4   5]
#                   [  6 300   7   8]]
```
`[1,]` yerine `[1,0]` gibi şeyler yazarsanız yine değişik davranışlarla karşılaşırsınız. Yukarıdaki çözümü şans eseri deneyerek buldum. Bu yüzden neden böyle olduğunu açıklayamam. Nasıl olduğunu kurcalayarak kendiniz bulun.

### `vstack(tup)` Fonksiyonu

`vstack` "vertical (dikey, row, satır) stack" anlamına gelmektedir. 1D array'leri 2D matrix olarak, 2D matrix'leri 2D matrix olarak, 3D matrixleri 3D matrix olarak istifler. Örnek:
```py
import numpy as np

A = np.arange(1,4)
B = np.arange(4,7)
print(A) # Output: [1 2 3]
print(B) # Output: [4 5 6]

C = np.vstack((A,B))
print(C) # Output: [[1 2 3]
#                   [4 5 6]]

C = np.vstack((B,A))
print(C) # Output: [[4 5 6]
#                   [1 2 3]]

#####################################

A = np.arange(1,10).reshape(3,3)
B = np.arange(11,20).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(B) # Output: [[11 12 13]
#                   [14 15 16]
#                   [17 18 19]]

C = np.vstack((A,B))
print(C) # Output: [[ 1  2  3]
#                   [ 4  5  6]
#                   [ 7  8  9]
#                   [11 12 13]
#                   [14 15 16]
#                   [17 18 19]]

C = np.vstack((B,A))
print(C) # Output: [[11 12 13]
#                   [14 15 16]
#                   [17 18 19]
#                   [ 1  2  3]
#                   [ 4  5  6]
#                   [ 7  8  9]]

#####################################

A = np.arange(1,28).reshape(3,3,3)
B = np.arange(31,58).reshape(3,3,3)
print(A) # Output: [[[ 1  2  3]
#                    [ 4  5  6]
#                    [ 7  8  9]]
#                 
#                   [[10 11 12]
#                    [13 14 15]
#                    [16 17 18]]
#                 
#                   [[19 20 21]
#                    [22 23 24]
#                    [25 26 27]]]
print(B) # Output: [[[31 32 33]
#                    [34 35 36]
#                    [37 38 39]]
#                 
#                   [[40 41 42]
#                    [43 44 45]
#                    [46 47 48]]
#                 
#                   [[49 50 51]
#                    [52 53 54]
#                    [55 56 57]]]

C = np.vstack((A,B))
print(C) # Output: [[[ 1  2  3]
#                    [ 4  5  6]
#                    [ 7  8  9]]
#                 
#                   [[10 11 12]
#                    [13 14 15]
#                    [16 17 18]]
#                 
#                   [[19 20 21]
#                    [22 23 24]
#                    [25 26 27]]
#                 
#                   [[31 32 33]
#                    [34 35 36]
#                    [37 38 39]]
#                 
#                   [[40 41 42]
#                    [43 44 45]
#                    [46 47 48]]
#                 
#                   [[49 50 51]
#                    [52 53 54]
#                    [55 56 57]]]

C = np.vstack((B,A))
print(C) # Output: [[[31 32 33]
#                    [34 35 36]
#                    [37 38 39]]
#                  
#                   [[40 41 42]
#                    [43 44 45]
#                    [46 47 48]]
#                  
#                   [[49 50 51]
#                    [52 53 54]
#                    [55 56 57]]
#                  
#                   [[ 1  2  3]
#                    [ 4  5  6]
#                    [ 7  8  9]]
#                  
#                   [[10 11 12]
#                    [13 14 15]
#                    [16 17 18]]
#                  
#                   [[19 20 21]
#                    [22 23 24]
#                    [25 26 27]]]
```


### `hstack(tup)` Fonksiyonu

`hstack` "horizontal (yatay, column, sütun) stack" anlamına gelmektedir. 1D array'leri 2D matrix olarak, 2D matrix'leri 2D matrix olarak, 3D matrixleri 3D matrix olarak istifler. Örnek:
```py
import numpy as np

A = np.arange(1,4)
B = np.arange(4,7)
print(A) # Output: [1 2 3]
print(B) # Output: [4 5 6]

C = np.hstack((A,B))
print(C) # Output: [1 2 3 4 5 6]

C = np.hstack((B,A))
print(C) # Output: [4 5 6 1 2 3]

#####################################

A = np.arange(1,10).reshape(3,3)
B = np.arange(11,20).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(B) # Output: [[11 12 13]
#                   [14 15 16]
#                   [17 18 19]]

C = np.hstack((A,B))
print(C) # Output: [[ 1  2  3 11 12 13]
#                   [ 4  5  6 14 15 16]
#                   [ 7  8  9 17 18 19]]

C = np.hstack((B,A))
print(C) # Output: [[11 12 13  1  2  3]
#                   [14 15 16  4  5  6]
#                   [17 18 19  7  8  9]]

#####################################

A = np.arange(1,28).reshape(3,3,3)
B = np.arange(31,58).reshape(3,3,3)
print(A) # Output: [[[ 1  2  3]
#                    [ 4  5  6]
#                    [ 7  8  9]]
#                 
#                   [[10 11 12]
#                    [13 14 15]
#                    [16 17 18]]
#                 
#                   [[19 20 21]
#                    [22 23 24]
#                    [25 26 27]]]
print(B) # Output: [[[31 32 33]
#                    [34 35 36]
#                    [37 38 39]]
#                 
#                   [[40 41 42]
#                    [43 44 45]
#                    [46 47 48]]
#                 
#                   [[49 50 51]
#                    [52 53 54]
#                    [55 56 57]]]

C = np.hstack((A,B))
print(C) # Output: [[[ 1  2  3]
#                    [ 4  5  6]
#                    [ 7  8  9]
#                    [31 32 33]
#                    [34 35 36]
#                    [37 38 39]]
#                 
#                   [[10 11 12]
#                    [13 14 15]
#                    [16 17 18]
#                    [40 41 42]
#                    [43 44 45]
#                    [46 47 48]]
#                 
#                   [[19 20 21]
#                    [22 23 24]
#                    [25 26 27]
#                    [49 50 51]
#                    [52 53 54]
#                    [55 56 57]]]

C = np.hstack((B,A))
print(C) # Output: [[[31 32 33]
#                    [34 35 36]
#                    [37 38 39]
#                    [ 1  2  3]
#                    [ 4  5  6]
#                    [ 7  8  9]]
#                  
#                   [[40 41 42]
#                    [43 44 45]
#                    [46 47 48]
#                    [10 11 12]
#                    [13 14 15]
#                    [16 17 18]]
#                  
#                   [[49 50 51]
#                    [52 53 54]
#                    [55 56 57]
#                    [19 20 21]
#                    [22 23 24]
#                    [25 26 27]]]
```

### `delete(arr, obj, axis=None)` Fonksiyonu

`arr` parametresine argüman olarak girilen array'in `obj` parametresinde belirtilen index'lerini siler. Örnek:
```py
import numpy as np

A = np.arange(12)
print(A) # Output: [ 0  1  2  3  4  5  6  7  8  9 10 11]
A = np.delete(A, [0,3]) # 0 ve 3 indexlerinde bulunan elementler silindi
print(A) # Output: [ 1  2  4  5  6  7  8  9 10 11]

A = np.arange(24).reshape((6,4))
print(A) # Output: [[ 0  1  2  3]
#                   [ 4  5  6  7]
#                   [ 8  9 10 11]
#                   [12 13 14 15]
#                   [16 17 18 19]
#                   [20 21 22 23]]

B = np.delete(A, [0,2], axis=0) # 0 ve 2 indexlerinde bulunan sütunlar silindi
print(B) # Output:[[ 4  5  6  7]
#                  [12 13 14 15]
#                  [16 17 18 19]

C = np.delete(A, [0,2], axis=1) # 0 ve 2 indexlerinde bulunan satırlar silindi
print(C) # Output:[[ 1  3]
#                  [ 5  7]
#                  [ 9 11]
#                  [13 15]
#                  [17 19]
#                  [21 23]]
```

## Array'lerde Matematiksel İşlemler

### `sqrt(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])` Fonksiyonu

`x` parametresine argüman olarak girilen array'in elementlerinin karekökünü aldığı bir array döndürür. `dtype` parametresine girilen argüman ile döndürülen array'in elementlerinin type'ını belirleyebilirsiniz (burası önemli). Örnek:
```py
import numpy as np

A = np.sqrt(np.array([1, 4, 9], dtype=np.float64))
print(A) # Output: [1. 2. 3.]
print(A.dtype) # Output: float64

A = np.sqrt(np.array([-1, 4, 9], dtype=np.float64))
print(A) # Output: [nan  2.  3.]
print(A.dtype) # Output: float64

A = np.sqrt(np.array([-1, 4, 9], dtype=np.complex128))
print(A) # Output: [0.+1.j 2.+0.j 3.+0.j]
print(A.dtype) # Output: complex128
```
Matematikte `-1` sayısının kökünü almak için complex sayılarla uğraşmanız gerekmektedir. Burada da aynısı geçerli. `-1` sayısının kökünü aldıktan sonra sonucu `float64` type'ında ifade edemezsiniz. Bu yüzden `-1` sayısının karekökünün olması gereken yerde `nan` var. Ama `dtype` parametresine argüman olarak `np.complex128` girerseniz, karekök alma işlemi hata yükseltilmeden gerçekleşir.

**Not:** Complex sayılardan oluşan bir array'in `real` ve `imag` kısımlarını alabilirsiniz. Örnek:
```py
import numpy as np

A = np.sqrt(np.array([-1, 4, 9], dtype=np.complex128))
print(A) # Output: [0.+1.j 2.+0.j 3.+0.j]
print(A.real) # Output: [0. 2. 3.]
print(A.imag) # Output: [1. 0. 0.]
print((A.real).dtype) # Output: float64
print((A.imag).dtype) # Output: float64
print(A.dtype) # Output: complex128
```
Gördüğünüz gibi complex sayılardan oluşan bir array'in `real` ve `imag` kısımları `float64` type'ı ile ifade ediliyor.

### `exp(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])` Fonksiyonu

`x` parametresine argüman olarak girilen array'in elementlerini `e**(element)` işlemine tabi tutarak oluşan array'i döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,5).reshape(2,2)
print(np.exp(A)) # Output: [[ 2.71828183  7.3890561 ]
#                           [20.08553692 54.59815003]]
```

**Not:** `e = 2.71828`

### `min(a, axis=None, out=None, keepdims=False, initial=<no value>, where=True)` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin en küçüğünü döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(np.min(A)) # Output: 1
print(np.min(A, axis=0)) # Output: [1 2 3]
print(np.min(A, axis=1)) # Output: [1 4 7]
```

**Not:** Method olarak da kullanılabilir.
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(A.min()) # Output: 1
print(A.min(axis=0)) # Output: [1 2 3]
print(A.min(axis=1)) # Output: [1 4 7]
```

### `max((a, axis=None, out=None, keepdims=False, initial=<no value>, where=True))` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin en büyüğünü döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(np.max(A)) # Output: 9
print(np.max(A, axis=0)) # Output: [7 8 9]
print(np.max(A, axis=1)) # Output: [3 6 9]
```

**Not:** Method olarak da kullanılabilir.
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(A.min()) # Output: 9
print(A.min(axis=0)) # Output: [7 8 9]
print(A.min(axis=1)) # Output: [3 6 9]
```

### `argmin(a, axis=None, out=None)` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin en küçüğünün kaçıncı index'de olduğunu döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(np.argmin(A)) # Output: 0
print(np.argmin(A, axis=0)) # Output: [0 0 0]
print(np.argmin(A, axis=1)) # Output: [0 0 0]
```

**Not:** Method olarak da kullanılabilir.
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(A.argmin()) # Output: 0
print(A.argmin(axis=0)) # Output: [0 0 0]
print(A.argmin(axis=1)) # Output: [0 0 0]
```

### `argmax(a, axis=None, out=None)` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin en büyüğünün kaçıncı index'de olduğunu döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(np.argmax(A)) # Output: 8
print(np.argmax(A, axis=0)) # Output: [2 2 2]
print(np.argmax(A, axis=1)) # Output: [2 2 2]
```

**Not:** Method olarak da kullanılabilir.
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(A.argmax()) # Output: 8
print(A.argmax(axis=0)) # Output: [2 2 2]
print(A.argmax(axis=1)) # Output: [2 2 2]
```

### `sum(a, axis=None, dtype=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)` fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin toplamını döndürür. Döndürülen değerin hangi type'da olacağını `dtype` parametresine gireceğiniz argüman ile belirleyebilirsiniz. Örnek:
```py
import numpy as np

A = np.arange(1,26).reshape(5,5)
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(np.sum(A)) # Output: 325
print(np.sum(A, axis=0)) # Output: [55 60 65 70 75]
print(np.sum(A, axis=1)) # Output: [ 15  40  65  90 115]
```

### `mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin **aritmetik ortalamasını** döndürür. 2D de aşağıdaki kural geçerlidir:
```
axis = None
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]] Output: 13.0

axis = 0
   |  |  |  |  |
   V  V  V  V  V
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]] Output: [11. 12. 13. 14. 15.]

axis = 1
-> [[ 1  2  3  4  5]
->  [ 6  7  8  9 10]
->  [11 12 13 14 15]
->  [16 17 18 19 20]
->  [21 22 23 24 25]] Output: [ 3.  8. 13. 18. 23.]
```

### `median(a, axis=None, out=None, overwrite_input=False, keepdims=False)` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin **medyan değerini** döndürür. 2D de aşağıdaki kural geçerlidir:
```
axis = None
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]] Output: 13.0

axis = 0
   |  |  |  |  |
   V  V  V  V  V
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]] Output: [11. 12. 13. 14. 15.]

axis = 1
-> [[ 1  2  3  4  5]
->  [ 6  7  8  9 10]
->  [11 12 13 14 15]
->  [16 17 18 19 20]
->  [21 22 23 24 25]] Output: [ 3.  8. 13. 18. 23.]
```

### `std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>)` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin **standart sapmasını** döndürür. 2D de aşağıdaki kural geçerlidir:
```
axis = None
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]] Output: 7.211102550927978

axis = 0
   |  |  |  |  |
   V  V  V  V  V
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]] Output: [7.07106781 7.07106781 7.07106781 7.07106781 7.07106781]

axis = 1
-> [[ 1  2  3  4  5]
->  [ 6  7  8  9 10]
->  [11 12 13 14 15]
->  [16 17 18 19 20]
->  [21 22 23 24 25]] Output: [1.41421356 1.41421356 1.41421356 1.41421356 1.41421356]
```

### `all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)` Fonksiyonu

`a` parametresine girilen array'in elemetlerinin boolean değerlerine göre farklı davranışlar sergiler. Örnek:
```py
import numpy as np

A = np.array([True,True,True])
print(A) # Output: [ True  True  True]
print(np.all(A)) # Output: True

A = np.array([False,False,False])
print(A) # Output: [False False False]
print(np.all(A)) # Output: False

A = np.array([True,True,False])
print(A) # Output: [ True  True False]
print(np.all(A)) # Output: False

A = np.array([])
print(A) # Output: []
print(np.all(A)) # Output: True
```

### `any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)` Fonksiyonu

`a` parametresine girilen array'in elemetlerinin boolean değerlerine göre farklı davranışlar sergiler. Örnek:

```py
A = np.array([True,True,True])
print(A) # Output: [ True  True  True]
print(np.any(A)) # Output: True

A = np.array([False,False,False])
print(A) # Output: [False False False]
print(np.any(A)) # Output: False

A = np.array([True,True,False])
print(A) # Output: [ True  True False]
print(np.any(A)) # Output: True

A = np.array([])
print(A) # Output: []
print(np.any(A)) # Output: False
```

### `array_equal(a1, a2, equal_nan=False)` fonksiyonu

`a1` ve `a2` parametrelerine argüman olarak girilen array'lerin yapısal olarak (boyut, eksen, elemanları, elemanlarının bulunduğu index'ler vs.) tamamen birbirinin aynısı olup olmadıklarını denetler. Aynılarsa `True`, aksi durumda `False` döndürür. Örnek:
```py
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[1,2],[3,4]])
C = np.array([[2,1],[3,4]])
print(np.array_equal(A,B)) # Output: True
print(np.array_equal(A,C)) # Output: False
print(np.array_equal(C,B)) # Output: False
```

İki `NDArray`'in boyut, eksen ve elemanları ve elemanlarının indexleri konusunda birbirine eşit olup olmadığını denetlemek için `array_equal(x,y)` fonksiyonunu kullanıyoruz. Yani bu fonksiyon iki `NDArray`'in birbirinin her açıdan aynısı olup olmadığını denetler.

### `intersect1d(ar1, ar2, assume_unique=False, return_indices=False)` Fonksiyonu

`ar1` ve `ar2` parametrelerine girilen array'lerin kesişimini döndürür. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4,5])
B = np.array([3,4,5,6,7])
C = np.intersect1d(A,B)
print(C) # Output: [3 4 5]
```

### `setdiff1d(ar1, ar2, assume_unique=False)` Fonksiyonu

`ar1` parametresine girilen array'de olan, `ar2` parametresine girilen array'de olmayan elementleri döndürür. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4,5])
B = np.array([3,4,5,6,7])
C1 = np.setdiff1d(A,B)
C2 = np.setdiff1d(B,A)
print(C1) # Output: [1 2]
print(C2) # Output: [6 7]
```

### `union1d(ar1, ar2)` Fonksiyonu

`ar1` ve `ar2` parametrelerine girilen array'lerin birleşimini döndürür. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4,5])
B = np.array([3,4,5,6,7])
C = np.union1d(A,B)
print(C) # Output: [1 2 3 4 5 6 7]
```

### `in1d(ar1, ar2, assume_unique=False, invert=False)` Fonksiyonu

`ar1` parametresine argüman olarak girilen array'in elementleri `ar2` parametresine argüman olarak girilen array'de varsa, o elementin bulunduğu index'de `True`, aksi durumlarda `False` olacak şekilde boolean data'lar içeren bir array döndürür. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4,5])
B = np.array([3,4,5,6,7])
C = np.in1d(A,B)
print(C) # Output: [False False  True  True  True]
```
Gördüğünüz gibi `1` ve `2` elemanları `B` array'inde olmadığı için bu elemanların bulunduğu indexlerde `False`; `3`, `4`, `5`  elemanları `B` array'inde olduğu için bu elemanların bulunduğu indexlerde `True` değerleri olan bir array döndürdü.

```py
import numpy as np

A = np.array([1,2,3,4,5])
B = np.array([3,4,5,6,7])
C = np.in1d(B,A)
print(C) # Output: [ True  True  True False False]
```
Gördüğünüz gibi `6` ve `7` elemanları `A` array'inde olmadığı için bu elemanların bulunduğu indexlerde `False`; `3`, `4`, `5`  elemanları `A` array'inde olduğu için bu elemanların bulunduğu indexlerde `True` değerleri olan bir array döndürdü.

### `unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)` Fonksiyonu

`ar` parametresine argüman olarak girilen array'in her elementinden 1 tane bulunduğu (tekrar edenler dahil) ve bunların küçükten büyüğe doğru sıralı olduğu bir array döndürür. Örnek:
```py
import numpy as np

A = np.array([1,1,2,4,6,6,3,1,7,5,3,3,1,6,7,8,4,4])
print(np.unique(A)) # Output: [1 2 3 4 5 6 7 8]
```

### `sort(a, axis=- 1, kind=None, order=None)` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerini `kind` parametresine belirtilen sorting algorithm'e göre `order` parametresinde belirtilen ölçüte göre sıralar ve döndürür. Bu algoritmalara ulaşmak için [tıklayınız](https://numpy.org/doc/stable/reference/generated/numpy.sort.html?highlight=sort#numpy.sort "https://numpy.org/doc/stable/reference/generated/numpy.sort.html?highlight=sort#numpy.sort"). Örnek:
```py
import numpy as np

A = np.array([1,1,2,4,6,6,3,1,7,5,3,3,1,6,7,8,4,4])
print(np.sort(A)) # Output: [1 1 1 1 2 3 3 3 4 4 4 5 6 6 6 7 7 8]

data_type = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38), ('Galahad', 1.7, 38)]
A = np.array(values, dtype=data_type)
print(np.sort(A, order='height')) # Output: [(b'Galahad', 1.7, 38) (b'Arthur', 1.8, 41) (b'Lancelot', 1.9, 38)]
```

**Not:** Merthod hali kullanılırsa, uygulandığı array'i etkiler. Örnek:
```py
import numpy as np

A = np.array([5,3,4,1,2])
print(np.sort(A)) # Output: [1 2 3 4 5]
print(A) # Output: [5 3 4 1 2]

A.sort()
print(A) # Output: [1 2 3 4 5]
```