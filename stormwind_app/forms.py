from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('city', 'street', 'number_home', 'number_flat', 'floor', 'rooms', 'area', 'floor_count', 'property_type')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('client', 'realtor', 'property', 'price')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class ReqForm(forms.ModelForm):
    class Meta:
        model = Req
        fields = ('client', 'realtor', 'min_price', 'max_price','min_floor', 'max_floor', 'min_room_count', 'max_room_count', 'min_area', 'max_area', 'min_floor_count', 'max_floor_count','property_type')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'middle_name', 'phone', 'email')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = ('first_name', 'last_name', 'middle_name', 'commission')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ('req', 'offer')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
