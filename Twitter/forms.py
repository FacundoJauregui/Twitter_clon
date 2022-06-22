from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from platformdirs import user_cache_dir
from Twitter.models import Post, Profile

class UserRegisterForm(UserCreationForm):
    
    
    class Meta:
        model = User
        fields = ['first_name','username', 'email', 'password1', 'password2']
        

class PostForm(forms.ModelForm):
    content = forms.CharField(widget = forms.Textarea(attrs = {'class': "form-control w-100",
                                                               'id':"contentsBox",
                                                               'rows': "3",
                                                               'placeholder':"What's happening?" }))
    
    class Meta:
        model = Post
        fields = ['content']
        
class UserEditForm(forms.ModelForm):
    
    password1 = forms.CharField(label='Modificar Contraseña', widget = forms.PasswordInput, required=False)
    password2 = forms.CharField(label= 'Confirmar contraseña', widget = forms.PasswordInput, required=False)
     
    class Meta:
        model = User
        fields = ['first_name','username']

        
class ProfileEditForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image', 'bio']