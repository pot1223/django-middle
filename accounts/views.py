from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView,PasswordChangeView,PasswordResetConfirmView
from django.http import Http404
from django.urls.http import urlsafe_base64_decode
from django.views.generic import CreateView
from django.shortcuts import render, redirect,resolve_url
from .forms import SignupForm

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'piroproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            next_url=request.GET.get('next') or 'profile'
            return redirect('profile')



    else:
        form = SignupForm()
        return render(request, 'accounts/signup.html', {
            'form': form,
        })

class SignupView(CreateView):
    model=User
    form_class = SignupForm
    template_name='accounts/signup.html'


    def get_success_url(self):
        next_url=self.request.GET.get('next')or 'profile'
        return resolve_url(next_url)

    def form_valid(self, form):
        user=form.save()
        auth_login(self.request, user)
        return redirect(self.get_success_url())

'''signup= CreateView.as_view(model=User,
          form_class=SignupForm
           success_url=settings.LOGIN_URL,
           template_name='accounts/signup.html')'''


class MyPasswordChangeView(PasswordChangeView):
    success_url=reverse_lazy('profile')
    template_name='accounts/password_change_form.html'
    pass

def form_vaild(self,form):
    messages.info(self.request,'암호 변경을 완료했습니다.')
    return super().form_valid(form)


class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('')

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('')


@login_required
def profile(request):
    return render(request,'accounts/profile.html')