from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django_hello_world.hello.views.bio', name='bio'),
    # url(r'^django_hello_world/', include('django_hello_world.foo.urls')),
    url(r'^edit/', 'django_hello_world.hello.views.edit', name='edit'),

    url(r'^requests/', 'django_hello_world.hello.views.requests', name='requests'),

    url(r'^login/', 'django.contrib.auth.views.login', {
        'template_name': 'hello/login.html', 
        'extra_context': {'next': '/'}
    }),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
