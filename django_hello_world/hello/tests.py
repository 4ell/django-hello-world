from django.test import TestCase

from json import loads
from models import Person, ReqData
from datetime import date, datetime


class HttpTest(TestCase):
    def test_index(self):
        params = ['name', 'last_name', 'birthday', 'email',
                  'jabber', 'skype', 'bio', 'contacts']

        Person.objects.create(
            name='Steve',
            last_name='Jobs',
            birthday=date(1955, 2, 24),
            email='steve@apple.com',
            jabber='steve@apple.im',
            skype='steve_jobs',
            bio='Some information',
            contacts='Some information'
        )

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('person' in response.context)
        for param in params:
            self.assertTrue(hasattr(response.context['person'], param))
        self.assertContains(response, '42 Coffee Cups Test Assignment')


class MiddlewareTest(TestCase):
    def test_create_obj(self):
        ReqData.objects.create(
            time=datetime.now(),
            path='/',
            get='{}',
            post='{}',
            cookies='{}'
        )

    def test_do_requests(self):
        for i in range(5):
            self.client.get('/?{0}={1}'.format(i, i**2))

        self.client.login()

        for i in range(5):
            self.client.post('/', {i: i**2})

        response = self.client.get('/requests/')

        templ = '{0}: {{&quot;{1}&quot;: &quot;{2}&quot;}}'
        for i in range(5):
            data = templ.format('Post', i, i**2)
            self.assertContains(response, data)

        for i in range(1, 5):
            data = templ.format('Get', i, i**2)
            self.assertContains(response, data)

        self.assertContains(response, 'Path: /requests/')


    def test_views_requests(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'requests')

    def test_views_requests(self):
        response = self.client.get('/requests/')
        self.assertEqual(response.status_code, 200)
