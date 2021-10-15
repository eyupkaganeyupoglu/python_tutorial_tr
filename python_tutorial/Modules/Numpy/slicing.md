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
Yukarıda `A[2,1]` 2. satır, 1. sütun'un kesişimindeki index'de bulunan elemanı ifade etmektedir.
```
 Birinci Sütun
      |
      V
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15] <- İkinci Satır
 [16 17 18 19 20]
 [21 22 23 24 25]]
```

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
  # 3. satır, 3. sütundaki elemana atıfta bulunur.
  print(A[3, 3]) # Output: 18

  # 0. index'ten başlar, (3. index'i dahil etmeden) 3. index'e kadar array'in satırlarını,
  # 0. index'ten başlar, (3. index'i dahil etmeden) 3. index'e kadar array'in sütunlarını yazdırır.
  print(A[0:3, 0:3]) # Output: [[ 0  1  2]
  #                             [ 5  6  7]
  #                             [10 11 12]]

  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (4. index'i dahil etmeden) 4. index'e kadar array'in satırlarını,
  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (5. index'i dahil etmeden) 5. index'e kadar array'in sütunlarını yazdırır.
  print(A[:4, :5]) # Output: [[ 0  1  2  3  4]
  #                           [ 5  6  7  8  9]
  #                           [10 11 12 13 14]
  #                           [15 16 17 18 19]]

  # Bitiş index'i belirtilmediği için 3. indexten başlar, en son index'e kadar array'in satırlarını,
  # Bitiş index'i belirtilmediği için 3. indexten başlar, en son index'e kadar array'in sütunlarını yazdırır.
  print(A[3:, 3:]) # Output: [[18 19]
  #                           [23 24]]

  # Başlangıç ve bitiş intex'i belirtilmediği için array'in bütün satır ve sütunlarını yazdırır.
  print(A[:, :]) # Output: [[ 0  1  2  3  4]
  #                         [ 5  6  7  8  9]
  #                         [10 11 12 13 14]
  #                         [15 16 17 18 19]
  #                         [20 21 22 23 24]]

  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (-1. index'i dahil etmeden) -1. index'e kadar (sonran bir önceki index) array'in satırlarını,
  # Başlangıç index'i belirtilmediği için en baştan (0. index'ten) başlar, (-1. index'i dahil etmeden) -1. index'e kadar (sonran bir önceki index) array'in sütunlarını yazdırır.
  print(A[:-1, :-1]) # Output: [[ 0  1  2  3]
  #                             [ 5  6  7  8]
  #                             [10 11 12 13]
  #                             [15 16 17 18]]

  # Baştan sona index atlamadan array'in satır ve sütunlarını yazdırır.
  print(A[::1, ::1]) # Output: [[ 0  1  2  3  4]
  #                             [ 5  6  7  8  9]
  #                             [10 11 12 13 14]
  #                             [15 16 17 18 19]
  #                             [20 21 22 23 24]]

  # Baştan sona 1 index atlaya atlaya array'in satır ve sütunlarını yazdırır.
  print(A[::2, ::2]) # Output: [[ 0  2  4]
  #                             [10 12 14]
  #                             [20 22 24]]

  # 0. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar 2 index atlaya atlaya array'in satırlarını,
  # 0. index'ten başlar, (9. index'i dahil etmeden) 9. index'e kadar 2 index atlaya atlaya array'in sütunlarını yazdırır.
  print(A[0:9:3, 0:9:3]) # Output: [[ 0  3]
  #                                 [15 18]]

  # Sondan başa index atlamadan array'in satırlarını yazdırır.
  print(A[::-1,:]) # Output: [[20 21 22 23 24]
  #                           [15 16 17 18 19]
  #                           [10 11 12 13 14]
  #                           [ 5  6  7  8  9]
  #                           [ 0  1  2  3  4]]

  # Sondan başa index atlamadan array'in sütunlarını yazdırır.
  print(A[:, ::-1]) # Output: [[ 4  3  2  1  0]
  #                            [ 9  8  7  6  5]
  #                            [14 13 12 11 10]
  #                            [19 18 17 16 15]
  #                            [24 23 22 21 20]]

  # Sondan başa index atlamadan array'i yazdırır. (matrix'i ters çevirme)
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