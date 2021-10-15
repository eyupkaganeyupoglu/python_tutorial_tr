# Numpy Fonksiyonları

**Ön Bilgi:** `axis = 0` sütun yörüngesini, `axis = 1` satır yörüngesini ifade etmektedir. Örnek:
```
axis = 0
  | | |
  V V V
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```
`[[1],[4],[7]]`, `[[2],[5],[8]]`, `[[3],[6],[9]]` dilimlerinin her biri bir sütunu ifade etmektedir.

```
[ -> [1 2 3]
  -> [4 5 6]
  -> [7 8 9]]
```
`[1 2 3]`, `[4 5 6]`, `[7 8 9]` dilimlerinin her biri bir satırı ifade etmektedir.

## Array'ler Hakkında Bilgi Veren Fonksiyonlar

### `shape` Methodu

Uygulandığı array'in eksenlerinden bulunan elementlerin sayısını ifade eden bir `tuple` döndüren property'dir. Bu `tuple`'lar **Shape Like**'dır. Bundan sonra Shape Like dediğimde bu `tuple`'lar aklınıza gelsin. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4])
print(A) # Output: [1 2 3 4]
print(A.shape) # Output: (4,)
print(type(A.shape)) # Output: <class 'tuple'>

B = np.array([[1,2,3],[1,2,3],[1,2,3],[1,2,3]])
print(B) # Output: [[1 2 3]
#                   [1 2 3]
#                   [1 2 3]
#                   [1,2,3]]
print(B.shape) # Output: (4,3)
print(type(B.shape)) # Output: <class 'tuple'>
```
`B` array'i 4 satır, 3 sütundan oluşmaktadır.

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

### `data` Methodu

Uygulandığı array'in data'larının başlangıcın işaret eden (pointing) Python buffer objesini döndürür. Kısaca, array'in bulunduğu bellek adresini döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,10)
print(A.data) # Output: <memory at 0x000002C680F11F40>
```

### `dtype` Methodu

`dtype` 'data type' anlamına gelmektedir. Uygulandığı array'in elementlerinin type'ını ifade eden class'ı döndüren property'dir. Örnek:
```py
import numpy as np

A = np.array([1,2,3,4])
print(A.dtype) # Output: 16
print(type(A.dtype)) # Output: <class 'numpy.dtype[int32]'>
```

### `itemsize` Methodu

Uygulandığı array'in elemenetlerinin her birinin kaç byte yer kapladığını döndürür. Örnek:
```py
import numpy as np

A = np.array([1,2,20,99999999999])
print(A.itemsize) # Output: 8
print(A.size) # Output: 4
print(A.nbytes) # Output: 32
```

**Not:** `itemsize * size == nbytes`

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

### `random.random(size)` Fonksiyonu

`size` parametresine argüman olarak girilen shape like tuple'a uygun boyutlarda, `[0,1)` aralığından rastgele seçilmiş sayılardan oluşan elementlere sahip bir array döndürür. Örnek:
```py
import numpy as np

A = np.random.random((3,3))
print(A) # Output: [[0.88235214 0.81570764 0.79655713]
#                   [0.95037606 0.58507694 0.29642059]
#                   [0.11532438 0.80199224 0.82846779]]
```

### `random.randint(low, high, size, dtype)` Fonksiyonu

`[low, high)` aralığında rastgele seçtiği **integer type** elementleri kullanarak, `size` parametresine argüman olarak girilen shape like `tuple`'ın belirttiği boyutta ve `dtype` parametresine argüman olarak girilen type'da bir array döndürür. `dtype` parametresi bulunsa bile bu parametreye `float64` veya `complex128` type'larını argüman olarak giremezsiniz. Aksi halde `TypeError: Unsupported dtype dtype('complex128') for randint` gibi hatalar yükseltilir. Örnek:
```py
import numpy as np

A = np.random.randint(3,12, size=(3,3))
print(A) # Output: [[ 9 11  4]
#                   [ 9  6  8]
#                   [ 4  3  9]]
```

### `random.uniform(low=0.0, high=1.0, size=None)` Fonksiyonu

