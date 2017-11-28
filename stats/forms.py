from .models import Test
from django.db import models
from django import forms

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
        'title',
		'a_users',
        'a_conversions',
        'a_conversionrate',
		'b_users',
		'b_conversions',
        'b_conversionrate',
        'winner',]

        widgets = {
            'a_conversionrate': forms.NumberInput(attrs={'readonly': 'True'}),
            'b_conversionrate': forms.NumberInput(attrs={'readonly': 'True'}),
            'winner': forms.TextInput(attrs={'readonly': 'True'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        a_conversions = cleaned_data['a_conversions']
        a_users = cleaned_data['a_users']
        b_conversions = cleaned_data['b_conversions']
        b_users = cleaned_data['b_users']

        if a_users < a_conversions | b_users < b_conversions:
            raise forms.ValidationError("Conversions Cannot Be Higher Than Users")
        if cleaned_data['a_users'] < 1 | cleaned_data['b_users'] < 1:
            raise forms.ValidationError("Must be more than 0")
