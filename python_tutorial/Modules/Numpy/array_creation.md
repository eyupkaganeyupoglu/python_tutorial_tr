# İçindekiler

- []()

<h1 id="1">Array Oluşturmak</h1>

<h2 id="1.1"><code>object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None</code> Methodu</h2>

Bir array oluşturmak için en temel yöntem `array` methodunu kullanmaktır. Örnek:
```py
import numpy as np
print(type(np.array([1,2,3]))) # Output: <class 'numpy.ndarray'>
```
- **`object:array_like`**: Bu parametreye argüman olarak sequence, nested sequence, scalar bir değer (integer, float vs.), array döndüren `__array__` methoduna sahip bir şey... kısaca array interface ortaya çıkarabilecek (exposing) herhangi bir obje verilebilir. Bu parametre zorunludur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`dtype:data-type` (optional)**: Bu parametreye argüman olarak C-like veri türleri girilebilir. Böylece array'in öğeleri belirttiğiniz veri türünde olacaktır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`copy:bool` (optional)**: Bu parametreye argüman olarak `True` veya `False` girilebilir. `True` ise array'in bellekteki verilerini kopyalar, `False` ise kopyalamaz. Default değeri `True`'dur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`order:{'C', 'F', 'A', 'K'}` (optional)**: Bu parametreye argüman olarak `C`, `F`, `A` veya `K` girilebilir. `C` ise array'in bellekte C dilindeki gibi (row-major) sıralandığı anlamına gelir (C-style contiguous segment), `F` ise array'in bellekte Fortran dilindeki gibi (column-major) sıralandığı anlamına gelir (Fortran-style contiguous segment), `A` ise array'in bellekteki verilerini kopyalamadan sıralamaya çalışır, `K` ise array'in bellekteki verilerini kopyalamadan sıralamaya çalışır. Default değeri `K`'dur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`subok:bool` (optional)**: Bu parametreye argüman olarak `True` veya `False` girilebilir. `True` ise array'in alt sınıflarını (subclass) döndürür, `False` ise döndürmez. Default değeri `False`'dur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`ndmin:int` (optional)**: Bu parametreye argüman olarak integer girilebilir. Array'in en az kaç boyutlu (dimension) olacağını belirtir. Default değeri `0`'dır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.array.html?highlight=array#numpy.array).

<h2 id="1.2"><code>empty(shape, dtype=float, order='C', *, like=None)</code> Methodu</h2>

İstenilen boyutlarda ve veri türünde başlatılmamış (uninitialized) bir array oluşturmak için kullanılır. Örnek:
```py
import numpy as np
print(np.empty((3,2), dtype = int))
```
**Output:**
```
[[1948283503  656434536]
 [1629497131  656434286]
 [1663051567 1634885992]]
```
- **`shape:int or sequence of ints`**: Array'in boyutlarını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.empty.html?highlight=empty#numpy.empty).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.empty.html?highlight=empty#numpy.empty).
- **`order:{'C', 'F'}` (optional)**: Array'in bellekteki sıralamasını belirtir. `C` ise C dilindeki gibi (row-major), `F` ise Fortran dilindeki gibi (column-major). Default değeri `C`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.empty.html?highlight=empty#numpy.empty).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.empty.html?highlight=empty#numpy.empty).

<h2 id="1.3"><code>zeros(shape, dtype=float, order='C', *, like=None)</code> Method

İstenilen boyutlarda ve veri türünde sıfırlardan oluşan bir array oluşturmak için kullanılır. Örnek:
```py
import numpy as np
print(np.zeros((3,2), dtype = int))
```
**Output:**
```
[[0 0]
 [0 0]
 [0 0]]
```
- **`shape:int or sequence of ints`**: Array'in boyutlarını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros).
- **`dtype:data-type` (optional):** Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros).
- **`order:{'C', 'F'}` (optional)**: Array'in bellekteki sıralamasını belirtir. `C` ise C dilindeki gibi (row-major), `F` ise Fortran dilindeki gibi (column-major). Default değeri `C`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.zeros.html?highlight=zeros#numpy.zeros).

<h2 id="1.4"><code>ones(shape, dtype=float, order='C', *, like=None)</code> Methodu</h2>

