from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self) -> None:
        super().__init__()
        self.fields['password1'].help_text = ''
        self.fields['username'].help_text = ''
        self.fields['password2'].help_text = ''