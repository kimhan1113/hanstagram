from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.generic import FormView

from accounts.forms import SignupForm
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