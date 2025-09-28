from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
from urllib3 import request


# Create your tests here.
class HomePageTest(TestCase):
    '''тест домашней страницы'''
    def test_root_url_resolves_to_home_page_view(self):
        '''тест: корневой url преобразуется в представление домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''тест: домашняя страница возвращает корректный html'''
        # создаём объект HttpRequest
        request = HttpRequest()
        # передаём его представлению home_page, которое даёт отклик
        response = home_page(request)
        # извлекаем содержимое .content отклика, конвертируя их в html кодировки utf8 при помощи .decode
        html = response.content.decode('utf8')
        # Проверка, что полученная html-строка начинается с тэга <html>
        self.assertTrue(html.startswith('<html>'))
        # Проверяем правильность содержимого <title>
        self.assertIn('<title>To-Do lists</title>', html)
        # Проверка, что полученная html-строка заканчивается тэгом </html>
        self.assertTrue(html.endswith('</html>'))