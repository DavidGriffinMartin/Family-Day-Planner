from django.forms import ModelForm
from .models import Date


class DateForm(ModelForm):
    class Meta:
        model = Date
        fields =['date']