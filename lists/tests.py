from django.test import TestCase

from lists.views import home_page
from lists.models import Item

# Create your tests here.
class HomePageTest(TestCase):
    def test_uses_home_template(self):
        '''тест: используется домашний шаблон'''
        # передаём в self.client.get адрес, который хотим протестировать
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_only_saves_items_when_necessary(self):
        '''тест: сохраняет элементы, только когда это нужно'''
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    # Код с душком: тест пост-запроса слишком длинный?
    def test_can_save_a_POST_request(self):
        '''тест: можно сохранить post-запрос'''
        # Вызываем self.client.post для выполнения post-запроса
        self.client.post('/', data={'item_text': 'A new list item'})
        # Один новый объект Item был сохранён в базе данных .objects.count()
        self.assertEqual(Item.objects.count(), 1)
        # objects.first() - то же самое, что и objects.all()[0]
        new_item = Item.objects.first()
        # текст элемента правильный
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        '''тест: переадресует после POST-запроса'''
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_displays_all_list_items(self):
        '''тест: отображаются все элементы списка'''
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

class ItemModelTest(TestCase):
    '''тест модели элемента списка'''
    def saving_and_retrieving_items(self):
        '''тест сохранения и получения элементов списка'''
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')