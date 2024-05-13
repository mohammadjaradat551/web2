from django import forms
from .models import BorrowBook


class BorrowBookForm(forms.ModelForm):
    date_from= forms.DateField(widget= forms.DateInput(attrs= {'id':'checkin_date'}))
    date_to= forms.DateField(widget= forms.DateInput(attrs= {'id':'checkin_date'}))

    class Meta:
        model = BorrowBook
        fields= ['date_from', 'date_to']


        