from django import forms
from django.core import validators

def check_for_letter(value):
    #if want to make sure letter starts with z
    if value[0].isalpha()==False:
        raise forms.ValidationError('Need to Start with a letter')

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_letter])
    email = forms.EmailField()
    verify_email = forms.EmailField(label = 'Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Emails do not match!')

