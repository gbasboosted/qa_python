import pytest


class TestBooksCollector:

    @pytest.mark.parametrize(
        'name, should_be_added',
        [
            ('К', True),
            ('К' * 40, True),
            ('', False),
            ('К' * 41, False),
        ],
    )
    def test_add_new_book_name_length_validation(
        self,
        collector,
        name,
        should_be_added,
    ):
        collector.add_new_book(name)
        assert (name in collector.books_genre) is should_be_added

    def test_add_new_book_does_not_add_duplicate(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert list(collector.books_genre) == ['Дюна']

    @pytest.mark.parametrize(
        'name, genre, expected_genre',
        [
            ('Книга', 'Фантастика', 'Фантастика'),
            ('Книга', 'Ужасы', 'Ужасы'),
            ('Книга', 'Детективы', 'Детективы'),
            ('Книга', 'Мультфильмы', 'Мультфильмы'),
            ('Книга', 'Комедии', 'Комедии'),
            ('Неизвестная книга', 'Фантастика', ''),
            ('Книга', 'Приключения', ''),
        ],
    )
    def test_set_book_genre_sets_available_genre_only(
        self,
        collector,
        name,
        genre,
        expected_genre,
    ):
        collector.add_new_book('Книга')
        collector.set_book_genre(name, genre)
        assert collector.books_genre['Книга'] == expected_genre

    @pytest.mark.parametrize(
        'name, expected_genre',
        [
            ('Дюна', 'Фантастика'),
            ('Неизвестная книга', None),
        ],
    )
    def test_get_book_genre_returns_genre_by_name(
        self,
        collector,
        name,
        expected_genre,
    ):
        collector.books_genre['Дюна'] = 'Фантастика'
        assert collector.get_book_genre(name) == expected_genre

    def test_get_books_with_specific_genre_returns_only_matching_books(
        self,
        collector,
    ):
        for name, genre in (
            ('Дюна', 'Фантастика'),
            ('Солярис', 'Фантастика'),
            ('Оно', 'Ужасы'),
        ):
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre('Фантастика') == [
            'Дюна',
            'Солярис',
        ]

    def test_get_books_genre_returns_added_book_without_genre(self, collector):
        collector.add_new_book('Дюна')
        assert collector.get_books_genre() == {'Дюна': ''}

    def test_get_books_for_children_excludes_age_rated_genres(self, collector):
        for name, genre in (
            ('Малыш и Карлсон', 'Мультфильмы'),
            ('Оно', 'Ужасы'),
            ('Шерлок Холмс', 'Детективы'),
            ('Дюна', 'Фантастика'),
        ):
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == ['Малыш и Карлсон', 'Дюна']

    def test_add_book_in_favorites_adds_existing_book_only_once(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Неизвестная книга')
        assert collector.favorites == ['Дюна']

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in collector.favorites

    def test_get_list_of_favorites_books_returns_favorites(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Солярис')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Солярис')
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Солярис']
