import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()


    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже

    @pytest.mark.parametrize('name', [
        'A',
        'Название книги из сорока символов',
        'Название книги из двадцати символов'
    ])
    def test_add_new_book_valid_name(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()
        
    def test_add_new_book_has_no_genre(self, collector): 
        collector.add_new_book('Гордость и предубеждение')
        assert collector.get_book_genre('Гордость и предубеждение') == ""

    def test_set_book_genre_valid(self,collector):
        collector.add_new_book('Нейромант') 
        collector.set_book_genre('Нейромант', 'Фантастика') 
        assert collector.get_book_genre('Нейромант') == 'Фантастика'

    def test_books_for_children_valid__genre_added(self, collector):
        collector.add_new_book('Золушка') 
        collector.set_book_genre('Золушка', 'Мультфильмы')  
        assert 'Золушка' in collector.get_books_for_children()

    def test_get_books_for_children_excludes_horror(self, collector):
        collector.add_new_book('Астрал')
        collector.set_book_genre('Астрал', 'Ужасы') 
        assert 'Астрал' not in collector.get_books_for_children()  

        # проверка получения списка книг по жанру
    def test_get_books_with_specific_genre_returns_correct_list(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert 'Гарри Поттер' in collector.get_books_with_specific_genre('Фантастика')
    
        # проверка получения словаря книг
    def test_get_books_genre_retuns_dict(self, collector):
        collector.add_new_book('Гарри Поттер') 
        assert isinstance(collector.get_books_genre(), dict)  
        assert 'Гарри Поттер' in collector.get_books_genre() 

    def test_add_book_in_favorites_added(self, collector):
        collector.add_new_book('Униженные и оскорблённые') 
        collector.add_book_in_favorites('Униженные и оскорблённые')
        assert 'Униженные и оскорблённые' in collector.get_list_of_favorites_books() 

    def test_delete_book_favorites_deleted(self, collector):
        collector.add_new_book('Униженные и оскорблённые')
        collector.add_book_in_favorites('Униженные и оскорблённые')
        collector.delete_book_from_favorites('Униженные и оскорблённые')
        assert 'Униженные и оскорблённые' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_double_not_added(self, collector):
        collector.add_new_book('Униженные и оскорблённые') 
        collector.add_book_in_favorites('Униженные и оскорблённые') 
        collector.add_book_in_favorites('Униженные и оскорблённые')  
        assert collector.get_list_of_favorites_books().count('Униженные и оскорблённые') == 1