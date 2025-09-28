from django.test import TestCase

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        '''тест: используется домашний шаблон'''
        # передаём в self.client.get адрес, который хотим протестировать
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_saave_a_POST_request(self):
        '''тест: можно сохранить post-запрос'''
        # Вызываем self.client.post для выполнения post-запроса
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')