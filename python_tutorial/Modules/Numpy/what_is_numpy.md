# İçindekiler

- [NumPy Nedir](#1)
- [Numpy Installing ve Importing](#2)

<h1>NumPy Nedir?</h1>

Numerical Python'un kısaltması olan NumPy, multidimensional array objeleri üretmek ve bunlar üzerinde mathematical ve logical işlemler yapmak için çeşitli yöntemler sunan, science ve engineering alanlarında sıkça kullanılan open source library'dir.

Numerical data'lar ile çalışmak için evrensel bir standarttır. Kendi başına bir işe yaramaz ama Pandas, SciPy, Matplotlib, scikit-learn, scikit-image ve diğer birçok data science ve scientific gibi birçok Python paketinde; veri manipülasyonu, veri bilimi, yapay zeka gibi birçok alanda kullanılmaktadır.

Multidimensional array ve matrix data structure'ları içerir. n-dimensional array object olan `ndarray` ve methodlar barındırır. `ndarray`'ler hem vector'leri (1D array) hem matrix'leri (2D array) hem de tensor'leri (+3D array) temsil etmek için kullanılır.

[**vectorization**](https://stackoverflow.com/a/1422181/15170972 "https://stackoverflow.com/a/1422181/15170972")'ı desteklediği ve Python listelerinden farklı olarak homojen bir yapıya sahip olduğu için daha hızlıdır, compact'tır, daha az bellek tüketir, daha optimize ve verimlidir. Örnek:
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

<h1 id="2">Numpy Installing ve Importing</h1>

Windows ve `pip` kullanıyorsanız CMD'ye `pip install numpy` yazarak Numpy yükleyebilirsiniz.

Python programınızıda Numpy'ı kullanmak için önce import etmelisiniz:
```py
import numpy as np
```
Sürekli numpy yazmak yerine np kullanmak daha pratik olduğu için böyle tercih etmeniz sizin yararınıza olur.