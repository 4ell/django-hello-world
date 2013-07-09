from django.test import TestCase
from django.test.client import RequestFactory

from django.template import RequestContext

from json import loads
from models import Person, ReqData
from datetime import date, datetime
import PIL


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


class ContextProcessorTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_settings(self):
        from django.conf import settings
        from context_processors import add_settings

        request = self.factory.get('/')
        context = RequestContext(request, {}, processors=[add_settings])

        self.assertTrue('settings' in context)
        self.assertEqual(settings, context['settings'])


class EditFormTest(TestCase):
    def setUp(self):
        from django.core.files import File
        from django.core.files.uploadedfile import SimpleUploadedFile

        self.image = open('django_hello_world/media/example/grey_day.jpg')
        self.image2 = open('django_hello_world/media/example/grey_day.jpg')
        self.form_data = {
            'name': 'Steve',
            'last_name': 'Jobs',
            'birthday': date(1955, 2, 24),
            'email': 'steve@apple.com',
            'jabber': 'steve@apple.im',
            'skype': 'steve_jobs',
            'bio': 'Some information',
            'contacts': 'Some information',
            'photo': File(self.image2)
        }

        name = self.image.name
        data = self.image.read()
        self.post_dict = {
            'photo': SimpleUploadedFile(name, data)
        }

    def test_form_simple(self):
        from forms import PersonForm

        form = PersonForm(self.form_data, self.post_dict)
        self.assertTrue(form.is_valid())

    def test_login_http(self):
        response = self.client.post("/login/")
        self.assertEqual(response.status_code, 200)

        response = self.client.post("/edit/")
        self.assertEqual(response.status_code, 302)

    def test_form_http(self):
        login = self.client.login(username='admin', password='admin')
        self.assertTrue(login)

        response = self.client.get("/edit/")
        self.assertEqual(response.status_code, 200)

        response = self.client.post("/edit/", self.form_data)
        self.assertEqual(response.status_code, 302)
