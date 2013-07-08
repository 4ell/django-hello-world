from annoying.decorators import render_to
from django.contrib.auth.models import User

from models import Person


@render_to('hello/bio.html')
def bio(request):
    try:
        person = Person.objects.latest('id')
    except:
        person = None
    return {'person': person}


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()
    return {'users': users}
