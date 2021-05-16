from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('Email',)


class UserProfileChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('Email',)