`[low, high)` aralığında rastgele seçtiği **float type** elementleri kullanarak, `size` parametresine argüman olarak girilen shape like `tuple`'ın belirttiği boyutta bir array döndürür. `low` ve `high` parametrelerine argüman olarak float type sayı girebilirsiniz. Örnek:
```py
import numpy as np

A = np.random.uniform(1.5,5.85,size=10)
print(A) # Output: [3.57113264 2.3821391  1.81529321 2.84556355 5.07186779 5.6814039 5.35484855 2.49282832 4.08940967 2.05561592]
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

### `repeat(a, repeats, axis=None)` Fonksiyonu

`a` parametresine argüman olarak girilen array like obje'yi `repeats` parametresine argüman olarak girilen sayı kadar tekrar ettiği bir array döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,4)
B = np.arange(1,10).reshape(3,3)
print(A) # Output: [1 2 3]
print(B) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]

print(np.repeat(3,3)) # Output: [3 3 3]
print(np.repeat(A,3)) # Output: [1 1 1 2 2 2 3 3 3]
print(np.repeat(B,3)) # Output: [1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7 8 8 8 9 9 9]
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
`N` ve `M` parametresine argüman (integer olmalı) girilirse, `M x N` (`M` satır, `N` sütun) birim matrix döndürür. Örnek:
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

`arr` parametresine argüman olarak girilen array'i, `file` parametresine argüman olarak PATH girilirse, o PATH'da; dosya ismi girilirse, terminalin bulunduğu PATH'da dosya olarak yaratır. `file` parametresine argüman olarak PATH veya dosya ismi girmeniz farketmeksizin array dosyası olarak yaratır (create). Dosya uzantısı belirtip belirtmemeniz farketmez, o dosya `npy` uzantılı yaratılır. Örnek:
```py
import numpy as np

A = np.array([[1,2,3],[1,2,3],[1,2,3]])
np.save("array_exp", A)
```
![](https://i.ibb.co/pW0HYdF/image.png)

### `savez(savez(file, *args, **kwds))` Fonksiyonu

`*args` veya `**kwds` parametresine argüman olarak girilen array'leri, `file` parametresine argüman olarak PATH girilirse, o PATH'da; dosya ismi girilirse, terminalin bulunduğu PATH'da dosya olarak yaratır. `file` parametresine argüman olarak PATH veya dosya ismi girmeniz farketmeksizin array dosyası olarak yaratır (create). Dosya uzantısı belirtip belirtmemeniz farketmez, o dosya `npz` uzantılı yaratılır. Örnek:
```py
import numpy as np

A = np.array([[1,2,3],[1,2,3],[1,2,3]])
np.save("array_exp", A)
```
![](https://i.ibb.co/pW0HYdF/image.png)

**Not:** `npy` ile `npz` dosya formatları farklı işlerde kullanılır. Farkları hakkında bilgi için [tıklayınız](https://stackoverflow.com/a/57268286/15170972 "https://stackoverflow.com/a/57268286/15170972"). `npy` tek (single) array depolarken, `npz` birden fazla (multiple) array depolar. `npz` dosyasına depolanacak array objelerini `savez` fonksiyonuna argüman olarak girerken `*args` parametretresine girersek, bu array objeleri `npz` dosyasında `arr_1`, `arr_2` vb. isimlerle depolanırken; `**kwargs` parametretresine girersek, bu array objeleri `npz` dosyasında kendi identifier'larıyla depolanır.

**Not:** `savez` ve `save` fonksiyonu ile oluşturulan, içinde aynı array objesi olan dosyalar aynı boyuttadır. `savez_compressed(file, *args, **kwds)` fonksiyonu ile oluşturulan dosyalar, normal `npz` dosyalardan daha düşük boyuttadır çünkü sıkıştırılmışlardır (compressed).

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

### `astype(dtype, order='K', casting='unsafe', subok=True, copy=True)` Methodu

Uygulandığı array'in `dtype` parametresine argüman olarak girilen type'da elementlere sahip versiyonunu döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,10)
print(A.astype(np.float64)) # Output: [1. 2. 3. 4. 5. 6. 7. 8. 9.]
print(A) # Output: [1 2 3 4 5 6 7 8 9]
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

**Not:** `newshape` parametresine argüman olarak girdiğiniz shape like tuple'da negarif sayılar kullanırsanız, uygulanduğu array'in elemanlarını sığdırdığı bir array elde edersiniz. Örnek
```py
import numpy as np

