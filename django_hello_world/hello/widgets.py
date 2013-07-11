from django.forms.widgets import DateInput
from django.conf import settings

class JQueryDatepicker(DateInput):
    class Media:
        css = {
            'all': (settings.STATIC_URL + 'css/jquery-ui.min.css',)
        }
        js = (
            settings.STATIC_URL + 'js/jquery-ui.min.js',
            settings.STATIC_URL + 'js/datepicker.js',
        )

    def __init__(self, attrs={}, format=None):
        if 'class' not in attrs:
            attrs['class'] = 'jquery_datepicker'
        else:
            attrs['class'] += ' jquery_datepicker'

        super(JQueryDatepicker, self).__init__(attrs, format)
