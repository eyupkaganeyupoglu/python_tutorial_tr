# İçindekiler

- [Copy & View](#1)

<h1 id="1">Copy & View</h1>

NumPy'da array'lerin kopyalanması ve görünümü (view) alınması iki farklı işlemdir. Kopyalam işlemi, array'i her şeyiyle birlikte kopyalar. Görünüm almak ise array'in sadece görünümünü alır. Bu işlemler aşağıdaki şekilde gerçekleştirilir: Örnek:
```py
# view
import numpy as np
arr = np.array([[10,10], [2,3], [4,5]])

print('Array arr is:', arr, sep="\n", end="\n\n")

print('Create a view of arr: b = a.view()')
b = arr.view()
print('Array b is:', b, sep="\n", end="\n\n")

print('b is arr:', b is arr, end="\n\n")

print ('Change the contents of b: b[0,0] = 100')
b[0,0] = 100
print('Modified array b:', b, sep="\n")
print('arr remains unchanged:', arr, sep="\n")
```
**Output:**
```
Array arr is:
[[10 10]
 [ 2  3]
 [ 4  5]]

Create a view of arr: b = a.view()
Array b is:
[[10 10]
 [ 2  3]
 [ 4  5]]

b is arr: False

Change the contents of b: b[0,0] = 100
Modified array b:
[[100  10]
 [  2   3]
 [  4   5]]
arr remains unchanged:
[[100  10]
 [  2   3]
 [  4   5]]
```
```py
# Copy
import numpy as np
arr = np.array([[10,10], [2,3], [4,5]])

print('Array arr is:', arr, sep="\n", end="\n\n")

print('Create a deep copy of arr: b = a.copy()')
b = arr.copy()
print('Array b is:', b, sep="\n", end="\n\n")

print('b is arr:', b is arr, end="\n\n")

print ('Change the contents of b: b[0,0] = 100')
b[0,0] = 100
print('Modified array b:', b, sep="\n")
print('arr remains unchanged:', arr, sep="\n")
```
**Output:**
```
Array a is:
[[10 10]
 [ 2  3]
 [ 4  5]]

Create a deep copy of a: b = a.copy()
Array b is:
[[10 10]
 [ 2  3]
 [ 4  5]]

Can we write b is a False

Change the contents of b: b[0,0] = 100
Modified array b:
[[100  10]
 [  2   3]
 [  4   5]]
a remains unchanged:
[[10 10]
 [ 2  3]
 [ 4  5]]
```
Gördüğünüz gibi `view` işlemi ile array'in sadece görünümünü alındığı için orjinal array'de yapılan değişiklikler görünüm alınan array'de de görünür. `copy` işlemi ise array'i tamamen kopyalayıp orjinal array'den tamamen bağımsız bir array oluşturur. Bu yüzden orjinal array'de yapılan değişiklikler kopyalanan array'de görünmez.