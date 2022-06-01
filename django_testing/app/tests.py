from django.test import TestCase

from app.db_queries import book_list


class QueryTest(TestCase):
    def setUp(self) -> None:
        book_list()

    def test_number_of_query(self):
        return True