A = np.arange(1,11)
print(np.reshape(A,(2,-1))) # Output: [[ 1  2  3  4  5]
#                                      [ 6  7  8  9 10]]

print(np.reshape(A,(-1,2))) # Output: [[ 1  2]
#                                      [ 3  4]
#                                      [ 5  6]
#                                      [ 7  8]
#                                      [ 9 10]]
```

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
Gördüğünüz gibi append fonksiyonu eklemek istediğiniz array'i, `arr` parametresine argüman olarak girilen array'in sonuna ekliyor. (`axis = 0`) olursa `[[100,200,300]]` gibi bir şekle sahip array, (`axis = 1`) olursa `[[100],[200],[300]]` gibi bir şekle sahip array kullanmak gerekiyor.

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

**Not:** Farklı type array'lerde uniform bir görüntü elde etmek için upcasting işlemi yapılır. Örnek:
```py
import numpy as np

A = np.arange(1,10,dtype=np.int32).reshape(3,3)
B = np.arange(11,20,dtype=np.float64).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]

print(B) # Output: [[11. 12. 13.]
#                   [14. 15. 16.]
#                   [17. 18. 19.]]

C = np.vstack((A,B))
print(C) # Output: [[ 1.  2.  3.]
#                   [ 4.  5.  6.]
#                   [ 7.  8.  9.]
#                   [11. 12. 13.]
#                   [14. 15. 16.]
#                   [17. 18. 19.]]
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

**Not:** Farklı type array'lerde uniform bir görüntü elde etmek için upcasting işlemi yapılır. Örnek:
```py
import numpy as np

A = np.arange(1,10,dtype=np.int32).reshape(3,3)
B = np.arange(11,20,dtype=np.float64).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]

print(B) # Output: [[11. 12. 13.]
#                   [14. 15. 16.]
#                   [17. 18. 19.]]

C = np.hstack((A,B))
print(C) # Output: [[ 1.  2.  3. 11. 12. 13.]
#                   [ 4.  5.  6. 14. 15. 16.]
#                   [ 7.  8.  9. 17. 18. 19.]]
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

### `flip(m, axis=None)` Fonksiyonu

`m` parametresine argüman olarak girilen array'i ters çevirir.
```py
import numpy as np

A = np.arange(1,10)
B = np.arange(11,20).reshape(3,3)

print(A) # Output: [1 2 3 4 5 6 7 8 9]
print(B) # Output: [[11 12 13]
#                   [14 15 16]
#                   [17 18 19]]

print(np.flip(A)) # Output: [9 8 7 6 5 4 3 2 1]
print(np.flip(B)) # Output: [[19 18 17]
#                            [16 15 14]
#                            [13 12 11]]
```

### `unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)` Fonksiyonu

`ar` parametresine argüman olarak girilen array'in her elementinden 1 tane bulunduğu (tekrar edenler dahil) ve bunların küçükten büyüğe doğru sıralı olduğu bir array döndürür. Örnek:
```py
import numpy as np

A = np.array([1,1,2,4,6,6,3,1,7,5,3,3,1,6,7,8,4,4])
print(np.unique(A)) # Output: [1 2 3 4 5 6 7 8]
```

### `ndenumerate(arr)` Fonksiyonu

`arr` parametresine argüman olarak girilen array'in elementlerini numaralandırır. Normal `enumerate` fonksiyonundan farkı, matrix'lerde tam index'i gösterir. Örnek:
```py
import numpy as np

A = np.arange(1,6)
for i in np.ndenumerate(A):
    print(i) # Output:
# ((0,), 1)
# ((1,), 2)
# ((2,), 3)
# ((3,), 4)
# ((4,), 5)

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
for i in np.ndenumerate(A):
    print(i) # Output:
