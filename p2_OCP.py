# Принцип открытости/закрытости (OCP, Open/Closed Principle)
# Программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации.
# Суть в том, что уже существующий код не должен модифиироваться при добавлении новых функций.
# Это достигается за счёт использования абстракций и интерфейсов.

# 1. Код не использующий этот принцип
# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def doc_print(self):
#         print(f"Отчет: {self.title}: {self.content}")

#2. Исправленный код
from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass


class TextFormatted(Formatted):
    def format(self, report):
        print(report.title)
        print(report.content)

class HtmlFormatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.title}</h1>")
        print(f"<p>{report.content}</p>")

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

    def doc_print(self):
        self.formatted.format(self)

report1 = Report('Заголовок отчета', 'Это текст отчета, его тут много', TextFormatted())
report2 = Report('Заголовок отчета', 'Это текст отчета, его тут много', HtmlFormatted())
report1.doc_print()
report2.doc_print()

