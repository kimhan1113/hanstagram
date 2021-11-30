from django.contrib.auth.forms import (
    UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm
)
from django.core.exceptions import ValidationError
from django.forms import ModelForm, forms

from accounts.models import User


class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    # 이메일 중복 확인 로직!
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = User.objects.filter(email=email)
            if qs.exists():
                raise forms.ValidationError("이미 등록된 이메일 주소입니다.")
        return email

    # class Meta:
    #     model = User
    #     fields = ['username', 'password']


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'website_url', 'bio', 'phone_number', 'gender']

class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')

        # new_password2 = super().clean_new_password2()

        if old_password and new_password1:

        # new_password1 = super().clean_new_password2()
            if old_password == new_password1:
                raise ValidationError("새로운 암호는 기존 암호과 다르게 입력해주세요.")
        return new_password1