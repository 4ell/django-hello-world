from django.forms import ModelForm, ClearableFileInput
from models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person

        widgets = {
            'photo': ClearableFileInput(attrs={'onchange': 'show_photo()'})
        }
