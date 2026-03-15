import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name', [
        'A',
        'Название книги из сорока символов',
        'Название книги из двадцати символов'
    ])
    def test_add_ntw_book_valid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre()
        
    def test_add_new_book_has_no_genre(self):
        collector = BooksCollector() 
        collector.add_new_book('Гордость и предубеждение')
        assert collector.get_book_genre('Гордость и предубеждение') == ""

    def test_set_book_genre_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Нейромант') 
        collector.set_book_genre('Нейромант', 'Фантастика') 
        assert collector.get_book_genre('Нейромант') == 'Фантастика' 

    def test_get_books_for_children_excludes_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Астрал')
        collector.set_book_genre('Астрал', 'Ужасы') 
        assert 'Астрал' not in collector.get_books_for_children()  

    def test_add_book_in_favorites_added(self):
        collector = BooksCollector()
        collector.add_new_book('Униженные и оскорблённые') 
        collector.add_book_in_favorites('Униженные и оскорблённые')
        assert 'Униженные и оскорблённые' in collector.get_list_of_favorites_books() 

    def test_delete_book_favorites_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Униженные и оскорблённые')
        collector.add_book_in_favorites('Униженные и оскорблённые')
        collector.delete_book_from_favorites('Униженные и оскорблённые')
        assert 'Униженные и оскорблённые' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_double_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Униженные и оскорблённые') 
        collector.add_book_in_favorites('Униженные и оскорблённые') 
        collector.add_book_in_favorites('Униженные и оскорблённые')  
        assert collector.get_list_of_favorites_books().count('Униженные и оскорблённые') == 1