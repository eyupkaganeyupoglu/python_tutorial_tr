# xxx

Qt için ana modüller:
- QtWidgets
- QtGui
- QtCore

Her PyQt programı 2 nesne üzerine kuruludur. Bunlar:
- `QApplication`, direkt application'ı başlatan modüldür. Her application'da kullanılması zorunludur. Event handling ve Inıtiliasation işlemlerini yapar.
- `QWidget`(MainWindow), Graphical elementleri ve Logic işlemleri ekleyip yönettiğiniz boş bir kap (container) işlevi görür. Her application'da en az bir tane kullanılması zorunludur. MainWindows class'ı bu class'dan miras alır. Örnek:
    ```py
    import PyQt5.QtWidgets as qtw

    class MainWindow(qtw.QWidget):
        def __init__(self):
            super().__init__()
            
            self.show()
            
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()
    ```
`QWidgets`, window'a koyabileceğiniz bütün widget'leri barındıran modüldür. Window'u göstermek için `.window.show`, ekranda tutmak için de `.app.exec()` kullanılır. 

