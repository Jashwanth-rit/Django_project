# payment/forms.py

from django import forms
from .models import ShippingAddress

# forms.py
from django import forms

class PaymentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Amount")
    payment_method = forms.ChoiceField(
        choices=[('online', 'Online'), ('offline', 'Offline')],
        label="Payment Method"
    )
    card_number = forms.CharField(max_length=16, required=False, label="Card Number")
    expiry_date = forms.CharField(max_length=5, required=False, label="Expiry Date (MM/YY)")
    cvv = forms.CharField(max_length=3, required=False, label="CVV")

    # You can add custom validation or clean methods if needed
    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get("payment_method")
        card_number = cleaned_data.get("card_number")
        expiry_date = cleaned_data.get("expiry_date")
        cvv = cleaned_data.get("cvv")

        # If online payment, ensure card details are filled
        if payment_method == 'online' and not (card_number and expiry_date and cvv):
            raise forms.ValidationError("Please provide all card details for online payment.")

        return cleaned_data


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', 'phone_number']

        widgets = {
            'address_line_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }
