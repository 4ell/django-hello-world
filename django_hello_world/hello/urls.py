from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'django_hello_world.hello.views.bio', name='bio'),
    
    url(r'^edit/save/', 'django_hello_world.hello.views.save_person', name='save_person'),
    url(r'^edit/', 'django_hello_world.hello.views.edit', name='edit'),

    url(r'^requests/(asc|desc)?/?', 'django_hello_world.hello.views.requests', name='requests'),

    url(r'^login/', 'django.contrib.auth.views.login', {
        'template_name': 'hello/login.html', 
        'extra_context': {'next': '/'}
    }),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
