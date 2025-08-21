from django import forms
from .models import Booking


# Create forms here
class MakeBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'date',
            'time',
            'party_size',
        ]
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'input input-bordered w-full mb-2'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'input input-bordered w-full mb-2'
            }),
            'party_size': forms.NumberInput(attrs={
                'class': 'input input-bordered w-full mb-2',
                'min': 1,
                'max': 20
            }),
        }

    def clean_party_size(self):
        party_size = self.cleaned_data.get('party_size')
        if party_size <= 0 or party_size > 100:
            raise forms.ValidationError("Invalid party size")
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


class UpdateBookingForm(forms.ModelForm):
    reference_code = forms.UUIDField(widget=forms.HiddenInput())

    class Meta:
        model = Booking
        fields = ['date', 'time', 'party_size']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date', 'class': 'input input-bordered w-full mb-2'
                }),
            'time': forms.TimeInput(attrs={
                'type': 'time', 'class': 'input input-bordered w-full mb-2'
                }),
            'party_size': forms.NumberInput(attrs={
                'class': 'input input-bordered w-full mb-2', 'min': 1,
                'max': 20
                }),
        }

    def clean_reference_code(self):
        code = self.cleaned_data['reference_code']
        if not Booking.objects.filter(reference_code=code).exists():
            raise forms.ValidationError('Invalid reference code')
        return code
