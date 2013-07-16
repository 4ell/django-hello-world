from django.forms import ModelForm, ClearableFileInput
from widgets import JQueryDatepicker
from models import Person, ReqData


class PersonForm(ModelForm):
    class Meta:
        model = Person

        widgets = {
            'birthday': JQueryDatepicker(),
            'photo': ClearableFileInput(attrs={'onchange': 'ui.photo.show()'})
        }


class ReqDataForm(ModelForm):
    class Meta:
        model = ReqData
        fields = ['priority']
