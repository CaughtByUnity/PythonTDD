from django.test import TestCase

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        '''тест: домашняя страница возвращает корректный html'''
        # передаём в self.client.get адрес, который хотим протестировать
        response = self.client.get('/')
        # извлекаем содержимое .content отклика, конвертируя их в html кодировки utf8 при помощи .decode
        html = response.content.decode('utf8')
        # Проверка, что полученная html-строка начинается с тэга <html>
        self.assertTrue(html.startswith('<html>'))
        # Проверяем правильность содержимого <title>
        self.assertIn('<title>To-Do lists</title>', html)
        # Проверка, что полученная html-строка заканчивается тэгом </html>
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(response, 'home.html')