İstenilen boyutlarda ve veri türünde birlerden oluşan bir array oluşturmak için kullanılır. Örnek:
```py
import numpy as np
print(np.ones((3,2), dtype = int))
```
**Output:**
```
[[1 1]
 [1 1]
 [1 1]]
```
- **`shape:int or sequence of ints`**: Array'in boyutlarını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.ones.html?highlight=ones#numpy.ones).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.ones.html?highlight=ones#numpy.ones).
- **`order:{'C', 'F'}` (optional)**: Array'in bellekteki sıralamasını belirtir. `C` ise C dilindeki gibi (row-major), `F` ise Fortran dilindeki gibi (column-major). Default değeri `C`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.ones.html?highlight=ones#numpy.ones).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.ones.html?highlight=ones#numpy.ones).

<h2 id="1.5"><code>asarray(a, dtype=None, order=None, *, like=None)</code> Methodu</h2>

Verilen argümanı array objesine dönüştürür. `array` methodundan farkı, daha az parametre almasıdır. Örnek:
```py
import numpy as np
print(np.asarray([1,2,3])) # Ourput: [1 2 3]
```
- **`a:array_like`**: Array objesine dönüştürülecek argüman. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.asarray.html?highlight=asarray#numpy.asarray).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.asarray.html?highlight=asarray#numpy.asarray).
- **`order:{'C', 'F'}` (optional)**: Array'in bellekteki sıralamasını belirtir. `C` ise C dilindeki gibi (row-major), `F` ise Fortran dilindeki gibi (column-major). Default değeri `C`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.asarray.html?highlight=asarray#numpy.asarray).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.asarray.html?highlight=asarray#numpy.asarray).

**Not:** `asarray` methodu, `array` methodundan farklı olarak, argüman olarak verilen array'i kopyalamaz. Yani argüman olarak verilen array'i değiştirdiğinizde, `asarray` methodu ile oluşturulan array de değişecektir. Örnek:
```py
import numpy as np

a = np.array([1,2,3,4,5])
array_exp = np.array(a)
asarray_exp = np.asarray(a)
print(a,array_exp,asarray_exp,sep='\n')
a[0] = 10
print(a,array_exp,asarray_exp,sep='\n')
```
**Output:**
```
[1 2 3 4 5]
[1 2 3 4 5]
[1 2 3 4 5]
[10  2  3  4  5]
[1 2 3 4 5]
[10  2  3  4  5]
```

<h2 id="1.6"><code>frombuffer(buffer, dtype=float, count=- 1, offset=0, *, like=None)</code> Methodu</h2>

Verilen buffer'ı array objesine dönüştürür. Örnek:
```py
import numpy as np

s = b'Hello World'
a = np.frombuffer(s, dtype = 'S1')
print(a) # Output: [b'H' b'e' b'l' b'l' b'o' b' ' b'W' b'o' b'r' b'l' b'd']
```
- **`buffer:object`**: Array objesine dönüştürülecek buffer. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).
- **`count:int` (optional)**: Dönüştürülecek buffer'daki byte sayısını belirtir. Default değeri `-1`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).
- **`offset:int` (optional)**: Dönüştürülecek buffer'daki ilk byte'ın indexini belirtir. Default değeri `0`'dır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.frombuffer.html?highlight=frombuffer#numpy.frombuffer).

<h2 id="1.7"><code>fromiter(iter, dtype, count=- 1, *, like=None)</code> Methodu</h2>

Verilen iterable objeyi array objesine dönüştürür. Örnek:
```py
import numpy as np

a = iter(range(5))
b = np.fromiter(a, dtype = float)
print(b) # Output: [0. 1. 2. 3. 4.]
```
- **`iterable:iterable`**: Array objesine dönüştürülecek iterable obje. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.fromiter.html?highlight=fromiter#numpy.fromiter).
- **`dtype:data-type`**: Array'in veri türünü belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.fromiter.html?highlight=fromiter#numpy.fromiter).
- **`count:int` (optional)**: Dönüştürülecek iterable objedeki eleman sayısını belirtir. Default değeri `-1`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.fromiter.html?highlight=fromiter#numpy.fromiter).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.fromiter.html?highlight=fromiter#numpy.fromiter).

<h2 id="1.8"><code>arange(start, stop, step, dtype=None, *, like=None)</code> Methodu</h2>

`start` ve `stop` (`stop` hariç) arasındaki sayıları `step` kadar arttırarak elde edilen sayı dizisini array objesine dönüştürür. Örnek:
```py
import numpy as np

a = np.arange(10)
b = np.arange(1,9,2)
print(a) # Output: [0 1 2 3 4 5 6 7 8 9]
print(b) # Output: [1 3 5 7]
```
- **`start:int` (optional)**: Array'in ilk elemanını belirtir. Default değeri `0`'dır. `range` fonksiyonundaki `start` parametresindeki kurallar geçerlidir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).
- **`stop:int`**: Array'in son elemanını belirtir. `stop` dahil değildir. `range` fonksiyonundaki `stop` parametresindeki kurallar geçerlidir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).
- **`step:int` (optional)**: Array'in elemanlarının arasındaki farkı belirtir. Default değeri `1`'dir. `range` fonksiyonundaki `step` parametresindeki kurallar geçerlidir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).
- **`like:array_like` (optional)**: Bu parametreye argüman olarak array verilebilir. NumPy array objesi olmayan array'ler oluşturmanız gerektiğinde bu parametreye argüman olarak girilen array'in özelliklerini (properties) kullanarak array oluşturur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.arange.html?highlight=arange#numpy.arange).

