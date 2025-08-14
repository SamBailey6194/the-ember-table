from django import forms
from .models import Booking, Table


# Create forms here
class SearchSlotsForm(forms.Form):
    date = forms.CharField()

    def clean_date(self):
        data = self.cleaned_data['date']
        if '/' in data:
            raise forms.ValidationError('Invalid date format')
        return data


class MakeBookingForm(forms.Form):
    date = forms.DateField(input_formats=['%Y-%m-%d'])
    time = forms.TimeField(input_formats=['%H:%M'])
    party_size = forms.IntegerField(min_value=1, max_value=100)
    tables = forms.ModelMultipleChoiceField(queryset=Table.objects.all())
    contact_name = forms.CharField()
    contact_email = forms.EmailField()
    contact_phone = forms.CharField()

    def clean_party_size(self):
        party_size = self.cleaned_data.get('party_size', 0)
        if party_size is None or party_size <= 0 or party_size > 100:
            raise forms.ValidationError('Invalid party size')
        return party_size


class CancelBookingForm(forms.Form):
    reference_code = forms.UUIDField(
        error_messages={'invalid': 'Invalid reference code'}
    )

    def clean_reference_code(self):
        code = self.cleaned_data['reference_code']
        if not Booking.objects.filter(reference_code=code).exists():
            raise forms.ValidationError('Invalid reference code')
        return code
