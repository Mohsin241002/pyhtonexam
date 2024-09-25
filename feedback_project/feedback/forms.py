
from django import forms

class FeedbackForm(forms.Form):
    user_name = forms.CharField(max_length=100, label='User Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm Password')
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Phone Number')
    feedback_message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Feedback Message')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        phone_number = cleaned_data.get("phone_number")

        # Validate that passwords match
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        # Validate phone number
        if not phone_number.isdigit() or len(phone_number) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits and contain only numbers.")
