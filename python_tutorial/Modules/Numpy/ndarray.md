# NDArray (N-Dimensional Array)

Numpy kütüphanesinin temel veri yapısı (basic data structure) array'lerdir. NDArray, 'N-Dimensional Array' yani 'Çok Boyutlu Dizin' anlamına gelmektedir. NDArray'ler normal Python dizinlerinden (`list` vs.) daha hızlı çalışır. NDArray'ler aynı type data'ları tutabilirler. Bir NDArray oluştururken farklı type data'lar tanımlamaya kalkarsanız Numpy upcasting (daha sonra anlatılacak) yaparak bütün data'ları aynı type'a dönüştürür. NDArrayler tek veya çok boyutlu olabilir. Burada **Eksen** ve **Boyut** kavramları devreye giriyor.
- **Eksen:** NDArray'ler çok eksenli olabilir. Sahip olduğu eksene göre boyutu değişkenlik gösterir. Örneğin 1 eksenli ise 1D (bir boyutlu), 5 eksenli ise 5D (5 boyutlu) denir.
- **Boyut:** Matrixler çok boyutlu olabilir. Sadece bir satırdan (sütunlardan) (X) oluşanlarına 1D (bir boyutlu), sütun ve satırlardan (X ve Y, column ve row) oluşanlarına 2D (iki boyutlu) veya matrix, birden fazla matrix'den (Z) oluşanlarına da 3D (üç boyutlu, Z, Y, X) denir ve böyle devam eder.

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