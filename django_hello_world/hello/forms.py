from django.forms import ModelForm, ClearableFileInput
from widgets import JQueryDatepicker
from models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person

        widgets = {
            'birthday': JQueryDatepicker(),
            'photo': ClearableFileInput(attrs={'onchange': 'show_photo()'})
        }