<h2 id="1.9"><code>linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)</code> Methodu</h2>

`start` ve `stop` arasındaki `num` kadar birbirine eşit uzaklıkta olan sayıları içeren bir array objesi döndürür. Örnek:
```py
import numpy as np

a = np.linspace(10,20,5)
print(a) # Output: [10.  12.5 15.  17.5 20. ]
```
- **`start:int`**: Array'in ilk elemanını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`stop:int`**: Array'in son elemanını belirtir. Dahil edilip edilmeyeceğini `endpoint` parametresi belirler. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`num:int`**: Array'in eleman sayısını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`endpoint:bool` (optional)**: `stop` değerinin dahil edilip edilmeyeceğini belirtir. Default değeri `True`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`retstep:bool` (optional)**: Array'in elemanlarının arasındaki farkı döndürüp döndürmeyeceğini belirtir. Default değeri `False`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace). Örnek:
  ```py
  import numpy as np

  a = np.linspace(10,20,5,retstep=True)
  print(a) # Output: (array([10. , 12.5, 15. , 17.5, 20. ]), 2.5)
  ```
  Buradaki `2.5` array'in elemanlarının arasındaki farktır.
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).
- **`axis:int` (optional)**: Array'in boyutunu belirtir. Default değeri `0`'dır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.linspace.html?highlight=linspace#numpy.linspace).

<h2 id="1.10"><code>logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)</code> Methodu</h2>

`start` ve `stop` arasındaki `num` kadar birbirine eşit uzaklıkta olan sayıların `base` parametresinde belirtilen taban üzerindeki logaritmasını içeren bir array objesi döndürür. Yani `base ** start` ile `base ** stop` arasındaki `num` kadar birbirine eşit uzaklıkta olan sayıları içeren bir array objesi döndürür. Örnek:
```py
import numpy as np

a = np.logspace(1,10,10,base=2)
print(a) # Output: [   2.    4.    8.   16.   32.   64.  128.  256.  512. 1024.]
```
- **`start:int`**: Array'in ilk elemanının logaritmasını alınacak sayıyı belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`stop:int`**: Array'in son elemanının logaritmasını alınacak sayıyı belirtir. Dahil edilip edilmeyeceğini `endpoint` parametresi belirler. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`num:int`**: Array'in eleman sayısını belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`endpoint:bool` (optional)**: `stop` değerinin dahil edilip edilmeyeceğini belirtir. Default değeri `True`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`base:float` (optional)**: Array'in elemanlarının logaritmasını alınacak sayıyı belirtir. Default değeri `10.0`'dur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).
- **`axis:int` (optional)**: Array'in boyutunu belirtir. Default değeri `0`'dır. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.logspace.html?highlight=logspace#numpy.logspace).

<h2 id="1.?"><code>full(shape, fill_value, dtype=None, order='C', *, like=None)</code> Methodu</h2>

`shape` parametresinde belirtilen boyutta `fill_value` parametresinde belirtilen değeri içeren bir array objesi döndürür. Örnek:
```py
import numpy as np

a = np.full((2,2),7)
print(a)
```
**Output:**
```
[[7 7]
 [7 7]]
```
- **`shape:int`**: Array'in boyutunu belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.full.html?highlight=full#numpy.full).
- **`fill_value:int`**: Array'in elemanlarının değerini belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.full.html?highlight=full#numpy.full).
- **`dtype:data-type` (optional)**: Array'in veri türünü belirtir. Default değeri `float`'tur. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.full.html?highlight=full#numpy.full).
- **`order:{'C', 'F', 'A'}` (optional)**: Array'in bellekte nasıl saklanacağını belirtir. Default değeri `'C'`'dir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.full.html?highlight=full#numpy.full).
- **`like:array_like` (optional)**: Array'in boyutunu ve veri türünü belirtir. Daha fazla bilgi için [tıklayın](https://numpy.org/doc/1.23/reference/generated/numpy.full.html?highlight=full#numpy.full).

