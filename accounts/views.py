from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView as AuthPasswordChangeView
)
from django.db import transaction
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from accounts.forms import SignupForm, ProfileForm, PasswordChangeForm
from accounts.models import User


login = LoginView.as_view(template_name="accounts/login_form.html")


class LogoutViews(LogoutView):

    def get_next_page(self):
        messages.success(self.request, '로그아웃 되었습니다.')
        return reverse('root')

logout = LogoutViews.as_view()


@transaction.atomic
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():

            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, '회원가입 환영합니다.')
            next_url = request.GET.get('next', '/')

            return redirect(next_url)
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })

# def complete_verification(request, key):
#     try:
#         if request.user.is_authenticated:
#             raise LoggedOutOnlyFunctionView("Please verify email first")
#         user = User.objects.get_or_none(email_secret=key)
#         if user is None:
#             messages.error(request, "User does not exist")
#             return redirect(reverse("core:home"))
#         user.email_verified = True
#         user.email_secret = ""
#         user.save()
#         login(request, user)
#         messages.success(request, f"{user.email} verification is completed")
#         return redirect(reverse("core:home"))
#     except LoggedOutOnlyFunctionView as error:
#         messages.error(request, error)
#         return redirect("core:home")

# class SignupView(FormView):
#
#     form_class = SignupForm

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필을 수정/저장했습니다.")
            return redirect(reverse("root"))
    else:
        form = ProfileForm(instance=request.user)

    return render(request, "accounts/profile_edit_form.html",{
        "form": form,
    })
    pass

class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
    success_url = reverse_lazy('root')
    template_name = 'accounts/password_change_form.html'
    form_class = PasswordChangeForm

    def form_valid(self, form):
        messages.success(self.request, "암호를 변경했습니다.")
        return super().form_valid(form)



password_change = PasswordChangeView.as_view()