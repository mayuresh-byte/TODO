from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm  # This UserCreationForm is given by  django
from django.contrib.auth.models import User
from django.forms import ModelForm
from app.models import Todo


# We are creating our own custmozied register form bcoz Default form given by Django consists only username and password field.
# We have created a new form inherting the default form that is UserCreationForm below.
# fields means what we want in our form. It will work totally same as UserCreationForm.
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'status', 'priority']