from annoying.decorators import render_to
from django.contrib.auth.models import User

from models import Person


@render_to('hello/bio.html')
def bio(request):
    person = Person.objects.latest('id')
    return {'person': person}


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()
    return {'users': users}
