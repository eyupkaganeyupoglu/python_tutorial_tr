Paketler konusu için [Yazbel](https://python-istihza.yazbel.com/paketler.html) gayet yeterli bir kaynaktır. Buna ek olarak:
- Windows için bütün modül ve paketleri upgrade (güncelleme de denebilir) etmek için PowerShell'i açın ve şu kodu yazın:
    ```
    pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
    ```
- Windows için `pip`'i upgrade (güncelleme de denebilir) etmek için PowerShell'i açın ve şu kodu yazın:
    ```
    python -m pip install --upgrade pip
    ```