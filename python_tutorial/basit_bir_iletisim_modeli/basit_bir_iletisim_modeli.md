# Binary Sistem
İkili anlam taşıyan sistemler arasında iletişimi sağlamak için yapılan dönüşümlere **kodlama (encoding)** denir. Bu ikili anlam taşıyan değerler binary sistemde **0** ve **1** olarak ifade edilir.

# 8 bit'lik Sistem
8 bit'in bir araya gelerek oluşturduğu sisteme denir. Bu sistem, binary sayıları kullanarak 0'dan 255'e (0 ve 255 dahil) kadar olan sayılar üretebilir. Dolayısıyla 256 tane farklı sinyal oluşturabilir. Bir ve byte kavramlarını şöyle listeleyebilirim:
- 8 bit'in bir araya gelmesi ile oluşan yapıya: byte
- 1024 byte'ın bir araya gelmesi ile oluşan yapıya: kilobyte
- 1024 kilobyte'ın bir araya gelmesi ile oluşan yapıya: megabyte
- 1024 megabyte'ın bir araya gelmesi ile oluşan yapıya: gigabyte
- 1024 gigabyte'ın bir araya gelmesi ile oluşan yapıya: terabyte
- 1024 terabyte'ın bir araya gelmesi ile oluşan yapıya: petabyte

# Hata Kontrolü
Alıcı ile verici arasında paylaşılan veriler herhangi bir nedenden dolayı bozulabilir. Bunun yaratabileceği sorunlardan kurtulmak için hata kontrol sistemleri geliştirilmiştir. 8 bit'lik hata kontrol mekanizmalarında 7 bit'i kullanıp 8. bit'i hata kontrol mekanizması için ayırırız. Hata kontrol makenizması için kullanılan 8. bit'in çalışma mantığı, sayının çift mi tek mi olduğunu kontrol etmeye dayanır. Sayıdaki birlerin sayısı tekse, sayı tektir; çiftse, sayı çiftir. Örneğin `0110111` sayısında beş tane bir olduğu için bu sayı tektir. Kullanıcının göndermek istediği sayı tekse, gönderilen sayı da tek olmalıdır. Hata kontrol mekanizması bunu denetler.

## Örnek Protokol
Bir sistemde, bütün sayıların tek sayı olarak iletilmesini istiyorsak kullanılacak protokolü şöyle düzenleyebiliriz:
- Eğer karşı tarafa iletilen bir sayı zaten tekse, o sayının başına `0` ekleyeceğiz. Böylece sayının teklik-çiftlik durumu değişmemiş olacak. Ama eğer iletilecek sayı çiftse, o sayının başına `1` ekleyeceğiz. Böylece çift sayıyı, sistemimizin gerektirdiği şekilde, tek sayıya çevirmiş olacağız. Bu kontrol türüne **eşlik denetimi (parity check)** denir. Bu yapmamızı sağlayan bit'e de **eşlik bit'i (parity bit)** denir. `Tek eşlik denetimi (odd parity check)` ve **Çift eşlik denetimi (even parity check)** adlı iki tür eşlik denetimi bulunur.

# Karakterlerin Temsili
`1` ve `0` sinyallerini bir ara getirerek farklı karakterleri temsil etmesini sağlayabiliriz. Örneğin:
<img src="https://i.ibb.co/6XhWqFb/binary-chart.png" alt="binary-chart" border="0">

