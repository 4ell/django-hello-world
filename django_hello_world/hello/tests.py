from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse

from django.template import RequestContext

from json import loads
from models import Person, ReqData, Action
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

        response = self.client.get(reverse('bio'))
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

        response = self.client.get(reverse('requests'))

        templ = '{0}: {{&quot;{1}&quot;: &quot;{2}&quot;}}'
        for i in range(5):
            data = templ.format('Post', i, i**2)
            self.assertContains(response, data)

        for i in range(1, 5):
            data = templ.format('Get', i, i**2)
            self.assertContains(response, data)

        self.assertContains(response, 'Path: /requests/')


    def test_views_requests(self):
        response = self.client.get(reverse('bio'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'requests')

    def test_views_requests(self):
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)


class ContextProcessorTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def check_context(self, context):
        from django.conf import settings

        self.assertTrue('settings' in context)
        self.assertEqual(settings, context['settings'])

    def test_add_settings_separatly(self):
        from context_processors import add_settings

        request = self.factory.get('/')
        context = RequestContext(request, {}, processors=[add_settings])

        self.check_context(context)

    def test_add_settings_http(self):
        request = self.client.get(reverse('bio'))
        self.check_context(request.context)


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

        response = self.client.get(reverse('edit'))
        self.assertEqual(response.status_code, 302)

    def test_form_ajax(self):
        response = self.client.post(reverse('save_person'))
        content = loads(response.content)
        self.assertTrue('saved' in content)
        self.assertTrue('errors' in content)
        self.assertEqual(content['saved'], False)

        login = self.client.login(username='admin', password='admin')
        self.assertTrue(login)

        response = self.client.post(reverse('save_person'), {'0': '0'})
        content = loads(response.content)
        self.assertTrue('saved' in content)
        self.assertTrue('errors' in content)
        self.assertEqual(content['saved'], False)

        response = self.client.post(reverse('save_person'), self.form_data)
        content = loads(response.content)
        self.assertTrue('saved' in content)
        self.assertEqual(content['saved'], True)

        items = self.form_data.items()
        person = Person.objects.latest('id')
        for field, value in items:
            attr = getattr(person, field)
            if field == 'photo':
                self.assertEqual(value.size, attr.size)
                continue
            self.assertEqual(attr, value)

        # Editing should not affect number of objects
        self.assertEqual(Person.objects.count(), 1)


class DatepickerTest(TestCase):
    def test_datepicker_silly(self):
        login = self.client.login(username='admin', password='admin')
        self.assertTrue(login)

        response = self.client.post(reverse('edit'))

        self.assertContains(response, 'jquery_datepicker')


class TemplateTagTest(TestCase):
    def render_template(self, template, context={}):
        from django.template import Context, Template
        template = Template(template)
        context = Context(context)
        return template.render(context)

    def test_edit_page(self):
        context = {
            'req': ReqData.objects.latest('time'),
            'person': Person.objects.latest('id')
        }
        rendered = self.render_template(
            '{% load edit_link %}'
            '{% edit_link req %}\n'
            '{% edit_link person %}',
            context
        )
        self.assertEqual(
            rendered, 
            "/admin/hello/reqdata/1/\n"
            "/admin/hello/person/1/"
        )

    def test_index_page(self):
        login = self.client.login(username='admin', password='admin')
        self.assertTrue(login)

        pattern = '<a href="/admin/hello/person/\d+/">.+?</a>'

        response = self.client.get(reverse('bio'))
        self.assertEqual(response.status_code, 200)
        self.assertRegexpMatches(response.content, pattern)


class CommandsTestCase(TestCase):
    def test_models_command(self):
        import os

        fout = os.popen4('make this command="models"')[1]
        result = fout.read()

        self.assertTrue('ReqData' in result)
        self.assertTrue('Person' in result)
        self.assertTrue('Count' in result)


class SignalTestCase(TestCase):
    def test_data_saving(self):
        Person.objects.create(
            name='Steve',
            last_name='JKobs',
            birthday=date(1955, 2, 24),
            email='steve@apple.com',
            jabber='steve@apple.im',
            skype='steve_jobs',
            bio='Some information',
            contacts='Some information'
        )

        person = Person.objects.latest('id')
        person.last_name = 'Jobs'
        person.save()

        person.delete()

        ReqData.objects.create(
            time=datetime.now(),
            path='/', get='{0:0}',
            post='{}', cookies='{}'
        )

        actions = Action.objects.order_by("-time")[:4]
        actions = list(actions)

        models_actions = [
            ['ReqData', 'create'], 
            ['Person', 'delete'], 
            ['Person', 'edit'], 
            ['Person', 'create'], 
        ]

        self.assertEqual(len(actions), 4)

        for index, value in enumerate(models_actions):
            model, action = value
            self.assertEqual(actions[index].model, model)
            self.assertEqual(actions[index].action, action) 
