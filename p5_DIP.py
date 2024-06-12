# Принцип инверсии зависимости (DIP, Dependency Inversion Principle)
# Модули высокого уровня не должны зависеть от модулей низкого уровня. Оба типа модулей должны зависеть от абстракций.
# Абстракции не должны зависеть от деталей; детали должны зависеть от абстракций. Это позволяет разрабатывать систему более гибкой
# и способствует её лёгкому тестированию.

# 1. Код не использующий этот принцип
# class Book():
#     def read(self):
#         print("Чтение")
# class StoryReader():
#     def __init__(self):
#         self.book = Book()
#     def tell_story(self):
#         self.book.read()
# sr = StoryReader()
# sr.tell_story()

#2. Исправленный код
from abc import ABC, abstractmethod
class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Чтение историю")

class AudioBook(StorySource):
    def get_story(self):
        print("Слушаю историю")

class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

book = Book()
audiobook = AudioBook()
book_reader = StoryReader(book)
audiobook_listener = StoryReader(audiobook)
book_reader.tell_story()
audiobook_listener.tell_story()