# ((0, 0), 1)
# ((0, 1), 2)
# ((0, 2), 3)
# ((1, 0), 4)
# ((1, 1), 5)
# ((1, 2), 6)
# ((2, 0), 7)
# ((2, 1), 8)
# ((2, 2), 9)
```

### `where(condition, x=None, y=None)` Fonksiyonu

`y` parametresine argüman olarak girilen array'in elementleri arasında `condition` parametresinde belirtilen koşulu sağlayan veya `bool` type elementlere sahip array ile uyumlu olanları `x` parametresine argüman olarak girilen data ile değiştirdiği bir array döndürür. Örnek:

```py
import numpy as np

A = np.arange(1,26).reshape(5,5)
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

B = np.where(A%2==0, 99, A)
print(A) # Output: [[ 1  2  3  4  5]
#                   [ 6  7  8  9 10]
#                   [11 12 13 14 15]
#                   [16 17 18 19 20]
#                   [21 22 23 24 25]]

print(B) # Output: [[ 1 99  3 99  5]
#                   [99  7 99  9 99]
#                   [11 99 13 99 15]
#                   [99 17 99 19 99]
#                   [21 99 23 99 25]]
```

**Not:** `condition` parametresinde argüman olarak `bool` type elementlere sahip bir array girilirse, sağlayanları (yani `True` elementleri) referans alarak sağlayanların (yani `True` elementlerin) index'lerini içeren array objesini içeren shape like tuple döndürür. Örnek:
```py
import numpy as np

A = np.array([1, 2, np.nan, 1, 2, np.nan, 1, 2, np.nan])
print(np.isnan(A))
print(np.where(np.isnan(A))) # Output: (array([2, 5, 8], dtype=int64),)

A = np.array([[1,2,np.nan],[1,2,np.nan]])
print(np.where(np.isnan(A))) # Output: (array([0, 1], dtype=int64), array([2, 2], dtype=int64))
```
`(array([2, 5, 8], dtype=int64),)` output'u bize tek boyutlu bu array'in ikinci, beşinci ve sekizinci index'lerinde `nan` olduğunu; `(array([0, 1], dtype=int64), array([2, 2], dtype=int64))` output'u bize iki boyutlu bu array'in (0,2) ve (1,2) index'lerinde `nan` olduğunu söylüyor.

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
Matematikte `-1` sayısının kökünü almak için complex sayılarla uğraşmanız gerekmektedir. Burada da aynısı geçerli. `-1` sayısının kökünü aldıktan sonra sonucu `float64` type'ında ifade edemezsiniz. Bu yüzden `-1` sayısının karekökünün olması gereken yerde `nan` ('not a number') var. Ama `dtype` parametresine argüman olarak `np.complex128` girerseniz, karekök alma işlemi hata yükseltilmeden gerçekleşir.

**Not:** Numpy'da 'sayı olmayan' anlamına gelen 'not a number' objeleri `numpy.nan`, 'sonsuz' anlamına gelen 'infinity' objeleri `numpy.inf` kullanarak kolayca elde edebiliriz.

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

### `amin(a, axis=None, out=None, keepdims=False, initial=<no value>, where=True)` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin en küçüğünü döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(np.amin(A)) # Output: 1
print(np.amin(A, axis=0)) # Output: [1 2 3]
print(np.amin(A, axis=1)) # Output: [1 4 7]
```

**Not:** `np.min()` olarak da kullanılabilir. `np.min()`, `np.amin()` için sadece bir alias'dır (takma ad).

**Not:** Method olarak kullanılmak istenirse `min` şeklinde kullanılmalıdır.
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

### `amax((a, axis=None, out=None, keepdims=False, initial=<no value>, where=True))` Fonksiyonu

`a` parametresine argüman olarak girilen array'in elementlerinin en büyüğünü döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(np.amax(A)) # Output: 9
print(np.amax(A, axis=0)) # Output: [7 8 9]
print(np.amax(A, axis=1)) # Output: [3 6 9]
```

**Not:** `np.amax()` olarak da kullanılabilir. `np.max()`, `np.amax()` için sadece bir alias'dır (takma ad).

**Not:** Method olarak kullanılmak istenirse `max` şeklinde kullanılmalıdır.
```py
import numpy as np

