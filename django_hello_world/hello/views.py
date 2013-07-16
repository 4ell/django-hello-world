from annoying.decorators import render_to, ajax_request

from models import Person, ReqData
from forms import PersonForm, ReqDataForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@render_to('hello/bio.html')
def bio(request):
    try:
        person = Person.objects.latest('id')
    except:
        person = None
    return {'person': person}


@login_required
@render_to('hello/edit.html')
def edit(request):
    try:
        person = Person.objects.latest('id')
    except:
        person = Person()
    return {
        'form': PersonForm(instance=person)
    }


@ajax_request
def save_person(request):
    if not request.user.is_authenticated():
        return {'saved': False, 'errors': ['Not authenticated']}

    try:
        person = Person.objects.latest('id')
    except:
        person = Person()

    post = request.POST or None
    data = request.FILES or None
    form = PersonForm(post, data, instance=person)

    if form.is_valid():
        form.save()
        return {'saved': True}
    else:
        return {'saved': False, 'errors': form.errors}


@render_to('hello/reqs.html')
def requests(request, order):
    try:
        if order == 'asc':
            requests = ReqData.objects.all().order_by("priority")[:10]
        elif order == 'desc':
            requests = ReqData.objects.all().order_by("-priority")[:10]
        else:
            requests = ReqData.objects.all().order_by("-time")[:10]
    except:
        requests = []
    if request.POST:
        inst = ReqData.objects.get(id=request.POST['id'])
        form = ReqDataForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
    for req in requests:
        req.form = ReqDataForm(instance=req)
    return {'requests': requests}


@render_to('hello/home.html')
def home(request):
    users = User.objects.filter()
    return {'users': users}
