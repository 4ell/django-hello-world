from django.test import TestCase

from json import dumps, loads
from models import Person, ReqData
from datetime import date, datetime


class HttpTest(TestCase):
    def test_index(self):
        params = ['name', 'last_name', 'birthday', 'email',
                  'jabber', 'skype', 'bio', 'contacts']

        person = Person.objects.create(
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
        self.client.get('/')
        
        for i in range(5):
            self.client.get('/?{0}={1}'.format(i, i**2))
        
        self.client.login('admin', 'admin')

        for i in range(5):
            self.client.post('/', {a:i, b:i**2})

    def test_read_db(self):
        requests = ReqData.objects.all()[-11:]
        for req in requests:
            get = loads(req.get)
            post = loads(req.post)
            for k, v in get.items():
                assertEqual(k**2, v)
            for k, v in post.items():
                assertEqual(k**2, v)