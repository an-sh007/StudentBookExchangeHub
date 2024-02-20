from django import forms

class RegistrationForm(forms.Form):
		username = forms.CharField(max_length=100)
		email = forms.EmailField()
		password = forms.CharField(widget=forms.PasswordInput)
		# Add other fields as needed
