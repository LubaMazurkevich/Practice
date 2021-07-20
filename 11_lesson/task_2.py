

class Media:
    def __init__(self,objname,objcount,objgenre,objtopic):
        self.name=objname
        self.count=objcount
        self.genre=objgenre
        self.topic=objtopic

    def finish_m(self):
        print("Медиа закрыта")

    def type_m(self):
        print("Тип медиа-s")

    def listen(self):
        print("Слушать медиа")

    def read(self):
        print("Читать медиа")

    def watch(self):
        print("Смотреть медиа")

    def __str__(self):
        return f"Название книги :{self.name} \nКоличество страниц: {self.count} \
        \nЖанр книги : {self.genre}\nТема книги: {self.topic}\n"


First_book=Media("Лукоморье", 280, "Фантастика", "Зачем?")
Second_book=Media("Глаз", 200, "Хоррор", "Глаза")
print(First_book)
print(Second_book)

First_book.finish_m()
First_book.type_m()
First_book.finish_m()
Second_book.listen()
Second_book.read()
Second_book.watch()


class Book(Media):
    def __init__(self, objname, objcount, objgenre, objtopic):
        super().__init__(objname, objcount, objgenre, objtopic)

    def reading(self):
        print("Книга читается ")

    def open(self):
        print("Книга открыта")

    def finish(self):
        print("Книга закрыта")

    def open_page(self):
        print("Открыто содержание книги")

    def see_at_book(self):
        print("Cмотреть на книгу")

    def search_word_in_book(self):
        print("Вы ищете слово в книге")


print("///")
third_book = Book("Крестный отец",400,"Криминальный фильм","Мафия")
print(third_book)
third_book.reading()
third_book.open()
third_book.open_page()
third_book.search_word_in_book()
third_book.see_at_book()