# İçindekiler

- [Python Buffer Protocol](#1)
- [Bellek Görüntüsü (Memoryview)](#2)
    - [Memoryview Methodları](#2.1)
        - [`cast(format, shape)` Methodu](#2.1.1).1.1)
        - [`contiguous` Methodu](#2.1.2)
        - [`c_contiguous` Methodu](#2.1.2.1)
        - [`f_contiguous` Methodu](#2.1.2.2)
        - [`format` Methodu](#2.1.3)
        - [`hex(sep, bytes_per_sep)` Methodu](#2.1.4)
        - [`itemsize` Methodu](#2.1.5)
        - [`nbytes` Methodu](#2.1.6)
        - [`ndim` Methodu](#2.1.7)
        - [`obj` Methodu](#2.1.8)
        - [`readonly` Methodu](#2.1.9)
        - [`release()` Methodu](#2.1.10)
        - [`shape` Methodu](#2.1.11)
        - [`strides` Methodu](#2.1.12)
        - [`suboffsets` Methodu](#2.1.13)
        - [`tobytes(order=None)` Methodu](#2.1.14).1.14)
        - [`tolist()` Methodu](#2.1.15)
        - [`toreadonly()` Methodu](#2.1.16)

<h1 id="1">Python Buffer Protocol</h1>

Buffer protocol, bir objenin internal data'sına (dahili veri) erişmenin (access) bir yolunu sağlar. Bu internal data bir memory array veya buffer'dır. Buffer protocol, bir objenin internal data'sını (buffer'lar) açığa çıkarmasına (expose) ve diğerlerini intermediate copying olmadan bu buffer'lara erişmesine (access) izin verir. Bu protocol'e yalnızca [C-API](https://docs.python.org/3/c-api/ "https://docs.python.org/3/c-api/") düzeyinde erişilebilir ve normal codebase'i kullanmaz. Bu nedenler aynı protocol'ü normal Python codebase'e maruz bırakmak için (in order to expose) memoryview mevcuttur.

Memoryview, Python'da buffer protocol'ünü ortaya çıkarmanın (expose) güvenli bir yoludur. Memoryview, bir `memoryview` objesi oluşturarak bir objenin internal buffer'larına erişmenizi sağlar.

Buffer protocol ve Memoryview neden önemlidir? Bir obje üzerinde herhangi bir eylem (bir objenin fonksiyonunu çağırmak (call) veya bir array'ı dilimlemek) gerçekleştirdiğimizde, Python'un o objenin bir kopyasını oluşturması gerektiğini hatırlamamız gerekir. Büyük data'larla çalışıyorsanız (örneğin bir image'in binary data'ları), neredeyse hiçbir işe yaramayan büyük data yığınlarının (huge chunks of data) gereksiz yere kopyalarını oluştururuz. Buffer protocol'ünü kullanarak, büyük data'ları kopyalamadan use/modify işlemleri için başka bir objeye erişim verebiliriz. Bu da programın daha hızlı çalışmasını sağlar. Buralar işin teknik kısmı. Şimdi anlayabileceğimiz dilden anlatayım.

Bir array düşünün. Array'e element (item) eklemek için her defasında boyutunu yükseltmeniz gerekir (örneğin 10'luk bir array'e 11. elementi eklemek için boyutunu 11'e yükseltmeniz gerekir). Bu işlemi her defasında baştan tekrar tekrar yapmak sisteme ek iş yükü bindirir. Buffer protocol, bellekten (memory) örneğin 100 elementlik bir buffer alır ve array'e her element eklediğinizde yeniden boyutlandırma işlemi yapmaktan sistemi kurtarır. Bu durum sistemi ek iş yükünden kurtardığı için hız konusunda bir kazanç sağlasa da bellekten (memory) yer çalar (çünkü örneğin 100'lük yer alıp 10 kullanırsanız, 90 yeri boşuna işgal etmiş olursunuz). Bu yüzden buffer kullandırken atanan boyutun tamamını kullanmaya dikkat etmeliyiz. Yani Buffer protocol'ünü kullanırsan, büyük data'larla uğraşırken (use/modify işlemleri yaparken) o büyük data'lar buffer sınırları içerisindeyse, büyük data'ları kopyalarken falan boyut adaptasyonu ile uğraşmana gerek kalmaz.

<h1 id="2">Bellek Görüntüsü (Memoryview)</h1>

`memoryview(object)` fonksiyonu, `object` parametresine argüman olarak girilen objenin bellek görünümü nesnesini (memoryview object) döndürür. `memoryview` fonksiyonu argüman olarak sadece [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object "https://docs.python.org/3/glossary.html#term-bytes-like-object") (`bytes`, `bytearray`) kabul eder. Örnek:
```py
print(memoryview(b'abcefg')) # Output: <memory at 0x000001ACE0B14E80>
```
Daha fazla bilgi için:
- [Memoryview Type](https://docs.python.org/3/library/stdtypes.html#memoryview)
- [Programiz Memoryview Function](https://www.programiz.com/python-programming/methods/built-in/memoryview)

**Not:** Memoryview konusu C-like dilleri alakadar eden bir konudur. Python high level bir dildir. Bu yüzden bellek seviyesinde çalışmak için low level dillere yönelmeniz sizin hayrınıza olur. `memoryview` konusunun bellek seviyesinde çalışmayacakların pek işine yarayacağını düşündüğüm için bu başlığın detaylarına inmeyeceğim. Bellek seviyesinde çalışmak isteyenler seri bir şekilde bu tutorial'ı kapatıp C-like dillere yönelsinler. Buradan sonraki başlıklarda sadece kaynak linki vereceğim, açıklama olmayacak.

<h2 id="2.1">Memoryview Methodları</h2>

<h3 id="2.1.1"><code>cast(format, shape)</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.cast).

<h3 id="2.1.2"><code>contiguous</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.contiguous "https://docs.python.org/3/library/stdtypes.html#memoryview.contiguous").

<h3 id="2.1.2.1"><code>c_contiguous</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.c_contiguous "https://docs.python.org/3/library/stdtypes.html#memoryview.c_contiguous")

<h3 id="2.1.2.2"><code>f_contiguous</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.f_contiguous "https://docs.python.org/3/library/stdtypes.html#memoryview.f_contiguous")

<h3 id="2.1.3"><code>format</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.format "https://docs.python.org/3/library/stdtypes.html#memoryview.format").

<h3 id="2.1.4"><code>hex(sep, bytes_per_sep)</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.hex "https://docs.python.org/3/library/stdtypes.html#memoryview.hex").

<h3 id="2.1.5"><code>itemsize</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.itemsize "https://docs.python.org/3/library/stdtypes.html#memoryview.itemsize").

<h3 id="2.1.6"><code>nbytes</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.nbytes "https://docs.python.org/3/library/stdtypes.html#memoryview.nbytes").

<h3 id="2.1.7"><code>ndim</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.ndim "https://docs.python.org/3/library/stdtypes.html#memoryview.ndim").

<h3 id="2.1.8"><code>obj</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.obj "https://docs.python.org/3/library/stdtypes.html#memoryview.obj").

<h3 id="2.1.9"><code>readonly</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.readonly "https://docs.python.org/3/library/stdtypes.html#memoryview.readonly").

<h3 id="2.1.10"><code>release()</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.release "https://docs.python.org/3/library/stdtypes.html#memoryview.release").

<h3 id="2.1.11"><code>shape</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.shape "https://docs.python.org/3/library/stdtypes.html#memoryview.shape").

<h3 id="2.1.12"><code>strides</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.strides "https://docs.python.org/3/library/stdtypes.html#memoryview.strides").

<h3 id="2.1.13"><code>suboffsets</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.suboffsets "https://docs.python.org/3/library/stdtypes.html#memoryview.suboffsets").

<h3 id="2.1.14"><code>tobytes(order=None)</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.tobytes "https://docs.python.org/3/library/stdtypes.html#memoryview.tobytes").

<h3 id="2.1.15"><code>tolist()</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.tolist "https://docs.python.org/3/library/stdtypes.html#memoryview.tolist").

<h3 id="2.1.16"><code>toreadonly()</code> Methodu</h3>

Bilgi için [tıklayınız](https://docs.python.org/3/library/stdtypes.html#memoryview.toreadonly "https://docs.python.org/3/library/stdtypes.html#memoryview.toreadonly")


