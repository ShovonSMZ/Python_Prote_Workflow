import datetime
from django import forms
from .models import LeaveRequest

class DateInput(forms.DateInput):
    input_type = 'date'

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['user', 'status']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date < datetime.date.today():
            raise forms.ValidationError("Date can't be in the past.")
        return start_date

    def clean_end_date(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if end_date < datetime.date.today() or end_date < start_date:
            raise forms.ValidationError("Please choose a valid date.")
        return end_date
