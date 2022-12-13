# İçindekiler

- [`ndarray` Object](#1)
- [Array'lerde Boyut (Dimension) ve Indexing](#2)

<h1 id="1"><code>ndarray</code> Object</h1>

NumPy'da tanımlanan en önemli obje, `ndarray` adı verilen N boyutlu bir array türüdür. `ndarray`, aynı type data'ların (bunlara element veya item denir ama ben element olarak bahsedeceğim) toplandığı bir koleksiyonudur (grid of value, collection). Bu elementlere erişmek için zero-based index'leme kullanılır (yani ilk elementin index'i `0` olarak ifade edilir). Bir `ndarray`'deki her bir element bellekte aynı boyutta yer kaplar ve `data-type` objesinin bir objesidir (`data-type` = `dtype`).

Bir ndarray'i slicing yoluyla (daha sonra anlatılacak) parçalarsan bir array scalar elde edersin.

![](./pics/1.jpg)

Görseldeki ndarray diyagramı, dtype ve array scalar arasındaki ilişkiyi gösteriyor. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])
b = a[0:2]
c = a[4]
print(type(b), b.dtype, b) # Output: <class 'numpy.ndarray'> int32 [1 2]
print(type(c), c.dtype, c) # Output: <class 'numpy.int32'> int32 5
```
Yani yukarıda anlattığım bütün olay, `c`'nin `'numpy.int32'` type bir obje olması için yaptığımız şeyin açıklaması.

**Not:** The ndarray object consists of contiguous one-dimensional segment of computer memory, combined with an indexing scheme that maps each item to a location in the memory block. The memory block holds the elements in a row-major order (C style) or a column-major order (FORTRAN or MatLab style).

<h1 id="2">Array'lerde Boyut (Dimension) ve Indexing</h1>

Array'leri indexlemek normal python'daki sequence'ları indexlemek gibidir. Örnek:
```py
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a,end="\n-------\n")
print(a[0],end="\n-------\n")
print(a[0][0])
```
**Output:**
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
-------
[1 2 3]
-------
1
```

Bir array'in **rank**'ı, o dizinin dimension sayısını ifade eden bir integer'dır. İki ya da daha fazla dimension'ı bulunan NumPy array'ler initialize (başlatmak) edebilmek için (kısaca oluşturabilmek için) nested listeler kullanılır. Örnek:
```py
import numpy as np
print(np.array([[1,2,3],[4,5,6],[7,8,9]]))
```
**Output:**
```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```
NumPy'da dimension'lar **axis** olarak isimlendirilir (birden fazla dimension'dan bahsediyorsak **axes**). 2D array'lerle uğraşırken column ve row kavramlarıyla karşılaşmışsınızdır. Column ve row kavramları sadece 2D array'lerde geçerli olduğu için genel olarak axis (eksen) terimi kullanılır. Çok dimention'lu array'lerde axis'ler dıştan içe anlamına gelecek şekilde soldan sağa doğru sıralanır. Örnek:
```
[[[1 2 3]
  [4 5 6]
  [7 8 9]]

 [[1 2 3]
  [4 5 6]
  [7 8 9]]]

a[first axis, second axis, third axis, ...]
```
```py
import numpy as np

a = np.zeros((2,3,4))
print(a,end="\n-------\n")
a[:,0,0] = 1
print(a,end="\n-------\n")
a = np.zeros((2,3,4))
a[0,:,0] = 2
print(a,end="\n-------\n")
a = np.zeros((2,3,4))
a[0,0,:] = 3
print(a)
```
**Output:**
```
[[[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
-------
[[[1. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[1. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
-------
[[[2. 0. 0. 0.]
  [2. 0. 0. 0.]
  [2. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
-------
[[[3. 3. 3. 3.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]
```
**Not:** Farklı array'ler aynı verileri içeriyor olabilir. Bu durumda array'lerin birinde yaptığınız değişiklikler diğer array'i de etkiler.

[Array attributes](https://numpy.org/doc/stable/reference/arrays.ndarray.html#arrays-ndarray) ve [array object](https://numpy.org/doc/stable/reference/arrays.html#arrays) hakkında daha fazla bilgi tıklayınız.