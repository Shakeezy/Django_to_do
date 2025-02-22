from django import forms
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Write your password', 'class': 'introduce'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password', 'class': 'introduce'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Write your username', 'class': 'introduce'}),
        }
        help_texts = {
            'username': None,
            'password': None,   # Elimina el texto de ayuda de username
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])  # Encripta la contraseña
        if commit:
            user.save()
        return user
