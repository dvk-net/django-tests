from django.test import TestCase
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import ForTesting

User = get_user_model()


class RecentTest(TestCase):
    
    def setUp(self):
        self.test_author = ForTesting.objects.create(name="test_name", description="test desc")
        self.now =  timezone.now()


    def test_create_obj_has_pub_date(self):
        self.assertIsNotNone(self.test_author.pub_date)
    
    def test_recent_older_30(self):
        delta = timedelta(days=31)
        pub_date = self.now - delta
        self.test_author.pub_date = pub_date
        self.test_author.save()
        self.assertTrue(not self.test_author.recent())


    def test_recent_younger_30(self):
        delta = timedelta(days=25)
        now = timezone.now()
        pub_date = now - delta
        post = ForTesting.objects.create(name="test_name", description="test desc")
        post.pub_date = pub_date
        post.save()
        post.pub_date = pub_date

        self.assertTrue(post.recent())




class ViewTest(TestCase):

    def test_dummy(self):
        response = self.client.get(reverse('dummy'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])
    
    def test_dummy_no_auth(self):
        response = self.client.get(reverse('dummy-auth'))
        self.assertEqual(response.status_code, 302)

    def test_dummy_auth(self):
        user = User.objects.create_user(username="dummy", password="dummy")
        self.client.login(username="dummy", password="dummy")
        response = self.client.get(reverse('dummy-auth'))
        self.assertEqual(response.status_code, 200)
    
    def test_dummy_create_form(self):
        user = User.objects.create_user(username="dummy", password="dummy")
        self.client.login(username="dummy", password="dummy")
        response = self.client.post(
            reverse('dummy-auth'),
            data={
                'name': 'from test_case',
                'description': 'from test_description'
            }
        )
        self.assertEqual(response.status_code, 302)
        count = ForTesting.objects.count()
        obj = ForTesting.objects.first()
        self.assertEqual(count, 1)
        self.assertEqual(obj.name, 'from test_case')
        self.assertEqual(obj.description, 'from test_description')

    def test_dummy_update_form(self):
        user = User.objects.create_user(username="dummy", password="dummy")
        self.client.login(username="dummy", password="dummy")
        obj = ForTesting.objects.create(name="test", description="test")

        response = self.client.post(
            reverse('dummy-update-auth', kwargs={'pk': obj.pk}),
            data={
                'name': 'new data',
                'description': 'new data'
            }
        )
        self.assertEqual(response.status_code, 302)
        count = ForTesting.objects.count()
        obj = ForTesting.objects.first()
        self.assertEqual(count, 1)
        self.assertEqual(obj.name, 'new data')
        self.assertEqual(obj.description, 'new data')



