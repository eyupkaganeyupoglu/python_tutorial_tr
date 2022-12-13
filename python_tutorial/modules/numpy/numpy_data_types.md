# İçindekiler

- [NumPy'ın Desteklediği Veri Türleri (`dtype`)](#1)

<h1 id="1">NumPy'ın Desteklediği Veri Türleri (<code>dtype</code>)</h1>

Bir `dtype`,
- Data'nın type'ına (integer, float ya da Python object),
- Data'nın size'ına,
- Byte order (little-endian or big-endian),
- Structured type olması durumunda, field'lerin adları (name), her field'ın data type'ı ve her filed tarafından alınan memory block parçasına ()part of memory block),
- Data dype bir subarray ise, shape ve data type'ına

bağlı olarak bir array'e karşılık gelen sabit bellek bloğunun (fixed block of memory) yorumlanmasını (interpretation) açıklar.

**Not:** Byte order'a data type'a prefix olarak `<` ya da `>` eklenerek karar verilir. `<` encoding'in little-endian olduğu anlamına gelir (en önemsizi (least significant) en küçük adreste saklanır). `>` encoding'in big-endian olduğu anlamına gelir (en önemli (most significant) byte en küçük adreste saklanır).

|     Type     | Description                                                                                                         |
| :----------: | :------------------------------------------------------------------------------------------------------------------ |
|   `bool_`    | Byte olarak depolanan boolean (`True` ya da `False`)                                                                |
|    `int_`    | Default integer type (C'deki `long` ile neredeyse aynı (same as), normalde ya `int32` ya da `int64`)                |
|    `intc`    | C'deki `int` ile birebir aynı (identical)(normalde ya `int32` ya da `int64`)                                        |
|    `intp`    | Indexing için kullanılan integer (C'deki `ssize_t` ile neredeyse aynı (same as), normalde ya `int32` ya da `int64`) |
|    `int8`    | Byte (-128 to 127)                                                                                                  |
|   `int16`    | Integer (-32768 to 32767)                                                                                           |
|   `int32`    | Integer (-2147483648 to 2147483647)                                                                                 |
|   `int64`    | Integer (-9223372036854775808 to 9223372036854775807)                                                               |
|   `uint8`    | Unsigned integer (0 to 255)                                                                                         |
|   `uint16`   | Unsigned integer (0 to 65535)                                                                                       |
|   `uint32`   | Unsigned integer (0 to 4294967295)                                                                                  |
|   `uint64`   | Unsigned integer (0 to 18446744073709551615)                                                                        |
|   `float_`   | `float64` için kısaltma (shorthand)                                                                                 |
|  `float16`   | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa                                                   |
|  `float32`   | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa                                                 |
|  `float64`   | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa                                                |
|  `complex_`  | `complex128` için kısaltma (shorthand)                                                                              |
| `complex64`  | İki 32-bit ile temsil edilen complex sayı (real and imaginary components)                                           |
| `complex128` | İki 64-bit ile temsil edilen complex sayı (real and imaginary components)                                           |

Bir `dtype` objesi oluşturmak için `dtype(object, align, copy)` methodu kullanılır.
- **`object`**: Argüman olarak bir data type objesine dönüştürülecek objeyi kabul eder.
- **`align:bool` (optional)**: Bilgi için [tıklayın](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html?highlight=numpy%20dtype#numpy.dtype).
- **`copy:bool` (optional)**: Bilgi için [tıklayın](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html?highlight=numpy%20dtype#numpy.dtype).

`dtype` ile ilgili daha fazla bilgi ve kullanımıyla ilgili örnekler için [tıklayınız](https://numpy.org/doc/stable/reference/generated/numpy.dtype.html?highlight=numpy%20dtype#numpy.dtype).