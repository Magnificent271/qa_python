from tkinter.font import names

from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.mark.parametrize('book_title', [
        'The Lord of the Rings',
        ])

    #Проверка добавления новой книги в словарь books_genre
    def test_add_new_book(self, book_title):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        assert book_title in collector.books_genre

    #Проверка валидации на количество символов в названии книги
    #Количество символов 0 и 42
    @pytest.mark.parametrize('invalid_book_title', [
        'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe',
        ''
    ])

    def test_add_new_book_invalid_length(self, invalid_book_title):
        collector = BooksCollector()
        collector.add_new_book(invalid_book_title)
        assert invalid_book_title not in collector.get_books_genre()

    #Проверка установки жанра книги
    #Позитивный кейс. Жанр есть в списке
    #Негативный кейс. Жанра нет в списке
    @pytest.mark.parametrize('book_title, genre, expected', [
        ('Homo Deus', 'Фантастика', True),
        ('Homo Deus', 'Фонтан', False),
    ])

    def test_set_book_genre_add_genre(self, book_title, genre, expected):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        assert (genre in collector.get_book_genre(book_title)) == expected

    #Негативный кейс. Установка жанра не существующей книге
    def test_set_book_genre_not_book_in_list(self):
        collector = BooksCollector()
        book_title = 'Homo Deus'
        genre = 'Фантастика'
        collector.set_book_genre(book_title, genre)
        assert genre not in collector.get_books_genre()

    #Проверка корректного возвращения жанра для указанной книги
    def test_get_book_genre(self):
        collector = BooksCollector()
        book_title = 'Homo Deus'
        genre = 'Фантастика'
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        assert collector.get_book_genre(book_title) == genre

    #Проверка получения списка книг с определенным жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        book_title_1 = 'Книга1'
        book_title_2 = 'Книга2'
        book_title_3 = 'Книга3'
        genre_1 = 'Ужасы'
        genre_2 = 'Ужасы'
        genre_3 = 'Комедии'
        collector.add_new_book(book_title_1)
        collector.add_new_book(book_title_2)
        collector.add_new_book(book_title_3)
        collector.set_book_genre(book_title_1, genre_1)
        collector.set_book_genre(book_title_2, genre_2)
        collector.set_book_genre(book_title_3, genre_3)
        assert collector.get_books_with_specific_genre(genre_1) == [book_title_1, book_title_2]

    #Проверка возвращения списка книг доступным детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Ужасы')  # Не для детей
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Комедии')  # Подходит для детей
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга3', 'Фантастика')  # Подходит для детей
        collector.add_new_book('Книга4')
        collector.set_book_genre('Книга4', 'Детективы')  # Не для детей
        expected_books = ['Книга2', 'Книга3']
        books_for_children = collector.get_books_for_children()
        assert books_for_children == expected_books

    #Проверка добавления книги в Избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Ужасы')
        collector.add_book_in_favorites('Книга1')
        assert 'Книга1' in collector.favorites

    #Проверка добавления одной и той же книги в Избранное
    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Ужасы')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга1')
        assert len(collector.favorites) == 1

    #Проверка удаления книги из Избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Ужасы')
        collector.add_book_in_favorites('Книга1')
        collector.delete_book_from_favorites('Книга1')
        assert len(collector.favorites) == 0

    #Проверка получения списка Избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга1', 'Ужасы')
        collector.set_book_genre('Книга2', 'Детективы')
        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга2')
        assert 'Книга1' in collector.get_list_of_favorites_books() and 'Книга2' in collector.get_list_of_favorites_books()
