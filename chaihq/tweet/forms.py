from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# making forms using the fields of models - power of django
class TweetForm(forms.ModelForm):
  class Meta:
    model = Tweet
    fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    # tuple used as we are using inbuilt form not custom form as in tweetform
    fields = ('username','email','password1','password2')