A = np.arange(1,10).reshape(3,3)
print(A) # Output: [[1 2 3]
#                   [4 5 6]
#                   [7 8 9]]
print(A.max()) # Output: 9
print(A.max(axis=0)) # Output: [7 8 9]
print(A.max(axis=1)) # Output: [3 6 9]
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

### `floor(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])` Fonksiyonu

`x` parametresine argüman olarak girilen array'in elementlerinin integer kısmını içeren, float type bir array döndürür. Örnek:
```py
import numpy as np

A = np.random.uniform(1.5,5.85,size=3)
print(A) # Output: [5.62692784 5.6615254  3.05950935]
print(np.floor(A)) # Output: [5. 5. 3.]
```

### `trunc(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])` Fonksiyonu

`x` parametresine argüman olarak girilen array'in elementlerinin decimal kısmını içeren, float type bir array döndürür. `floor` fonksiyonu ile aynı sonucu veriyor olarak görünse de, farklı amaçlar için kullanılır. Örnek:
```py
import numpy as np

A = np.random.uniform(1.5,5.85,size=3)
print(A) # Output: [5.62692784 5.6615254  3.05950935]
print(np.trunc(A)) # Output: [5. 5. 3.]
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

### `cumsum(a, axis=None, dtype=None, out=None)` Fonksiyonu

`a` parametresine argüman olarak girilen array like objenin element'lerini cumulative olarak topladığı bir array döndürür (ne demek istediğimi anlamadıysanız örneğe bakın). Örnek:
```py
import numpy as np

A = np.arange(1,6)
print(A) # Output: [1 2 3 4 5]
print(np.cumsum(A)) # Output: [ 1  3  6 10 15] ([ 1 1+2 1+2+3 1+2+3+4 1+2+3+4+5 ])
```

### `dot(a, b, out=None)` Fonksiyonu

`a` ve `b` parametrelerine argüman olarak girilen array'lerin noktasal çarpımlarını (Dot product) döndürür. Örnek:
```py
import numpy as np

A = np.arange(1,6)
B = np.arange(6,11)
print(np.dot(A,B)) # Output: 130
print(A@B) # Output: 130
print(sum(np.multiply(A,B))) # Output: 130
```

**Not:** Yukarıda gördüğünüz gibi `dot` fonksiyonu yerine `@` operator'ını ya da `sum(np.multiply(A))` fonksiyonlarını kullanabilirsiniz.

### `inner(a, b)` Fonksiyonu

**Burada Kaldın** En son gruba bunun ne olduğunu ve `dot`'dan ne farkı olduğunu sormuştun.

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

### `random.randn(d0, d1, ..., dn)` Fonksiyonu

Bilgi için [tıklayınız](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html?highlight=randn#numpy-random-randn "https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html?highlight=randn#numpy-random-randn").

### `var(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>, *, where=<no value>)` Fonksiyonu

Varyans (variance) hesaplamak için kullanılır. Bilgi için [tıklayınız](https://numpy.org/doc/stable/reference/generated/numpy.var.html?highlight=var#numpy.var "https://numpy.org/doc/stable/reference/generated/numpy.var.html?highlight=var#numpy.var").

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

### `isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])` Fonksiyonu

`x` parametresine girilen array'in elementlerin arasında `nan` type data'nın olduğu index'lerin `True` diğer index'lerin `False` olduğu bir array döndürür. Örnek:
```py
import numpy as np

A = np.array([1, 2, np.nan, 1, 2, np.nan, 1, 2, np.nan])
print(np.isnan(A)) # Output: [False False  True False False  True False False  True]
```

### `isinf(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])` Fonksiyonu

`x` parametresine girilen array'in elementlerin arasında `inf` type data'nın olduğu index'lerin `True` diğer index'lerin `False` olduğu bir array döndürür. Örnek:
```py
import numpy as np

A = np.array([1, 2, np.nan, 1, 2, np.nan, 1, 2, np.nan])
print(np.isinf(A)) # Output: [False False  True False False  True False False  True]
```