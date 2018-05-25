from django import forms
from AppTwo.models import User

class userform(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'