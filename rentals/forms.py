from django import forms
from django.contrib.auth.models import User
from .models import Customer, Booking, Review, Bike

# ==========================================
# 1. REGISTRATION FORM (For Sign Up)
# ==========================================
class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }
    
    # Save the custom phone number when saving the user
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

# ==========================================
# 2. BOOKING FORM (For Dates Only)
# ==========================================
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        # We only need dates here. The bike ID is handled by the URL.
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'How was the ride?'}),
        }
class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['make', 'model', 'year', 'daily_rate', 'image_url', 'availability']
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Yamaha'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. R15 V4'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'daily_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'availability': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }