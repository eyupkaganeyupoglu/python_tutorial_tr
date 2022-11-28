# İçindekiler

- [Array Üzerinde Iterating İşlemi(Iterating Over Array)](#1)

<h1 id="1">Array Üzerinde Iterating İşlemi(Iterating Over Array)</h1>

Array'ler üzerinde döngü oluşturmak için `nditer` fonksiyonunu kullanabilirsiniz. Örnek:
```py
import numpy as np

a = np.arange(0,60,5).reshape(3,4)
print("Original array is:\n", a)
b = a.T
print("Transpose of array is:\n", b)
print("Orjinal array'in sıralanması:")
for i in np.nditer(a):
    print(i,end=", ") # Output: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
    
print("\nOrjinal array'in Transpose'sinin sıralanması:")
for i in np.nditer(b):
    print(i,end=", ") # Output: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
```
**Output:**
```
Original array is:
 [[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]
Transpose of array is:
 [[ 0 20 40]
 [ 5 25 45]
 [10 30 50]
 [15 35 55]]
Orjinal array'in yazdırılması:
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
Orjinal array'in Transpose'sinin yazdırılması:
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
```
Gördüğünüz gibi buradaki yineleme sırası array'in elementlerinin array'deki konumlarına göre değil array'in bellekteki konumlarına göre yapılmışyır. Bu duruma sebep olan şeye Iteration Order (Yineleme Sırası) denir. Yineleme sırasını değiştirmek için `order` parametresini kullanabilirsiniz. Örnek:
```py
import numpy as np

a = np.arange(0,60,5).reshape(3,4)
print("Original array is:\n", a)
print("Transpose of array is:\n", a.T)
print("Sorted in C-style order:")
for i in np.nditer(a, order='C'):
    print(i,end=", ")
print("\nSorted in F-style order:")
for i in np.nditer(a, order='F'):
    print(i,end=", ")
```
**Output:**
```
Original array is:
 [[ 0  5 10 15]       
 [20 25 30 35]        
 [40 45 50 55]]       
Transpose of array is:
 [[ 0 20 40]
 [ 5 25 45]
 [10 30 50]
 [15 35 55]]
Sorted in C-style order:
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
Sorted in F-style order:
0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55,
```
Aynı elementler F-style order kullanılarak sıralanırsa, iterator, bir array üzerinde iterating işleminin daha verimli yolunu seçer.

`nditer` objesinin bir diğer optional parametresi `flags`'dır. Bu parametre, array üzerindeki her bir element için bir flag belirler. Bu flag'ler, elementlerin üzerinde yapılacak işlemleri belirler.
- `'c_index'`: C-order index kullanılır.
- `'f_index'`: Fortran-order index kullanılır.
- `'multi-index'`: Bir multi-index ya da iteration dimension başına bir tuple of indices kullanılır.
-  Causes a multi-index, or a tuple of indices with one per iteration dimension, to be tracked.
- `'external_loop'`: Causes the values given to be one-dimensional arrays with multiple values instead of zero-dimensional arrays. Örnek:
```py
import numpy as np

a = np.arange(0,60,5).reshape(3,4)

print("Original array is:\n", a)

print("\nSorting in C order with c_index flag:")
for i in np.nditer(a, flags=['c_index'], order='C'):
    print(i,end=", ")
print("\nSorting in F order with c_index flag:")
for i in np.nditer(a, flags=['c_index'], order='F'):
    print(i,end=", ")

print("\n\nSorting in C order with f_index flag:")
for i in np.nditer(a, flags=['f_index'], order='C'):
    print(i,end=", ")
print("\nSorting in F order with f_index flag:")
for i in np.nditer(a, flags=['f_index'], order='F'):
    print(i,end=", ")
    
print("\n\nSorting in C order with multi_index flag:")
for i in np.nditer(a, flags=['multi_index'], order='C'):
    print(i,end=", ")
print("\nSorting in F order with multi_index flag:")
for i in np.nditer(a, flags=['multi_index'], order='F'):
    print(i,end=", ")

print("\n\nSorting in C order with external_loop flag:")
for i in np.nditer(a, flags=['external_loop'], order='C'):
    print(i,end=", ")
print("\nSorting in F order with external_loop flag:")
for i in np.nditer(a, flags=['external_loop'], order='F'):
    print(i,end=", ")
```
**Output:**
```
Original array is:
 [[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]

Sorting in C order with c_index flag:
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
Sorting in F order with c_index flag:
0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55,

Sorting in C order with f_index flag:
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
Sorting in F order with f_index flag:
0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55,

Sorting in C order with multi_index flag:
0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55,
Sorting in F order with multi_index flag:
0, 20, 40, 5, 25, 45, 10, 30, 50, 15, 35, 55,

Sorting in C order with external_loop flag:
[ 0  5 10 15 20 25 30 35 40 45 50 55],
Sorting in F order with external_loop flag:
[ 0 20 40], [ 5 25 45], [10 30 50], [15 35 55],
```

`nditer` objesinin bir diğer optional parametresi `op_flags`'dır. Bu parametre, array üzerindeki her bir element için bir flag belirler. Bu flag'ler, elementlerin üzerinde yapılacak işlemleri belirler. Default değeri `'readonly'`'dır. Bu flag, array üzerindeki elementlerin üzerinde sadece okuma yapılmasını sağlar. `'readwrite'` flag'ini kullanarak array üzerindeki elementlerin üzerinde okuma ve yazma yapılmasını sağlayabilirsiniz. `'writeonly'` flag'ini kullanarak array üzerindeki elementlerin üzerinde sadece yazma yapılmasını sağlayabilirsiniz. Örnek:
```py
import numpy as np

a = np.arange(0,60,5).reshape(3,4)
print("Original array is:\n", a)
print("Transpose of array is:\n", a.T)
print("Sorted in C-style order:")
for i in np.nditer(a, order='C', op_flags=['readwrite']):
    i[...] = 2*i
print("Modified array is:\n", a)
```
**Output:**
```
Original array is:
 [[ 0  5 10 15]
 [20 25 30 35]
 [40 45 50 55]]
Modified array is:
 [[  0  10  20  30]
 [ 40  50  60  70]
 [ 80  90 100 110]]
```

Broadcastable iki array üzerinde aynı anda iterating yapmak için `nditer` objesini kullanabilirsiniz. Örnek:
```py
import numpy as np

a = np.arange(0,60,5).reshape(3,4)
b = np.array([1, 2, 3, 4], dtype=int)
for i,j in np.nditer([a,b]):
    print(f"{i}:{j}", end=", ") # Output: 0:1, 5:2, 10:3, 15:4, 20:1, 25:2, 30:3, 35:4, 40:1, 45:2, 50:3, 55:4, 
```
Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.nditer.html).