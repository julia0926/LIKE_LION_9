# CustomUser 폼을 따로 만들어서 여러가지를 입력 받을 수 있게
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm): #UserCreationForm 상속 받아 
    class Meta:
        model = CustomUser #지정한 값으로 변경해서 model 사용
        fields = ['username','password1','password2','age','address']