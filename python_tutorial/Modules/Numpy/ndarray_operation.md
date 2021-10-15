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

Bir array'i kullanarak boolean bir işlem yaparsanız, sonuçta `bool` type elementlere sahip bir array elde edersiniz. Örnek:
```py
import numpy as np

A = np.arange(1,26).reshape(5,5)
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

B = A%2==0
print(B) # Output: [[False  True False  True False]
#                   [ True False  True False  True]
#                   [False  True False  True False]
#                   [ True False  True False  True]
#                   [False  True False  True False]]
```

`bool` type elementlere sahip bir array'i başka bir array'i index'lemek için kullanırsanız, buna Maskelemek (Masking) denir. Örnek:
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